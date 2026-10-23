# parkktech/fastmagento

> 标签: catalog, elasticsearch, instant-search, layered-navigation, magento, magento-2, magento2, opensearch, performance, search

## 简介

FastMagento makes OpenSearch the serving layer for Magento 2 — products, category pages, search, and layered navigation are served from OpenSearch instead of MySQL, with MySQL kept as the source of truth. Drop-in, base-Magento-only (no Hyvä/Breeze required), cache/Varnish-safe, multi-store, and self-healing (every read degrades to native EAV on a miss or an OpenSearch outage).

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/parkktech/FastMagento
- 源码仓库：https://github.com/parkktech/FastMagento.git
- Packagist 页面：https://packagist.org/packages/parkktech%2Ffastmagento

## 历史版本号

- 当前版本：v2.11.1

- v2.4.1
- v2.4.2
- v2.5.0
- v2.5.1
- v2.6.0
- v2.6.1
- v2.7.0
- v2.7.1
- v2.7.2
- v2.8.0
- v2.8.1
- v2.9.0
- 共 25 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require parkktech/fastmagento`
- Packagist 仓库：https://repo.packagist.org/p2/parkktech/fastmagento.json
- 许可证：OSL-3.0, AFL-3.0
- PHP 要求：~8.1.0||~8.2.0||~8.3.0||~8.4.0||~8.5.0
