# drupal-eca-recipe/eca_lib_0049

> 标签: PHP

## 简介

Adds an AI-powered button to the Event node form. "Extract the event details" sends the node title and the description to a chat model with a strict JSON schema and fills the compound Event details field, a Custom Field whose columns hold the venue, the city, the capacity, the ticket price, whether the event is online, a contact address and a registration link. Custom Field columns are defined by the site builder, so the mapping the fill action returns is keyed by those column names, and the typed columns cast the strings the schema asks for. After applying the recipe, select a chat model that supports structured output in the chat action. Requires ECA Field Widget Actions 1.0.x-dev at or after commit c7c3edb, because both the compound fill and the recognition of the custom_field field type are unreleased. The recipe ships the Event content type with its Event details field.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0049
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0049
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0049

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0049`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0049.json
- 许可证：GPL-2.0-or-later
