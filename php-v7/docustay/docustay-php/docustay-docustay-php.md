# docustay/docustay-php

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

Send documents for signature and follow them, from your own software.  **Authentication.** Send `Authorization: Bearer <key>`. Make keys in Settings → Developers → API keys and give each only the scopes it needs (there are 12 in all): `documents:read`, `documents:write`, `people:read`, `plays:read`, `plays:write`, `drafts:write`, `templates:read`, `templates:write`, `webhooks:read`, `webhooks:write`, `account:read`, `embedded:write`. A key that starts `dsk_test_` works in **test mode**: documents it sends are practice runs (emailed only to the sender, stamped TEST, never counted or billed), it can only see and act on test documents (any other document answers `404`), and it can sign them itself with `POST /api/v1/documents/{id}/test-sign`. A key can also be limited to a list of addresses, given an expiry, or made **draft-only**.  **Draft-only keys.** A draft-only key can make and edit drafts but cannot send. Asking it to send answers `202` with an `approval`, the document stays a draft, and a person approves or declines in Settings → Developers → Approvals. Keys can also have a daily limit of drafts and sends; past it you get `429`.  **Payments.** A template may contain payment fields (text tag `type=payment` with a set `amount`, optionally a `deposit`, or an amount you give when you send it with `amount=custom.<name>`). The signer pays on Stripe's hosted page; the money goes to your own connected Stripe account; Docustay's fee is 2% on the Free plan and 0% on Pro, plus Stripe's own fees. The document's `payments` list shows each payment, its receipt and the fee. Card details never reach Docustay.  **Idempotency.** Requests that create a document or a template, or send one, need an `Idempotency-Key` header (8–200 characters). Repeating a request with the same key and body returns the first answer instead of doing it twice.  **Your own reference.** Documents and templates take `externalId` (your id for it) and `metadata` (up to 20 short key/value pairs). List with `externalId=` or `metadata[key]=value` to find them again, and both come back in webhooks.  **Errors.** Every error is `{ "error": { "kind", "message", "requestId", "retryable" } }`. `kind` is one of `invalid`, `unauthenticated`, `forbidden`, `not_found`, `conflict`, `rate_limited`, `dependency`, `timeout`. Quote the `requestId` to support, or search it in Settings → Developers → API log. **Plan limits** are `403 forbidden` with `error.detail.code`: `plan_document_limit` (the plan's documents this month are used) or `plan_template_limit` (Free: 5 new templates a month; a new version of a template you have does not count). Both carry `detail.used`, `detail.limit` and `detail.resetsAt` (the first of next month, UTC). Everything already made keeps working. Pro and self-hosted installs have no template limit.  **Rate limits.** Each key has its own per-minute budget. Every answer carries `RateLimit-Limit`, `RateLimit-Remaining` and `RateLimit-Reset` (seconds); over the budget you get `429` with a `Retry-After` header.  **Versions.** Every answer carries `Docustay-Version`, a date. A change that could break a caller gets a new date and is announced in the changelog before it ships; additions (a new field, a new route) are not breaking and do not change the date.  **Pagination.** Lists take `limit` (1–200) and `cursor`; the answer carries `page.nextCursor` (null on the last page).  **Signing links.** No response contains a signing link or access code, with one exception you control: a seat you send in `embedded` can be given an embedded signing session (`POST /api/v1/documents/{id}/embed-session`), a one-hour link for a frame on a website you listed. A key can start and follow a signature, and put your own signer in front of the form for seats you marked yourself; it cannot sign for anyone.

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/Docustay/docustay-php.git
- Packagist 页面：https://packagist.org/packages/docustay%2Fdocustay-php

## 历史版本号

- 当前版本：v0.2.1

- v0.1.0
- v0.1.1
- v0.1.2
- v0.2.0
- v0.2.1

## 获取地址

- Composer 安装：`composer require docustay/docustay-php`
- Packagist 仓库：https://repo.packagist.org/p2/docustay/docustay-php.json
- 许可证：unlicense
- PHP 要求：^7.4 || ^8.0
