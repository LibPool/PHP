# invoicetronic/php-sdk

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

The [Invoicetronic API][2] is a RESTful service that allows you to send and receive invoices through the Italian [Servizio di Interscambio (SDI)][1], or Interchange Service. The API is designed to be simple and easy to use, abstracting away SDI complexity while providing complete control over the invoice send/receive process. It provides advanced features as encryption at rest, multi-language pre-flight invoice validation, multiple upload formats, webhooks, event logging, client SDKs, and CLI tools.  For more information, see  [Invoicetronic website][2]  ## Before you start  For the full integration guide, tutorials, SDKs and quickstarts, see the **[Documentation](https://invoicetronic.com/en/docs/)**. A few cross-cutting topics worth knowing before integrating:  - **[Prerequisites](https://invoicetronic.com/en/docs/prerequisites/)** — what you need to start in Sandbox and what's required to move to production. - **[API Keys](https://invoicetronic.com/en/docs/apikeys/)** — how `ik_live_` and `ik_test_` keys select the environment. - **[Sandbox](https://invoicetronic.com/en/docs/sandbox/)** — free test environment that mirrors the live workflow, with no credits consumed. - **[Rate Limiting](https://invoicetronic.com/en/docs/ratelimiting/)** — per-second, per-minute and per-day limits; how to handle `429 Too Many Requests`. - **[Pagination](https://invoicetronic.com/en/docs/pagination/)** — `page` and `page_size` parameters and the `Invoicetronic-Total-Count` response header. - **[CORS](https://invoicetronic.com/en/docs/cors/)** — calling the API from the browser; allowed origins are configured per key. - **[Webhooks](https://invoicetronic.com/en/docs/webhooks/)** — real-time event notifications with HMAC-SHA256 signature validation. - **[Localization](https://invoicetronic.com/en/docs/accept-language/)** — use the `Accept-Language` header to receive error messages in Italian, English or German.  [1]: https://www.fatturapa.gov.it/it/sistemainterscambio/cose-il-sdi/ [2]: https://invoicetronic.com/

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://invoicetronic.com
- 源码仓库：https://github.com/invoicetronic/php-sdk.git
- Packagist 页面：https://packagist.org/packages/invoicetronic%2Fphp-sdk

## 历史版本号

- 当前版本：v1.11.0

- v1.1.6
- v1.1.7
- v1.10.0
- v1.11.0
- v1.2.0
- v1.3.0
- v1.4.0
- v1.5.0
- v1.6.0
- v1.7.0
- v1.8.0
- v1.9.0
- 共 20 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require invoicetronic/php-sdk`
- Packagist 仓库：https://repo.packagist.org/p2/invoicetronic/php-sdk.json
- 许可证：MIT
- PHP 要求：^8.1
