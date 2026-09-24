# zippendo/zippendo-php

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

Public API documentation for Zippendo. Authenticate using your API token (Bearer token prefixed with zipp_).  **Brands (sub-accounts).** An organization can be split into brands, each keeping its own orders, shipments and configuration separate. There are two ways to scope requests to one brand, and NEITHER changes any request body:  1. **Bind the token.** Create an API token with a `brandId` and every request it makes is confined    to that brand — reads filtered, writes stamped. This is the recommended way to give a single    brand's team its own credential. 2. **Send the `X-Zippendo-Brand` header.** An organization-wide token can scope an individual    request by sending the brand's id or slug in this header. Most SDKs let you set it once on the    client so every call inherits it.  A brand-bound token that receives an `X-Zippendo-Brand` header naming a different brand is rejected with `403 BRAND_ACCESS_DENIED` — the binding is never widened. Omit both and requests cover the whole organization, which is the behaviour of every existing token.  Records that belong to no brand carry `brandId: null`. Configuration (carriers, shipping rules, addresses) with a null brand is organization-wide and remains visible inside every brand; orders and shipments with a null brand are only visible organization-wide.  List endpoints additionally take a `?brandScope=own|shared|both` parameter to narrow further within whichever brand context already applies. `own` returns only rows assigned to that brand, and requires a brand context — a brand-bound token, a resolved brand session, or the `X-Zippendo-Brand` header above — otherwise `400`. `shared` returns only the organization-wide rows (equivalent to filtering `brandId=none`). The default, `both`, keeps the existing behaviour: a brand context sees its own rows plus the organization-wide ones. Set `X-Zippendo-Brand-Scope` as a client default to apply the same choice to every request instead of repeating the query parameter on each call — an explicit `brandScope` query parameter always wins over the header, and a blank header value is ignored.  Brands themselves are managed under the **Brands** tag. Retiring a brand is done with `POST /orgs/{orgId}/brands/{brandId}/archive` — permanent deletion is a dashboard-only action, since it is refused while any order, shipment, member or token still references the brand. Brands require a plan that includes them; creating one beyond your plan's limit returns `403`.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/zippendo/zippendo-php.git
- Packagist 页面：https://packagist.org/packages/zippendo%2Fzippendo-php

## 历史版本号

- 当前版本：v1.3.4

- v1.2.1
- v1.2.2
- v1.2.3
- v1.2.4
- v1.2.5
- v1.2.6
- v1.2.7
- v1.3.0
- v1.3.1
- v1.3.2
- v1.3.3
- v1.3.4
- 共 22 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require zippendo/zippendo-php`
- Packagist 仓库：https://repo.packagist.org/p2/zippendo/zippendo-php.json
- 许可证：MIT
- PHP 要求：^8.1
