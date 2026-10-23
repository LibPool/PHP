# kruegge82/dhl-authentication-oauth-api

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

This API describes how API client can obtain a token which is used to access various Parcel Germany APIs. Using this API is often the first step in making your API call. <p><h3>Preconditions</h3> You will need:  * client ID (aka "API Key", obtained when you create an app in developer.dhl.com) * client secret (obtained when you create an app in developer.dhl.com) * GKP user name (obtained when setting up your business account with Parcel Germany) * GKP password (obtained when setting up your business account with Parcel Germany)  <h3>Technical Information</h3> This uses an implementation of OAuth2 Password Grant (RFC 6749). After successfull usage you will:  * have an opaque access token to be used for API calls afterwards  * this token will have an expiration time

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/kruegge82/dhl-authentication-oauth-api.git
- Packagist 页面：https://packagist.org/packages/kruegge82%2Fdhl-authentication-oauth-api

## 历史版本号

- 当前版本：v2.0.7

- v2.0.5
- v2.0.6
- v2.0.7

## 获取地址

- Composer 安装：`composer require kruegge82/dhl-authentication-oauth-api`
- Packagist 仓库：https://repo.packagist.org/p2/kruegge82/dhl-authentication-oauth-api.json
- 许可证：unlicense
- PHP 要求：^8.1
