# griffnode/php-sdk

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

Accept Bitcoin, Litecoin, Dogecoin, Dash, Ethereum and ERC-20 tokens. Server-to-server, authenticated with a secret API key (`Authorization: Bearer sk_live_…` for live, or `sk_test_…` for test mode — same base URL). All monetary amounts in API responses are JSON numbers; **webhook** amounts are strings to preserve decimal precision (see the `webhooks` section).  **Rate limits.** Every request is rate-limited per API key in two windows — per minute and per hour — by plan tier (min/hour): starter 30/500, business 100/2000, professional 300/5000, enterprise 1000/20000. Every response carries `X-RateLimit-Limit`, `X-RateLimit-Remaining` and `X-RateLimit-Reset` (Unix seconds) for the per-minute window. On `429` the body is `error: "RATE_LIMIT_EXCEEDED"` (either window) with a `Retry-After` header (seconds) — clients should retry after it. A separate `429` with `error: "MONTHLY_LIMIT_REACHED"` means the plan's monthly transaction quota (not the request rate).

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://griffnode.com
- 源码仓库：https://github.com/GriffNode/php-sdk.git
- Packagist 页面：https://packagist.org/packages/griffnode%2Fphp-sdk

## 历史版本号

- 当前版本：1.1.0

- 1.1.0

## 获取地址

- Composer 安装：`composer require griffnode/php-sdk`
- Packagist 仓库：https://repo.packagist.org/p2/griffnode/php-sdk.json
- 许可证：Apache-2.0
- PHP 要求：^7.4 || ^8.0
