# birb/fancy-stubs-codegen

> 标签: PHP

## 简介

Build-time, attribute-driven code generator: write a stub class, mark members with #[DefinerAttribute], and get a real, finished PHP class back — conventions filled in (event names, ids, ...), or whole getters/setters/builder classes generated from the stub's properties. Unlike runtime-reflection tools, the output is a plain PHP file with zero dependency on this library and no per-request reflection cost; useful for scaffolding DDD value objects/aggregates/events, command classes and other boilerplate. Postprocessing (e.g. phpcbf) and framework-specific conventions (e.g. Laravel table/id naming) ship as separate packages — see birb/fancy-stubs-codegen-postprocessors and birb/fancy-stubs-codegen-laravel.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/birb%2Ffancy-stubs-codegen
- 源码仓库：https://gitlab.com/birb-group/fancy-stubs-codegen-packages/core.git
- Packagist 页面：https://packagist.org/packages/birb%2Ffancy-stubs-codegen

## 历史版本号

- 当前版本：0.3.0

- 0.0.1
- 0.1.0
- 0.1.1
- 0.2.0
- 0.3.0

## 获取地址

- Composer 安装：`composer require birb/fancy-stubs-codegen`
- Packagist 仓库：https://repo.packagist.org/p2/birb/fancy-stubs-codegen.json
- 许可证：MIT
- PHP 要求：^8.2
