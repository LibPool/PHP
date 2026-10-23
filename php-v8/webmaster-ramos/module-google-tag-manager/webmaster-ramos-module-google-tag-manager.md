# webmaster-ramos/module-google-tag-manager

> 标签: consent-mode, csp, google-tag-manager, gtm, hyva, magento2

## 简介

Google Tag Manager container loader for Adobe Commerce and Magento Open Source, Luma and Hyva. Loads the container only on listed production hosts, so staging and local copies of the production database send no hits or test orders. Hands the CSP nonce to gtm.js and to Custom HTML tags, so tags keep working on the strict-CSP checkout of Magento 2.4.7 and later. Sets Google Consent Mode v2 defaults before the container loads (denied in the EEA, UK and Switzerland) and updates them from Magento's cookie notice or leaves updates to an external consent platform.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://webmaster-ramos.com/extensions/google-tag-manager
- 源码仓库：https://github.com/webmaster-ramos/magento2-google-tag-manager.git
- Packagist 页面：https://packagist.org/packages/webmaster-ramos%2Fmodule-google-tag-manager

## 历史版本号

- 当前版本：1.0.1

- 1.0.1

## 获取地址

- Composer 安装：`composer require webmaster-ramos/module-google-tag-manager`
- Packagist 仓库：https://repo.packagist.org/p2/webmaster-ramos/module-google-tag-manager.json
- 许可证：OSL-3.0
- PHP 要求：~8.1.0||~8.2.0||~8.3.0||~8.4.0||~8.5.0
