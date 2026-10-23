# kruegge82/billbee-php-sdk-api

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

Documentation of the Billbee REST API to connect a Billbee account to external aplications.  ## Endpoint  The Billbee API endpoint base url is https://api.billbee.io/api/v1   ## Activation  You have to enable the API in the settings of your Billbee account. In addition you need a Billbee API Key identifying the application you develop. To get an API key, send a mail to support@billbee.io and send us a short note about what you are building.  ## Authorization & security  Because you can access private data with the Billbee API, every request has to be sent over https and must  * Contain a valid API Key identifying the application/developer. It has to be sent as the HTTP header X-Billbee-Api-Key * Contain a valid user login with billbee username and api password in form of a basic auth HTTP header  ## Throttling  50 calls per second for each API Key.  10 calls per second for each API Key in combination with Billbee user.  Besides that each endpoint has a throttle of max 2 requests per second per combination of API Key and Billbee user.  When you exceed the throttle threshold, the API will return a HTTP 429 status code and a Retry-After-Header indicating how many seconds you will have to wait before you can call the API again.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/kruegge82/billbee-php-sdk-api.git
- Packagist 页面：https://packagist.org/packages/kruegge82%2Fbillbee-php-sdk-api

## 历史版本号

- 当前版本：v1.1

- v1
- v1.0.1
- v1.0.2
- v1.0.3
- v1.0.4
- v1.0.5
- v1.0.6
- v1.1

## 获取地址

- Composer 安装：`composer require kruegge82/billbee-php-sdk-api`
- Packagist 仓库：https://repo.packagist.org/p2/kruegge82/billbee-php-sdk-api.json
- 许可证：unlicense
- PHP 要求：^8.1
