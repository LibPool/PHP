# zeus-server/bandwidth-throttler

> 标签: bandwidth, download limit, download speed, throttle, transfer limit, transfer speed

## 简介

This library can be used to limit (throttle) the speed of files served for download. It intercepts the PHP script output by setting a buffering handler that is called every time a given number of bytes are served to the browser. The library measures the time since the last time the PHP output buffer was flushed and hold on PHP for a while if the average download speed is above a given limit.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://github.com/artur-graniszewski/tigra-image-library
- 源码仓库：https://github.com/artur-graniszewski/Zeus-for-PHP-bandwidth-throttler.git
- Packagist 页面：https://packagist.org/packages/zeus-server%2Fbandwidth-throttler

## 历史版本号

- 当前版本：1.1.6

- 1.1.6

## 获取地址

- Composer 安装：`composer require zeus-server/bandwidth-throttler`
- Packagist 仓库：https://repo.packagist.org/p2/zeus-server/bandwidth-throttler.json
- 许可证：LGPL-3.0-only
- PHP 要求：^5.6
