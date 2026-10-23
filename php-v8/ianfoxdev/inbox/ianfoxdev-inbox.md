# ianfoxdev/inbox

> 标签: Messenger, cloudevents, consumer, deduplication, exactly-once, idempotency, inbox, kafka, laravel, rabbitmq

## 简介

Consumer-side deduplication for PHP: the message key is written in the same database transaction as the change it causes, so a redelivered message is skipped. Works with outbox's CloudEvents headers, Symfony Messenger and Laravel Queue.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/IanFoxDev/inbox
- 源码仓库：https://github.com/IanFoxDev/inbox.git
- Packagist 页面：https://packagist.org/packages/ianfoxdev%2Finbox

## 历史版本号

- 当前版本：v0.1.0

- v0.1.0

## 获取地址

- Composer 安装：`composer require ianfoxdev/inbox`
- Packagist 仓库：https://repo.packagist.org/p2/ianfoxdev/inbox.json
- 许可证：MIT
- PHP 要求：^8.3
