# silvershop-suite/import

> 标签: ERP, PIM, catalogue, ecommerce, import, silvershop, silverstripe, stock, sync

## 简介

Channel-agnostic import engine for SilverShop (CMS 6): a two-phase stage→apply pipeline (upsert by SKU/GTIN, delta/scheduled sync on queuedjobs, dry-run, declarable per-field validation, field-level source-of-truth ownership, immutable run log) that thin per-system connectors (e.g. silvershop-suite/import-excel, silvershop-suite/connector-k3) plug into without the core knowing any system specifics.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/silvershop-suite%2Fimport
- 源码仓库：https://github.com/silvershop-suite/silvershop-import.git
- Packagist 页面：https://packagist.org/packages/silvershop-suite%2Fimport

## 历史版本号

- 当前版本：1.1.0

- 1.0.0
- 1.1.0

## 获取地址

- Composer 安装：`composer require silvershop-suite/import`
- Packagist 仓库：https://repo.packagist.org/p2/silvershop-suite/import.json
- 许可证：BSD-3-Clause
- PHP 要求：^8.3
