# mouf/utils.common.lock

> 标签: lock, mouf

## 简介

A simple package that provides functions to get a lock. Typically, you want to use locks when you want to be sure that 2 actions do not happen at the same time. For instance, if you regularly schedule cron tasks, you might want to be sure the last cron task finished before running the new one. A lock can help you do that.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：http://mouf-php.com/packages/mouf/utils.common.lock
- 源码仓库：https://github.com/thecodingmachine/utils.common.lock.git
- Packagist 页面：https://packagist.org/packages/mouf%2Futils.common.lock

## 历史版本号

- 当前版本：v1.0.0

- v1.0.0

## 获取地址

- Composer 安装：`composer require mouf/utils.common.lock`
- Packagist 仓库：https://repo.packagist.org/p2/mouf/utils.common.lock.json
- 许可证：MIT
- PHP 要求：>=5.3.0
