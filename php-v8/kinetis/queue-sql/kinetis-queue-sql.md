# kinetis/queue-sql

> 标签: PHP

## 简介

A SQL-backed (MySQL/Postgres) queue implementation for kinetis/queue's QueueInterface — SELECT ... FOR UPDATE SKIP LOCKED for atomic reservation, token-fenced settlement, and a finite visibility timeout that redelivers a crashed worker's job.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/kinetis%2Fqueue-sql
- 源码仓库：https://github.com/kinetis-dev/queue-sql.git
- Packagist 页面：https://packagist.org/packages/kinetis%2Fqueue-sql

## 历史版本号

- 当前版本：v1.6.3

- v1.1.2
- v1.2.0
- v1.3.0
- v1.3.1
- v1.3.2
- v1.3.3
- v1.4.0
- v1.5.0
- v1.6.0
- v1.6.1
- v1.6.2
- v1.6.3
- 共 13 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require kinetis/queue-sql`
- Packagist 仓库：https://repo.packagist.org/p2/kinetis/queue-sql.json
- 许可证：MIT
- PHP 要求：^8.4
