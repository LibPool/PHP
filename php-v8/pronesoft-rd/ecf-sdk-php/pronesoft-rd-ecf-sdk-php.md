# pronesoft-rd/ecf-sdk-php

> 标签: api, openapi, openapi-generator, openapitools, php, rest, sdk

## 简介

## Descripción general API de nivel productivo para emitir Comprobantes Fiscales Electrónicos (e-CF) en la República Dominicana a través de la plataforma Pronesoft.  ## Autenticación — OAuth 2.0 Client Credentials  ### Pasos 1. Obtén tus credenciales desde el portal:    - Sandbox: https://ecf.sandbox.pronesoft.com → Apps → Default Sandbox App    - Producción: https://ecf.pronesoft.com → Integraciones → Apps → Crear App 2. Solicita un token via POST /oauth/token — válido por 24 horas (86400s). 3. Usa: Authorization: Bearer <accessToken> en cada request. 4. Renueva al recibir HTTP 401. Buena práctica: renovar 5 minutos antes del vencimiento.  ### Delegación multi-empresa Para actuar en nombre de una empresa asociada (sucursal), agrega:   x-tenant-id: <business-uuid> NO envíes x-tenant-id cuando actúes como la empresa principal.  ### Detalles del Sandbox - Usa cualquier RNC que comience con SBX (ej. SBX123456) — no se requiere certificado real. - Las secuencias son automáticas — no es necesario crearlas manualmente. - El campo environment en el cuerpo del documento DEBE ser TesteCF.  ### Scopes disponibles business:read, business:create, business:update, members:read, members:invite, members:revoke, certificates:read, certificates:upload, certificates:update, documents:read, documents:create, documents:send, documents:receive, documents:update, approvals:read, approvals:commercial, sequences:read, sequences:create, sequences:update, sequences:cancel, business_info:read, certification:read, certification:write, reports:read

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://openapi-generator.tech
- 源码仓库：https://github.com/ProneSoftSRL/pronesoft-ecf-sdk-php.git
- Packagist 页面：https://packagist.org/packages/pronesoft-rd%2Fecf-sdk-php

## 历史版本号

- 当前版本：v0.0.4

- v0.0.1
- v0.0.2
- v0.0.3
- v0.0.4

## 获取地址

- Composer 安装：`composer require pronesoft-rd/ecf-sdk-php`
- Packagist 仓库：https://repo.packagist.org/p2/pronesoft-rd/ecf-sdk-php.json
- 许可证：unlicense
- PHP 要求：^8.1
