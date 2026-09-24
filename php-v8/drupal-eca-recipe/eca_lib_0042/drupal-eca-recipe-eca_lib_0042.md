# drupal-eca-recipe/eca_lib_0042

> 标签: PHP

## 简介

Adds a Topic field and a Generate draft button to the Article node form. Selecting the button sends an Ajax request that fills the title and the body text in one go, without reloading the page and without saving the node. The topic is required for the button but not for saving, and the body is filled with HTML markup. The recipe brings in the library's Article content type; the button, the field and the behavior all come from the model, with no form display configuration needed.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0042
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0042
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0042

## 历史版本号

- 当前版本：1.0.3

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0042`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0042.json
- 许可证：GPL-2.0-or-later
