# elmo-software/user-api-sdk

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

# Overview    The ELMO API is a RESTful based API that facilitates user information management within the ELMO ecosystem. Our API is designed to empower businesses, including our valued customers and partners, in creating scalable integration solutions aligned with their evolving business needs. By using this API, you gain access to invaluable HR data, enabling you to supercharge your applications and integrations, driving efficient workflows and enhancing core business processes. The below section provides an overview of the current capabilities of the API:    * Get users list   * Get an individual user's details   * Get a user template to create a new user   * Create new user   * Get positions list   * Get locations list   * Get department list   * Get metadata of configurable fields   * Get all users employment details   * Get an individual user's employment details   * Get legal entity details   * Get payroll calendar details   * Get leave request details   * Get leave type details    Note that this is the latest version of the API Documentation that utilises OAuth2 authentication. The previous version of the documentation can be found at [API Documentation version 1](/v1/index.html)   <br />   <br />   Please be advised that endpoints labelled as beta are intended for customer testing and feedback and may change based on feedback, potentially impacting backward compatibility. Consider this before integrating it with production systems to avoid disruptions to your integrations.          <br />  ---    <br /> # Authentication    ELMO API utlises OAuth2.0 authentication. Company Admins are able to create and manage API Credentials.  <br />  ---    <br /> # API Rate Limits    There are limits applied to the number of API requests your application can make. This limit is lower in sandbox and higher in production environments.   The ELMO User API also supports custom usage plans to scale with your organisation's needs.    Sandbox Environment   * **Rate limit**: 1 request per second   * **Burst limit**: 10   * **Quota**: 500 requests in 1 day    Production Environment   * **Rate limit**: 1 requests per second   * **Burst limit**: 10   * **Quota**: 5000 requests in 1 day  <br />  ---    <br /> # Generating Client SDKs    You can use the OpenAPI Specification file to generate a client SDK. You can download the file from [here](index.yaml). Then use the tool of your choice to generate a client SDK. You can get started [here](https://swagger.io/tools/swagger-codegen/).  <br />

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/elmo-software/user-api-sdk-php.git
- Packagist 页面：https://packagist.org/packages/elmo-software%2Fuser-api-sdk

## 历史版本号

- 当前版本：0.1.1

- 0.1.0
- 0.1.1

## 获取地址

- Composer 安装：`composer require elmo-software/user-api-sdk`
- Packagist 仓库：https://repo.packagist.org/p2/elmo-software/user-api-sdk.json
- 许可证：unlicense
- PHP 要求：^8.4.27
