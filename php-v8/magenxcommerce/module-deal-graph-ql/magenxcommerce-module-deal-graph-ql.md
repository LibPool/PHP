# magenxcommerce/module-deal-graph-ql

> 标签: PHP

## 简介

Extends Magento Catalog Price Rules with a merchandising deal label + type (deal / first-order) and exposes them over GraphQL: a `deals` query, a per-product `deal` badge (label, type, authoritative deal price from the rule, schedule/countdown) for grids and the PDP, and a `deals_enabled` store-config flag. Gift deals: a Cart Price Rule with a gift SKU adds that product to the cart at price 0 while the rule applies (`giftDeals` query, `CartItemInterface.deal_gift`). The Catalog Price Rule is the single source of truth for conditions, actions and pricing; this module only adds the presentation on top.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/magenxcommerce%2Fmodule-deal-graph-ql
- 源码仓库：https://github.com/magenxcommerce/module-deal-graph-ql.git
- Packagist 页面：https://packagist.org/packages/magenxcommerce%2Fmodule-deal-graph-ql

## 历史版本号

- 当前版本：v1.1.0

- v1.0.0
- v1.0.1
- v1.0.2
- v1.0.3
- v1.0.4
- v1.0.5
- v1.1.0

## 获取地址

- Composer 安装：`composer require magenxcommerce/module-deal-graph-ql`
- Packagist 仓库：https://repo.packagist.org/p2/magenxcommerce/module-deal-graph-ql.json
- 许可证：OSL-3.0, AFL-3.0
- PHP 要求：~8.3.0||~8.4.0||~8.5.0
