# numerogeek/ebay-browse-api

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

<p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, image </b><a href="/api-docs/static/versioning.html#experimental " target="_blank"><img src="/cms/img/docs/experimental-icon.svg" class="legend-icon experimental-icon" alt="Experimental Method" title="Experimental Method" />(Experimental Method)</a>, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values, or UI parameters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  </ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href="/api-docs/static/oauth-client-credentials-grant.html">Application access token</a>.</p>

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/numerogeek/ebay-browse-api.git
- Packagist 页面：https://packagist.org/packages/numerogeek%2Febay-browse-api

## 历史版本号

- 当前版本：1.0

- 1.0

## 获取地址

- Composer 安装：`composer require numerogeek/ebay-browse-api`
- Packagist 仓库：https://repo.packagist.org/p2/numerogeek/ebay-browse-api.json
- 许可证：unlicense
- PHP 要求：^7.4 || ^8.0
