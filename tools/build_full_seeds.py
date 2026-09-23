#!/usr/bin/env python3
"""Download Packagist's complete package-name list into the seed file.

The generated seed contains every Composer package name returned by
https://packagist.org/packages/list.json so the full index can be rebuilt
without touching the live list again.

Run from the repo root:
    python tools/build_full_seeds.py
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path


PACKAGIST_LIST = "https://packagist.org/packages/list.json"
USER_AGENT = "LibPool-Indexer/1.0 (+https://github.com/LibPool)"
OUT = Path(__file__).resolve().parent / "seeds" / "php.json"


def main() -> int:
    request = urllib.request.Request(PACKAGIST_LIST, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as resp:
        data = json.load(resp)
    names = data.get("packageNames") or []
    if not names:
        print("Packagist returned an empty package list", file=sys.stderr)
        return 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps([{"name": name, "tags": []} for name in names], ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(names):,} Composer package names to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
