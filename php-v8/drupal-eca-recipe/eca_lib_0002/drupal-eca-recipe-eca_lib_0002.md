# drupal-eca-recipe/eca_lib_0002

> 标签: PHP

## 简介

Demonstrates how conditions are combined in ECA, where a successor link carries at most one condition and every combination is therefore built from the arrangement of links. The model shows the three idioms that follow from that constraint. An AND is chained through a pass-through action, an OR is drawn as several conditioned links into one target, and a nested combination composes the two into (A or B) and (C or D). It is driven entirely from the command line, reading three inputs from Drupal persistent state and reporting which of its three rules matched, so that changing one input and triggering again shows a different set of paths.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0002
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0002
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0002

## 历史版本号

- 当前版本：3.2.0

- 1.1.0
- 3.1.0
- 3.1.1
- 3.1.2
- 3.1.3
- 3.1.4
- 3.1.5
- 3.1.6
- 3.1.7
- 3.2.0

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0002`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0002.json
- 许可证：GPL-2.0-or-later
