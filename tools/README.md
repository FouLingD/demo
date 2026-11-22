# 素材工具

从仓库根目录运行以下命令。启动游戏不需要运行这些工具。

除 `trim_sfx.py` 依赖 PyAV 外，其余工具仅使用 Python 标准库。

| 命令 | 用途与输出 |
| --- | --- |
| `python tools/gen_menu_sfx.py _sfx_tmp` | 生成 `ui_hover.wav`、`ui_click.wav`、`ui_menu_in.wav`、`ui_menu_out.wav`；省略输出目录时写入当前目录 |
| `python tools/gen_ui_sfx.py` | 生成 `_sfx_tmp/ui_history_close.wav` |
| `python tools/gen_ui_slider_thumb.py` | 生成 `_sfx_tmp/ui_slider_thumb.png`，尺寸为 22 x 22 |
| `python tools/trim_sfx.py 输入文件 输出.wav --cut-ms 100 --fade-ms 12` | 裁剪音效并输出 48 kHz、单声道、16 位 WAV；输出目录需已存在 |
| `python tools/png_probe.py 输入.png [输出.png]` | 读取固定 UI 坐标的像素；指定输出文件时裁取图片的纵向 100 至 320 区间 |

## 音效裁剪

仅使用裁剪工具时需要安装依赖：

```sh
python -m pip install av
```

`trim_sfx.py` 的可选参数与默认值：

| 参数 | 默认值 | 用途 |
| --- | --- | --- |
| `--cut-ms` | `100` | 裁去开头的毫秒数 |
| `--fade-ms` | `12` | 开头淡入时长 |
| `--tail-ms` | `0` | 裁去结尾的毫秒数 |
| `--boost` | `1` | 起始片段的增益倍数 |
| `--boost-ms` | `0` | 起始增益作用时长 |

`_sfx_tmp/` 已加入忽略规则。生成结果需要用于游戏时，再放入 `game/audio/` 或 `game/gui/` 等对应目录。
