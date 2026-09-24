# daphascomp/daphascompsms

> 标签: Onfon Developer V1, api, daphascomp, daphascompsms, sdk

## 简介

# Authentication  Requests made to our APIs must be authenticated, there are two ways to do this:  1. Authenticating using your API apiUsername and apiPassword - `Basic Auth` 2. Authenticating using an Auth Token - `Bearer Token`  ## Method 1: Basic Auth  Basic Authentication is a method for an HTTP user agent (e.g., a web browser) to provide a apiUsername and apiPassword when making a request.  When employing Basic Authentication, users include an encoded string in the Authorization header of each request they make. The string is used by the request’s recipient to verify users’ identity and rights to access a resource.  The Authorization header follows this format:  > Authorization: Basic base64(apiUsername:apiPassword)  So if your apiUsername and apiPassword are `onfon` and `!@pas123`, the combination is `onfon:!@pas123`, and when base64 encoded, this becomes `b25mb246IUBwYXMxMjM=`. So requests made by this user would be sent with the following header:  > Authorization: Basic b25mb246IUBwYXMxMjM=  | Description                                                                                    | | ---------------------------------------------------------------------------------------------- | | **apiUsername** `String` `Required` <br> Your onfon account apiUsername, retrieved from portal | | **apiPassword** `String` `Required` <br> Your onfon account apiPassword, retrieved from portal |  ## Method 2: Bearer Tokens  This authentication stategy allows you to authenticate using JSON Web Token ``JWT` that will expire after given duration.  Each Access Token is a `JWT`, an encoded JSON object with three parts: the `header`, the `payload`, and the `signature`. The following is an example Access Token generated for Conversations  > Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c  ### Getting the token  To generate the token, make a `POST` request to `/v1/authorization` endpoint with your `apiUsername` and `apiPassword` This request should be made from your server and not on the client side such as browser or mobile environment.  You will receive a JSON similar to below:  `{ "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c", "validDurationSeconds": 3600}`  You can use the token received to make API calls. The token will be valid for value of `validDurationSeconds`, before which you should generate a new token.  #### Request Body  ``` {  "apiUsername": "root",  "apiPassword": "hakty11" } ```  #### Response Body  ``` {     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",     "validDurationSeconds": 3600 } ```  #### Example Curl  ``` curl --location --request POST 'https://apis.onfonmedia.co.ke/v1/authorization' \ --data-raw '{  "apiUsername": "correctapiUsername",  "apiPassword": "correctapiPassword" } ```  #### Making an API call  You will be required to pass the token in `Authorization` header prefixed by `Bearer` when calling other endpoints.  Example `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://www.apimatic.io
- 源码仓库：https://github.com/Gicehajunior/daphascomp-daphascompsms.git
- Packagist 页面：https://packagist.org/packages/daphascomp%2Fdaphascompsms

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require daphascomp/daphascompsms`
- Packagist 仓库：https://repo.packagist.org/p2/daphascomp/daphascompsms.json
- 许可证：MIT
- PHP 要求：>=7.2
