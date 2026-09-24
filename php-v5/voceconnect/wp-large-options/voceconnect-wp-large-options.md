# voceconnect/wp-large-options

> 标签: PHP

## 简介

You may wish to store a larger option value than is recommended on WordPress.com. If your option data will exceed 400K, or is of an unpredictable size (such as an HTML fragment etc.) you should use the wp_large_options plugin to store the option in a cache-safe manner. Failure to do this could result in the option not being cached, and instead fetched repeatedly from the DB, which could cause performance problems.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/voceconnect%2Fwp-large-options
- 源码仓库：https://github.com/voceconnect/wp-large-options.git
- Packagist 页面：https://packagist.org/packages/voceconnect%2Fwp-large-options

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- Composer 安装：`composer require voceconnect/wp-large-options`
- Packagist 仓库：https://repo.packagist.org/p2/voceconnect/wp-large-options.json
- 许可证：GPL-2.0+
