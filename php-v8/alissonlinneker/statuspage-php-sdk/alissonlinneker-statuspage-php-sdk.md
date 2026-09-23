# alissonlinneker/statuspage-php-sdk

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

# Code of Conduct Please don't abuse the API, and please report all feature requests and issues to https://support.atlassian.com/contact  # Rate Limiting Each API token is limited to 1 request / second as measured on a 60 second rolling window. To get this limit increased, please contact us at https://support.atlassian.com/contact  Error codes 420 or 429 indicate that you have exceeded the rate limit and the request has been rejected.  # Basics  ## HTTPS It's required  ## URL Prefix In order to maintain version integrity into the future, the API is versioned. All calls currently begin with the following prefix:    https://api.statuspage.io/v1/  ## RESTful Interface Wherever possible, the API seeks to implement repeatable patterns with logical, representative URLs and descriptive HTTP verbs. Below are some examples and conventions you will see throughout the documentation.  * Collections are buckets: https://api.statuspage.io/v1/pages/asdf123/incidents.json * Elements have unique IDs: https://api.statuspage.io/v1/pages/asdf123/incidents/jklm456.json * GET will retrieve information about a collection/element * POST will create an element in a collection * PATCH will update a single element * PUT will replace a single element in a collection (rarely used) * DELETE will destroy a single element  ## Sending Data Information can be sent in the body as form urlencoded or JSON, but make sure the Content-Type header matches the body structure or the server gremlins will be angry.  All examples are provided in JSON format, however they can easily be converted to form encoding if required.  Some examples of how to convert things are below:      // JSON     {       "incident": {         "name": "test incident",         "components": ["8kbf7d35c070", "vtnh60py4yd7"]       }     }      // Form Encoded (using curl as an example):     curl -X POST https://api.statuspage.io/v1/example \       -d "incident[name]=test incident" \       -d "incident[components][]=8kbf7d35c070" \       -d "incident[components][]=vtnh60py4yd7"  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/alissonlinneker/statuspage-php-sdk.git
- Packagist 页面：https://packagist.org/packages/alissonlinneker%2Fstatuspage-php-sdk

## 历史版本号

- 当前版本：v1.0

- v1.0

## 获取地址

- Composer 安装：`composer require alissonlinneker/statuspage-php-sdk`
- Packagist 仓库：https://repo.packagist.org/p2/alissonlinneker/statuspage-php-sdk.json
- 许可证：unlicense
- PHP 要求：^7.4 || ^8.0
