# cboxdk/laravel-siem

> 标签: Audit, SIEM, cef, circuit-breaker, dead-letter, delivery, elastic-ecs, graylog-gelf, laravel, log-streaming, outbox, redaction, security-events, splunk-hec, ssrf

## 简介

The SIEM log-streaming delivery engine for Laravel — a durable transactional outbox, queued batched delivery with retry/backoff/dead-letter/circuit-breaker, SSRF-guarded HTTP egress, encrypted destination secrets, and PII redaction, on top of the framework-agnostic cboxdk/siem core.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/cboxdk/laravel-siem
- 源码仓库：https://github.com/cboxdk/laravel-siem.git
- Packagist 页面：https://packagist.org/packages/cboxdk%2Flaravel-siem

## 历史版本号

- 当前版本：v0.1.1

- v0.1.0
- v0.1.1

## 获取地址

- Composer 安装：`composer require cboxdk/laravel-siem`
- Packagist 仓库：https://repo.packagist.org/p2/cboxdk/laravel-siem.json
- 许可证：MIT
- PHP 要求：^8.4
