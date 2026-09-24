# drupal-eca-recipe/eca_lib_0004

> 标签: PHP

## 简介

Demonstrates how to express an if/elseif/else decision in an ECA model, the pattern people usually reach for when they want a PHP switch statement. ECA has neither a switch construct nor a working exclusive gateway, so the model uses the sentinel-default idiom instead: it assigns the default value up front, lets a matching branch overwrite it, and then, one hop downstream, tests whether the value is still the default in order to detect that nothing matched. Along the way it demonstrates the four-links-to-one-target OR idiom, in which several conditioned links leaving the same predecessor point at the same successor, so that any one of them is enough to run it.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0004
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0004
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0004

## 历史版本号

- 当前版本：3.3.3

- 3.2.0
- 3.2.1
- 3.2.2
- 3.2.3
- 3.2.4
- 3.2.5
- 3.2.6
- 3.2.7
- 3.3.0
- 3.3.1
- 3.3.2
- 3.3.3
- 共 13 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0004`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0004.json
- 许可证：GPL-2.0-or-later
