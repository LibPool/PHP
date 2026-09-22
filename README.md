# PHP 库索引

本目录收录来自 Packagist 的 PHP 库索引，按 PHP 大版本与 Composer vendor/package 路径组织：

- 大版本目录：`php-v5`、`php-v7`、`php-v8`
- 包路径：`vendor/package/`，例如 `laravel/framework` 位于 `php-v8/laravel/framework/laravel-framework.md`
- 库若兼容多个 PHP 大版本，会同时出现在所有后续版本目录中
- 当前共收录 418 个 Composer 包（含按下载量爬取的头部包与人工种子）。

## 数据源

- Packagist 搜索/热门接口：https://packagist.org/explore/popular.json
- Packagist p2 元数据：https://repo.packagist.org/p2/<vendor>/<package>.json
- Packagist 官网：https://packagist.org/

## 生成方式

```bash
python tools/build_seed_list.py
python tools/generate_index.py --crawl --crawl-limit 3000
```

按 PHP 大版本统计：

- php-v8：397 个包
- php-v7：110 个包
- php-v5：36 个包

完整种子清单见 [tools/seeds/php.json](tools/seeds/php.json)。
