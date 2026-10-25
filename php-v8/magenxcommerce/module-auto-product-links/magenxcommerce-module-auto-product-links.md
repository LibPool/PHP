# magenxcommerce/module-auto-product-links

> 标签: PHP

## 简介

Automatically fills Magento's native Related Products, Up-Sells and Cross-Sells, plus a Frequently Bought Together link type of its own, from editable rules - with a default rule for each, so the whole catalog is linked on the first cron run. A rule pairs a source condition tree (which products it applies to) with a target condition tree (the candidate pool), both built with the same attribute-picker widget as a Catalog Price Rule, so candidates can be matched on colour, size, price, category, manufacturer or any combination. Targets are chosen either by attribute similarity to the source (same colour, shared category, a price band) or from mined co-purchase history ("customers who bought this also bought"), which feeds the Frequently Bought Together link type exposed as ProductInterface.frequently_bought_together_products in GraphQL. Links are written straight into catalog_product_link, so related, up-sell and cross-sell links need no storefront change. A ledger table records every link the module authored, so merchant hand-picked links are never overwritten or deleted.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/magenxcommerce%2Fmodule-auto-product-links
- 源码仓库：https://github.com/magenxcommerce/module-auto-product-links.git
- Packagist 页面：https://packagist.org/packages/magenxcommerce%2Fmodule-auto-product-links

## 历史版本号

- 当前版本：v1.1.1

- v1.0.0
- v1.0.1
- v1.0.2
- v1.0.3
- v1.1.0
- v1.1.1

## 获取地址

- Composer 安装：`composer require magenxcommerce/module-auto-product-links`
- Packagist 仓库：https://repo.packagist.org/p2/magenxcommerce/module-auto-product-links.json
- 许可证：OSL-3.0, AFL-3.0
- PHP 要求：~8.3.0||~8.4.0||~8.5.0
