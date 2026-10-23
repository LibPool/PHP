# herdwatch-oss/monolog-ecs-formatter

> 标签: ECS, elasticsearch, formatter, logging, monolog, symfony

## 简介

Monolog formatter and Symfony bundle that promotes typed ECS value objects (metrics, labels, text, tags, service, user, tracing, error) to top-level ECS-aligned JSON fields for clean Elasticsearch mapping, with a default copy mode that also keeps the legacy Monolog top-level keys (channel, level_name, level, datetime) so existing dashboards keep working during migration.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/herdwatch-oss%2Fmonolog-ecs-formatter
- 源码仓库：https://github.com/herdwatch-oss/monolog-ecs-formatter.git
- Packagist 页面：https://packagist.org/packages/herdwatch-oss%2Fmonolog-ecs-formatter

## 历史版本号

- 当前版本：v0.2.1

- v0.1.0
- v0.2.0
- v0.2.1

## 获取地址

- Composer 安装：`composer require herdwatch-oss/monolog-ecs-formatter`
- Packagist 仓库：https://repo.packagist.org/p2/herdwatch-oss/monolog-ecs-formatter.json
- 许可证：MIT
- PHP 要求：>=8.3
