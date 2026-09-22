<p align="center">
  <b><a href="README.md">🇻🇳 越南语 (Tiếng Việt)</a></b> • 
  <b><a href="README.en.md">🇬🇧 英语 (English)</a></b> • 
  <b><a href="README.zh-CN.md">🇨🇳 简体中文 (Chinese)</a></b>
</p>

# 🌲 英灵神殿 (Valheim) 越南语社区本地化项目

> **面向《Valheim: 英灵神殿》（版本 1.0.15 / Steam Build `25390630`）以及 18+ 款主流 Mod 生态的标准化开源汉化与本地化工具链。**

---

## 🌟 项目概述与核心指标

**Valheim 越南语社区项目** 为 Iron Gate Studio 的每一次官方更新提供标准化、可持续且高可靠性的本地化解决方案。本项目不采用破坏性的直接文件覆写，而是推行严格的技术规范：按行 JSONL 结构校验、100% 保护技术占位符与游戏变量不损坏，并支持一键自动化部署。

### 📊 核心数据统计 (截至 2026-09-22)

| 核心指标 | 数据 | 说明 |
|---|---|---|
| **翻译数据总量** | **10,736** 行 JSONL | 全面覆盖原生游戏以及 18 款大型模组 |
| **技术签名匹配率** | **100.0%** (0 错误) | 确保 `{0}`、`$item_...`、`<color>` 等占位符绝无损坏 |
| **原生游戏文本量** | **6,038 - 9,438** 条文本 | 覆盖 1.0.15 版本提取出的 100% 有效文本内容 |
| **已深度翻译模组** | **18 款大型模组** | 包含 EpicLoot、Innangard、ValheimArmory、PlanBuild、Skyheim 等 |
| **生态收录模组** | **74 款模组** | 完成全面审计、分类梳理并配备详细配置指南 |
| **模组配置集成度** | **104 个插件** | 均已在 `Valheim_Mod` 独立运行环境中调优就绪 |
| **自动化测试与校验** | **PASS 100%** | 通过 Schema 验证、Token 测试及公共文件安全性审计 |

---

## 📅 游戏版本与平台状态 (Patch 1.0.15)

- **本地 Steam 客户端：** Steam Build `25390630`，对应官方 Patch **1.0.15**（发布于 2026-09-18）。
- **原生资产提取：** 已从游戏原版 `resources.assets`（SHA-256：`86b7fbe9514e43f25bee157d1cc2c103680003118e9c3872459e34e264725f9d`）中提取 **13 个本地化资产**、**6,056 个文本键** 及 **37 种语言** 到内部 `local/` 目录中。
- **本地化加载器：** 采用纯净 C# BepInEx 插件 `ValheimVietnamese`，挂钩 `Localization.LoadLanguages` 与 `Localization.SetupLanguage`，无缝向游戏设置菜单注册“越南语”，不破坏原有语言。
- **专属服务端 (Dedicated Server)：** 本地服务端 Build 为 `21981590`（Steam 目标为 `25390671`）。

---

## 📂 仓库目录架构

仓库严格区分公共开源代码与本地开发二进制文件：

```text
valheim-vietnamese-community/
├── .github/                  # GitHub Actions CI 自动化流水线
├── data/                     # 公共开源数据 (标准化逐行 JSONL)
│   ├── mods/                 # 18 款大型模组的翻译候选数据 (_draft.jsonl & _vi.json)
│   ├── valheim/              # 原生游戏翻译候选数据
│   └── README.md             # 数据规范与指南
├── docs/                     # 架构文档与指南
│   ├── FOLDER_GUIDE.md       # 仓库目录和文件架构解析
│   ├── INTEGRATION.md        # 游戏版本整合与本地工具链文档
│   ├── MODS_GUIDE.md         # 74 款模组生态分类与配置全书
│   └── STATUS.md             # QA 测试状态与验证报告
├── sources/                  # 溯源与版本元数据
│   ├── game_build_25390630.json # 从 1.0.15 提取的哈希与键数量
│   └── local_sources.json    # 本地工作区与客户端来源清单
├── tools/                    # 自动化 CLI 工具链
│   ├── check_public_files.py # 安全门禁：禁止二进制/快照文件泄露入 Git
│   ├── deploy_translations.py# 一键部署翻译到本地游戏安装目录
│   ├── export_embedded_resources.ps1 # 利用反射从 DLL 提取 Manifest 资源
│   ├── install_mods_to_valheim_mod.py # 自动部署 24 款精选模组至 Valheim_Mod
│   └── validate.py           # 校验 JSONL Schema 与 100% 占位符签名
├── tests/                    # 单元测试模块
├── local/                    # 本地私有工作区 (已加入 .gitignore)
├── mods/                     # 74 款本地模组素材包 (已加入 .gitignore)
├── Lich_Su_Truy_Van/         # 代理活动历史记录 (本地专属)
├── .gitignore                # 排除规则
├── CONTRIBUTING.md           # 贡献指南
├── LICENSE                   # MIT 开源协议
├── README.md                 # 越南语主文档
├── README.en.md              # 英文文档
└── README.zh-CN.md           # 简体中文文档
```

---

## ⚔️ 已完整本地化的 18 款大型模组

本项目利用深度 .NET 反射技术直接从 DLL 中抽取内嵌语言资产，完成高质量翻译并生成标准化数据：

| 序号 | 模组名称 | 命名空间 | 键数 | 核心玩法与特性 |
|---|---|---|---|---|
| 1 | **EpicLoot** (v0.14.11) | `epicloot` | **2,114** | 完整暗黑破坏神风格 RPG 掉落重构：魔法、稀有、史诗、传奇品阶，附魔与碎石镶嵌系统。 |
| 2 | **Innangard** (v0.1.9) | `innangard` | **757** | 维京殖民与村庄建设：招募定居者、分配工种，蓝图自动化建造。 |
| 3 | **CoreWoodExtras** (v2.2.6) | `corewoodextras` | **359** | 50+ 种核心木建筑部件、集市货摊、各色鱼箱与家具。 |
| 4 | **SeneaL UI** (v1.1.3) | `senealui` | **358** | 现代化 HUD：数字化血条、敌怪星级、浮动伤害跳字与护甲数值。 |
| 5 | **MagicRevamp** (v1.5.1) | `magicrevamp` | **343** | 魔法系统扩展：编根套装、影叶先锋长袍、元素法杖。 |
| 6 | **ValheimArmory** (v1.33.0) | `valheimarmory` | **286** | 庞大武器库：各材质十字弩、重型弩机、双手大剑、塔盾与锁子甲。 |
| 7 | **PlanBuild** (v0.19.1) | `planbuild` | **174** | 规划建造工具：在消耗实际材料前放置蓝图虚影框架，支持蓝图导入导出。 |
| 8 | **WeaponAdditions** (v1.2.6) | `weaponadditions` | **80** | 神话武器扩展：龙族系列、精灵系列、黑曜石与烈焰金属系列武器。 |
| 9 | **Skyheim / SkyheimFix** (v1.3.12) | `skyheim` | **77** | 类似天际省风格的符文魔法：自然、神圣、火焰与冰霜魔法。 |
| 10 | **Digitalroot.ArrowsJvL** (v1.0.0) | `digitalroot_arrows` | **40** | 重型箭矢与钝头箭：远程击晕与强力破甲。 |
| 11 | **Quick Stack - Store - Sort - Trash** (v1.4.15) | `quickstackstore` | **29** | 一键箱子堆叠、背包快速整理、自动补给与收藏防丢。 |
| 12 | **Jotunn** (v2.20+) | `jotunn` | **21** | 社区工业级模组开发基础设施框架。 |
| 13 | **MagicBows** (v1.1.9) | `magicbows` | **20** | 元素魔法弓弩（火、冰、雷、魂、毒）。 |
| 14 | **Better Archery** (v2.0.2) | `betterarchery` | **11** | 独立箭袋装备槽、缩放瞄准与箭矢回收机制。 |
| 15 | **TeleportEverything** (v2.9.1) | `teleporteverything` | **8** | 允许携带矿物与驯服动物穿过传送门（支持过路费配置）。 |
| 16 | **DvergerStaves** (v1.1.0) | `dvergerstaves` | **7** | 迷雾矮人火、冰与群体治疗法杖。 |
| 17 | **ModSettings** | `modsettings` | **4** | 游戏内模组可视化配置管理界面。 |
| 18 | **CraftFromChestsPlus** (v1.0.5) | `craftfromchestsplus` | **1** | 制作工作台自动调取附近箱内材料。 |

---

## 🕹️ 双配置运行架构 (Dual-Profile Architecture)

支持原汁原味的纯净联机版与高配置模组版并行：

```text
E:\SteamLibrary\steamapps\common\
├── Valheim/                   # 方案一：原生纯净版 + 官方级汉化/越化
│   ├── valheim.exe            # 通过 Steam "开始游戏" 按钮直接运行
│   └── BepInEx/plugins/       # 仅含纯净语言加载器插件
│
└── Valheim_Mod/               # 方案二：终极超级模组版 (104 个插件)
    ├── valheim.exe            # 通过独立桌面快捷方式启动 ("Valheim 超级模组版")
    └── BepInEx/plugins/       # 104 款热门插件全开 (装备掉落、魔法、画质滤镜)
```

---

## 🛠️ 命令行工具箱使用指南 (CLI Suite)

```bash
# 1. 一键将本地化文本部署安装到本地游戏目录
python tools/deploy_translations.py

# 2. 将 24 款精选超级模组及汉化包自动注入 Valheim_Mod
python tools/install_mods_to_valheim_mod.py

# 3. 校验数据完整性与占位符签名 (确保 0 错误)
python tools/validate.py data

# 4. 安全检查：确保 Git 未追踪任何二进制文件
python tools/check_public_files.py

# 5. 运行全部单元测试
python -m unittest discover -s tests
```

---

<p align="center">
  <b>由 Valheim 社区开发者联合构建 • 2026</b><br>
  <i>“致敬九界之中的每一位无畏维京勇士！”</i>
</p>
