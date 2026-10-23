# mk-josias/laravel-distributable

> 标签: distributable, events, laravel, microservices, modular-monolith, modules, outbox

## 简介

The foundations for designing each Laravel module as a microservice: its code runs in a context bounded to its module, blind to the others, whether they run in the same process or in separate, distributed processes, and it talks to them only through messages and events. Whether modules run as microservices or several to a process, depending on load, release pace or cost, becomes an infrastructure choice rather than a code one, allowing greater flexibility.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://mk-josias.github.io/laravel-distributable/
- 源码仓库：https://github.com/mk-josias/laravel-distributable-core.git
- Packagist 页面：https://packagist.org/packages/mk-josias%2Flaravel-distributable

## 历史版本号

- 当前版本：v0.4.0

- v0.3.0
- v0.4.0

## 获取地址

- Composer 安装：`composer require mk-josias/laravel-distributable`
- Packagist 仓库：https://repo.packagist.org/p2/mk-josias/laravel-distributable.json
- 许可证：MIT
- PHP 要求：^8.4
