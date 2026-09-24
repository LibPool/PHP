# fyrst/shopware-cd

> 标签: ci, deploy, docker, flex, shopware, symfony

## 简介

Thin Packagist library for fyrst.dev Shopware continuous deploy. Provides fyrst:sales-channel:rewrite-urls (sales_channel_domain.url after a non-live DB restore). Overlay files (CI, deploy Compose, .env.example) ship in overlay/ for Symfony Flex copy-from-package. The Flex recipe (fyrst-dev/recipes) is metadata only. Operators use fyrst-cli 0.1.0+ only. Dump stays shopware-cli. Root compose.yaml, .gitignore, and .shopware-project.yml / .yaml are owned by shopware-cli. Image builds use docker/Dockerfile from shopware/docker. Not a Shopware installation.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/fyrst-dev/shopware-cd
- 源码仓库：https://github.com/fyrst-dev/shopware-cd.git
- Packagist 页面：https://packagist.org/packages/fyrst%2Fshopware-cd

## 历史版本号

- 当前版本：1.1.0

- 1.0.0
- 1.1.0

## 获取地址

- Composer 安装：`composer require fyrst/shopware-cd`
- Packagist 仓库：https://repo.packagist.org/p2/fyrst/shopware-cd.json
- 许可证：MIT
- PHP 要求：>=8.2
