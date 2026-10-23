# milpa/runtime

> 标签: bootstrap, framework, kernel, milpa, php, psr-15, runtime

## 简介

The bootable Milpa kernel: composes milpa/core, milpa/container, milpa/events, milpa/http and milpa/resolver into container -> dispatcher -> architecture gate -> plugin boot in the resolver's loadOrder -> route registration, with zero Doctrine and zero legacy Web coupling. The active-plugins list is config/filesystem-driven, never a database entity.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/milpa%2Fruntime
- 源码仓库：https://github.com/getmilpa/runtime.git
- Packagist 页面：https://packagist.org/packages/milpa%2Fruntime

## 历史版本号

- 当前版本：v0.17.0

- v0.7.3
- v0.7.4
- v0.7.5
- v0.7.6
- v0.7.7
- v0.7.8
- v0.7.9
- v0.8.0
- v0.8.1
- v0.8.2
- v0.9.0
- v0.9.1
- 共 35 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require milpa/runtime`
- Packagist 仓库：https://repo.packagist.org/p2/milpa/runtime.json
- 许可证：Apache-2.0
- PHP 要求：>=8.3
