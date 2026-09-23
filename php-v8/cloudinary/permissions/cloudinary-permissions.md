# cloudinary/permissions

> 标签: cdn, cloud, cloudinary, image management, sdk

## 简介

Accounts with Permissions API access can manage custom permission policies. These policies assign permissions for a principal, allowing the principal to perform a specific action on a designated resource within a particular scope (your account or a product environment).   Refer to the [Permissions API guide](permissions_api_guide) for instructions on what to specify in the `policy_statement` to control Cloudinary activities, and to the Cedar schema, which defines the possible values for principals, actions, and resources.  The API uses **Basic Authentication** over HTTPS. Your **Provisioning Key** and **Provisioning Secret** are used for the authentication. These credentials (as well as your ACCOUNT_ID) are located in the [Cloudinary Console](https://console.cloudinary.com/pm) under **Settings > Account > Provisioning API Access**.  The Permissions API has dedicated SDKs for the following languages:  * JavaScript * PHP * Java

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://support.cloudinary.com
- 源码仓库：https://github.com/cloudinary/permissions-php.git
- Packagist 页面：https://packagist.org/packages/cloudinary%2Fpermissions

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require cloudinary/permissions`
- Packagist 仓库：https://repo.packagist.org/p2/cloudinary/permissions.json
- 许可证：MIT
- PHP 要求：^8.1
