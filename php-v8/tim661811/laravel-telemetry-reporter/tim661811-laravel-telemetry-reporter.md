# tim661811/laravel-telemetry-reporter

> 标签: Metrics, analytics, feature-flags, laravel, laravel-package, laravel-telemetry-reporter, license-checking, observer, reporter, telemetry, tim661811

## 简介

A reusable Laravel 10+ package that lets you annotate any service method with a PHP attribute to collect custom telemetry (e.g. user counts, disk usage, feature flags) and automatically report it—at configurable intervals—to a central server over HTTP. Data is grouped per application host, is fully configurable via a published telemetry.php config (backed by your chosen cache), and integrates seamlessly with Laravel’s scheduler and HTTP client.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/tim661811/laravel-telemetry-reporter
- 源码仓库：https://github.com/tim661811/laravel-telemetry-reporter.git
- Packagist 页面：https://packagist.org/packages/tim661811%2Flaravel-telemetry-reporter

## 历史版本号

- 当前版本：1.0

- 0.1
- 0.1.1
- 0.2
- 0.3
- 0.4
- 1.0

## 获取地址

- Composer 安装：`composer require tim661811/laravel-telemetry-reporter`
- Packagist 仓库：https://repo.packagist.org/p2/tim661811/laravel-telemetry-reporter.json
- 许可证：MIT
- PHP 要求：^8.1
