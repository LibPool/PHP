# magenxcommerce/module-abandoned-checkout

> 标签: PHP

## 简介

Abandoned checkout reminder: a cron scans active quotes that have items and a captured email but were left untouched past a configurable delay, and emails the shopper a recovery reminder with their cart contents and a one-click link back to the cart. Tracks reminders on the quote so a cart is only reminded once (or up to a configurable cap). The recovery link carries a signed, expiring token rather than the cart id itself.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/magenxcommerce%2Fmodule-abandoned-checkout
- 源码仓库：https://github.com/magenxcommerce/module-abandoned-checkout.git
- Packagist 页面：https://packagist.org/packages/magenxcommerce%2Fmodule-abandoned-checkout

## 历史版本号

- 当前版本：v1.0.2

- v1.0.0
- v1.0.1
- v1.0.2

## 获取地址

- Composer 安装：`composer require magenxcommerce/module-abandoned-checkout`
- Packagist 仓库：https://repo.packagist.org/p2/magenxcommerce/module-abandoned-checkout.json
- 许可证：OSL-3.0, AFL-3.0
- PHP 要求：~8.3.0||~8.4.0||~8.5.0
