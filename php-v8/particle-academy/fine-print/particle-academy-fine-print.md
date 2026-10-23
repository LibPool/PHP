# particle-academy/fine-print

> 标签: agentic, ai, document, particle-academy, pdf, pdf-parser, pdf-renderer, prompt-injection, security, text-extraction

## 简介

First-party PDF reader, writer and renderer for agentic docs, in pure PHP with zero runtime dependencies. Writes PDF 1.7 from the last-word JSON document model and never writes active content. Parses PDFs, extracts text in reading order, reports active content without executing it, and guards agent reads against prompt injection. Renders vector paths, TrueType text, sampled images and baseline JPEG to PNG. Hostile-input limits refuse bombs, cycles and oversized images cleanly; unsupported content is reported.

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://github.com/Particle-Academy/fine-print
- 源码仓库：https://github.com/Particle-Academy/fine-print.git
- Packagist 页面：https://packagist.org/packages/particle-academy%2Ffine-print

## 历史版本号

- 当前版本：v0.2.1

- v0.1.0
- v0.2.0
- v0.2.1

## 获取地址

- Composer 安装：`composer require particle-academy/fine-print`
- Packagist 仓库：https://repo.packagist.org/p2/particle-academy/fine-print.json
- 许可证：MIT
- PHP 要求：^8.4
