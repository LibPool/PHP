# jeffersongoncalves/laravel-ssrf-guard

> 标签: jeffersongoncalves, laravel, laravel-ssrf-guard

## 简介

A Laravel package that protects outbound HTTP requests from SSRF (Server-Side Request Forgery): it validates that a URL's host resolves only to public IPs (denying private, reserved, loopback and link-local ranges by default), pins the connection to the validated IP to close the DNS-rebinding TOCTOU window, and performs safe GET requests that re-validate every redirect hop.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/jeffersongoncalves/laravel-ssrf-guard
- 源码仓库：https://github.com/jeffersongoncalves/laravel-ssrf-guard.git
- Packagist 页面：https://packagist.org/packages/jeffersongoncalves%2Flaravel-ssrf-guard

## 历史版本号

- 当前版本：v1.1.0

- v1.0.0
- v1.0.1
- v1.1.0

## 获取地址

- Composer 安装：`composer require jeffersongoncalves/laravel-ssrf-guard`
- Packagist 仓库：https://repo.packagist.org/p2/jeffersongoncalves/laravel-ssrf-guard.json
- 许可证：MIT
- PHP 要求：^8.2
