# postboost/php-sdk

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

The PostBoost REST API lets you publish, schedule, and analyze social media posts across 12+ platforms from a single integration. No OAuth apps to maintain — PostBoost handles platform authorization for you.  ## Base URL All workspace-scoped endpoints are prefixed with `/{workspaceUuid}`. Panel/admin endpoints are prefixed with `/panel`.  ## Authentication All requests require a Bearer token in the `Authorization` header. Generate tokens in your PostBoost dashboard under **Settings → Access Tokens**.  ``` Authorization: Bearer YOUR_API_TOKEN ```

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/postboost-co/postboost-php.git
- Packagist 页面：https://packagist.org/packages/postboost%2Fphp-sdk

## 历史版本号

- 当前版本：1.6.0

- 1.2.0
- 1.3.0
- 1.4.0
- 1.5.0
- 1.6.0
- v1.0.0
- v1.1.0

## 获取地址

- Composer 安装：`composer require postboost/php-sdk`
- Packagist 仓库：https://repo.packagist.org/p2/postboost/php-sdk.json
- 许可证：unlicense
- PHP 要求：^7.4 || ^8.0
