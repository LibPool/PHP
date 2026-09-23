# cbeyersdorf/easybill

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

The first version of the easybill REST API. [CHANGELOG](https://api.easybill.de/rest/v1/CHANGELOG.md)  ## Authentication  You can choose between two available methods: `Basic Auth` or `Bearer Token`.  In each HTTP request, one of the following HTTP headers is required:  ``` # Basic Auth Authorization: Basic base64_encode('<email>:<api_key>') # Bearer Token Authorization: Bearer <api_key> ```  ## Limitations  ### Request Limit  * PLUS: 10 requests per minute * BUSINESS: 60 requests per minute  If the limit is exceeded, you will receive the HTTP error: `429 Too Many Requests`  ### Result Limit  All result lists are limited to 100 by default. This limit can be increased by the query parameter `limit` to a maximum of 1000.  ## Query filter  Many list resources can be filtered. In `/documents` you can filter e.g. by number with `/documents?number=111028654`. If you want to filter multiple numbers, you can either enter them separated by commas `/documents?number=111028654,222006895` or as an array `/documents?number[]=111028654&number[]=222006895`.  **Warning**: The maximum size of an HTTP request line in bytes is 4094. If this limit is exceeded, you will receive the HTTP error: `414 Request-URI Too Large`  ### Escape commas in query  You can escape commans in query `name=Patrick\, Peter` if you submit the header `X-Easybill-Escape: true` in your request.  ## Property login_id  This is the login of your admin or employee account.  ## Date and Date-Time format Please use the timezone `Europe/Berlin`. * **date** = *Y-m-d* = `2016-12-31` * **date-time** = *Y-m-d H:i:s* = `2016-12-31 03:13:37`  Date or datetime can be `null` because the attributes have been added later and the entry is older.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/cbeyersdorf/easybill.git
- Packagist 页面：https://packagist.org/packages/cbeyersdorf%2Feasybill

## 历史版本号

- 当前版本：v1.94.0

- v1.63.0
- v1.70.1
- v1.71.0
- v1.78.0
- v1.82.0
- v1.83.0
- v1.84.0
- v1.87.0
- v1.88.0
- v1.91.0
- v1.92.4
- v1.94.0
- 共 17 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require cbeyersdorf/easybill`
- Packagist 仓库：https://repo.packagist.org/p2/cbeyersdorf/easybill.json
- 许可证：unlicense
- PHP 要求：^8.1
