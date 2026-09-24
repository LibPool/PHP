# shell/card-management-sdk

> 标签: Card Management, SDKs, apimatic, shell

## 简介

The Shell Card Management API is REST-based and employs OAUTH 2.0,Basic and ApiKey authentication. The API endpoints accept JSON-encoded request bodies, return JSON-encoded responses and use standard HTTP response codes.All resources are located in the Shell Card Platform. The Shell Card Platform is the overall platform that encompasses all the internal Shell systems used to manage resources. The internal workings of the platform are not important when interacting with the API. However, it is worth noting that the platform uses a microservice architecture to communicate with various backend systems and some API calls are processed asynchronously. All endpoints use the POST verb for retrieving, updating, creating and deleting resources in the Shell Card Platform. The endpoints that retrieve resources from the Shell Card Platform allow flexible search parameters in the API request body.

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://www.shell.com/
- 源码仓库：https://github.com/sdks-io/card-management-php-sdk.git
- Packagist 页面：https://packagist.org/packages/shell%2Fcard-management-sdk

## 历史版本号

- 当前版本：3.0.0

- 1.0.0
- 1.1.0
- 1.2.0
- 1.3.0
- 1.4.0
- 2.0.0
- 2.0.1
- 3.0.0

## 获取地址

- Composer 安装：`composer require shell/card-management-sdk`
- Packagist 仓库：https://repo.packagist.org/p2/shell/card-management-sdk.json
- 许可证：MIT
- PHP 要求：^7.2 || ^8.0
