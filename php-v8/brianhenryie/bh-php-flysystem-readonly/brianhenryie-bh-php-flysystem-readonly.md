# brianhenryie/bh-php-flysystem-readonly

> 标签: Flysystem, Read-Only, adapter, copy-on-write, dry-run, filesystem, in-memory, readonly

## 简介

A League Flysystem adapter which wraps another adapter: reads pass through, writes and deletes are captured in memory so nothing ever touches the underlying filesystem. For --dry-run modes.

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/brianhenryie%2Fbh-php-flysystem-readonly
- 源码仓库：https://github.com/BrianHenryIE/bh-php-flysystem-readonly.git
- Packagist 页面：https://packagist.org/packages/brianhenryie%2Fbh-php-flysystem-readonly

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- Composer 安装：`composer require brianhenryie/bh-php-flysystem-readonly`
- Packagist 仓库：https://repo.packagist.org/p2/brianhenryie/bh-php-flysystem-readonly.json
- 许可证：MIT
- PHP 要求：^7.4 || ^8.0
