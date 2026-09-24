# progalaxyelabs/stonescriptphp-payments

> 标签: billing, gst, invoicing, payment-gateway, payments, php, postgresql, razorpay, sql, stonescriptphp, subscription, tax

## 简介

The unified payment system for StoneScriptPHP — merges what were separately-published stonescriptphp-pay (Razorpay/PayPal transport drivers) and stonescriptphp-invoice (SQL-first billing/invoicing) into one package: gateway drivers, the idempotent payment-capture primitive, and SQL-first subscription/one-time/credit/wallet/consumption/passthrough pricing, invoices, parties, pluggable regional tax computation (ships India GST), gateway routing, and durable transactional-outbox intimation. All business logic lives in PostgreSQL functions deployed via the StoneScriptDB Gateway; PHP is transport only.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://stonescriptphp.org
- 源码仓库：https://github.com/progalaxyelabs/stonescriptphp-payments.git
- Packagist 页面：https://packagist.org/packages/progalaxyelabs%2Fstonescriptphp-payments

## 历史版本号

- 当前版本：0.1.1

- 0.1.0
- 0.1.1

## 获取地址

- Composer 安装：`composer require progalaxyelabs/stonescriptphp-payments`
- Packagist 仓库：https://repo.packagist.org/p2/progalaxyelabs/stonescriptphp-payments.json
- 许可证：MIT
- PHP 要求：^8.2
