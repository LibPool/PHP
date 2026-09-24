# creatissimo/dhl-de-retoure

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

# Introduction ## Overview                  Note:   This is the specification of the DP-DHL Group Parcel DE Returns API. This web service allows business customers to create return labels on demand.  # Scenarios ## Main Scenario: Creating a returnlabel This is achieved by posting a return order to the URI '/rest/orders'. The service will respond with a return label. ## Querying to get receiver locations The single scenario supported by this service is the determination of the receiver's location. This is achieved by getting a location to the URI '/rest/locations'. The service will respond with a Receiver. # Technical Note on Authorization This API supports __two alternative ways__ to authorize yourself: 1. Combination of Apikey and Basic Authentication which you can provide with every call. 2. OAuth2 Password Flow: After having obtained your access token once, you provide this token as bearer token.   You can try it out here. More details can be found when clicking on "Authorize".

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/creatissimo/dhl-de-retoure.git
- Packagist 页面：https://packagist.org/packages/creatissimo%2Fdhl-de-retoure

## 历史版本号

- 当前版本：v1.0.0

- v1.0.0

## 获取地址

- Composer 安装：`composer require creatissimo/dhl-de-retoure`
- Packagist 仓库：https://repo.packagist.org/p2/creatissimo/dhl-de-retoure.json
- 许可证：unlicense
- PHP 要求：^8.1
