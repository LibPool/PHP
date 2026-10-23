# likun-mci/php-composer

> 标签: PSR-4, autoload, composer, composer-lock, dependency-manager, dependency-resolution, http, no-exec, package-manager, packagist, php-composer, proxy, restricted-hosting, semver, shared-hosting, socks5, vendor

## 简介

用原生 PHP 实现的 Composer 包管理器：依赖求解、下载安装、autoload 生成全程只走 HTTP，不调用任何 shell 命令。为禁用 exec/proc_open 的共享主机与受管控服务器而写，产出的 vendor 目录与官方 Composer 完全兼容，支持 HTTP/SOCKS5 代理。

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://github.com/likun-mci/php-composer
- 源码仓库：https://github.com/likun-mci/php-composer.git
- Packagist 页面：https://packagist.org/packages/likun-mci%2Fphp-composer

## 历史版本号

- 当前版本：v1.2.4

- v1.0.0
- v1.1.0
- v1.1.1
- v1.2.0
- v1.2.1
- v1.2.2
- v1.2.3
- v1.2.4

## 获取地址

- Composer 安装：`composer require likun-mci/php-composer`
- Packagist 仓库：https://repo.packagist.org/p2/likun-mci/php-composer.json
- 许可证：MIT
- PHP 要求：>=7.1
