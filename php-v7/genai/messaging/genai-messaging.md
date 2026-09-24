# genai/messaging

> 标签: PHP

## 简介

Provider-agnostic messaging front (the third twin of genai/web and genai/console): the Producer/Consumer/MessageEvent contracts, a #[MessageHandler] attribute, a build-time MessageHandlerProcessor that compiles consumers.php, and a PHP 5.3-safe Worker runner that dispatches to handler beans. Ships NO broker — each app registers its own Consumer/Producer (Kafka, Pdo, SQS, ...). Shares the same compiled container as the web and CLI fronts.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/genai%2Fmessaging
- 源码仓库：https://github.com/GenAIIO/php-messaging.git
- Packagist 页面：https://packagist.org/packages/genai%2Fmessaging

## 历史版本号

- 当前版本：v1.0.1

- 1.0.0
- v1.0.1

## 获取地址

- Composer 安装：`composer require genai/messaging`
- Packagist 仓库：https://repo.packagist.org/p2/genai/messaging.json
- 许可证：Apache-2.0
- PHP 要求：>=5.3.0
