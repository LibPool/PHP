# atrocore-mcp/dbal-compat

> 标签: abstraction, database, db2, dbal, mariadb, mssql, mysql, oci8, oracle, pdo, pgsql, postgresql, queryobject, sasql, sql, sqlite, sqlserver, sqlsrv

## 简介

doctrine/dbal 3.2.2, unmodified except for one composer.json constraint: doctrine/deprecations relaxed from ^0.5.3 to ^0.5.3 || ^1, so it stops disjointly conflicting with mcp/sdk's phpdocumentor/reflection-docblock ^1.1 requirement on AtroCore instances (which pin doctrine/dbal ~3.2.2). Declares `replace` for doctrine/dbal 3.2.2 so Composer treats this as a drop-in, not a second copy.

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://www.doctrine-project.org/projects/dbal.html
- 源码仓库：https://github.com/TrendMend/atrocore-dbal-compat.git
- Packagist 页面：https://packagist.org/packages/atrocore-mcp%2Fdbal-compat

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require atrocore-mcp/dbal-compat`
- Packagist 仓库：https://repo.packagist.org/p2/atrocore-mcp/dbal-compat.json
- 许可证：MIT
- PHP 要求：^7.3 || ^8.0
