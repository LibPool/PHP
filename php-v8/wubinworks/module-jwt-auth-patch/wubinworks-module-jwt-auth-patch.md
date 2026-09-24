# wubinworks/module-jwt-auth-patch

> 标签: Authentication, cosmic sting, cve-2024-34102, encryption key, jwt, key rotation, magento 2, patch, token, webapi

## 简介

Fix the JWT authentication vulnerability on certain Magento 2 versions. Deny tokens issued by old encryption key. If you cannot upgrade Magento or cannot apply the official patch, try this one.

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://www.wubinworks.com
- 源码仓库：https://github.com/wubinworks/magento2-jwt-auth-patch.git
- Packagist 页面：https://packagist.org/packages/wubinworks%2Fmodule-jwt-auth-patch

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require wubinworks/module-jwt-auth-patch`
- Packagist 仓库：https://repo.packagist.org/p2/wubinworks/module-jwt-auth-patch.json
- 许可证：OSL-3.0
- PHP 要求：>=7.3
