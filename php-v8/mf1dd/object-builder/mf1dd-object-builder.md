# mf1dd/object-builder

> 标签: Fixture, builder, data, factory, generator, mock, object, random, reflection, test

## 简介

Automatically creates fully populated PHP object instances with random, type-safe values. Designed for test fixtures and runtime object generation. Supports all PHP class types — regular classes, readonly classes, abstract classes, enums, traits, interfaces, and built-in stock classes like DateInterval or ArrayObject. Recursively resolves nested object graphs, detects property names for semantically meaningful values (timezone, email, firstname …), and offers constraint-based value ranges via a fluent API. No framework required; zero runtime dependencies beyond nikic/php-parser. PHP 8.2+.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/mf1dd%2Fobject-builder
- 源码仓库：https://github.com/MF1DD/ObjectBuilder.git
- Packagist 页面：https://packagist.org/packages/mf1dd%2Fobject-builder

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- Composer 安装：`composer require mf1dd/object-builder`
- Packagist 仓库：https://repo.packagist.org/p2/mf1dd/object-builder.json
- 许可证：MIT
- PHP 要求：^8.2
