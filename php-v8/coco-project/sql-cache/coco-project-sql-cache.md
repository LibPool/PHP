# coco-project/sql-cache

> 标签: PHP

## 简介

Based on the lexical analysis of "update," "select," "insert," and "delete" SQL statements, an automatic caching strategy is implemented. The strategy involves caching the data when executing a select operation and associating the table name contained in the SQL statement with the corresponding cached records. When executing update, insert, or delete operations, the table name from the SQL statement is extracted, and any cached records containing this table name from previous select operations are deleted. This strategy enables seamless caching without delay and eliminates the need to worry about data synchronization issues. It is particularly effective for tables with infrequent data modifications. For tables with frequent modifications, they can be ignored by configuring the strategy accordingly.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/coco-project%2Fsql-cache
- 源码仓库：https://github.com/coco-projects/sql-cache.git
- Packagist 页面：https://packagist.org/packages/coco-project%2Fsql-cache

## 历史版本号

- 当前版本：v1.0.6

- v1.0.0
- v1.0.1
- v1.0.2
- v1.0.3
- v1.0.4
- v1.0.5
- v1.0.6

## 获取地址

- Composer 安装：`composer require coco-project/sql-cache`
- Packagist 仓库：https://repo.packagist.org/p2/coco-project/sql-cache.json
- 许可证：MIT
- PHP 要求：>=8.0
