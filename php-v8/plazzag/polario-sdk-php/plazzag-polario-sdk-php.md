# plazzag/polario-sdk-php

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

API for Polario  __Naming:__  * json properties are formatted in camel case (fooBar) besides of enums (FooBar) * route params are formatted in hyphen case (foo-bar) * query params are formatted in snake case (foo_bar) * query params could hold lists of elements if they are comma separated * enum properties are formatted in capitalized camel case (FooBar)  __Default values:__  * default values are specified for optional parameters do only apply to POST requests  __Types:__  * numbers are considered to be float values * strings that are not specified to be html formatted should not be interpreted as html to avoid unexpected bahavior, like xss attacks * timestamps are considered to be in unix time  __Headers:__  * ___Platform___: can be always set as header param to specify the platform of the request for the logging output

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/plazzag/polario-sdk-php.git
- Packagist 页面：https://packagist.org/packages/plazzag%2Fpolario-sdk-php

## 历史版本号

- 当前版本：5.11.0

- 5.10.0
- 5.11.0
- 5.5.2
- 5.7.0
- 5.8.0
- v5.4.3

## 获取地址

- Composer 安装：`composer require plazzag/polario-sdk-php`
- Packagist 仓库：https://repo.packagist.org/p2/plazzag/polario-sdk-php.json
- 许可证：unlicense
- PHP 要求：^8.1
