# drupal-eca-recipe/eca_lib_0052

> 标签: PHP

## 简介

Intercepts every chat request that leaves the site through the AI module's provider proxy and sends the ones made on behalf of anonymous visitors to a cheaper provider and model, while a request made for an account keeps whatever the calling code chose. Nothing in the model calls an AI provider: it listens to the "AI request: before provider call" event that the ai_eca_interceptor submodule of AI Integration - ECA exposes, so it governs calls made by AI Assistants, automators, agents and custom code alike without owning any of them. The reroute is recorded as intent and executed by a subscriber that runs last, and it fails open - if the target provider throws, the originally chosen one answers instead. Requires the AI module at 1.4 or newer, and the provider and model ids in the reroute action have to be changed to a target configured on your site.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0052
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0052
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0052

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0052`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0052.json
- 许可证：GPL-2.0-or-later
