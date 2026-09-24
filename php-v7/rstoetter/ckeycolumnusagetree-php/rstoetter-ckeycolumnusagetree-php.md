# rstoetter/ckeycolumnusagetree-php

> 标签: dependencies, dependency, mysql, php, scanner, tables

## 简介

The class cKeyColumnUsageTree represents a sorted collection of the key column usage of a mysql database. The main purpose of the class is to determine the dependencies of the tables among each other: The class is able to find dependency paths of more than two tables, when another tables are involved. Dependencies which include self referencing tables are considered, too.

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/rstoetter%2Fckeycolumnusagetree-php
- 源码仓库：https://github.com/rstoetter/ckeycolumnusagetree-php.git
- Packagist 页面：https://packagist.org/packages/rstoetter%2Fckeycolumnusagetree-php

## 历史版本号

- 当前版本：v1.0.4

- v1.0.0
- v1.0.1
- v1.0.2
- v1.0.3
- v1.0.4

## 获取地址

- Composer 安装：`composer require rstoetter/ckeycolumnusagetree-php`
- Packagist 仓库：https://repo.packagist.org/p2/rstoetter/ckeycolumnusagetree-php.json
- 许可证：MIT
- PHP 要求：>=7.0
