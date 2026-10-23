# ordereazi/commerce-sdk

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

Build a fully custom headless storefront - your own web app, mobile app, or POS - against a             single OE Commerce store. Every endpoint below is namespaced under `/api/v1/store/...`. Building             admin/back-office tooling instead? See [/docs/admin](/docs/admin).              New here? [/guides/store](/guides/store) walks through getting a key, the anonymous cart             session, and calling your first endpoints step by step - this page is the field-level reference             to come back to afterward.              ## Getting Started              1. Click the **Authorize** button at the top of this page.             2. Provide credentials:                - **X-Commerce-Key** (always required) - your store's Store Access Key from Backoffice >                  Settings > Application APIs. `pk_store_...` (publishable) is safe for browser/mobile code;                  `sk_store_...` (secret) is server-to-server only and is rejected outright if a browser                  Origin header is present.                - **Bearer** (only for endpoints acting on a specific customer - Account, Orders, Wishlists,                  etc.) - the token from **Auth > register** or **Auth > login**.              Once authorized, you can explore and test all available endpoints directly from this interface.              ## Anonymous Carts              A guest cart is tracked by an `X-Session-Ref` header, not a cookie - the server generates one on             your first request and echoes it back on every response after. Keep sending back whatever value             you last received. Logging in carries that same cart forward onto the customer's account             automatically, with no separate merge step.              ## Errors              Failures use RFC 9457 Problem Details (`application/problem+json`) with a stable `code` field             for programmatic handling, e.g. `store_key_invalid`, `store_key_revoked`, `store_key_scope_denied`,             `rate_limited`. A rejected *business* action (e.g. adding fewer than a product's minimum order             quantity to the cart) instead comes back as HTTP 200 with `"success": false` and a human-readable             `message` - always check `success` in the body, not just the HTTP status code.              ## Rate Limits              Requests are limited per Store Access Key (200/minute). The credential-stuffing surface             (register/login/forgot-password/reset-password) is limited more tightly per caller IP (10 per 5             minutes). A 429 response includes a `Retry-After` header.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/OrderEazi/commerce-sdk
- 源码仓库：https://github.com/OrderEazi/commerce-sdk-php.git
- Packagist 页面：https://packagist.org/packages/ordereazi%2Fcommerce-sdk

## 历史版本号

- 当前版本：1.1.4

- 1.0.0
- 1.0.1
- 1.1.0
- 1.1.1
- 1.1.2
- 1.1.3
- 1.1.4

## 获取地址

- Composer 安装：`composer require ordereazi/commerce-sdk`
- Packagist 仓库：https://repo.packagist.org/p2/ordereazi/commerce-sdk.json
- 许可证：MIT
- PHP 要求：^8.1
