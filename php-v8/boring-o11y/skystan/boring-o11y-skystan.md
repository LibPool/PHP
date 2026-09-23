# boring-o11y/skystan

> 标签: PHPStan, jobs, larastan, laravel, phpstan-extension, phpstan-rules, queue, static-analysis

## 简介

Larastan/PHPStan rules for queued Laravel jobs: ShouldBeUnique jobs must declare uniqueFor and (when parameterized) uniqueId, unique jobs may not be batched or bulk-dispatched, batched jobs must be Batchable and honour cancellation, and jobs holding an Eloquent model in a public property must use SerializesModels.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/boring-o11y/skystan
- 源码仓库：https://github.com/boring-o11y/skystan.git
- Packagist 页面：https://packagist.org/packages/boring-o11y%2Fskystan

## 历史版本号

- 当前版本：v0.1.0

- v0.1.0

## 获取地址

- Composer 安装：`composer require boring-o11y/skystan`
- Packagist 仓库：https://repo.packagist.org/p2/boring-o11y/skystan.json
- 许可证：MIT
- PHP 要求：^8.2
