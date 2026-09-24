# vitexsoftware/rbczpremiumapi

> 标签: api, openapi, openapi-generator, openapitools, php, raiffeisenbank, rest, sdk

## 简介

##### API Overview - Accounts list and balance - Transaction overview (also for saving accounts) - Payments import - Statement list and download - FX rates  ##### Authentication Before making a call to Premium API, you need to register your app at our _Developer portal_. This is where you get the **ClientID** that your application must send in the request as `X-IBM-Client-Id`. This is the key that grants your app access to the API.  However, this may not be enough. Your application needs to use mTLS to call most operations here. Thus, you not only need _https_ but also a client certificate issued by us. The exception is two operations for FX rates that are accessible also without a client certificate.  Each bank client/user can issue several certificates. Each certificate can permit different sets of operations (http methods) on different bank accounts. All this must be configured in Internet Banking first by each bank client/user (bank clients need to look under _Settings_ and do not forget to download the certificate at the last step). The certificate is downloaded in **PKCS#12** format as **\*.p12** file and protected by a password chosen by the bank client/user. Yes, your app needs the password as well to get use of the **\*p12** file for establishing mTLS connection to the bank.  Client certificates issued in Internet Banking for bank clients/users have limited validity (e.g. **5 years**). However, **each year** certificates are automatically blocked and bank client/user must unblock them in Internet Banking. It is possible to do it in advance and prolong the time before the certificate is blocked. Your app should be prepared for these scenarios and it should communicate such cases to your user in advance to provide seamless service and high user-experience of your app.  ##### Rate Limiting The number of requests in each API operation is limited to 10 per client per sliding second and 5000 per client per sliding day. The exception is the 'Download Statement' operation with the limits lowered to 5 per client per sliding second and 1500 per client per sliding day. This is because it transports potentially sizeable binary files. The consumer must be able to handle HTTP status 429 in case of exceeding these limits.  Response headers `X-RateLimit-Limit-Second` and `X-RateLimit-Limit-Day` show the actual limits configured for the specific operation. Response headers `X-RateLimit-Remaining-Second` and `X-RateLimit-Remaining-Day` are returned to help prevent the limits from being exceeded.  ##### Notes Be aware, that in certain error situations, API can return specific error structures along with 5xx status code, which is not explicitely defined below.  ##### Quick Start Client Feel free to download a <a href="assets/PremiumApiClient.java" download>simple Java client</a> that gives you quick access to our API.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/VitexSoftware/php-vitexsoftware-raiffeisenbank
- 源码仓库：https://github.com/VitexSoftware/php-vitexsoftware-rbczpremiumapi.git
- Packagist 页面：https://packagist.org/packages/vitexsoftware%2Frbczpremiumapi

## 历史版本号

- 当前版本：v1.5.8

- 1.1.0
- 1.1.1
- 1.2.3
- 1.3.0
- 1.3.1
- 1.4.1
- v1.4.0
- v1.5.0
- v1.5.1
- v1.5.2
- v1.5.5
- v1.5.8
- 共 13 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require vitexsoftware/rbczpremiumapi`
- Packagist 仓库：https://repo.packagist.org/p2/vitexsoftware/rbczpremiumapi.json
- 许可证：MIT
- PHP 要求：>= 8.1
