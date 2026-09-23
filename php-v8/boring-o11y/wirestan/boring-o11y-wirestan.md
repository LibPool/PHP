# boring-o11y/wirestan

> 标签: PHPStan, larastan, laravel, livewire, phpstan-extension, phpstan-rules, security, static-analysis

## 简介

PHPStan rule for Livewire components: public properties that are never reassigned outside lifecycle methods must be marked #[Locked], so the client cannot tamper with them via $wire.set.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/boring-o11y/wirestan
- 源码仓库：https://github.com/boring-o11y/wirestan.git
- Packagist 页面：https://packagist.org/packages/boring-o11y%2Fwirestan

## 历史版本号

- 当前版本：v0.1.0

- v0.1.0

## 获取地址

- Composer 安装：`composer require boring-o11y/wirestan`
- Packagist 仓库：https://repo.packagist.org/p2/boring-o11y/wirestan.json
- 许可证：MIT
- PHP 要求：^8.2
