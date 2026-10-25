# magenxcommerce/module-price-history-graph-ql

> 标签: PHP

## 简介

Tracks a rolling daily snapshot of each product's final price and exposes the lowest price over a configurable look-back window (default 30 days) over GraphQL as `ProductInterface.price_history`, plus a `price_history_enabled` store-config flag. This is the EU Omnibus Directive (Art. 6a of Directive 98/6/EC) "prior price" — the lowest price applied during at least the 30 days before a price reduction, which must be shown whenever a reduction is announced. A daily cron snapshots the native price index; the per-product field is a batch resolver, so it is safe on listing grids.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/magenxcommerce%2Fmodule-price-history-graph-ql
- 源码仓库：https://github.com/magenxcommerce/module-price-history-graph-ql.git
- Packagist 页面：https://packagist.org/packages/magenxcommerce%2Fmodule-price-history-graph-ql

## 历史版本号

- 当前版本：v1.0.2

- v1.0.0
- v1.0.1
- v1.0.2

## 获取地址

- Composer 安装：`composer require magenxcommerce/module-price-history-graph-ql`
- Packagist 仓库：https://repo.packagist.org/p2/magenxcommerce/module-price-history-graph-ql.json
- 许可证：OSL-3.0, AFL-3.0
- PHP 要求：~8.3.0||~8.4.0||~8.5.0
