# mfonte/sparsedigest

> 标签: Fingerprint, binary-files, change-detection, checksum, fast-hash, file-hash, file-integrity, hash, hashing, performance, sampling, sparse-hash

## 简介

Fast PHP file hashing library using intelligent sampling. Reads only selected portions of large binary files instead of full content, dramatically reducing I/O overhead. Automatically falls back to full-file hashing for text files. Deterministic, non-cryptographic, optimized for change detection.

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://github.com/mauriziofonte/sparsedigest
- 源码仓库：https://github.com/mauriziofonte/sparsedigest.git
- Packagist 页面：https://packagist.org/packages/mfonte%2Fsparsedigest

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- Composer 安装：`composer require mfonte/sparsedigest`
- Packagist 仓库：https://repo.packagist.org/p2/mfonte/sparsedigest.json
- 许可证：MIT
- PHP 要求：>=7.2
