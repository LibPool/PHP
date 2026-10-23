# liufencn/flarum-user-delete

> 标签: PHP

## 简介

后台用户管理补回「删除用户」入口：Flarum 2.0 核心的编辑用户弹窗移除了删除按钮，但后端 DELETE /api/users/{id} 与 canDelete 字段仍在。本扩展在 EditUserModal 注入一个两步确认的删除按钮。

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/liufencn%2Fflarum-user-delete
- 源码仓库：https://github.com/LiuFenCN/flarum-ext-user-delete.git
- Packagist 页面：https://packagist.org/packages/liufencn%2Fflarum-user-delete

## 历史版本号

- 当前版本：v1.0.0

- v1.0.0

## 获取地址

- Composer 安装：`composer require liufencn/flarum-user-delete`
- Packagist 仓库：https://repo.packagist.org/p2/liufencn/flarum-user-delete.json
- 许可证：AGPL-3.0-or-later
