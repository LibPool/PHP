# aseemann/pihole-api-client

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

The Pi-hole API is organized around [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts and returns reliable UTF-8 [JavaScript Object Notation (JSON)-encoded](http://www.json.org/) data for all API responses, and uses standard HTTP response codes and verbs. Most (but not all) endpoints require authentication. API endpoints requiring authentication will fail with code `401 Unauthorized` when used outside a valid session.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://codeberg.org/aseemann/pihole-api-client.git
- Packagist 页面：https://packagist.org/packages/aseemann%2Fpihole-api-client

## 历史版本号

- 当前版本：1.1.0

- 1.0.0
- 1.1.0

## 获取地址

- Composer 安装：`composer require aseemann/pihole-api-client`
- Packagist 仓库：https://repo.packagist.org/p2/aseemann/pihole-api-client.json
- 许可证：unlicense
- PHP 要求：^8.1
