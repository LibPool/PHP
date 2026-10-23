# likun-mci/acme

> 标签: ACME, acme-client, acme-v2, acme.sh, auto-renew, buypass, certificate, csr, dns-01, dns-api, free-ssl, http-01, https, lets-encrypt, letsencrypt, no-exec, rfc8555, shared-hosting, ssl, tls, tls-alpn-01, x509, zerossl

## 简介

用原生 PHP 实现的 ACME v2 (RFC 8555) 证书客户端，acme.sh 的完整功能对等实现：账户、订单、http-01/dns-01/tls-alpn-01 验证、签发续期吊销、部署与通知钩子。全程不调用 openssl/curl/crontab 等外部进程，为禁用 exec 的共享主机与受管控服务器而写。支持 Let's Encrypt、ZeroSSL、BuyPass、Google Trust Services、SSL.com 与数十家 DNS 提供商。

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://github.com/likun-mci/acme
- 源码仓库：https://github.com/likun-mci/acme.git
- Packagist 页面：https://packagist.org/packages/likun-mci%2Facme

## 历史版本号

- 当前版本：v1.0.2

- v1.0.0
- v1.0.1
- v1.0.2

## 获取地址

- Composer 安装：`composer require likun-mci/acme`
- Packagist 仓库：https://repo.packagist.org/p2/likun-mci/acme.json
- 许可证：MIT
- PHP 要求：>=7.2
