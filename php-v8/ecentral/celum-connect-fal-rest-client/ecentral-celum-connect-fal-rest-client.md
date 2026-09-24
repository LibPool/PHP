# ecentral/celum-connect-fal-rest-client

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

### Authorization If you are already logged into CELUM Content via browser, no further authorization is required. Otherwise, please use one of the below methods:   1. Click on 'Authorize' on the right and either provide an API Key, type in your username/password or use OpenID Connect to log in. 2. OpenId implicit flow is disabled for security reasons and will not work as Authorization option.   ### Creating an asset  1. Request upload via [upload endpoint](#/Upload/requestUpload). The endpoint will return a URl for uploading the binary and a upload handle to identify the upload. 2. Upload the content of your asset by sending a POST request to the upload URL from step 1 and setting the ```Content-Type``` header to ```application/octet-stream```. Optionally, you can also use multipart upload with ```multipart/form-data``` as ```Content-Type``` - like our Nova UI. 3. Create the asset via [create asset endpoint](#/Assets/createAssetInCollection) by passing in the upload handle from step 1 together with other parameters.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/ecentral/celum-connect-fal-rest-client.git
- Packagist 页面：https://packagist.org/packages/ecentral%2Fcelum-connect-fal-rest-client

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require ecentral/celum-connect-fal-rest-client`
- Packagist 仓库：https://repo.packagist.org/p2/ecentral/celum-connect-fal-rest-client.json
- 许可证：unlicense
- PHP 要求：^8.1
