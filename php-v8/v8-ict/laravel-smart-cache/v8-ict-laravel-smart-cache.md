# v8-ict/laravel-smart-cache

> 标签: PHP

## 简介

Allows  to capture the entire response with a middleware, and while caching it observer the checksum of the database tables used to create the response, if any related table has a modified checksum, it refreshes the response. This makes it serve live data, but then cached as long as it is not modified. Huge reduction of resource consumption and keep data live.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://bitbucket.org/v8-ict/laravel-smart-cache
- 源码仓库：https://bitbucket.org/v8-ict/laravel-smart-cache.git
- Packagist 页面：https://packagist.org/packages/v8-ict%2Flaravel-smart-cache

## 历史版本号

- 当前版本：v0.2.1

- v0.2.1

## 获取地址

- Composer 安装：`composer require v8-ict/laravel-smart-cache`
- Packagist 仓库：https://repo.packagist.org/p2/v8-ict/laravel-smart-cache.json
- 许可证：MIT
- PHP 要求：>=5.6.4
