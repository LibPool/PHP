# nythros/framework

> 标签: PHP

## 简介

Nythros 游戏框架层（Game framework layer）：三基类（BasePlayer/BaseMonster/BaseNPC，继承 engine 的 Actor\BaseActor）+ 战斗模块（Combat/CombatService + MonsterActor + DropEntity/DropTable + EntityTypeIndex）+ 背包（Inventory）+ 社交模块（Social/SocialService + Team/Guild/Location 存储）+ 玩家 Actor（Actor/PlayerActor）+ 身份（Auth/Identity）+ 插件机制（PluginInterface/PluginRegistry + Skill/Item/Buff 官方插件）+ 实时服务器运行时（Server/RealtimeServer + ConnectionRegistry + FrameMerger）+ 部署（Deploy/DeployConfig）+ 观测（Observability/PerfSampler）+ 持久化管道（Persistence/ArchivePipeline）。

按 require.php 推断最低支持 PHP 8；已收录于 php-v8。

## 官网

- 官网：https://packagist.org/packages/nythros%2Fframework
- 源码仓库：https://github.com/Nythros/framework.git
- Packagist 页面：https://packagist.org/packages/nythros%2Fframework

## 历史版本号

- 当前版本：v0.2.0

- v0.1.0
- v0.2.0

## 获取地址

- Composer 安装：`composer require nythros/framework`
- Packagist 仓库：https://repo.packagist.org/p2/nythros/framework.json
- 许可证：MIT
- PHP 要求：>=8.3
