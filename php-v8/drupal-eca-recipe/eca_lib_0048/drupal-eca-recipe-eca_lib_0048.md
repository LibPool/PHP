# drupal-eca-recipe/eca_lib_0048

> 标签: PHP

## 简介

Adds two AI-powered buttons to the Business node form. "Look up the address" asks a chat model for the company's postal address and fills the compound Address field, "Look up the website" fills the Link field. Each branch sends the node title and the body text to the chat model with a strict JSON schema, decodes the answer and maps it onto the field's properties, so a country code, street, city and postal code land in the widget for the editor to review before saving. After applying the recipe, select a chat model that supports structured output in both chat actions. Requires ECA Field Widget Actions 1.0.x-dev newer than 1.0.0-beta2, because the compound fill and its "use_yaml" setting are unreleased. The recipe ships the Business content type with its Address and Link fields.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0048
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0048
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0048

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0048`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0048.json
- 许可证：GPL-2.0-or-later
