# jeffersongoncalves/laravel-page-cache

> 标签: jeffersongoncalves, laravel, laravel-page-cache

## 简介

This Laravel package provides a full-page response cache middleware for stateless public GET pages. It caches 200 responses keyed by a version token, locale, and theme cookie, skips authenticated requests, exposes an X-Page-Cache HIT/MISS header, and offers a static flush() helper to invalidate every cached page at once.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/jeffersongoncalves/laravel-page-cache
- 源码仓库：https://github.com/jeffersongoncalves/laravel-page-cache.git
- Packagist 页面：https://packagist.org/packages/jeffersongoncalves%2Flaravel-page-cache

## 历史版本号

- 当前版本：v1.3.0

- v1.0.0
- v1.0.1
- v1.1.0
- v1.1.1
- v1.2.0
- v1.3.0

## 获取地址

- Composer 安装：`composer require jeffersongoncalves/laravel-page-cache`
- Packagist 仓库：https://repo.packagist.org/p2/jeffersongoncalves/laravel-page-cache.json
- 许可证：MIT
- PHP 要求：^8.2
