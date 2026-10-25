# magenxcommerce/module-ai-mcp

> 标签: PHP

## 简介

Serves a Model Context Protocol (MCP) endpoint from Magento so an AI agent such as Claude Code can inspect and manage the backend: products with their images, links, variants, bundle options, downloadable links, attachments and custom options, categories, orders with their addresses, invoices, shipments and their tracking numbers, credit memos, customers, admin users, stock, tier prices, cart and catalog price rules, CMS pages and blocks, widgets, e-mail templates, design configuration and the media gallery, product attributes and attribute sets, URL rewrites, return requests, help desk tickets, quick search promotions, product reviews, storefront search terms, sales and customer reports, store configuration, caches, indexers, cron and the Magento logs and error reports. Authenticated with a Magento Integration access token, or with an admin's own OAuth 2.1 sign-in (PKCE, approved behind the admin login and two-factor check) so claude.ai custom connectors work, and authorized against that integration's or admin's ACL role; disabled by default, writes opt-in.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/magenxcommerce%2Fmodule-ai-mcp
- 源码仓库：https://github.com/magenxcommerce/module-ai-mcp.git
- Packagist 页面：https://packagist.org/packages/magenxcommerce%2Fmodule-ai-mcp

## 历史版本号

- 当前版本：v1.13.0

- v1.2.0
- v1.3.0
- v1.3.1
- v1.3.2
- v1.4.0
- v1.5.0
- v1.5.1
- v1.6.0
- v1.7.0
- v1.8.0
- v1.9.0
- v1.9.1
- 共 20 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require magenxcommerce/module-ai-mcp`
- Packagist 仓库：https://repo.packagist.org/p2/magenxcommerce/module-ai-mcp.json
- 许可证：OSL-3.0, AFL-3.0
- PHP 要求：~8.3.0||~8.4.0||~8.5.0
