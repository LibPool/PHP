# mhinspeya/mhinspeya-brand

> 标签: MHinspeya, magento, magento 2

## 简介

### 1. **Module Overview:**   - **Name:** Brand Inventory Manager   - **Purpose:** The module dynamically lists all the brands that have products currently in stock on the website, allowing customers to view and browse products by brand. This list updates automatically based on the store's inventory. ### 2. **Key Features:**   - **Dynamic Brand Listing:**     - The module generates a list of brands that have at least one product in stock.     - The list is updated in real-time based on changes in inventory levels (e.g., if a brand's products go out of stock, that brand is removed from the list).    - **Filter by Inventory:**     - Customers can filter the brand list by product availability, ensuring they only see brands with products they can purchase immediately.   - **Brand Page:**     - Each brand name in the list is clickable, leading to a dedicated brand page.     - The brand page displays all in-stock products for that brand, with options for sorting, filtering, and searching within the brand's catalog.    - **SEO-Friendly URLs:**     - The module creates SEO-friendly URLs for each brand page, enhancing visibility on search engines.    - **Inventory-Based Brand Widget:**     - A widget can be placed on various parts of the website (e.g., homepage, sidebar, footer) that highlights popular or new brands with available stock.   - **Admin Configuration:**     - The admin can configure how brands are displayed (e.g., sorting by popularity, alphabetical order, etc.).     - Options to include or exclude specific brands regardless of inventory (e.g., always show premium brands).   - **Caching Mechanism:**     - To ensure performance, the module uses caching to store brand lists, refreshing only when inventory changes occur. ### 3. **Integration with Other Features:**   - **Product Pages:** On each product page, the brand name is linked to the corresponding brand page.   - **Search Functionality:** When customers search for a brand name, the search results include the brand page and all relevant products. ### 4. **Customizable Design:**   - The module’s front-end is fully customizable, allowing the store’s design team to style the brand listing and pages in line with the overall website design. ### 5. **Reporting and Analytics:**   - The module provides reports on brand performance, showing metrics such as which brands are viewed most frequently, which have the highest sales, etc. ### 6. **Multi-Store Support:**   - For stores with multiple websites or store views, the module supports configuration per store view, allowing different brands to be highlighted in different regions or languages. This Magento module would be particularly useful for e-commerce stores with diverse product offerings across many brands, ensuring that customers have an efficient way to find and purchase products by their favorite brands.has context menu

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/mhinspeya%2Fmhinspeya-brand
- 源码仓库：https://git.modehaus.de/inspeya/inspeya-brand
- Packagist 页面：https://packagist.org/packages/mhinspeya%2Fmhinspeya-brand

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require mhinspeya/mhinspeya-brand`
- Packagist 仓库：https://repo.packagist.org/p2/mhinspeya/mhinspeya-brand.json
- 许可证：OSL-3.0
