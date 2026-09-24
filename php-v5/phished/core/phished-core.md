# phished/core

> 标签: bug-bounty, canary, dependency-confusion, namespace-claim, phished.io

## 简介

AUTHORIZED BUG BOUNTY DEPENDENCY-CONFUSION CANARY. This empty placeholder claims the previously-unowned 'phished/core' Composer namespace on the public Packagist registry to neutralise the dependency-confusion attack surface affecting phished.io's CI. Contains zero functional code. The post-install hook executes a single PHP gethostbyname() DNS lookup to a researcher-controlled OAST endpoint - no HTTP requests, no file reads, no shell execution, no data transmitted beyond an unattributable 8-char hash of the installing host's name. Authorised by phished.io bug bounty program. Contact: mdinjamulhaque1@gmail.com.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://github.com/mdinjamulhaque/phished-bounty-canary
- 源码仓库：https://github.com/mdinjamulhaque/phished-bounty-canary.git
- Packagist 页面：https://packagist.org/packages/phished%2Fcore

## 历史版本号

- 当前版本：99.99.99

- 99.99.99

## 获取地址

- Composer 安装：`composer require phished/core`
- Packagist 仓库：https://repo.packagist.org/p2/phished/core.json
- 许可证：MIT
