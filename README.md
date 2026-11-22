# 二手时间 - After the Rooftop

基于 Ren'Py 8.5.3 的 BanG Dream! It's MyGO!!!!! 同人视觉小说。

## 启动

将仓库所在的父目录设为 Ren'Py 启动器的项目目录，选择本项目并启动。`game/` 是游戏内容目录，日常编辑时用编辑器打开整个仓库。

## 目录导航

| 路径 | 内容 |
| --- | --- |
| [game/script.rpy](game/script.rpy) | 游戏入口与章节路由 |
| [game/options.rpy](game/options.rpy) | 项目设置与发行配置 |
| [game/gui.rpy](game/gui.rpy)、[game/screens.rpy](game/screens.rpy) | 基础界面配置与屏幕定义 |
| [game/scripts/story/](game/scripts/story/) | 分章剧情与特殊演出段落 |
| [game/scripts/core/](game/scripts/core/) | 角色定义、音频、状态与基础逻辑 |
| [game/scripts/gui/](game/scripts/gui/) | 自定义菜单与特殊界面 |
| [game/scripts/vfx/](game/scripts/vfx/) | 视觉效果与演出引擎 |
| `game/images/`、`game/gui/` | 剧情图片与界面素材 |
| `game/audio/`、`game/video/`、`game/fonts/` | 音频、视频与字体 |
| [docs/story/](docs/story/) | 纯文本剧本与台词文稿 |
| [docs/notes/](docs/notes/) | 制作备注、演出说明与素材缺口记录 |
| [docs/screenshots/ui/](docs/screenshots/ui/) | 历次界面截图，后续一批位于 `iterations/` |
| [archive/](archive/) | 旧版 GUI、背景原图与调试资料 |
| [tools/](tools/README.md) | 素材制作辅助工具及用法 |
| [.vscode/](.vscode/) | 仓库统一的编辑器设置 |

## 制作资料

- [2026-11-21 项目备注](docs/notes/2026-11-21-项目备注.md)
- [剧情与演出建议](docs/notes/剧情与演出建议.md)
- [特殊演出与素材缺口记录](docs/notes/逆向相关说明.md)

## 日常维护

- 剧情沿用 `ch01_...rpy` 至 `ch11_...rpy` 的章节命名；图片、音频等资源沿用现有路径。
- 文稿、备注和截图分别放入 `docs/` 对应目录，旧版资源放入 `archive/`。
- 编辑 `.rpy` 源文件，不提交重新生成的编译文件、缓存、个人存档和临时锁文件；忽略规则统一在根目录 `.gitignore`。
- 现有四个无对应源码的 `.rpyc` 暂保留在原位置：`story/test_chain`、`story/test_extend`、`story/test_extend2` 和 `vfx/00_oblivion_showcase`（均位于 `game/scripts/` 下）。
- 工具中间产物使用 `_sfx_tmp/`；正式素材放入 `game/` 对应目录。`docs/`、`archive/`、`tools/` 不进入游戏发行包。
