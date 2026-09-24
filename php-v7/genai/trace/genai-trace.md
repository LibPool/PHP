# genai/trace

> 标签: PHP

## 简介

Request correlation IDs for centralized logging. A TraceInterceptor reads X-Request-Id (or generates one), exposes it via a TraceContext bean + a global trace_id(), echoes it on the response, and a Monolog processor stamps it on every log line. PHP 5.3-safe at runtime.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/genai%2Ftrace
- 源码仓库：https://github.com/GenAIIO/php-trace.git
- Packagist 页面：https://packagist.org/packages/genai%2Ftrace

## 历史版本号

- 当前版本：v1.0.1

- 1.0.0
- v1.0.1

## 获取地址

- Composer 安装：`composer require genai/trace`
- Packagist 仓库：https://repo.packagist.org/p2/genai/trace.json
- 许可证：Apache-2.0
- PHP 要求：>=5.3.0
