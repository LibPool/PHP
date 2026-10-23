# sugarcommerce/outbox

> 标签: cron, email, outbox, queue, retry, sqlite, webhooks

## 简介

A durable send queue on SQLite: rows claimed atomically under a lease so overlapping workers never send twice, a crashed worker's rows come back on their own, and retries follow a status-aware backoff policy. An inbox that handles each incoming event once. Plus the pieces that bound a cron run: a lock, a time budget and steps that cannot stop each other.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/sugarcommerce/outbox
- 源码仓库：https://github.com/SugarCommerce/outbox.git
- Packagist 页面：https://packagist.org/packages/sugarcommerce%2Foutbox

## 历史版本号

- 当前版本：1.3.0

- 1.3.0

## 获取地址

- Composer 安装：`composer require sugarcommerce/outbox`
- Packagist 仓库：https://repo.packagist.org/p2/sugarcommerce/outbox.json
- 许可证：GPL-2.0-or-later
- PHP 要求：>=8.5
