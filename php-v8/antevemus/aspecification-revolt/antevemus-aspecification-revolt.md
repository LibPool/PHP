# antevemus/aspecification-revolt

> 标签: Specification-pattern, amphp, async, concurrency, data-resolution, event-loop, fiber, php82, revolt, specification

## 简介

Revolt/Fibers satellite of antevemus/aspecification: RevoltDataSource and RevoltStageTransport fetch the non-HTTP external data of a resolution stage concurrently under the Revolt event loop (Fibers, Amp futures), through the IDeferredDataSource/IStageTransport hook of the core, with a concurrency limit, per-source time limits and the resolution deadline

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/antevemus-it/Antevemus.ASpecificationRevolt
- 源码仓库：https://github.com/antevemus-it/Antevemus.ASpecificationRevolt.git
- Packagist 页面：https://packagist.org/packages/antevemus%2Faspecification-revolt

## 历史版本号

- 当前版本：v1.0.1

- v1.0.1

## 获取地址

- Composer 安装：`composer require antevemus/aspecification-revolt`
- Packagist 仓库：https://repo.packagist.org/p2/antevemus/aspecification-revolt.json
- 许可证：MIT
- PHP 要求：^8.2
