# bubnov-mikhail/landedcostcalculationapi

> 标签: LandedCost Calculation API, api, sdk

## 简介

Landed Cost API providing duty rates, calculation, and item harmonization. A set of sample requests are available as a [Postman Collection](https://www.getpostman.com/collections/ad308f6c9351a18c2c12). ## Basics ### Timestamps Timestamps should be formatted using ISO-8601 to the nearest second, in UTC e.g `2015-06-12T09:17:37Z` ### Expiries All Requests will have an associated timestamp. The validity for any request is 1 minute to account for any clock-skew.  ## Authorization All API requests require an http header that contains your account ID and your account API Key. During account provisioning, you will be issued an API Key which you must supply with every request. ### Authorization Header To make an authorized API request, set the following HTTP header:  `authorization: avalaraapikey id:<accountId> key:<apiKey>`

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://apimatic.io
- 源码仓库：https://github.com/bubnov-mikhail/landedcostcalculationapi.git
- Packagist 页面：https://packagist.org/packages/bubnov-mikhail%2Flandedcostcalculationapi

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require bubnov-mikhail/landedcostcalculationapi`
- Packagist 仓库：https://repo.packagist.org/p2/bubnov-mikhail/landedcostcalculationapi.json
- 许可证：MIT
- PHP 要求：>=5.4.0
