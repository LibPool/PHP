# charm/router

> 标签: PHP

## 简介

A very fast, tiny single file router implementation. Compatible with PSR Middlware. Takes you from /users/{id:\d+} to `User::profile($id)`. Also in reverse: `$router->url([User::class, 'profile'], 123)` gives you the URL.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://bitbucket.org/ennerd/charm-router
- 源码仓库：https://bitbucket.org/ennerd/charm-router.git
- Packagist 页面：https://packagist.org/packages/charm%2Frouter

## 历史版本号

- 当前版本：0.0.9

- 0.0.1
- 0.0.2
- 0.0.3
- 0.0.4
- 0.0.5
- 0.0.6
- 0.0.7
- 0.0.8
- 0.0.9

## 获取地址

- Composer 安装：`composer require charm/router`
- Packagist 仓库：https://repo.packagist.org/p2/charm/router.json
- 许可证：MIT
