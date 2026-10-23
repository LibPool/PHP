# malkusch/php-autoloader

> 标签: autoload, autoloader

## 简介

This autoloader supports every autoloadable PHP feature up to PHP 5.4’s traits. It find’s every class, interface or traits definition in any situation. No matter what convention is used. The autoloader is index based. After building the index there will be no performance issue. The building is done dynamically. There is no explicit need of calling a build script. For the sake of comfortability there exists a script for prebuilding an index.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：http://php-autoloader.malkusch.de/en/
- 源码仓库：https://github.com/malkusch/php-autoloader.git
- Packagist 页面：https://packagist.org/packages/malkusch%2Fphp-autoloader

## 历史版本号

- 当前版本：1.14.6

- 1.14.1.1
- 1.14.1.2
- 1.14.2
- 1.14.3
- 1.14.4
- 1.14.5
- 1.14.6

## 获取地址

- Composer 安装：`composer require malkusch/php-autoloader`
- Packagist 仓库：https://repo.packagist.org/p2/malkusch/php-autoloader.json
- 许可证：GPL-3.0+
- PHP 要求：>=5.4.0
