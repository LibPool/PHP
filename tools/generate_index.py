#!/usr/bin/env python3
"""Generate the LibPool PHP library index from Packagist metadata.

Layout:
  php-v<major>/<vendor>/<package>/<vendor>-<package>.md

Run from the repo root:
    python tools/generate_index.py --crawl --crawl-limit 3000
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import threading
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path


PACKAGIST_SEARCH = "https://packagist.org/search.json"
PACKAGIST_POPULAR = "https://packagist.org/explore/popular.json"
P2 = "https://repo.packagist.org/p2"
USER_AGENT = "LibPool-Indexer/1.0 (+https://github.com/LibPool)"
CACHE_PATH = Path(__file__).resolve().parent / "cache" / "php.json"
PHP_RELEASES = ["php-v5", "php-v7", "php-v8"]
API_LOCK = threading.Lock()


@dataclass
class PhpLib:
    name: str
    tags: list[str] = field(default_factory=list)
    version: str = ""
    description: str = ""
    homepage: str = ""
    source_url: str = ""
    license: str = ""
    keywords: list[str] = field(default_factory=list)
    require_php: str = ""
    versions: list[str] = field(default_factory=list)
    downloads: int = 0
    favers: int = 0

    @property
    def vendor(self) -> str:
        return self.name.split("/", 1)[0] if "/" in self.name else self.name

    @property
    def package(self) -> str:
        return self.name.split("/", 1)[1] if "/" in self.name else self.name

    @property
    def safe_name(self) -> str:
        return re.sub(r"[^A-Za-z0-9._+-]", "-", self.name)


def http_json(url: str) -> dict | None:
    last_exc: Exception | None = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except Exception as exc:
            last_exc = exc
            if getattr(exc, "code", None) in (429, 500, 502, 503, 504):
                time.sleep(1 + attempt * 2)
                continue
            if attempt < 2:
                time.sleep(0.4 * (attempt + 1))
                continue
            break
    print(f"  fetch failed: {url} -> {last_exc}", flush=True)
    return None


def load_seeds(path: Path) -> list[PhpLib]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [PhpLib(name=item["name"], tags=item.get("tags", [])) for item in data]


def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(data: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def crawl_popular(limit: int) -> list[PhpLib]:
    """Crawl Packagist's download-rank popular list."""
    libs: list[PhpLib] = []
    page = 1
    url = f"{PACKAGIST_POPULAR}?page=1"
    print(f"Crawling Packagist popular list, target {limit} packages...", flush=True)
    while len(libs) < limit and url:
        data = http_json(url)
        if not data:
            break
        rows = data.get("packages") or []
        if not rows:
            break
        for row in rows:
            if len(libs) >= limit:
                break
            name = row.get("name") or ""
            if not name:
                continue
            libs.append(
                PhpLib(
                    name=name,
                    description=(row.get("description") or "").strip(),
                    downloads=int(row.get("downloads") or 0),
                    favers=int(row.get("favers") or 0),
                )
            )
        print(f"  page {page}: collected {len(libs)}", flush=True)
        page += 1
        url = data.get("next")
        time.sleep(0.15)
    return libs


def stable_versions(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        v = (row.get("version") or "").strip()
        if not v:
            continue
        if re.search(r"(?:dev|alpha|beta|rc|RC|snapshot|patch[0-9])", v, re.I):
            continue
        out.append(row)
    return out


def current_version(rows: list[dict]) -> dict:
    st = stable_versions(rows)
    return st[0] if st else (rows[0] if rows else {})


def php_baseline(require: str) -> int:
    """Best-effort minimum PHP major from a composer require.php expression."""
    if not require:
        return 5
    candidates: list[int] = []
    for m in re.finditer(r"(>=\s*)?(\d+)(?:\.\d+){0,2}", require):
        prefix = (m.group(1) or "").strip()
        num = int(m.group(2))
        if m.group(0).startswith("<"):
            continue
        candidates.append(num)
    if not candidates:
        return 5
    return min(candidates)


def php_dirs_for(require_php: str) -> list[str]:
    major = max(php_baseline(require_php), 5)
    return [d for d in PHP_RELEASES if int(d.replace("php-v", "")) >= major]


def enrich_one(lib: PhpLib, cache: dict, use_cache: bool) -> tuple[PhpLib, dict | None]:
    key = lib.name
    if use_cache and key in cache:
        entry = cache[key]
        for attr in (
            "version",
            "description",
            "homepage",
            "source_url",
            "license",
            "keywords",
            "require_php",
            "versions",
            "downloads",
            "favers",
        ):
            setattr(lib, attr, entry.get(attr, lib.__dict__.get(attr, "")))
        lib.tags = list(dict.fromkeys(lib.tags + entry.get("tags", [])))
        if lib.description or lib.version:
            return lib, None

    with API_LOCK:
        data = http_json(f"{P2}/{lib.vendor}/{lib.package}.json")
    if not data:
        return lib, None
    rows = (data.get("packages") or {}).get(lib.name) or []
    if not rows:
        rows = (data.get("packages") or {}).get(lib.package) or []
    if not rows:
        return lib, None
    cur = current_version(rows)
    lib.version = cur.get("version") or ""
    lib.homepage = (cur.get("homepage") or "").strip()
    source = cur.get("source") or {}
    lib.source_url = (source.get("url") or "").strip()
    lic = cur.get("license") or []
    if isinstance(lic, list):
        lib.license = ", ".join(str(x) for x in lic if x)
    elif lic:
        lib.license = str(lic)
    req = cur.get("require") or {}
    lib.require_php = (req.get("php") or "").strip()
    lib.versions = sorted({r.get("version") for r in stable_versions(rows) if r.get("version")}, key=lambda s: s)
    if not lib.description:
        lib.description = (cur.get("description") or "").strip()
    lib.keywords = list(cur.get("keywords") or [])
    if not lib.homepage:
        lib.homepage = f"https://packagist.org/packages/{urllib.parse.quote(lib.name, safe='')}"
    entry = {
        "version": lib.version,
        "description": lib.description,
        "homepage": lib.homepage,
        "source_url": lib.source_url,
        "license": lib.license,
        "keywords": lib.keywords,
        "require_php": lib.require_php,
        "versions": lib.versions,
        "downloads": lib.downloads,
        "favers": lib.favers,
        "tags": lib.tags,
    }
    return lib, entry


def readme_md(lib: PhpLib) -> str:
    version_lines = "\n".join(f"- {v}" for v in lib.versions[-12:] or ["-"])
    if len(lib.versions) > 12:
        version_lines += f"\n- 共 {len(lib.versions)} 个稳定版本，完整清单见 Packagist。"
    websites = []
    if lib.homepage:
        websites.append(f"- 官网：{lib.homepage}")
    if lib.source_url and lib.source_url != lib.homepage:
        websites.append(f"- 源码仓库：{lib.source_url}")
    websites.append(f"- Packagist 页面：https://packagist.org/packages/{urllib.parse.quote(lib.name, safe='')}")

    downloads = [
        f"- Composer 安装：`composer require {lib.name}`",
        f"- Packagist 仓库：https://repo.packagist.org/p2/{lib.vendor}/{lib.package}.json",
    ]
    if lib.license:
        downloads.append(f"- 许可证：{lib.license}")
    if lib.require_php:
        downloads.append(f"- PHP 要求：{lib.require_php}")
    if lib.downloads:
        downloads.append(f"- Packagist 下载量：{lib.downloads:,}")
    if lib.favers:
        downloads.append(f"- Packagist 收藏：{lib.favers:,}")
    tags = ", ".join(sorted(set(lib.tags + lib.keywords))) if (lib.tags or lib.keywords) else "PHP"
    desc = lib.description or f"{lib.name} - PHP library from Packagist"
    dirs = php_dirs_for(lib.require_php)
    compat = f"按 require.php 推断最低支持 PHP {php_baseline(lib.require_php)}；已收录于 {', '.join(dirs)}。"
    return f"""# {lib.name}

> 标签: {tags}

## 简介

{desc}

{compat}

## 官网

{chr(10).join(websites)}

## 历史版本号

- 当前版本：{lib.version or "未知"}

{version_lines}

## 获取地址

{chr(10).join(downloads)}
"""


def generate(root: Path, libs: list[PhpLib]) -> dict[str, int]:
    counts = defaultdict(int)
    for lib in libs:
        if not lib.version:
            continue
        text = readme_md(lib)
        for release in php_dirs_for(lib.require_php):
            target = root / release / lib.vendor / lib.package
            target.mkdir(parents=True, exist_ok=True)
            (target / f"{lib.safe_name}.md").write_text(text, encoding="utf-8")
            counts[release] += 1
    return dict(counts)


def write_php_readme(root: Path, libs: list[PhpLib], counts: dict[str, int]) -> None:
    lines = [
        "# PHP 库索引",
        "",
        "本目录收录来自 Packagist 的 PHP 库索引，按 PHP 大版本与 Composer vendor/package 路径组织：",
        "",
        "- 大版本目录：`php-v5`、`php-v7`、`php-v8`",
        "- 包路径：`vendor/package/`，例如 `laravel/framework` 位于 `php-v8/laravel/framework/laravel-framework.md`",
        "- 库若兼容多个 PHP 大版本，会同时出现在所有后续版本目录中",
        f"- 当前共收录 {len(libs)} 个 Composer 包（含按下载量爬取的头部包与人工种子）。",
        "",
        "## 数据源",
        "",
        "- Packagist 搜索/热门接口：https://packagist.org/explore/popular.json",
        "- Packagist p2 元数据：https://repo.packagist.org/p2/<vendor>/<package>.json",
        "- Packagist 官网：https://packagist.org/",
        "",
        "## 生成方式",
        "",
        "```bash",
        "python tools/build_seed_list.py",
        "python tools/generate_index.py --crawl --crawl-limit 3000",
        "```",
        "",
        "按 PHP 大版本统计：",
        "",
    ]
    lines += [f"- {k}：{v} 个包" for k, v in counts.items()]
    lines += ["", "完整种子清单见 [tools/seeds/php.json](tools/seeds/php.json)。", ""]
    (root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default="tools/seeds/php.json")
    ap.add_argument("--out", default=".")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--crawl", action="store_true")
    ap.add_argument("--crawl-limit", type=int, default=3000)
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--refresh-cache", action="store_true")
    args = ap.parse_args()
    root = Path(args.out).resolve()
    libs: list[PhpLib] = []
    if args.crawl:
        libs = crawl_popular(args.crawl_limit)
        seed_path = Path(args.seeds)
        if seed_path.exists():
            existing = {lib.name for lib in libs}
            for seed in load_seeds(seed_path):
                if seed.name not in existing:
                    libs.append(seed)
    else:
        libs = load_seeds(Path(args.seeds))
    if args.limit:
        libs = libs[: args.limit]
    cache = load_cache()
    print(f"Processing {len(libs)} packages...", flush=True)
    results: list[tuple[PhpLib, dict | None]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(enrich_one, lib, cache, not args.refresh_cache) for lib in libs]
        for i, fut in enumerate(as_completed(futures), 1):
            lib, entry = fut.result()
            results.append((lib, entry))
            if i % 100 == 0 or i == len(futures):
                print(f"  enriched {i}/{len(futures)}", flush=True)
    for lib, entry in results:
        if entry:
            cache[lib.name] = entry
    save_cache(cache)
    counts = generate(root, [lib for lib, _ in results])
    print("Generated per PHP major:", json.dumps(counts, sort_keys=True), flush=True)
    write_php_readme(root, [lib for lib, _ in results], counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
