# igne-agency/laravel-boot-up

> 标签: bitbucket-pipelines, boot-up, ci-cd, deployment, dev-tools, development, forge, fortrabbit, github-actions, herd, laravel, local-development, onboarding, sail

## 简介

Boot a Laravel project on any machine with one command: php artisan app:up installs missing tools (PHP, Node, Composer, Herd, Docker), creates .env, sets up the database, runs migrations, builds assets and serves via Herd, Sail or artisan serve, then runs Laravel's own dev terminal and cleanly stops everything it started when you quit it; app:down does the same on demand. Also exports deployment scripts for Laravel Forge and fortrabbit (generate:deploy-script) and generates CI/CD pipelines with linting, tests and webhook deploys for GitHub Actions and Bitbucket Pipelines (generate:pipeline). Development only - not for production use.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/igne-agency%2Flaravel-boot-up
- 源码仓库：https://github.com/IGNE-Agency/laravel-boot-up-package.git
- Packagist 页面：https://packagist.org/packages/igne-agency%2Flaravel-boot-up

## 历史版本号

- 当前版本：v3.2.0

- v1.0.0
- v1.1.0
- v2.0.0
- v3.0.0
- v3.1.0
- v3.2.0

## 获取地址

- Composer 安装：`composer require igne-agency/laravel-boot-up`
- Packagist 仓库：https://repo.packagist.org/p2/igne-agency/laravel-boot-up.json
- 许可证：MIT
- PHP 要求：^8.3
