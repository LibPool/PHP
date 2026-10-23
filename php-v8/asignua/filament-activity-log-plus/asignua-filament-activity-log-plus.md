# asignua/filament-activity-log-plus

> 标签: Audit, activity-log, audit-trail, filament, filament-plugin, history, laravel, spatie, translatable

## 简介

An audit trail for Filament 5 on top of spatie/laravel-activitylog 5 that records what really happened: per-language diffs of translatable JSON fields (title.uk / title.en), no phantom changes caused by database defaults, one Save in the panel = one batch, pivot sync() and media uploads recorded against the owner record, and labels frozen at write time. Ships a History header action, a read-only activity log resource, auth events and pruning.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/asignua/filament-activity-log-plus
- 源码仓库：https://github.com/asignua/filament-activity-log-plus.git
- Packagist 页面：https://packagist.org/packages/asignua%2Ffilament-activity-log-plus

## 历史版本号

- 当前版本：v1.1.0

- v1.0.0
- v1.0.1
- v1.1.0

## 获取地址

- Composer 安装：`composer require asignua/filament-activity-log-plus`
- Packagist 仓库：https://repo.packagist.org/p2/asignua/filament-activity-log-plus.json
- 许可证：MIT
- PHP 要求：^8.4
