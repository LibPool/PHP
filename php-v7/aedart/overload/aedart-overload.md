# aedart/overload

> 标签: Magic Method, Overload, __get, __isset, __set, __unset, property

## 简介

Provides means to dynamically deal with inaccessible properties, by implementing PHP's magic methods; __get(), __set(), __isset(), and __unset(). This package, however, enforces the usage of getters- and setters-methods, ensuring that if a property is indeed available, then its corresponding getter or setter method will be invoked. The term 'overload', in this context, refers to PHP’s own definition hereof. (http://php.net/manual/en/language.oop5.overloading.php)

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://github.com/aedart/overload
- 源码仓库：https://github.com/aedart/overload.git
- Packagist 页面：https://packagist.org/packages/aedart%2Foverload

## 历史版本号

- 当前版本：5.1.0

- 1.5.0
- 1.6.0
- 1.6.1
- 2.0.0
- 2.0.1
- 2.1.0
- 2.2.0
- 3.0.0
- 4.0.0
- 4.0.1
- 5.0.0
- 5.1.0
- 共 28 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require aedart/overload`
- Packagist 仓库：https://repo.packagist.org/p2/aedart/overload.json
- 许可证：BSD-3-Clause
- PHP 要求：>=7.1.0
