# cloud-castle/cache

> 标签: cache, cache-pool, cloud-castle, hmac, lru, memcached, namespaces, php, php8, psr-16, psr-6, redis, serialization, simple-cache, stampede, tags, ttl

## 简介

Кэш для PHP 8.1+: PSR-16 и PSR-6 из одного пакета, remember со stampede-защитой (XFetch), теги с O(1)-инвалидацией, пространства имён, цепочки L1/L2, LRU-лимит, нативные счётчики с сохранением TTL, статистика, prune, детерминированный TTL в тестах (PSR-20). Бэкенды: память, файлы с атомарной записью, Redis и Memcached; безопасная сериализация (белые списки классов, HMAC-подпись). Нулевые тяжёлые зависимости.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/cloud-castle/cache
- 源码仓库：https://gitverse.ru/cloud-castle/cache
- Packagist 页面：https://packagist.org/packages/cloud-castle%2Fcache

## 历史版本号

- 当前版本：v1.2.2

- v0.1.0
- v0.1.1
- v1.0.0
- v1.0.1
- v1.0.2
- v1.1.0
- v1.1.1
- v1.2.0
- v1.2.1
- v1.2.2

## 获取地址

- Composer 安装：`composer require cloud-castle/cache`
- Packagist 仓库：https://repo.packagist.org/p2/cloud-castle/cache.json
- 许可证：MIT
- PHP 要求：>=8.1
