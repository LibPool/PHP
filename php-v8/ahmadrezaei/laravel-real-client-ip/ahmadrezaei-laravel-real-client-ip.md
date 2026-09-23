# ahmadrezaei/laravel-real-client-ip

> 标签: cdn, client-ip, cloudflare, ingress-nginx, ip-spoofing, laravel, middleware, php, real-ip, remote-addr, reverse-proxy, security, trusted-proxy, x-forwarded-for

## 简介

Laravel middleware that restores the real client IP behind a CDN, load balancer or ingress controller that overwrites X-Forwarded-For, verified with a shared secret so the header cannot be spoofed.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/ahmadrezaei/laravel-real-client-ip
- 源码仓库：https://github.com/ahmadrezaei/laravel-real-client-ip.git
- Packagist 页面：https://packagist.org/packages/ahmadrezaei%2Flaravel-real-client-ip

## 历史版本号

- 当前版本：v1.0.0

- v1.0.0

## 获取地址

- Composer 安装：`composer require ahmadrezaei/laravel-real-client-ip`
- Packagist 仓库：https://repo.packagist.org/p2/ahmadrezaei/laravel-real-client-ip.json
- 许可证：MIT
- PHP 要求：^8.2
