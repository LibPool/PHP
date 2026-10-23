# lockally/sdk

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

The lockally control plane lets integrators and direct customers manage everything except actual mail data flow (which uses standard JMAP / IMAP / SMTP-submission against the data plane endpoints).  **Authentication.** All `/v1/_*` endpoints require a Bearer API key in the `Authorization` header. Keys are formatted `lk_live_<8-char-prefix>_<32-char-secret>`, or `lk_test_<...>` for a test key. Create keys in the dashboard, or with `POST /v1/api-keys` using a key that holds `tenant:admin`.  The key's plan is checked on every request, so a key stops working if the account moves to a plan without API access, and works again if it moves back.  **Errors.** Failures return [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457) `application/problem+json` documents.  **Scopes.** Each endpoint requires a specific scope on the presented key. Insufficient scope returns `403` with the required scope name in `detail`.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/LockallyInc/lockally-php.git
- Packagist 页面：https://packagist.org/packages/lockally%2Fsdk

## 历史版本号

- 当前版本：0.3.3

- 0.1.0
- 0.2.0
- 0.3.0
- 0.3.1
- 0.3.2
- 0.3.3

## 获取地址

- Composer 安装：`composer require lockally/sdk`
- Packagist 仓库：https://repo.packagist.org/p2/lockally/sdk.json
- 许可证：unlicense
- PHP 要求：^8.1
