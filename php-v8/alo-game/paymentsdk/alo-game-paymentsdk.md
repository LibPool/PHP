# alo-game/paymentsdk

> 标签: alogame, iap, payment, sdk, webhook, webpay

## 简介

Server-side SDK for game backends integrating with Alogame payment flows. Handles signature verification, timestamp freshness, and request/response envelopes so a partner only implements a handful of business hooks. Ships WebPay (co-pub, HMAC) and Expub (exclusive/direct-publishing, MD5, covers web top-up and Mobile IAP).

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://docs.alogame.vn/server-integration/webpay-sdk-php
- 源码仓库：https://github.com/alo-game/alogame-paymentsdk-php.git
- Packagist 页面：https://packagist.org/packages/alo-game%2Fpaymentsdk

## 历史版本号

- 当前版本：2.1.0

- 1.0.0
- 1.1.0
- 2.0.0
- 2.1.0

## 获取地址

- Composer 安装：`composer require alo-game/paymentsdk`
- Packagist 仓库：https://repo.packagist.org/p2/alo-game/paymentsdk.json
- 许可证：MIT
- PHP 要求：>=8.1
