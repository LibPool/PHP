# drupal-eca-recipe/eca_lib_0038

> 标签: PHP

## 简介

Sends the article text to an AI chat model on presave and writes the structured answer into real node fields: SEO meta description, reading time, sentiment and Tags terms. Triggered by node entity presave, guarded so that each article is enriched only once. Includes the library's Article tags recipe, which provides the Article content type with its body and Tags fields and the Tags vocabulary. Requires the ai_integration_eca and eca_tamper contributed modules. After applying the recipe, select a chat model that supports structured output in the "Ask AI for structured enrichment data" action.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0038
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0038
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0038

## 历史版本号

- 当前版本：3.0.8

- 3.0.0
- 3.0.1
- 3.0.2
- 3.0.3
- 3.0.4
- 3.0.5
- 3.0.6
- 3.0.7
- 3.0.8

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0038`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0038.json
- 许可证：GPL-2.0-or-later
