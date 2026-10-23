# kode/parallel

> 标签: async, concurrency, coroutine, ext-parallel, fiber, kode, multithreading, parallel, 协程, 并发, 并行, 真线程, 高性能

## 简介

适用于 PHP 8.4+ 的高性能多线程并行并发库：基于 ext-parallel 真线程（ZTS）的主引擎 + 同步回退引擎，可通过 EngineFactory::register() 接入 kode/process 等多进程后端；提供 Runtime、Task、Future、Concurrency 同步原语（Lock/Atomic/Semaphore/Barrier/Channel）、Fiber、WorkerPool 等完整能力

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/kode%2Fparallel
- 源码仓库：https://github.com/kodephp/parallel.git
- Packagist 页面：https://packagist.org/packages/kode%2Fparallel

## 历史版本号

- 当前版本：2.0.11

- 2.0.0
- 2.0.1
- 2.0.10
- 2.0.11
- 2.0.2
- 2.0.3
- 2.0.4
- 2.0.5
- 2.0.6
- 2.0.7
- 2.0.8
- 2.0.9
- 共 38 个稳定版本，完整清单见 Packagist。

## 获取地址

- Composer 安装：`composer require kode/parallel`
- Packagist 仓库：https://repo.packagist.org/p2/kode/parallel.json
- 许可证：Apache-2.0
- PHP 要求：^8.4
