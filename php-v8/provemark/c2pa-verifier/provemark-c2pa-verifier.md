# provemark/c2pa-verifier

> 标签: COSE, c2pa, cbor, content-credentials, jumbf, provenance, verifier

## 简介

Verifier for C2PA Content Credentials in pure PHP: reads the manifest store out of a JPEG, PNG, WebP or ISOBMFF file and checks the signature, the hash binding, the certificate chain, the timestamp and the revocation responses stapled into the signature, with c2patool's verdict semantics. Read and verify only; no signing, no keys, no network.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/provemark%2Fc2pa-verifier
- 源码仓库：https://github.com/provemark/c2pa-verifier.git
- Packagist 页面：https://packagist.org/packages/provemark%2Fc2pa-verifier

## 历史版本号

- 当前版本：v0.1.0

- v0.1.0

## 获取地址

- Composer 安装：`composer require provemark/c2pa-verifier`
- Packagist 仓库：https://repo.packagist.org/p2/provemark/c2pa-verifier.json
- 许可证：MIT
- PHP 要求：^8.3
