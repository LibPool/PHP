# yanlongli/app-store-server-api

> 标签: App Store Server API, apple, in-app, itunes, purchases, renewal, storekit, subscription, transactions

## 简介

PHP client for App Store Server API. Manage your customers’ App Store transactions from your server.The App Store Server API is a REST API that you call from your server to request and provide information about your customers' in-app purchases. The App Store signs the transaction and subscription renewal information that this API returns using the JSON Web Signature (JWS) specification.App Store Server API is independent of the app’s installation status on the customer’s devices. The App Store server returns information based on the customer’s in-app purchase history regardless of whether the customer installed, removed, or reinstalled the app on their devices.To request transaction and subscription status information with this API, provide any original transaction identifier that belongs to the customer. The transaction history API responds with a complete list of transactions, 20 at a time, starting with the oldest first. The subscription status API returns the status for all of the customer’s subscriptions, organized by their subscription group identifier.Use the Send Consumption Information endpoint to send information to the App Store when customers request a refund for a consumable in-app purchase, after you receive the CONSUMPTION_REQUEST App Store server notification. Your data helps inform refund decisions.

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/yanlongli%2Fapp-store-server-api
- 源码仓库：https://github.com/yanlong-li/AppStoreServerAPI.git
- Packagist 页面：https://packagist.org/packages/yanlongli%2Fapp-store-server-api

## 历史版本号

- 当前版本：1.15

- 0.1.1
- 1.0.0
- 1.13
- 1.15
- 1.6.0
- v1.6.1

## 获取地址

- Composer 安装：`composer require yanlongli/app-store-server-api`
- Packagist 仓库：https://repo.packagist.org/p2/yanlongli/app-store-server-api.json
- 许可证：MIT
- PHP 要求：>=7.1
