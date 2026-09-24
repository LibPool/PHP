# drupal-eca-recipe/eca_lib_0050

> 标签: PHP

## 简介

An external MCP assistant drafts a conference talk with a user and submits it to Drupal, which owns every rule. The model turns the five tool arguments into tokens, checks the submission window, the audience level, the track and a per-level duration limit before anything is written, and returns a structured result either way. The speaker is taken from the authenticated account and is not a tool argument. A valid proposal is created unpublished in the talk_review workflow, awaiting human review, and the result carries a link to it. The beginner duration rule is a single action in the diagram, so changing it live changes the tool's behavior with no change on the assistant side.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0050
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0050
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0050

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0050`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0050.json
- 许可证：GPL-2.0-or-later
