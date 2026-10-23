# amjadiqbal/laravel-redis-advisor

> 标签: amjadiqbal, big-keys, cache, eviction, horizon, laravel, laravel-package, maxmemory, phpredis, predis, queue, redis, redis-health, ttl, valkey

## 简介

Read-only Redis and Valkey health advisor for Laravel: finds queues that can silently lose jobs to eviction, keys with no TTL, big keys, memory and fragmentation trouble, persistence turned off under queues, cache prefix collisions, Horizon backlog and session TTL drift, with the exact config line or command to fix each one. Artisan report with a CI exit code plus a Blade dashboard.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://amjad.com.pk/laravel/packages/laravel-redis-advisor
- 源码仓库：https://github.com/amjadiqbal/laravel-redis-advisor.git
- Packagist 页面：https://packagist.org/packages/amjadiqbal%2Flaravel-redis-advisor

## 历史版本号

- 当前版本：v0.1.1

- v0.1.0
- v0.1.1

## 获取地址

- Composer 安装：`composer require amjadiqbal/laravel-redis-advisor`
- Packagist 仓库：https://repo.packagist.org/p2/amjadiqbal/laravel-redis-advisor.json
- 许可证：MIT
- PHP 要求：^8.3
