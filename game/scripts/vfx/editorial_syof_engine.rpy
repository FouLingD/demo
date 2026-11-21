# ==============================================================================
# 《Set Yourself on Fire》风格原生 Ren'Py 书籍排版与磨损演出引擎
# Editorial Typography & Eroded Multiply Presentation System (1920x1080)
# ==============================================================================
# 设计规范：
# - 12 栏瑞士书籍网格（左右留白 160px，上下留白 120px，正文宽 740px / 21-24 汉字）
# - 完美四度模数音阶（1.333x）：30px 正文 / 28px 轻声细无衬线 / 42px 情绪重拍
# - 零粗体、零多余页眉页脚小字、高速打字节奏（slow_cps 48-55）
# - Part 2 单人剪影左右交替（爱音粉底左人右字 ↔ 灯灰底右人左字）+ 首字主题色
# ==============================================================================

init -5 python:
    import re

    def ed_accent_first(text, accent_color):
        """
        自动将段落首字（含段首引号 “ / 「 / 『 及紧随的第一个汉字）包裹角色主题色。
        跳过开头已存在的 Ren'Py 文本标签（如 {cps=...} / {w=...}）。
        """
        if not accent_color or not text:
            return text

        # 分离开头可能存在的 Ren'Py 花括号标签
        idx = 0
        n = len(text)
        while idx < n and text[idx] == "{":
            close = text.find("}", idx)
            if close == -1:
                break
            idx = close + 1

        if idx >= n:
            return text

        prefix_tags = text[:idx]
        rest = text[idx:]

        # 若首字符是左引号或省略号，连同后面第一个实字一起高亮
        take = 1
        if rest[0] in u"“「『‘（(":
            if len(rest) >= 2 and rest[1] not in u"{}":
                take = 2
        elif rest.startswith(u"……"):
            take = 3 if len(rest) >= 3 and rest[2] not in u"{}" else 2

        head = rest[:take]
        tail = rest[take:]
        return u"{}{{color={}}}{}{{/color}}{}".format(prefix_tags, accent_color, head, tail)


# ==============================================================================
# 1. 背景与剪影图层注册（1920x1080）
# ==============================================================================
image ed_corridor_right        = "images/editorial/ed_corridor_right.png"
image ed_bed_left              = "images/editorial/ed_bed_left.png"
image ed_hospital_right        = "images/editorial/ed_hospital_right.png"
image ed_bedroom_right         = "images/editorial/ed_bedroom_right.png"
image ed_bedroom_blender_left  = "images/editorial/ed_bedroom_blender_left.png"
image ed_rehearsal_left        = "images/editorial/ed_rehearsal_left.png"
image ed_station_right         = "images/editorial/ed_station_right.png"
image ed_sea_wide_right        = "images/editorial/ed_sea_wide_right.png"
image ed_sea_close_left        = "images/editorial/ed_sea_close_left.png"

image ed_p2_anon_pink          = "images/editorial/ed_p2_anon_pink.png"
image ed_p2_tomori_gray        = "images/editorial/ed_p2_tomori_gray.png"
image ed_black_ink             = Solid("#050507")

# A / C / D 拓展演出图层
image ed_a_paper_white         = "images/editorial/ed_a_paper_white.png"
image ed_a_pink_stain_1        = "images/editorial/ed_a_pink_stain_1.png"
image ed_a_pink_stain_2        = "images/editorial/ed_a_pink_stain_2.png"
image ed_a_pink_stain_3        = "images/editorial/ed_a_pink_stain_3.png"

# A 升级版：逆向自《Oblivion 2666》第一章结尾的 35mm 摄影光晕 + 受损胶片叠层（无粉底，仅局部粉字）
image ed_ob_lightleak          = Movie(play="video/editorial/ob_lightleak_flare.webm", size=(1920, 1080))
image ed_ob_filmdamage         = Movie(play="video/editorial/ob_film_damage.webm", size=(1920, 1080))
image ed_ob_sprockets          = Movie(play="video/editorial/ob_sprockets.webm", size=(1920, 1080))
image ed_ob_filmroll_frame:
    At(
        Fixed(
            Solid("#0b0a0a", size=(1920, 1080)),
            At("images/editorial/ed_bed_left.png", gateweave(24, 0.8, 0.8)),
            At("ed_ob_sprockets", sprocketoverlay()),
            Transform("ed_ob_filmdamage", blend="add", alpha=0.82)
        ),
        gateweave(24, 1.0, 1.0)
    )
    ytile 2
    xalign 0.5
    yoffset 0.0
    block:
        yoffset 0.0
        linear 7.5 yoffset -1080
        repeat

transform ed_ob_flare_ambient:
    blend "add"
    alpha 0.38

transform ed_ob_flare_burst:
    blend "add"
    alpha 0.96
    pause 0.16
    ease 0.72 alpha 0.24

transform ed_ob_flare_flash:
    blend "add"
    alpha 0.98
    pause 0.12
    ease 0.35 alpha 0.0

transform ed_ob_damage_ambient:
    blend "add"
    alpha 0.55

transform ed_ob_filmroll_zoom:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    ease_cubic 1.35 zoom 0.62

# 冷青 X 光 / 医院底片负片着色器（与焦橙柯达负片 photosnap 形成双化学显影对照）
transform ed_cyan_neg_grade:
    mesh True
    shader "cam.colorgrade"
    u_lift (-0.04, -0.02, 0.02)
    u_gamma (0.85, 0.72, 0.48)
    u_gain (0.25, 0.58, 0.92)
    u_sat 1.0

screen _ed_photoneg_cyan(d, dur=0.25):
    zorder 1000
    add Solid("#000000FF")
    frame at negativecol(dur), ed_cyan_neg_grade:
        background None
        add Transform(d, fit="fill", xysize=(config.screen_width, config.screen_height))

init python:
    def photosnap_cyan(duration=0.26, size=(1920, 1080)):
        """极速冷青 X 光负片快门闪切（适配医院宣判 / 雨夜逃亡）"""
        sc = renpy.screenshot_to_bytes(size)
        renpy.show_screen("_ed_photoneg_cyan", d=im.Data(sc, "screencap.png"), dur=duration)
        renpy.pause(duration, hard=True)
        renpy.hide_screen("_ed_photoneg_cyan")

image ed_c_bus_window_strip    = "images/editorial/ed_c_bus_window_strip.png"
image ed_c_bus_poles_tile      = HBox(
    "images/editorial/ed_c_bus_poles_overlay.png",
    "images/editorial/ed_c_bus_poles_overlay.png"
)

image ed_d_dark_ink            = "images/editorial/ed_d_dark_ink.png"
image ed_d_clinical_white      = "images/editorial/ed_d_clinical_white.png"

# 大巴车窗内电线杆高速掠过动画（锁在 y=360 车窗条内循环）
transform ed_c_poles_pass:
    ypos 360
    xpos 0
    linear 1.05 xpos -1920
    repeat


# ==============================================================================
# 2. 逆向自 SYOF 的微动效与切场节奏
# ==============================================================================
define ed_cut  = Dissolve(0.14)
define ed_fade = Dissolve(0.32)
define ed_snap = None

# 镜头轻微呼吸惯性（让静态磨损图产生胶片浮动感）
transform ed_bg_breath:
    xalign 0.5
    yalign 0.5
    zoom 1.025
    easeout 6.5 zoom 1.0

# 近景压迫感缓推
transform ed_bg_push:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    easeout 5.5 zoom 1.045

# 书籍文字区轻柔入场位移（零拖拽感）
transform ed_text_enter_left:
    alpha 0.0
    xoffset -10
    parallel:
        linear 0.16 alpha 1.0
    parallel:
        easeout_cubic 0.22 xoffset 0

transform ed_text_enter_right:
    alpha 0.0
    xoffset 10
    parallel:
        linear 0.16 alpha 1.0
    parallel:
        easeout_cubic 0.22 xoffset 0

transform ed_text_enter_center:
    alpha 0.0
    yoffset 8
    parallel:
        linear 0.18 alpha 1.0
    parallel:
        easeout_cubic 0.24 yoffset 0


# ==============================================================================
# 3. 无底框全屏书籍排版 Screen（保留原生回滚、历史记录、快进、自动阅读）
# ==============================================================================
screen editorial_say(
    who,
    what,
    ed_side="left",
    ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    ed_size=30,
    ed_leading=24,
    ed_kerning=1.8,
    ed_color="#EAE8E4",
    ed_accent=None,
    ed_shadow=False,
    ed_shadow_color="#2A263099",
    ed_cps=52
):
    zorder 90
    style_prefix "editorial"

    $ display_what = ed_accent_first(what, ed_accent) if ed_accent else what

    if ed_side == "left":
        frame:
            background None
            xpos 160
            ypos 0.5
            yanchor 0.5
            xsize 740
            padding (0, 0)
            at ed_text_enter_left

            text display_what id "what":
                font ed_font
                size ed_size
                color ed_color
                bold False
                line_leading ed_leading
                kerning ed_kerning
                slow_cps ed_cps
                if ed_shadow:
                    outlines [(0, ed_shadow_color, 1, 2)]
                else:
                    outlines []

    elif ed_side == "right":
        frame:
            background None
            xpos 1000
            ypos 0.5
            yanchor 0.5
            xsize 740
            padding (0, 0)
            at ed_text_enter_right

            text display_what id "what":
                font ed_font
                size ed_size
                color ed_color
                bold False
                line_leading ed_leading
                kerning ed_kerning
                slow_cps ed_cps
                if ed_shadow:
                    outlines [(0, ed_shadow_color, 1, 2)]
                else:
                    outlines []

    elif ed_side == "top_bar":
        frame:
            background None
            xpos 180
            ypos 165
            xsize 1160
            padding (0, 0)
            at ed_text_enter_left

            text display_what id "what":
                font ed_font
                size ed_size
                color ed_color
                bold False
                line_leading ed_leading
                kerning ed_kerning
                slow_cps ed_cps
                if ed_shadow:
                    outlines [(0, ed_shadow_color, 1, 2)]
                else:
                    outlines []

    elif ed_side == "bottom_bar":
        frame:
            background None
            xpos 180
            ypos 800
            xsize 1280
            padding (0, 0)
            at ed_text_enter_right

            text display_what id "what":
                font ed_font
                size ed_size
                color ed_color
                bold False
                line_leading ed_leading
                kerning ed_kerning
                slow_cps ed_cps
                if ed_shadow:
                    outlines [(0, ed_shadow_color, 1, 2)]
                else:
                    outlines []

    else:
        frame:
            background None
            xalign 0.5
            yalign 0.5
            xsize 880
            padding (0, 0)
            at ed_text_enter_center

            text display_what id "what":
                font ed_font
                size ed_size
                color ed_color
                bold False
                text_align 0.5
                xalign 0.5
                line_leading ed_leading
                kerning ed_kerning
                slow_cps ed_cps
                if ed_shadow:
                    outlines [(0, ed_shadow_color, 1, 2)]
                else:
                    outlines []


# ==============================================================================
# 4. 书籍排版专用角色定义（对应不同栏位、模数字号与主题色）
# ==============================================================================

# 暗底正文（左栏 / 右栏）：30px 思源宋体 ExtraLight
define ed_l = Character(
    None,
    screen="editorial_say",
    show_ed_side="left",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=30,
    show_ed_leading=24,
    show_ed_kerning=1.8,
    show_ed_color="#EAE8E4",
    show_ed_cps=54
)

define ed_r = Character(
    None,
    screen="editorial_say",
    show_ed_side="right",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=30,
    show_ed_leading=24,
    show_ed_kerning=1.8,
    show_ed_color="#EAE8E4",
    show_ed_cps=54
)

# 暗底情绪重拍 / 金句放大（1.333x 模数跃迁）：42px 思源宋体 ExtraLight
define ed_beat_l = Character(
    None,
    screen="editorial_say",
    show_ed_side="left",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=42,
    show_ed_leading=26,
    show_ed_kerning=3.2,
    show_ed_color="#F4F0EE",
    show_ed_cps=44
)

define ed_beat_r = Character(
    None,
    screen="editorial_say",
    show_ed_side="right",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=42,
    show_ed_leading=26,
    show_ed_kerning=3.2,
    show_ed_color="#F4F0EE",
    show_ed_cps=44
)

define ed_beat_c = Character(
    None,
    screen="editorial_say",
    show_ed_side="center",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=42,
    show_ed_leading=28,
    show_ed_kerning=3.4,
    show_ed_color="#F4F0EE",
    show_ed_cps=42
)

# 暗底次要低语 / 冷静补白：28px HarmonyOS Sans SC Thin
define ed_sub_l = Character(
    None,
    screen="editorial_say",
    show_ed_side="left",
    show_ed_font="fonts/HarmonyOS_Sans_SC_Thin.ttf",
    show_ed_size=28,
    show_ed_leading=22,
    show_ed_kerning=1.6,
    show_ed_color="#C0C2CA",
    show_ed_cps=58
)

define ed_sub_r = Character(
    None,
    screen="editorial_say",
    show_ed_side="right",
    show_ed_font="fonts/HarmonyOS_Sans_SC_Thin.ttf",
    show_ed_size=28,
    show_ed_leading=22,
    show_ed_kerning=1.6,
    show_ed_color="#C0C2CA",
    show_ed_cps=58
)

# 暗底首字角色印象色对白（用于 Part 5 / Part 6 高密度问答）
define ed_anon_l = Character(
    None,
    screen="editorial_say",
    show_ed_side="left",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=30,
    show_ed_leading=24,
    show_ed_kerning=1.8,
    show_ed_color="#EAE8E4",
    show_ed_accent="#FFB3C9",
    show_ed_cps=56
)

define ed_anon_r = Character(
    None,
    screen="editorial_say",
    show_ed_side="right",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=30,
    show_ed_leading=24,
    show_ed_kerning=1.8,
    show_ed_color="#EAE8E4",
    show_ed_accent="#FFB3C9",
    show_ed_cps=56
)

define ed_tomori_l = Character(
    None,
    screen="editorial_say",
    show_ed_side="left",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=30,
    show_ed_leading=24,
    show_ed_kerning=1.8,
    show_ed_color="#EAE8E4",
    show_ed_accent="#9BE3F7",
    show_ed_cps=54
)

define ed_tomori_r = Character(
    None,
    screen="editorial_say",
    show_ed_side="right",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=30,
    show_ed_leading=24,
    show_ed_kerning=1.8,
    show_ed_color="#EAE8E4",
    show_ed_accent="#9BE3F7",
    show_ed_cps=54
)

define ed_taki_r = Character(
    None,
    screen="editorial_say",
    show_ed_side="right",
    show_ed_font="fonts/SourceHanSerifCN-ExtraLight.otf",
    show_ed_size=30,
    show_ed_leading=24,
    show_ed_kerning=1.8,
    show_ed_color="#EAE8E4",
    show_ed_accent="#B6A8E8",
    show_ed_cps=56
)

# Part 2 粉灰交替单人剪影对白（31px 尚古明朝体 Light + 首字主题色）
# 爱音：粉底、爱音剪影在左、字在右（樱粉首字）
define ed_p2_anon = Character(
    None,
    screen="editorial_say",
    show_ed_side="right",
    show_ed_font="fonts/ShangguSerif-Light.ttf",
    show_ed_size=31,
    show_ed_leading=24,
    show_ed_kerning=1.6,
    show_ed_color="#F8F6F8",
    show_ed_accent="#FFD0E0",
    show_ed_shadow=True,
    show_ed_shadow_color="#3A283499",
    show_ed_cps=52
)

# 高松灯：灰底、灯剪影在右、字在左（冰蓝首字）
define ed_p2_tomori = Character(
    None,
    screen="editorial_say",
    show_ed_side="left",
    show_ed_font="fonts/ShangguSerif-Light.ttf",
    show_ed_size=31,
    show_ed_leading=24,
    show_ed_kerning=1.6,
    show_ed_color="#F4F6F9",
    show_ed_accent="#9BE3F7",
    show_ed_shadow=True,
    show_ed_shadow_color="#23263299",
    show_ed_cps=50
)


# ==============================================================================
# 5. A / C / D 拓展演出专用角色（沿用本游戏常规字体 ChillHuoSong 32px，收紧字距/行距塑造压迫感）
# ==============================================================================

# A（Ch02 草莓布丁 — 逆向 Oblivion 2666 Ch1 结尾：无粉底、摄影漏光光晕 + 胶片损坏 + 局部粉字）
define ed_a_paper = Character(
    None,
    screen="editorial_say",
    show_ed_side="left",
    show_ed_font="fonts/ChillHuoSong_F_Regular.otf",
    show_ed_size=32,
    show_ed_leading=10,
    show_ed_kerning=0.4,
    show_ed_color="#ECEAE6",
    show_ed_shadow=True,
    show_ed_shadow_color="#050406CC",
    show_ed_cps=48
)

# C（Ch07 长途大巴车窗窄条）：上下黑边常规体，收紧行距字距
define ed_c_top = Character(
    None,
    screen="editorial_say",
    show_ed_side="top_bar",
    show_ed_font="fonts/ChillHuoSong_F_Regular.otf",
    show_ed_size=32,
    show_ed_leading=10,
    show_ed_kerning=0.4,
    show_ed_color="#E4E8EE",
    show_ed_cps=52
)

define ed_c_bottom = Character(
    None,
    screen="editorial_say",
    show_ed_side="bottom_bar",
    show_ed_font="fonts/ChillHuoSong_F_Regular.otf",
    show_ed_size=32,
    show_ed_leading=10,
    show_ed_kerning=0.4,
    show_ed_color="#A8CBE4",
    show_ed_cps=50
)

# D（Ch10 假死刑真相黑白负片反色硬切，无人物剪影）：常规 32px + 紧缩字距行距压迫感
define ed_d_black = Character(
    None,
    screen="editorial_say",
    show_ed_side="left",
    show_ed_font="fonts/ChillHuoSong_F_Regular.otf",
    show_ed_size=32,
    show_ed_leading=9,
    show_ed_kerning=0.3,
    show_ed_color="#ECEAEF",
    show_ed_cps=50
)

define ed_d_white = Character(
    None,
    screen="editorial_say",
    show_ed_side="center",
    show_ed_font="fonts/ChillHuoSong_F_Regular.otf",
    show_ed_size=32,
    show_ed_leading=9,
    show_ed_kerning=0.3,
    show_ed_color="#0E1014",
    show_ed_cps=46
)
