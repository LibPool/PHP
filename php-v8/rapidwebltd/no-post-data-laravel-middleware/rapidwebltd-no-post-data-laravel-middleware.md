# rapidwebltd/no-post-data-laravel-middleware

> 标签: laravel, middleware, no post data middleware, post, post data

## 简介

Under certain conditions, when posting data from a form, the web server may lose the post data. This commonly happens if a user is uploading a large file beyond the size limits set in the web server's configuration. Laravel does not handle this situation and may end up throwing a somewhat confusing `TokenMismatchException in VerifyCsrfToken` due to CSRF protection. The 'No Post Data Laravel Middleware' handles situations in which a post request has been submitted and contains no post data - a situation which should not occur under normal usage. By default, the middleware will redirect back to the previous page with an error message flashed to the session. This can then be output on your view as you would normally handle validation errors. If needed, you can also modify this default behaviour and allow any code to run when the 'post request with no post data' situation is encountered.

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://github.com/rapidwebltd/no-post-data-laravel-middleware
- 源码仓库：https://github.com/rapidwebltd/no-post-data-laravel-middleware.git
- Packagist 页面：https://packagist.org/packages/rapidwebltd%2Fno-post-data-laravel-middleware

## 历史版本号

- 当前版本：v1.0.3

- v1.0
- v1.0.1
- v1.0.2
- v1.0.3

## 获取地址

- Composer 安装：`composer require rapidwebltd/no-post-data-laravel-middleware`
- Packagist 仓库：https://repo.packagist.org/p2/rapidwebltd/no-post-data-laravel-middleware.json
- 许可证：LGPL-3.0-only
- PHP 要求：>=5.5.9
