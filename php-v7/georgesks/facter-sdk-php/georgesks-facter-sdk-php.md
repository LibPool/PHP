# georgesks/facter-sdk-php

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

API pública para timbrar **CFDI 4.0** usando la infraestructura de Facter.  **Modelo comercial:** un **cliente principal** (plan PREPAGO) compra timbres; sus **emisores** (cada uno un tenant con su propio RFC y CSD) consumen del saldo del principal.  El contrato de entrada es el **JSON canónico CFDI 4.0**: el integrador envía el comprobante completo (Emisor, Receptor, Conceptos, Impuestos, Complemento...). Facter **valida** consistencia aritmética y contra catálogos SAT pero **no recalcula** totales — tu sistema es el sistema de registro.  **Ambientes:** prueba en **Demo** `https://demo.facter.com.mx/api/ext/v1` (sandbox de pruebas, sin cobro real, datos efímeros) y, cuando estés listo, pasa a **Producción** `https://v2.facter.com.mx/api/ext/v1` (timbrado real, consume timbres). Necesitas **una cuenta y una API key por ambiente**; la key de un ambiente no funciona en el otro. El host define el comportamiento.  **Autenticación:** `Authorization: Bearer fct_live_xxx`. **Idempotencia obligatoria** en endpoints mutadores vía header `Idempotency-Key`. Toda respuesta incluye `X-Request-Id` para soporte.  Documentación completa, quickstart y ejemplos: https://v2.facter.com.mx/developers

按 require.php 推断最低支持 PHP 7；已收录于 php-v7, php-v8。

## 官网

- 官网：https://github.com/georgesks/facter-sdk-php
- 源码仓库：https://github.com/georgesks/facter-sdk-php.git
- Packagist 页面：https://packagist.org/packages/georgesks%2Ffacter-sdk-php

## 历史版本号

- 当前版本：v2.0.0

- v0.1.0
- v2.0.0

## 获取地址

- Composer 安装：`composer require georgesks/facter-sdk-php`
- Packagist 仓库：https://repo.packagist.org/p2/georgesks/facter-sdk-php.json
- 许可证：MIT
- PHP 要求：^7.4 || ^8.0
