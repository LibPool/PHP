# drupal-eca-recipe/eca_lib_0045

> 标签: PHP

## 简介

Separates two questions that are routinely conflated: whether a field changed, and what its previous value was. The condition Entity: field value changed answers the first on its own, with no original entity, no token and no loop. Only the message text needs the old title, so the model additionally loads the unchanged article and reads it back as [original_article:title]. There is no token for a previous field value, and [user:unchanged:field_user_networks] and its variants do not exist.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0045
- 源码仓库：https://gitlab.lakedrops.com/drupal/recipes/eca_lib_0045
- Packagist 页面：https://packagist.org/packages/drupal-eca-recipe%2Feca_lib_0045

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- Composer 安装：`composer require drupal-eca-recipe/eca_lib_0045`
- Packagist 仓库：https://repo.packagist.org/p2/drupal-eca-recipe/eca_lib_0045.json
- 许可证：GPL-2.0-or-later
