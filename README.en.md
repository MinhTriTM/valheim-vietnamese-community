<p align="center">
  <b><a href="README.md">🇻🇳 Tiếng Việt</a></b> • 
  <b><a href="README.en.md">🇬🇧 English</a></b> • 
  <b><a href="README.zh-CN.md">🇨🇳 简体中文</a></b>
</p>

# 🌲 Valheim Vietnamese Community Translation Project

> **An open-source repository, standardized translation database, and automated localization toolkit for Valheim (Patch 1.0.15 / Steam Build `25390630`) and an ecosystem of 18+ popular mods.**

---

## 🌟 Project Overview & Key Metrics

The **Valheim Vietnamese Community** project provides a standardized, maintainable, and reliable localization framework aligned with every official Valheim update by Iron Gate Studio. Rather than unmonitored string overwrites, this project implements a strict technical standard: line-by-line JSONL validation, 100% preservation of technical tokens and game placeholders, and 1-click automated deployment.

### 📊 Key Project Statistics (As of 22/09/2026)

| Metric | Value | Details |
|---|---|---|
| **Total Translation Records** | **10,736** JSONL rows | Full coverage of Vanilla game and 18 major mods |
| **Token Signature Match** | **100.0%** (0 errors) | Zero corruption of placeholders `{0}`, `$item_...`, `<color>` |
| **Vanilla Game Translations** | **6,038 - 9,438** strings | 100% coverage of extracted meaningful strings from Patch 1.0.15 |
| **Fully Translated Mods** | **18 Major Mods** | Including EpicLoot, Innangard, ValheimArmory, PlanBuild, Skyheim... |
| **Ecosystem Mods Cataloged** | **74 Mods** | Fully audited, categorized, and documented with config guides |
| **Integrated Plugins in Modded Profile** | **104 Plugins** | Pre-configured and tested in the `Valheim_Mod` profile |
| **Automated CI/Test Validation** | **PASS 100%** | Schema checks, token tests, and public files safety checks |

---

## 📅 Version & Game Platform (Patch 1.0.15)

- **Local Steam Client:** Steam Build `25390630`, corresponding to official Patch **1.0.15** (Released 18/09/2026).
- **Extracted Game Assets:** Cleanly extracted from `resources.assets` (SHA-256: `86b7fbe9514e43f25bee157d1cc2c103680003118e9c3872459e34e264725f9d`) containing **13 localization assets**, **6,056 keys**, and **37 parallel languages** into the private `local/` directory (ignored by Git to respect game IP).
- **Localization Loader:** Utilizes the clean C# BepInEx plugin `ValheimVietnamese` patching `Localization.LoadLanguages` and `Localization.SetupLanguage`, seamlessly registering **"Tiếng Việt"** into the game settings menu without altering existing languages.
- **Dedicated Server:** Local dedicated server build `21981590` (Steam targeting `25390671`).

---

## 📂 Repository Directory Architecture

The repository enforces strict separation between public code/data on GitHub and local binary/snapshot assets:

```text
valheim-vietnamese-community/
├── .github/                  # Automated CI workflows verifying syntax and schemas
├── data/                     # PUBLIC REPO DATA (Standardized line-by-line JSONL)
│   ├── mods/                 # Translation candidates for 18 mods (_draft.jsonl & _vi.json)
│   ├── valheim/              # Translation candidates for vanilla game
│   └── README.md             # Data specification and guidelines
├── docs/                     # TECHNICAL DOCUMENTATION & GUIDES
│   ├── FOLDER_GUIDE.md       # Detailed guide to repository folders and files
│   ├── INTEGRATION.md        # Integration summary of game builds and local tools
│   ├── MODS_GUIDE.md         # Comprehensive handbook covering all 74 mods
│   └── STATUS.md             # QA status and validation reports
├── sources/                  # PROVENANCE & BUILD METADATA
│   ├── game_build_25390630.json # Hashes and key counts extracted from 1.0.15
│   └── local_sources.json    # Local workspace and client source inventory
├── tools/                    # AUTOMATION CLI SUITE
│   ├── audit_candidates.py   # Static audit for untranslated or fallback strings
│   ├── audit_local.py        # Audits local resources and snapshots
│   ├── build_local_corpus.py # Builds local search corpus into SQLite3
│   ├── build_translation.py  # Builds deployment JSON by namespace
│   ├── check_public_files.py # Security gate blocking forbidden binary/snapshot leaks
│   ├── deploy_translations.py# 1-CLICK DEPLOYMENT to local game installations
│   ├── export_embedded_resources.ps1 # Extracts Manifest Resources from DLLs via Reflection
│   ├── extract_game.py       # Extracts strings from vanilla resources.assets
│   ├── install_mods_to_valheim_mod.py # Auto-installs 24 selected mods to Valheim_Mod
│   ├── package_preview.py    # Packages preview zip for local QA
│   ├── search_local.py       # Quick search in local corpus
│   ├── translate_*.py        # Translation and validation automation scripts
│   └── validate.py           # VALIDATES SCHEMAS & TOKEN SIGNATURE MATCHES
├── tests/                    # UNIT TESTS
│   └── test_validate.py      # Validates signature hashing and schema constraints
├── local/                    # LOCAL WORKSPACE (GIT IGNORED)
│   ├── game_sources.jsonl    # Raw English extracted from 1.0.15
│   └── extracted_mods/       # Extracted manifest strings from 74 mod DLLs
├── mods/                     # 74 LOCAL MOD FOLDERS (GIT IGNORED)
├── Lich_Su_Truy_Van/         # AGENT ACTIVITY LOGS (LOCAL ONLY)
├── .gitignore                # Excludes binaries, snapshots, and internal logs
├── CONTRIBUTING.md           # Contribution guide and token preservation rules
├── LICENSE                   # MIT Open Source License
└── README.md                 # Primary documentation entrypoint
```

---

## ⚙️ Technical Mechanics: Token Preservation & Signature Hashing

Corrupted placeholders (`{0}`, `$item_...`, `<color=...>`, `%`) frequently lead to game crashes or broken UI strings. This project enforces an automated **`technical_signature`** validation algorithm:

```python
def signature(value: str) -> str:
    tokens = re.findall(r"\$[A-Za-z_0-9][\w]*|\{\d+(?::[^{}]+)?\}|<[^>]+>", value)
    return hashlib.sha256(json.dumps(sorted(tokens), ensure_ascii=False).encode("utf-8")).hexdigest()
```

### JSONL Schema Standard (`data/**/*.jsonl`):
Each record requires 10 mandatory fields:
1. `namespace`: Unique namespace (`valheim`, `epicloot`, `planbuild`, `skyheim`...).
2. `key`: Original string identifier in the game/mod source.
3. `source_sha256`: SHA-256 hash of the original English text.
4. `technical_signature`: SHA-256 signature of sorted placeholders and tokens.
5. `vi`: Vietnamese translation (signature must match original 100%).
6. `status`: Lifecycle state (`draft` or `reviewed`).
7. `origin`: Provenance tag (`monokaijs-mit`, `mod-EpicLoot`, `project-written`).
8. `game_build`: Target game build (e.g., `25390630`).
9. `mod_version`: Target mod version.
10. `reviewer`: Name of reviewer once promoted to `reviewed`.

---

## ⚔️ The 18 Fully Translated Major Mods

Deep .NET reflection was employed to extract raw language files and Manifest Resources from mod assemblies, translated and structured as standard JSONL:

| # | Mod Name | Namespace | Keys | Core Features |
|---|---|---|---|---|
| 1 | **EpicLoot** (v0.14.11) | `epicloot` | **2,114** | Complete RPG overhaul: Magic, Rare, Epic, Legendary tiers, enchantments, tempering, shardstones, and bounty hunts. |
| 2 | **Innangard** (v0.1.9) | `innangard` | **757** | Viking settlement system: recruit settlers, professions, automated blueprint construction under Frith protection. |
| 3 | **CoreWoodExtras** (v2.2.6) | `corewoodextras` | **359** | 50+ core wood architectural pieces, market stalls, fish crates, furniture. |
| 4 | **SeneaL UI** (v1.1.3) | `senealui` | **358** | Modernized HUD: detailed health numbers, enemy star ratings, damage popups, armor stats. |
| 5 | **MagicRevamp** (v1.5.1) | `magicrevamp` | **343** | Magic system expansion: Rootweave armor, Shadowleaf Vanguard robes, elemental staffs. |
| 6 | **ValheimArmory** (v1.33.0) | `valheimarmory` | **286** | Massive weapon armory: crossbows, heavy arbalests, two-handed greatswords, tower shields. |
| 7 | **PlanBuild** (v0.19.1) | `planbuild` | **174** | Architectural planning tool: place blueprint ghost frames before committing resources. |
| 8 | **WeaponAdditions** (v1.2.6) | `weaponadditions` | **80** | Mythical weapons: Draconic, Elven, Obsidian, and Flametal greatswords and scythes. |
| 9 | **Skyheim / SkyheimFix** (v1.3.12) | `skyheim` | **77** | Skyrim-inspired runic magic system: Fire, Frost, Holy, and Nature spells. |
| 10 | **Digitalroot.ArrowsJvL** (v1.0.0) | `digitalroot_arrows` | **40** | Heavy and blunted arrows for ranged staggering and armor penetration. |
| 11 | **Quick Stack - Store - Sort - Trash** (v1.4.15) | `quickstackstore` | **29** | 1-click chest stacking, inventory sorting, item restocking, and favorites protection. |
| 12 | **Jotunn** (v2.20+) | `jotunn` | **21** | The industry-standard modding framework for custom items, pieces, and localizations. |
| 13 | **MagicBows** (v1.1.9) | `magicbows` | **20** | Elemental bows and crossbows (Fire, Frost, Lightning, Spirit, Poison). |
| 14 | **Better Archery** (v2.0.2) | `betterarchery` | **11** | Dedicated quiver system, zoom mechanics, and arrow retrieval after combat. |
| 15 | **TeleportEverything** (v2.9.1) | `teleporteverything` | **8** | Transport tamed animals, wolves, and ores through portals with configurable fees. |
| 16 | **DvergerStaves** (v1.1.0) | `dvergerstaves` | **7** | Dvergr staves of Fire, Healing, and Frost. |
| 17 | **ModSettings** | `modsettings` | **4** | In-game configuration UI for registered BepInEx mods. |
| 18 | **CraftFromChestsPlus** (v1.0.5) | `craftfromchestsplus` | **1** | Craft and build pulling materials directly from nearby containers. |

---

## 🕹️ Dual-Profile Architecture: Vanilla vs Super-Mod

Run both an unmodded clean game and an extensive modpack concurrently without file collisions:

```text
E:\SteamLibrary\steamapps\common\
├── Valheim/                   # PROFILE 1: CLEAN VANILLA + VIETNAMESE
│   ├── valheim.exe            # Launch directly via Steam "Play" button
│   └── BepInEx/plugins/       # Clean loader only (ValheimVietnamese.dll)
│
└── Valheim_Mod/               # PROFILE 2: SUPER-MODDED (104 PLUGINS + VIETNAMESE)
    ├── valheim.exe            # Launch via custom Desktop Shortcut ("Valheim Super Mod")
    └── BepInEx/plugins/       # 104 plugins (EpicLoot, Weapons, Magic, ReShade, QoL)
```

---

## 🛠️ CLI Automation Suite

```bash
# 1. One-click deploy translations to local game installations
python tools/deploy_translations.py

# 2. Install selected 24 mods and translation packs into Valheim_Mod
python tools/install_mods_to_valheim_mod.py

# 3. Validate JSONL schemas and 100% token signature matches
python tools/validate.py data

# 4. Check public files policy (guarantees zero binary leaks)
python tools/check_public_files.py

# 5. Run unit test suite
python -m unittest discover -s tests
```

---

## 🤝 Contributing

Contributions to translations, mod adaptations, and bug fixes are warmly welcomed. Please check [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a Pull Request:
1. Ensure 100% token signature consistency.
2. Run `python tools/validate.py data` (must report 0 errors).
3. Run `python tools/check_public_files.py` (must PASS).

---

<p align="center">
  <b>Developed by the Valheim Vietnamese Community • 2026</b><br>
  <i>"For a complete and legendary journey across the Tenth World!"</i>
</p>
