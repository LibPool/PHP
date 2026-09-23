# cdma-numiscorner/ebay-developer-key-management-api

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

Due to regulatory requirements applicable to our EU/UK sellers, for certain APIs, developers need to add digital signatures to the respective HTTP call. The Key Management API creates keypairs that are required when creating digital signatures for the following APIs:<ul><li>All methods in the <a href="/api-docs/sell/finances/resources/methods " target="_blank ">Finances API</a></li><li><a href="/api-docs/sell/fulfillment/resources/order/methods/issueRefund " target="_blank ">issueRefund</a> in the Fulfillment API</li><li><a href="/Devzone/XML/docs/Reference/eBay/GetAccount.html " target="_blank ">GetAccount</a> in the Trading API</li><li>The following methods in the Post-Order API:<ul><li><a href="/Devzone/post-order/post-order_v2_inquiry-inquiryid_issue_refund__post.html " target="_blank ">Issue Inquiry Refund</a></li><li><a href="/Devzone/post-order/post-order_v2_casemanagement-caseid_issue_refund__post.html " target="_blank ">Issue case refund</a></li><li><a href="/Devzone/post-order/post-order_v2_return-returnid_issue_refund__post.html " target="_blank ">Issue return refund</a></li><li><a href="/Devzone/post-order/post-order_v2_return-returnid_decide__post.html " target="_blank ">Process Return Request</a></li><li><a href="/devzone/post-order/post-order_v2_cancellation-cancelid_approve__post.html " target="_blank ">Approve Cancellation Request</a></li><li><a href="/devzone/post-order/post-order_v2_cancellation__post.html " target="_blank ">Create Cancellation Request</a></li></ul></li></ul><span class="tablenote"><b>Note:</b> For additional information about keypairs and creating Message Signatures, refer to <a href= "/develop/guides/digital-signatures-for-apis " target= "_blank ">Digital Signatures for APIs</a>.</span>

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/cdma-numiscorner/ebayDeveloperKeyManagementApi.git
- Packagist 页面：https://packagist.org/packages/cdma-numiscorner%2Febay-developer-key-management-api

## 历史版本号

- 当前版本：1.0

- 1.0

## 获取地址

- Composer 安装：`composer require cdma-numiscorner/ebay-developer-key-management-api`
- Packagist 仓库：https://repo.packagist.org/p2/cdma-numiscorner/ebay-developer-key-management-api.json
- 许可证：unlicense
- PHP 要求：>=7.2
