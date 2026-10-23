# anun333/oe-module-migration

> 标签: bulk-data, fhir, import, migration, openemr, openemr-module

## 简介

Migration into OpenEMR from other EHRs: reads the FHIR R4 export every certified EHR must offer (bulk NDJSON or Bundles), reports what maps before anything is written, then imports the core chart through OpenEMR's own services, safe to rerun

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/anun333%2Foe-module-migration
- 源码仓库：https://github.com/anun333/oe-module-migration.git
- Packagist 页面：https://packagist.org/packages/anun333%2Foe-module-migration

## 历史版本号

- 当前版本：v0.2.3

- v0.1.0
- v0.2.0
- v0.2.1
- v0.2.2
- v0.2.3

## 获取地址

- Composer 安装：`composer require anun333/oe-module-migration`
- Packagist 仓库：https://repo.packagist.org/p2/anun333/oe-module-migration.json
- 许可证：GPL-3.0-or-later
- PHP 要求：>=8.3
