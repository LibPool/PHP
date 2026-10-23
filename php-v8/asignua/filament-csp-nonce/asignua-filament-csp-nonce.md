# asignua/filament-csp-nonce

> 标签: content-security-policy, csp, filament, filament-plugin, laravel, nonce, security

## 简介

A strict Content-Security-Policy for Filament 5 panels without 'unsafe-inline' scripts: a per-request nonce wired into Laravel's Vite::useCspNonce() so Filament, Livewire and Vite tags carry it, nonces added to the inline script and style tags Filament still prints without one, a ready configurable CSP header (enforce or report-only) and an endpoint that collects violation reports. No Filament view is overridden.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/asignua/filament-csp-nonce
- 源码仓库：https://github.com/asignua/filament-csp-nonce.git
- Packagist 页面：https://packagist.org/packages/asignua%2Ffilament-csp-nonce

## 历史版本号

- 当前版本：v1.0.1

- v1.0.0
- v1.0.1

## 获取地址

- Composer 安装：`composer require asignua/filament-csp-nonce`
- Packagist 仓库：https://repo.packagist.org/p2/asignua/filament-csp-nonce.json
- 许可证：MIT
- PHP 要求：^8.3
