# genai/sql-mapper

> 标签: PHP

## 简介

MyBatis-style SQL mapper: mark an interface #[Mapper] and its methods #[Select]/#[Insert]/#[Update]/#[Delete] with the SQL. A build-time processor compiles a reflection-free Cache\<Name> implementation (prepared statements, #{name} bound params, optional row->object hydration) and registers it as a container bean keyed by the interface. Self-contained: a bundled DatabaseConfig provides the 'PDO' bean from a [database] group in the app's app.ini, so you only edit config. Runtime is PHP 5.3-safe.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/genai%2Fsql-mapper
- 源码仓库：https://github.com/GenAIIO/php-sql-mapper.git
- Packagist 页面：https://packagist.org/packages/genai%2Fsql-mapper

## 历史版本号

- 当前版本：v1.0.1

- 1.0.0
- v1.0.1

## 获取地址

- Composer 安装：`composer require genai/sql-mapper`
- Packagist 仓库：https://repo.packagist.org/p2/genai/sql-mapper.json
- 许可证：Apache-2.0
- PHP 要求：>=5.3.0
