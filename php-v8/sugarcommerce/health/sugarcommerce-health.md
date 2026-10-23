# sugarcommerce/health

> 标签: alerts, deploy, diagnostics, doctor, health

## 简介

The mechanism of a doctor script: collect ok/warn/fail checks, print an aligned report, exit non-zero on failure so a deploy can be gated on it, and post the failures to a chat webhook. The checks themselves stay in your application.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/sugarcommerce/health
- 源码仓库：https://github.com/SugarCommerce/health.git
- Packagist 页面：https://packagist.org/packages/sugarcommerce%2Fhealth

## 历史版本号

- 当前版本：1.1.0

- 1.1.0

## 获取地址

- Composer 安装：`composer require sugarcommerce/health`
- Packagist 仓库：https://repo.packagist.org/p2/sugarcommerce/health.json
- 许可证：GPL-2.0-or-later
- PHP 要求：>=8.5
