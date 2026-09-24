# creatissimo/dhl-oauth

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

This API describes how API client can obtain a token which is used to access various Parcel Germany APIs. Using this API is often the first step in making your API call. <p><h3>Preconditions</h3> You will need:  * client ID (aka "API Key", obtained when you create an app in developer.dhl.com) * client secret (aka "API Secret", obtained when you create an app in developer.dhl.com) * GKP user name (obtained when setting up your business account with Parcel Germany) * GKP password (obtained when setting up your business account with Parcel Germany)  <h3>Technical Information</h3> This uses an implementation of OAuth2 Password Grant (RFC 6749). After successfull usage you will: * have an opaque access token to be used for API calls afterwards  * this token will have an expiration time

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/creatissimo/dhl-oauth.git
- Packagist 页面：https://packagist.org/packages/creatissimo%2Fdhl-oauth

## 历史版本号

- 当前版本：v1.0.0

- v1.0.0

## 获取地址

- Composer 安装：`composer require creatissimo/dhl-oauth`
- Packagist 仓库：https://repo.packagist.org/p2/creatissimo/dhl-oauth.json
- 许可证：unlicense
- PHP 要求：^8.1
