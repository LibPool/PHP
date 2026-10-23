# drupal-eca-recipe/eca_lib_0051

> 标签: PHP

## 简介

Scores every newly submitted comment for toxicity and spam with one AI call that returns a strict JSON verdict, then routes that verdict through ordinary ECA conditions into one of three exits: publish, hold for review, or block. The thresholds are two "Token: set value" actions in the model, not numbers in the prompt, so the policy can be changed without touching the prompt. Every run writes both scores, both thresholds and the exit taken to the eca_comment_verdict log channel, and a failed or undecodable AI response holds the comment instead of publishing it. Requires the ai_integration_eca and eca_tamper contributed modules, and a chat model that supports structured output has to be selected in the "Ask AI to score the comment" action.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0051
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0051
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0051

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0051`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0051.json
- 许可证：GPL-2.0-or-later
