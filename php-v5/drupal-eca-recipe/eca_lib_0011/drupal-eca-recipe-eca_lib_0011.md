# drupal-eca-recipe/eca_lib_0011

> 标签: PHP

## 简介

Increments a site-wide counter and returns it, keeping the value between requests in ECA's own persistent store rather than in Drupal's state service. An "Acquire lock" action guards the read and the write so that two concurrent requests cannot receive the same number.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0011
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0011
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0011

## 历史版本号

- 当前版本：3.2.9

- 1.2.0
- 3.2.0
- 3.2.1
- 3.2.2
- 3.2.3
- 3.2.4
- 3.2.5
- 3.2.6
- 3.2.7
- 3.2.8
- 3.2.9

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0011`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0011.json
- 许可证：GPL-2.0-or-later
