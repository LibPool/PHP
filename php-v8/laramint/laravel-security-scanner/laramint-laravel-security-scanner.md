# laramint/laravel-security-scanner

> 标签: SAST, laravel, owasp, scanner, security, static-analysis

## 简介

Laravel-aware security rules for php-security-scanner. Detects Laravel SQL injection (DB::raw, whereRaw), mass assignment, debug/dd leaks, unsafe validators, CSRF bypass, insecure cookies, env exposure, Blade raw echo, open redirect, Http SSRF, Storage/File path traversal, file-upload validation gaps, Auth/Crypt/Artisan/Process/Config injection, view-name injection, session fixation, and Mail header injection.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/laramint%2Flaravel-security-scanner
- 源码仓库：https://github.com/laramint/laravel-security-scanner.git
- Packagist 页面：https://packagist.org/packages/laramint%2Flaravel-security-scanner

## 历史版本号

- 当前版本：v0.1.0

- v0.1.0

## 获取地址

- Composer 安装：`composer require laramint/laravel-security-scanner`
- Packagist 仓库：https://repo.packagist.org/p2/laramint/laravel-security-scanner.json
- 许可证：MIT
- PHP 要求：^8.1
