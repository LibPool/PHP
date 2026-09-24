# frc/wp-env-heroku-custom-php-constant

> 标签: constant, heroku, wordpress

## 简介

Allow PHP constants to be defined through Heroku environment, as long as the environment key starts with FRC_PHP_CONST_ prefix. The prefix gets removed when the constant is set in the PHP side. For example, an environment variable FRC_PHP_CONST_PLL_COOKIE will define the PHP constant PLL_COOKIE within WordPress (with the value coming from the env key)

按 require.php 推断最低支持 PHP 5；已收录于 php-v5, php-v7, php-v8。

## 官网

- 官网：https://packagist.org/packages/frc%2Fwp-env-heroku-custom-php-constant
- 源码仓库：https://github.com/frc/wp-env-heroku-custom-php-constant.git
- Packagist 页面：https://packagist.org/packages/frc%2Fwp-env-heroku-custom-php-constant

## 历史版本号

- 当前版本：v1.0.2

- v1.0.0
- v1.0.1
- v1.0.2

## 获取地址

- Composer 安装：`composer require frc/wp-env-heroku-custom-php-constant`
- Packagist 仓库：https://repo.packagist.org/p2/frc/wp-env-heroku-custom-php-constant.json
- 许可证：MIT
- PHP 要求：>=5.3
