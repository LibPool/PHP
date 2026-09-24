# tuutti/php-klarna-payments

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

The payments API is used to create a session to offer Klarna's payment methods as part of your checkout. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).  **Note:** Examples provided in this section includes full payloads, including all supported fields , required and optionals. In order to implement a best in class request we recommend you don't include customer details when initiating a payment session. Refer to [Initiate a payment](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/) section for further details.  Read more on [Klarna payments](https://docs.klarna.com/klarna-payments/).

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/tuutti/php-klarna-payments.git
- Packagist 页面：https://packagist.org/packages/tuutti%2Fphp-klarna-payments

## 历史版本号

- 当前版本：3.0.1

- 1.1.1
- 1.1.2
- 1.1.3
- 1.1.4
- 1.1.5
- 1.2.0
- 1.2.1
- 2.0.0
- 2.0.1
- 2.1.0
- 3.0.0
- 3.0.1
- 共 15 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require tuutti/php-klarna-payments`
- Packagist 仓库：https://repo.packagist.org/p2/tuutti/php-klarna-payments.json
- 许可证：unlicense
- PHP 要求：^7.4 || ^8.0
