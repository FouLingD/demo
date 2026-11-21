## 02_defines.rpy - 角色声明、立绘映射、头像（Side Image）、传说之下拨片音效回调与转场
## 严格对标 Lemma Soft 规范与 01_renpy_basic_style_guide.md

init python:
    # 传说之下风格：打字机打字时播放专属乐器拨片/杂音音效
    # 智能立绘展出：当非主视角（非高松灯第一视角）角色发言时，若场上尚未展出该角色，自动呈现立绘！

    ## 打字机状态（供 10_ui_menu.rpy 的进出菜单逻辑判断要不要接回拨片音）
    if not hasattr(store, "_blip_typing"):
        store._blip_typing = False
    if not hasattr(store, "_blip_sound"):
        store._blip_sound = None

    def make_blip_callback(blip_sound):
        def _blip_cb(event, interact=True, **kwargs):
            if not interact:
                return
            if event == "show":
                store._blip_typing = True
                store._blip_sound = blip_sound
                renpy.sound.play(blip_sound, channel="blip", loop=True)
            elif event in ("slow_done", "end"):
                store._blip_typing = False
                renpy.sound.stop(channel="blip")
        return _blip_cb

    blip_cb_tomori = make_blip_callback("audio/sfx/blip_tomori.ogg")
    blip_cb_anon = make_blip_callback("audio/sfx/blip_anon.ogg")
    blip_cb_soyo = make_blip_callback("audio/sfx/blip_soyo.ogg")
    blip_cb_sakiko = make_blip_callback("audio/sfx/blip_sakiko.ogg")
    blip_cb_taki = make_blip_callback("audio/sfx/blip_default.ogg")
    blip_cb_mutsumi = make_blip_callback("audio/sfx/blip_default.ogg")
    blip_cb_doctor = make_blip_callback("audio/sfx/blip_default.ogg")
    blip_cb_nurse = make_blip_callback("audio/sfx/blip_default.ogg")
    blip_cb_default = make_blip_callback("audio/sfx/blip_default.ogg")

## 角色定义 ####################################################################

# 旁白
define narrator = Character(
    None,
    callback=blip_cb_default,
    what_color="#000000",
    what_italic=False,
    what_slow_cps=35
)

# 主要角色（绑定立绘与头像标签 image="...", 支持自动属性联动与 SideImage）
define tomori = Character(
    "高松灯",
    image="tomori",
    who_color="#000000",
    who_outlines=[],
    what_color="#000000",
    callback=blip_cb_tomori,
    what_prefix="“",
    what_suffix="”",
    what_slow_cps=32
)

define anon = Character(
    "千早爱音",
    image="anon",
    who_color="#000000",
    who_outlines=[],
    what_color="#000000",
    callback=blip_cb_anon,
    what_prefix="“",
    what_suffix="”",
    what_slow_cps=38
)

define soyo = Character(
    "长崎素世",
    image="soyo",
    who_color="#000000",
    who_outlines=[],
    what_color="#000000",
    callback=blip_cb_soyo,
    what_prefix="“",
    what_suffix="”",
    what_slow_cps=34
)

define sakiko = Character(
    "丰川祥子",
    image="sakiko",
    who_color="#000000",
    who_outlines=[],
    what_color="#000000",
    callback=blip_cb_sakiko,
    what_prefix="“",
    what_suffix="”",
    what_slow_cps=32
)

define taki = Character(
    "椎名立希",
    image="taki",
    who_color="#000000",
    who_outlines=[],
    what_color="#000000",
    callback=blip_cb_taki,
    what_prefix="“",
    what_suffix="”",
    what_slow_cps=36
)

define mutsumi = Character(
    "若叶睦",
    image="mutsumi",
    who_color="#000000",
    who_outlines=[],
    what_color="#000000",
    callback=blip_cb_mutsumi,
    what_prefix="“",
    what_suffix="”",
    what_slow_cps=30
)

# 配角与医护人员
define doctor = Character("主治医生", image="doctor", who_color="#000000", what_color="#000000", callback=blip_cb_doctor, what_prefix="“", what_suffix="”")
define nurse_a = Character("护士A", who_color="#000000", what_color="#000000", callback=blip_cb_nurse, what_prefix="“", what_suffix="”")
define nurse_b = Character("护士B", who_color="#000000", what_color="#000000", callback=blip_cb_nurse, what_prefix="“", what_suffix="”")
define nurse_c = Character("护士C", who_color="#000000", what_color="#000000", callback=blip_cb_nurse, what_prefix="“", what_suffix="”")
define nurse = Character("护士", image="nurse", who_color="#000000", what_color="#000000", callback=blip_cb_nurse, what_prefix="“", what_suffix="”")
define patrol_nurse = Character("巡房护士", image="nurse", who_color="#000000", what_color="#000000", callback=blip_cb_nurse, what_prefix="“", what_suffix="”")
define nurse_head = Character("护士长", image="nurse", who_color="#000000", what_color="#000000", callback=blip_cb_nurse, what_prefix="“", what_suffix="”")
define intern_doctor = Character("实习医生", who_color="#000000", what_color="#000000", callback=blip_cb_default, what_prefix="“", what_suffix="”")
define mother = Character("灯的母亲", who_color="#000000", what_color="#000000", callback=blip_cb_default, what_prefix="“", what_suffix="”")
define father = Character("灯的父亲", who_color="#000000", what_color="#000000", callback=blip_cb_default, what_prefix="“", what_suffix="”")
define grandpa = Character("老爷爷", who_color="#000000", what_color="#000000", callback=blip_cb_default, what_prefix="“", what_suffix="”")

# 未知角色阶段过渡
define unknown = Character("？？？", who_color="#000000", what_color="#000000", callback=blip_cb_anon, what_prefix="“", what_suffix="”")
define pink_girl = Character("粉发少女", who_color="#000000", what_color="#000000", callback=blip_cb_anon, what_prefix="“", what_suffix="”")

## NVL 全屏小说模式专属角色（纯黑/纯白背景，优雅留白，不显底部对话底框）
define vn_white = Character(
    None,
    kind=nvl,
    what_color="#ffffff",
    what_size=30,
    what_line_spacing=18,
    what_font=gui.text_font
)

define vn_black = Character(
    None,
    kind=nvl,
    what_color="#000000",
    what_size=30,
    what_line_spacing=18,
    what_font=gui.text_font
)

## 纯色背景
image bg white = Solid("#ffffff")
image bg black = Solid("#000000")

## 雪花微粒特效：细小雪花正向飘落（白）与倒转升腾（黑）
image snow_white = SnowBlossom("images/vfx/particle_snow_white.png", count=45, border=50, xspeed=(-15, 15), yspeed=(35, 80), fast=True)
image snow_black_reverse = SnowBlossom("images/vfx/particle_snow_black.png", count=45, border=50, xspeed=(-15, 15), yspeed=(-80, -35), fast=True)

## 非线性苏醒睁眼效果 (Eyelids Awakening)
transform eye_upper:
    xsize 1920 ysize 560
    xpos 0 ypos 0 yanchor 0.0
    # 第一次虚弱微睁 (基于 easings.net 的 easeInOutQuad 非线性平滑曲线)
    pause 0.2
    warp ease_in_out_quad 0.6 ypos -160
    pause 0.2
    warp ease_in_out_quad 0.4 ypos 0
    pause 0.35
    # 第二次苏醒彻底张开 (基于 easings.net 的 easeInOutCubic 曲线)
    warp ease_in_out_cubic 1.3 ypos -560

transform eye_lower:
    xsize 1920 ysize 560
    xpos 0 ypos 1080 yanchor 1.0
    # 第一次虚弱微睁
    pause 0.2
    warp ease_in_out_quad 0.6 ypos 1240
    pause 0.2
    warp ease_in_out_quad 0.4 ypos 1080
    pause 0.35
    # 第二次苏醒彻底张开
    warp ease_in_out_cubic 1.3 ypos 1640

screen eyes_opening():
    zorder 180
    add Solid("#000000") at eye_upper
    add Solid("#000000") at eye_lower


## 转场与变换 ##################################################################

define slow_dissolve = Dissolve(2.0)
define fast_dissolve = Dissolve(0.3)
define cut_white_fade = Fade(0.15, 0.05, 0.35, color="#ffffff")
define cut_black_fade = Fade(0.15, 0.05, 0.35, color="#000000")
define slow_whiteout = Fade(0.8, 0.2, 1.5, color="#ffffff")
define push_right = PushMove(0.50, "pushright")
define push_left = PushMove(0.45, "pushleft")
define flash_white = Fade(0.1, 0.0, 0.4, color="#ffffff")
define flash_red = Fade(0.1, 0.0, 0.4, color="#e53e3e")
define flash_warm = Fade(0.15, 0.05, 0.45, color="#fff0f5")
define flash_cyan = Fade(0.12, 0.04, 0.40, color="#e6fffa")
define shake_h = Move((12, 0), (-12, 0), .08, bounce=True, repeat=True, delay=.24, subpixel=True)

transform center_standee:
    xalign 0.5
    yalign 0.0
    yoffset -60

transform left_standee:
    xalign 0.22
    yalign 0.0
    yoffset -60

transform right_standee:
    xalign 0.78
    yalign 0.0
    yoffset -60

transform slight_shake:
    linear 0.05 xoffset -8
    linear 0.05 xoffset 8
    linear 0.05 xoffset -4
    linear 0.05 xoffset 4
    linear 0.05 xoffset 0

## 双人对峙与争吵动态镜头视线流转系统 (基于 easings.net 非线性缓动) ##############
# 占位色块立绘（正式立绘替换前供测试观察镜头与站位）
image standee_block_taki = Composite(
    (500, 1100),
    (0, 0), Solid("#2B3D54", xsize=500, ysize=1100),
    (10, 10), Solid("#384E6B", xsize=480, ysize=1080),
    (0, 480), Text("椎名立希\n(Taki)", size=44, color="#ffffff", bold=True, xalign=0.5, text_align=0.5)
)

image standee_block_soyo = Composite(
    (500, 1100),
    (0, 0), Solid("#7A542E", xsize=500, ysize=1100),
    (10, 10), Solid("#9E6C3B", xsize=480, ysize=1080),
    (0, 480), Text("长崎爽世\n(Soyo)", size=44, color="#ffffff", bold=True, xalign=0.5, text_align=0.5)
)

# 站位与镜头焦点动态流转变换
transform standee_duo_init_left:
    xalign 0.22
    yalign 0.0
    yoffset -50
    zoom 1.0
    alpha 1.0
    matrixcolor BrightnessMatrix(0.0)

transform standee_duo_init_right:
    xalign 0.78
    yalign 0.0
    yoffset -50
    zoom 1.0
    alpha 1.0
    matrixcolor BrightnessMatrix(0.0)

# 视线/镜头平移至左侧角色（左说话居中高亮，右侧避让暗淡）
transform focus_standee_left(d=0.55):
    warp ease_in_out_cubic d xalign 0.36 zoom 1.04 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform unfocus_standee_right(d=0.55):
    warp ease_in_out_cubic d xalign 0.86 zoom 0.94 alpha 0.55 matrixcolor BrightnessMatrix(-0.22)

# 视线/镜头平移至右侧角色（右说话居中高亮，左侧避让暗淡）
transform focus_standee_right(d=0.55):
    warp ease_in_out_cubic d xalign 0.64 zoom 1.04 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

transform unfocus_standee_left(d=0.55):
    warp ease_in_out_cubic d xalign 0.14 zoom 0.94 alpha 0.55 matrixcolor BrightnessMatrix(-0.22)

# 左侧迫近质问
transform standee_left_press(d=0.45):
    warp ease_out_quart d xalign 0.44 zoom 1.10 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

# 右侧厉声喝止
transform standee_right_burst(d=0.35):
    warp ease_out_quart d xalign 0.66 zoom 1.08 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

## 第三章与单人叙事角色站位与动效 (基于 easings.net 非线性曲线，固定坐标锚点) ##############
transform anon_center:
    warp ease_in_out_cubic 0.6 xalign 0.50 yalign 0.0 yoffset -60 zoom 1.0

transform anon_sit:
    warp ease_in_out_cubic 0.65 xalign 0.62 yalign 0.0 yoffset 40 zoom 0.94

transform anon_wander:
    warp ease_in_out_cubic 0.65 xalign 0.38 yalign 0.0 yoffset -60 zoom 1.0

transform anon_table:
    warp ease_in_out_cubic 0.55 xalign 0.34 yalign 0.0 yoffset -60 zoom 1.02

transform anon_retreat:
    warp ease_in_out_cubic 0.50 xalign 0.58 yalign 0.0 yoffset -60 zoom 0.98

transform anon_lean_in:
    warp ease_in_out_cubic 0.50 xalign 0.44 yalign 0.0 yoffset -55 zoom 1.05

transform anon_door:
    warp ease_in_out_cubic 0.60 xalign 0.72 yalign 0.0 yoffset -60 zoom 0.96

transform anon_pace_right(d=0.75):
    warp ease_in_out_sine d xalign 0.62 yalign 0.0 yoffset -60 zoom 1.0

transform anon_pace_left(d=0.80):
    warp ease_in_out_sine d xalign 0.36 yalign 0.0 yoffset -60 zoom 1.0

transform anon_pace_center(d=0.70):
    warp ease_in_out_sine d xalign 0.50 yalign 0.0 yoffset -60 zoom 1.0

transform anon_burst_in:
    xalign 0.50 yalign 0.0 yoffset 60 zoom 0.95 alpha 0.0
    parallel:
        easein 0.20 alpha 1.0
    parallel:
        warp ease_out_back 0.55 yoffset -60 zoom 1.0
    easein 0.10 xoffset -10
    easeout 0.10 xoffset 10
    easein 0.08 xoffset -5
    easeout 0.08 xoffset 0

transform stand_up_stagger:
    easein 0.22 yoffset -30
    easeout 0.35 yoffset -85 xoffset -10
    easein 0.20 yoffset -50 xoffset 8
    easeout 0.25 yoffset -60 xoffset 0


transform standee_shake_h:
    easein 0.04 xoffset -12
    easeout 0.04 xoffset 12
    easein 0.04 xoffset -8
    easeout 0.04 xoffset 8
    easein 0.04 xoffset -4
    easeout 0.04 xoffset 4
    easeout 0.04 xoffset 0

transform standee_jump:
    easein 0.14 yoffset -102
    easeout 0.14 yoffset -56
    easein 0.10 yoffset -76
    easeout 0.12 yoffset -60

transform standee_nod:
    easein 0.18 yoffset -36
    easeout 0.22 yoffset -60

transform standee_tremble:
    block:
        linear 0.04 xoffset -3
        linear 0.04 xoffset 3
        linear 0.04 xoffset -2
        linear 0.04 xoffset 2
        linear 0.04 xoffset 0
        repeat 4

transform standee_step_in:
    warp ease_in_out_cubic 0.55 xalign 0.50 yalign 0.0 yoffset -42 zoom 1.08

transform standee_step_back:
    warp ease_in_out_cubic 0.55 xalign 0.56 yalign 0.0 yoffset -60 zoom 0.95

transform camera_heartbeat:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    easein 0.12 zoom 1.035
    easeout 0.16 zoom 1.005
    easein 0.10 zoom 1.022
    easeout 0.35 zoom 1.0

transform camera_gentle_sway:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 1.02
    block:
        ease 3.2 xoffset 8 yoffset -4
        ease 3.2 xoffset -8 yoffset 4
        repeat

## 苏醒倾斜与高斯模糊镜头变换 (Ren'Py 8 Camera Transform，动态动作曲线系统) ############
transform waking_camera_intro:
    rotate_pad False
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 1.05
    rotate -3.0
    # 阶段一：初醒时完全模糊 (50.0 彻底失焦，仅能隐约感知大片粉色色块)
    blur 50.0
    # 第一次虚弱微睁 (与 eyelids 0.2s pause + 0.6s warp ease_in_out_quad 同步进光)
    pause 0.2
    warp ease_in_out_quad 0.6 blur 28.0
    # 闭眼短暂回缩 (0.2s pause + 0.4s warp ease_in_out_quad)
    pause 0.2
    warp ease_in_out_quad 0.4 blur 38.0
    pause 0.35
    # 第二次苏醒彻底张开：沿 ease_in_out_cubic 运动函数收敛至约 9.5 初始焦距
    warp ease_in_out_cubic 1.3 blur 9.5
    # 阶段二：镜头角度保持固定微倾（不晃镜头），单纯由高斯模糊在“模糊与清楚”之间往复游移（模拟刚睁眼对不上焦的视觉感受）
    block:
        warp ease_in_out_sine 2.2 blur 15.0
        warp ease_in_out_sine 2.2 blur 3.0
        warp ease_in_out_sine 2.0 blur 13.5
        warp ease_in_out_sine 2.0 blur 2.5
        repeat

transform waking_tilt_blur:
    rotate_pad False
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 1.05
    rotate -3.0
    blur 10.0
    block:
        warp ease_in_out_sine 2.2 blur 15.0
        warp ease_in_out_sine 2.2 blur 3.0
        warp ease_in_out_sine 2.0 blur 13.5
        warp ease_in_out_sine 2.0 blur 2.5
        repeat

transform waking_focus_restore(d=1.6):
    # 阶段三：认出“千早爱音”后，模糊度与倾斜度通过非线性动作曲线彻底回归正常
    parallel:
        warp ease_out_cubic d blur 0.0
    parallel:
        warp ease_in_out_cubic d rotate 0.0 zoom 1.0




## 实际背景资产定义（58张 2K NovelAI V5 风格图）
image bg arcade_01_blue = "images/bg/arcade_01_blue.png"
image bg arcade_01_orange = "images/bg/arcade_01_orange.png"
image bg bedroom_01_blue = "images/bg/bedroom_01_blue.png"
image bg bedroom_01_magenta = "images/bg/bedroom_01_magenta.png"
image bg bedroom_01_orange = "images/bg/bedroom_01_orange.png"
image bg bedroom_01_purple = "images/bg/bedroom_01_purple.png"
image bg bedroom_01_red = "images/bg/bedroom_01_red.png"
image bg bedroom_01_rose = "images/bg/bedroom_01_rose.png"
image bg car_window_01_blue = "images/bg/car_window_01_blue.png"
image bg car_window_01_orange = "images/bg/car_window_01_orange.png"
image bg city_01_blue = "images/bg/city_01_blue.png"
image bg city_01_orange = "images/bg/city_01_orange.png"
image bg city_02_blue = "images/bg/city_02_blue.png"
image bg city_02_orange = "images/bg/city_02_orange.png"
image bg cloud_01_blue = "images/bg/cloud_01_blue.png"
image bg cloud_01_orange = "images/bg/cloud_01_orange.png"
image bg cloud_02_blue = "images/bg/cloud_02_blue.png"
image bg cloud_02_orange = "images/bg/cloud_02_orange.png"
image bg corridor_01_blue = "images/bg/corridor_01_blue.png"
image bg corridor_01_orange = "images/bg/corridor_01_orange.png"
image bg corridor_02_blue = "images/bg/corridor_02_blue.png"
image bg corridor_02_orange = "images/bg/corridor_02_orange.png"
image bg corridor_03_blue = "images/bg/corridor_03_blue.png"
image bg corridor_03_orange = "images/bg/corridor_03_orange.png"
image bg corridor_04_blue = "images/bg/corridor_04_blue.png"
image bg corridor_04_orange = "images/bg/corridor_04_orange.png"
image bg corridor_05_blue = "images/bg/corridor_05_blue.png"
image bg corridor_05_orange = "images/bg/corridor_05_orange.png"
image bg hospital_bed_01_blue = "images/bg/hospital_bed_01_blue.png"
image bg hospital_bed_01_orange = "images/bg/hospital_bed_01_orange.png"
image bg hospital_bed_02_blue = "images/bg/hospital_bed_02_blue.png"
image bg hospital_bed_02_orange = "images/bg/hospital_bed_02_orange.png"
image bg hospital_exterior_01_blue = "images/bg/hospital_exterior_01_blue.png"
image bg hospital_exterior_01_orange = "images/bg/hospital_exterior_01_orange.png"
image bg hospital_interior_01_blue = "images/bg/hospital_interior_01_blue.png"
image bg hospital_interior_01_orange = "images/bg/hospital_interior_01_orange.png"
image bg rehearsal_room_01_blue = "images/bg/rehearsal_room_01_blue.png"
image bg rehearsal_room_01_orange = "images/bg/rehearsal_room_01_orange.png"
image bg restaurant_01_blue = "images/bg/restaurant_01_blue.png"
image bg restaurant_01_orange = "images/bg/restaurant_01_orange.png"
image bg road_01_blue = "images/bg/road_01_blue.png"
image bg road_01_orange = "images/bg/road_01_orange.png"
image bg road_02_blue = "images/bg/road_02_blue.png"
image bg road_02_orange = "images/bg/road_02_orange.png"
image bg school_01_blue = "images/bg/school_01_blue.png"
image bg school_01_orange = "images/bg/school_01_orange.png"
image bg sea_01_blue = "images/bg/sea_01_blue.png"
image bg sea_01_orange = "images/bg/sea_01_orange.png"
image bg sea_02_blue = "images/bg/sea_02_blue.png"
image bg sea_02_orange = "images/bg/sea_02_orange.png"
image bg sea_03_blue = "images/bg/sea_03_blue.png"
image bg sea_03_orange = "images/bg/sea_03_orange.png"
image bg sea_04_blue = "images/bg/sea_04_blue.png"
image bg sea_04_orange = "images/bg/sea_04_orange.png"
image bg station_01_blue = "images/bg/station_01_blue.png"
image bg station_01_orange = "images/bg/station_01_orange.png"
image bg station_02_blue = "images/bg/station_02_blue.png"
image bg station_02_orange = "images/bg/station_02_orange.png"

## 兼容别名映射
image bg whiteout = Solid("#ffffff")
image bg hospital_room = "images/bg/hospital_bed_01_blue.png"
image bg hospital_corridor = "images/bg/corridor_01_blue.png"
image bg hospital = "images/bg/hospital_interior_01_blue.png"
image bg music_room = "images/bg/rehearsal_room_01_blue.png"
image bg school = "images/bg/school_01_blue.png"
image bg school_rooftop = "images/bg/cloud_01_blue.png"
image bg street = "images/bg/road_01_blue.png"
image bg night_street = "images/bg/road_02_blue.png"
image bg bus_stop = "images/bg/road_01_blue.png"
image bg cafe = "images/bg/restaurant_01_blue.png"
image bg arcade = "images/bg/arcade_01_blue.png"
image bg seaside = "images/bg/sea_01_blue.png"
image bg sunset_beach = "images/bg/sea_01_orange.png"
image bg station_platform = "images/bg/station_01_blue.png"
image bg apartment_bedroom = "images/bg/bedroom_01_blue.png"
image bg apartment_bedroom_dark = "images/bg/bedroom_01_purple.png"
image bg apartment_entrance = "images/bg/corridor_01_blue.png"
image bg aquarium_tunnel = "images/bg/sea_02_blue.png"
image bg bus_interior = "images/bg/car_window_01_blue.png"
image bg train_window = "images/bg/car_window_01_blue.png"

## 角色立绘定义 ################################################################
image anon casual blush = "images/characters/anon/anon_casual_blush.png"
image anon casual confident = "images/characters/anon/anon_casual_grin.png"
image anon casual excited = "images/characters/anon/anon_casual_excited.png"
image anon casual grin = "images/characters/anon/anon_casual_grin.png"
image anon casual smirk = "images/characters/anon/anon_casual_smirk.png"
image anon coat confident = "images/characters/anon/anon_casual_grin.png"
image anon coat grin = "images/characters/anon/anon_casual_grin.png"
image anon coat smirk = "images/characters/anon/anon_casual_smirk.png"
image anon hospital blush = "images/characters/anon/anon_hospital_flustered.png"
image anon hospital confident = "images/characters/anon/anon_hospital_confident.png"
image anon hospital embarrassed = "images/characters/anon/anon_hospital_flustered.png"
image anon hospital excited = "images/characters/anon/anon_casual_excited.png"
image anon hospital flustered = "images/characters/anon/anon_hospital_flustered.png"
image anon hospital gun = "images/characters/anon/anon_hospital_smug.png"
image anon hospital happy = "images/characters/anon/anon_hospital_happy.png"
image anon hospital sad = "images/characters/anon/anon_hospital_tears.png"
image anon hospital shy = "images/characters/anon/anon_hospital_flustered.png"
image anon hospital sign = "images/characters/anon/anon_pose_gyaru_peace.png"
image anon hospital smile = "images/characters/anon/anon_hospital_smile.png"
image anon hospital smirk = "images/characters/anon/anon_hospital_smirk.png"
image anon hospital smug = "images/characters/anon/anon_hospital_smug.png"
image anon hospital surprised = "images/characters/anon/anon_hospital_flustered.png"
image anon hospital tears = "images/characters/anon/anon_hospital_tears.png"
image anon hospital up = "images/characters/anon/anon_hospital_up.png"
image anon hospital v = "images/characters/anon/anon_hospital_v.png"
image anon hospital viewer = "images/characters/anon/anon_hospital_smile.png"
image anon hospital waving = "images/characters/anon/anon_pose_pray.png"
image tomori casual expressionless = "images/characters/tomori/tomori_default_expressionless.png"
image tomori casual happy = "images/characters/tomori/tomori_default_happy.png"
image tomori casual pensive = "images/characters/tomori/tomori_default_pensive.png"
image tomori casual shy = "images/characters/tomori/tomori_default_shy.png"
image tomori casual smile = "images/characters/tomori/tomori_default_smile.png"
image tomori coat pensive = "images/characters/tomori/tomori_coat_pensive.png"
image tomori coat serious = "images/characters/tomori/tomori_coat_serious.png"
image tomori coat smile = "images/characters/tomori/tomori_coat_smile.png"
image tomori hospital chin = "images/characters/tomori/tomori_hospital_pensive.png"
image tomori hospital confused = "images/characters/tomori/tomori_hospital_confused.png"
image tomori hospital determined = "images/characters/tomori/tomori_hospital_determined.png"
image tomori hospital expressionless = "images/characters/tomori/tomori_hospital_expressionless.png"
image tomori hospital fidgeting = "images/characters/tomori/tomori_hospital_confused.png"
image tomori hospital fingers = "images/characters/tomori/tomori_hospital_fingers.png"
image tomori hospital hands = "images/characters/tomori/tomori_hospital_hands.png"
image tomori hospital happy = "images/characters/tomori/tomori_hospital_smile.png"
image tomori hospital pensive = "images/characters/tomori/tomori_hospital_pensive.png"
image tomori hospital serious = "images/characters/tomori/tomori_coat_serious.png"
image tomori hospital shushing = "images/characters/tomori/tomori_meme_hide.png"
image tomori hospital smile = "images/characters/tomori/tomori_hospital_smile.png"
image tomori hospital surprised = "images/characters/tomori/tomori_hospital_surprised.png"
image tomori hospital tears = "images/characters/tomori/tomori_hospital_tears.png"
image tomori wedding shy = "images/characters/tomori/tomori_wedding_shy.png"
image tomori wedding smile = "images/characters/tomori/tomori_wedding_smile.png"
image tomori wedding tears = "images/characters/tomori/tomori_wedding_tears.png"
image soyo annoyed annoyed = "images/characters/soyo/soyo_annoyed_annoyed.png"
image soyo annoyed disdain = "images/characters/soyo/soyo_annoyed_disdain.png"

# 素世立绘别名
image soyo = "images/characters/soyo/soyo_annoyed_annoyed.png"
image soyo annoyed = "images/characters/soyo/soyo_annoyed_annoyed.png"
image soyo disdain = "images/characters/soyo/soyo_annoyed_disdain.png"
image side soyo = "images/characters/side/side_soyo_annoyed_annoyed.png"
image side soyo annoyed = "images/characters/side/side_soyo_annoyed_annoyed.png"
image side soyo disdain = "images/characters/side/side_soyo_annoyed_annoyed.png"
image side tomori = "images/characters/side/side_tomori_hospital_expressionless.png"
image side anon = "images/characters/side/side_anon_hospital_smile.png"
image side sakiko = "images/characters/side/side_sakiko_annoyed_annoyed.png"

# 立希、睦、医生、护士立绘定义
image taki = "images/characters/taki/taki_serious.png"
image taki serious = "images/characters/taki/taki_serious.png"
image taki concerned = "images/characters/taki/taki_concerned.png"
image taki angry = "images/characters/taki/taki_angry.png"
image taki frown = "images/characters/taki/taki_frown.png"
image taki sad = "images/characters/taki/taki_sad.png"
image taki surprised = "images/characters/taki/taki_surprised.png"
image taki soft_smile = "images/characters/taki/taki_soft_smile.png"
image taki flustered = "images/characters/taki/taki_flustered.png"

image side taki = "images/characters/side/side_taki_serious.png"
image side taki serious = "images/characters/side/side_taki_serious.png"
image side taki concerned = "images/characters/side/side_taki_concerned.png"
image side taki angry = "images/characters/side/side_taki_angry.png"
image side taki frown = "images/characters/side/side_taki_frown.png"
image side taki sad = "images/characters/side/side_taki_sad.png"
image side taki surprised = "images/characters/side/side_taki_surprised.png"
image side taki soft_smile = "images/characters/side/side_taki_soft_smile.png"
image side taki flustered = "images/characters/side/side_taki_flustered.png"

image mutsumi = "images/characters/mutsumi/mutsumi_expressionless.png"
image mutsumi expressionless = "images/characters/mutsumi/mutsumi_expressionless.png"

image doctor = Null()
image doctor calm = Null()

image nurse = Null()
image nurse gentle = Null()
image nurse_a = Null()
image nurse_b = Null()
image nurse_c = Null()

# 灯属性别名（支持常用剧本感情词）
image tomori hospital light_smile = "images/characters/tomori/tomori_hospital_smile.png"
image tomori hospital sad = "images/characters/tomori/tomori_hospital_tears.png"
image tomori hospital flustered = "images/characters/tomori/tomori_hospital_confused.png"
image tomori hospital crossed_fingers = "images/characters/tomori/tomori_hospital_fingers.png"

# 爱音属性别名
image anon hospital light_smile = "images/characters/anon/anon_hospital_smile.png"
image anon hospital annoyed = "images/characters/anon/anon_hospital_tears.png"
image anon hospital curious = "images/characters/anon/anon_hospital_flustered.png"
image anon hospital double_thumbs_up = "images/characters/anon/anon_hospital_up.png"
image anon hospital shushing = "images/characters/anon/anon_hospital_smirk.png"
image anon hospital crossed_fingers = "images/characters/anon/anon_pose_gyaru_peace.png"
image anon hospital determined = "images/characters/anon/anon_hospital_confident.png"
image anon hospital pensive = "images/characters/anon/anon_hospital_flustered.png"
image anon hospital gentle = "images/characters/anon/anon_hospital_smile.png"
image anon hospital serious = "images/characters/anon/anon_hospital_confident.png"
image anon hospital angry = "images/characters/anon/anon_hospital_flustered.png"
image anon hospital confused = "images/characters/anon/anon_hospital_flustered.png"

# Side Image 对应别名
image side tomori hospital light_smile = "images/characters/side/side_tomori_hospital_smile.png"
image side tomori hospital sad = "images/characters/side/side_tomori_hospital_tears.png"
image side tomori hospital flustered = "images/characters/side/side_tomori_hospital_confused.png"
image side tomori hospital crossed_fingers = "images/characters/side/side_tomori_pose_notebook.png"

image side anon hospital light_smile = "images/characters/side/side_anon_hospital_smile.png"
image side anon hospital annoyed = "images/characters/side/side_anon_hospital_sad.png"
image side anon hospital curious = "images/characters/side/side_anon_hospital_surprised.png"
image side anon hospital double_thumbs_up = "images/characters/side/side_anon_hospital_up.png"
image side anon hospital shushing = "images/characters/side/side_anon_hospital_smirk.png"
image side anon hospital crossed_fingers = "images/characters/side/side_anon_pose_gyaru_peace.png"
image side anon hospital determined = "images/characters/side/side_anon_hospital_confident.png"
image side anon hospital pensive = "images/characters/side/side_anon_hospital_shy.png"
image side anon hospital gentle = "images/characters/side/side_anon_hospital_smile.png"
image side anon hospital serious = "images/characters/side/side_anon_hospital_confident.png"
image side anon hospital angry = "images/characters/side/side_anon_hospital_flustered.png"
image side anon hospital confused = "images/characters/side/side_anon_hospital_surprised.png"

## 角色头像（Side Image / 6_Spirit）定义 ########################################
image side anon casual blush = "images/characters/side/side_anon_casual_blush.png"
image side anon casual confident = "images/characters/side/side_anon_casual_grin.png"
image side anon casual excited = "images/characters/side/side_anon_casual_excited.png"
image side anon casual grin = "images/characters/side/side_anon_casual_grin.png"
image side anon casual smirk = "images/characters/side/side_anon_casual_smirk.png"
image side anon coat confident = "images/characters/side/side_anon_casual_grin.png"
image side anon coat grin = "images/characters/side/side_anon_casual_grin.png"
image side anon coat smirk = "images/characters/side/side_anon_casual_smirk.png"
image side anon hospital blush = "images/characters/side/side_anon_hospital_blush.png"
image side anon hospital confident = "images/characters/side/side_anon_hospital_confident.png"
image side anon hospital embarrassed = "images/characters/side/side_anon_hospital_blush.png"
image side anon hospital excited = "images/characters/side/side_anon_casual_excited.png"
image side anon hospital flustered = "images/characters/side/side_anon_hospital_flustered.png"
image side anon hospital gun = "images/characters/side/side_anon_hospital_smug.png"
image side anon hospital happy = "images/characters/side/side_anon_hospital_happy.png"
image side anon hospital sad = "images/characters/side/side_anon_hospital_sad.png"
image side anon hospital shy = "images/characters/side/side_anon_hospital_shy.png"
image side anon hospital sign = "images/characters/side/side_anon_pose_gyaru_peace.png"
image side anon hospital smile = "images/characters/side/side_anon_hospital_smile.png"
image side anon hospital smirk = "images/characters/side/side_anon_hospital_smirk.png"
image side anon hospital smug = "images/characters/side/side_anon_hospital_smug.png"
image side anon hospital surprised = "images/characters/side/side_anon_hospital_surprised.png"
image side anon hospital tears = "images/characters/side/side_anon_hospital_tears.png"
image side anon hospital up = "images/characters/side/side_anon_hospital_up.png"
image side anon hospital v = "images/characters/side/side_anon_hospital_v.png"
image side anon hospital viewer = "images/characters/side/side_anon_hospital_smile.png"
image side anon hospital waving = "images/characters/side/side_anon_pose_pray.png"
image side sakiko annoyed annoyed = "images/characters/side/side_sakiko_annoyed_annoyed.png"
image side sakiko annoyed frustrated = "images/characters/side/side_sakiko_annoyed_frustrated.png"
image side sakiko annoyed sulking = "images/characters/side/side_sakiko_annoyed_sulking.png"
image side soyo annoyed annoyed = "images/characters/side/side_soyo_annoyed_annoyed.png"
image side tomori casual expressionless = "images/characters/side/side_tomori_default_expressionless.png"
image side tomori casual happy = "images/characters/side/side_tomori_default_happy.png"
image side tomori casual pensive = "images/characters/side/side_tomori_default_pensive.png"
image side tomori casual shy = "images/characters/side/side_tomori_default_shy.png"
image side tomori casual smile = "images/characters/side/side_tomori_default_smile.png"
image side tomori coat pensive = "images/characters/side/side_tomori_coat_pensive.png"
image side tomori coat serious = "images/characters/side/side_tomori_coat_serious.png"
image side tomori coat smile = "images/characters/side/side_tomori_coat_smile.png"
image side tomori hospital chin = "images/characters/side/side_tomori_hospital_pensive.png"
image side tomori hospital confused = "images/characters/side/side_tomori_hospital_confused.png"
image side tomori hospital determined = "images/characters/side/side_tomori_hospital_determined.png"
image side tomori hospital expressionless = "images/characters/side/side_tomori_hospital_expressionless.png"
image side tomori hospital fidgeting = "images/characters/side/side_tomori_hospital_confused.png"
image side tomori hospital fingers = "images/characters/side/side_tomori_pose_notebook.png"
image side tomori hospital hands = "images/characters/side/side_tomori_pose_notebook.png"
image side tomori hospital pensive = "images/characters/side/side_tomori_hospital_pensive.png"
image side tomori hospital serious = "images/characters/side/side_tomori_coat_serious.png"
image side tomori hospital shushing = "images/characters/side/side_tomori_meme_hide.png"
image side tomori hospital smile = "images/characters/side/side_tomori_hospital_smile.png"
image side tomori hospital surprised = "images/characters/side/side_tomori_hospital_surprised.png"
image side tomori hospital tears = "images/characters/side/side_tomori_hospital_tears.png"
image side tomori wedding shy = "images/characters/side/side_tomori_wedding_shy.png"
image side tomori wedding smile = "images/characters/side/side_tomori_wedding_smile.png"
image side tomori wedding tears = "images/characters/side/side_tomori_wedding_tears.png"

## 物品道具图像定义 ############################################################
image item bouquet = "images/items/item_bouquet.png"
image item glasses = "images/items/item_glasses.png"
image item guitar = "images/items/item_guitar.png"
image item guitar pick = "images/items/item_guitar_pick.png"
image item headphones = "images/items/item_headphones.png"
image item iv drip bag = "images/items/item_iv_drip_bag.png"
image item notebook = "images/items/item_notebook.png"
image item pills = "images/items/item_pills.png"
image item smartphone = "images/items/item_smartphone.png"
image item water glass = "images/items/item_water_glass.png"
image item penguin plush = Placeholder("item", text="企鹅玩偶")
image item konpeito jar = Placeholder("item", text="金平糖玻璃罐")
image item strawberry sandwich = Placeholder("item", text="草莓奶油三明治")
image item anon diary = Placeholder("item", text="爱音的粉色日记本")
image item wedding dress = Placeholder("item", text="二手白色婚纱")
image item wedding veil = Placeholder("item", text="蕾丝头纱")
image item bandaid = Placeholder("item", text="创口贴")

## 新增服装立绘别名（风衣、居家服、婚纱、便服）############################
# 千早爱音 - 便服/常服别名映射 (多套常服与风衣过渡支持)
image anon casual smile = "images/characters/anon/anon_casual_smile.png"
image anon casual happy = "images/characters/anon/anon_casual_happy.png"
image anon casual grin = "images/characters/anon/anon_casual_grin.png"
image anon casual smirk = "images/characters/anon/anon_casual_smirk.png"
image anon casual blush = "images/characters/anon/anon_casual_blush.png"
image anon casual excited = "images/characters/anon/anon_casual_excited.png"
image anon casual pout = "images/characters/anon/anon_casual_pout.png"
image anon casual pensive = "images/characters/anon/anon_casual_blush.png"
image anon casual shy = "images/characters/anon/anon_casual_blush.png"
image anon casual wink = "images/characters/anon/anon_pose_gyaru_peace.png"

image anon windbreaker smile = "images/characters/anon/anon_casual_smile.png"
image anon windbreaker confident = "images/characters/anon/anon_casual_grin.png"
image anon windbreaker smirk = "images/characters/anon/anon_casual_smirk.png"
image anon windbreaker grin = "images/characters/anon/anon_casual_grin.png"
image anon windbreaker excited = "images/characters/anon/anon_casual_excited.png"
image anon windbreaker worried = "images/characters/anon/anon_hospital_tears.png"
image anon windbreaker tears = "images/characters/anon/anon_hospital_tears.png"
image anon windbreaker blush = "images/characters/anon/anon_casual_blush.png"
image anon windbreaker gentle = "images/characters/anon/anon_casual_smile.png"
image anon windbreaker serious = "images/characters/anon/anon_casual_smirk.png"
image anon windbreaker surprised = "images/characters/anon/anon_hospital_flustered.png"
image anon windbreaker confused = "images/characters/anon/anon_hospital_flustered.png"
image anon windbreaker pensive = "images/characters/anon/anon_casual_blush.png"
image anon windbreaker pout = "images/characters/anon/anon_casual_pout.png"
image anon windbreaker normal = "images/characters/anon/anon_casual_smile.png"

# 千早爱音 - 居家服 (loungewear)
image anon loungewear smile = "images/characters/anon/anon_casual_grin.png"
image anon loungewear gentle = "images/characters/anon/anon_casual_smirk.png"
image anon loungewear smirk = "images/characters/anon/anon_casual_smirk.png"
image anon loungewear blush = "images/characters/anon/anon_casual_blush.png"
image anon loungewear excited = "images/characters/anon/anon_casual_excited.png"
image anon loungewear tears = "images/characters/anon/anon_hospital_tears.png"

# 千早爱音 - 婚纱 (NovelAI V5 超清)
image anon wedding smile = "images/characters/anon/anon_wedding_smile.png"
image anon wedding blush = "images/characters/anon/anon_wedding_blush.png"
image anon wedding happy = "images/characters/anon/anon_wedding_happy.png"
image anon wedding tears = "images/characters/anon/anon_wedding_tears.png"
image anon wedding gentle = "images/characters/anon/anon_wedding_smile.png"

# 高松灯 - 大号风衣 (windbreaker)
image tomori windbreaker expressionless = "images/characters/tomori/tomori_coat_serious.png"
image tomori windbreaker smile = "images/characters/tomori/tomori_coat_smile.png"
image tomori windbreaker confused = "images/characters/tomori/tomori_hospital_confused.png"
image tomori windbreaker sad = "images/characters/tomori/tomori_coat_pensive.png"
image tomori windbreaker pensive = "images/characters/tomori/tomori_coat_pensive.png"
image tomori windbreaker tears = "images/characters/tomori/tomori_hospital_tears.png"

# 椎名立希 - 便服/Livehouse员工服 (casual)
image taki casual serious = "images/characters/taki/taki_serious.png"
image taki casual concerned = "images/characters/taki/taki_concerned.png"
image taki casual angry = "images/characters/taki/taki_angry.png"
image taki casual frown = "images/characters/taki/taki_frown.png"
image taki casual sad = "images/characters/taki/taki_sad.png"
image taki casual surprised = "images/characters/taki/taki_surprised.png"
image taki casual soft_smile = "images/characters/taki/taki_soft_smile.png"
image taki casual flustered = "images/characters/taki/taki_flustered.png"
image taki casual tears = "images/characters/taki/taki_sad.png"

image side taki casual serious = "images/characters/side/side_taki_serious.png"
image side taki casual concerned = "images/characters/side/side_taki_concerned.png"
image side taki casual angry = "images/characters/side/side_taki_angry.png"
image side taki casual frown = "images/characters/side/side_taki_frown.png"
image side taki casual sad = "images/characters/side/side_taki_sad.png"
image side taki casual surprised = "images/characters/side/side_taki_surprised.png"
image side taki casual soft_smile = "images/characters/side/side_taki_soft_smile.png"
image side taki casual flustered = "images/characters/side/side_taki_flustered.png"
image side taki casual tears = "images/characters/side/side_taki_sad.png"

## 事件 CG 定义 (2432x1664 高清重置) ############################################
image cg 01 = "images/cg/cg_01.png"
image cg 02 = "images/cg/cg_02.png"
image cg 03 = "images/cg/cg_03.png"
image cg 04 = "images/cg/cg_04.png"
image cg 05 = "images/cg/cg_05.png"
image cg 06 = "images/cg/cg_06.png"
image cg 07 = "images/cg/cg_07.png"
image cg 08 = "images/cg/cg_08.png"
image cg 09 = "images/cg/cg_09.png"
image cg 10 = "images/cg/cg_10.png"
image cg 11 = "images/cg/cg_11.png"
image cg 12 = "images/cg/cg_12.png"
image cg 13 = "images/cg/cg_13.png"
image cg 14 = "images/cg/cg_14.png"
image cg 15 = "images/cg/cg_15.png"
image cg 16 = "images/cg/cg_16.png"
image cg 17 = "images/cg/cg_17.png"
image cg 18 = "images/cg/cg_18.png"
image cg 20 = "images/cg/cg_20.png"
image cg 21 = "images/cg/cg_21.png"
image cg 24 = "images/cg/cg_24.png"
image cg 25 = "images/cg/cg_25.png"
image cg 26 = "images/cg/cg_26.png"
image cg 27 = "images/cg/cg_27.png"

# 常用事件 CG 别名
image cg awakening = "images/cg/cg_02.png"
image cg guitar = "images/cg/cg_03.png"
image cg escape = "images/cg/cg_05.png"
image cg stars = "images/cg/cg_04.png"
image cg wedding = "images/cg/cg_10.png"

# 新增高潮特写 CG (POV Cut-ins 2432x1664 超清)
image cg closeup rooftop = "images/cg/cg_closeup_rooftop.png"
image cg closeup bus = "images/cg/cg_closeup_bus.png"
image cg closeup arcade = "images/cg/cg_closeup_arcade.png"
image cg closeup bedroom = "images/cg/cg_closeup_bedroom.png"
image cg closeup bridge = "images/cg/cg_closeup_bridge.png"
image cg closeup reverse_rain = "images/cg/cg_closeup_reverse_rain.png"
image cg holding_hands = "images/cg/cg_creative_holding_hands.png"
image cg starry_sky = "images/cg/cg_creative_starry_sky.png"

# 演出特殊眼睛与动态姿态立绘 (NovelAI V5 专享)
image anon meme sparkle = "images/characters/anon/anon_meme_sparkle.png"
image anon meme spiral = "images/characters/anon/anon_meme_spiral.png"
image anon meme heart = "images/characters/anon/anon_meme_heart.png"
image anon meme puppy = "images/characters/anon/anon_meme_cat.png"
image anon meme dot = "images/characters/anon/anon_meme_dot.png"
image anon meme cat = "images/characters/anon/anon_meme_cat.png"
image anon meme pout = "images/characters/anon/anon_meme_pout.png"
image anon pose gyaru_peace = "images/characters/anon/anon_pose_gyaru_peace.png"
image anon pose hands_hips = "images/characters/anon/anon_pose_hands_hips.png"
image anon pose peek = "images/characters/anon/anon_pose_peek.png"
image anon pose pray = "images/characters/anon/anon_pose_pray.png"

image tomori meme sparkle = "images/characters/tomori/tomori_meme_sparkle.png"
image tomori pose notebook = "images/characters/tomori/tomori_hospital_hands.png"
image tomori pose reach = "images/characters/tomori/tomori_hospital_determined.png"
image tomori meme hide = "images/characters/tomori/tomori_meme_hide.png"

image taki pose drumstick = "images/characters/taki/taki_serious.png"
image taki pose coffee_tray = "images/characters/taki/taki_waitress_serious.png"
image taki meme irked = "images/characters/taki/taki_meme_irked.png"

# 对应头像 (Side Image) 定义
image side anon meme sparkle = "images/characters/side/side_anon_meme_sparkle.png"
image side anon meme spiral = "images/characters/side/side_anon_meme_spiral.png"
image side anon meme heart = "images/characters/side/side_anon_meme_heart.png"
image side anon meme puppy = "images/characters/side/side_anon_meme_puppy.png"
image side anon meme dot = "images/characters/side/side_anon_meme_dot.png"
image side anon meme cat = "images/characters/side/side_anon_meme_cat.png"
image side anon meme pout = "images/characters/side/side_anon_meme_pout.png"
image side anon pose gyaru_peace = "images/characters/side/side_anon_pose_gyaru_peace.png"
image side anon pose hands_hips = "images/characters/side/side_anon_pose_hands_hips.png"
image side anon pose peek = "images/characters/side/side_anon_pose_peek.png"
image side anon pose pray = "images/characters/side/side_anon_pose_pray.png"

image side tomori meme sparkle = "images/characters/side/side_tomori_meme_sparkle.png"
image side tomori pose notebook = "images/characters/side/side_tomori_pose_notebook.png"
image side tomori pose reach = "images/characters/side/side_tomori_pose_reach.png"
image side tomori meme hide = "images/characters/side/side_tomori_meme_hide.png"

image side taki pose drumstick = "images/characters/side/side_taki_pose_drumstick.png"
image side taki pose coffee_tray = "images/characters/side/side_taki_waitress_serious.png"
image side taki meme irked = "images/characters/side/side_taki_meme_irked.png"

# 高松灯丰富侧边头像与默认服饰 (Side Image & Default Attire)
image side tomori hospital sad = "images/characters/side/side_tomori_hospital_sad.png"
image side tomori hospital nervous = "images/characters/side/side_tomori_hospital_nervous.png"
image side tomori hospital shy = "images/characters/side/side_tomori_hospital_shy.png"
image side tomori hospital relieved = "images/characters/side/side_tomori_hospital_relieved.png"

image tomori default expressionless = "images/characters/tomori/tomori_default_expressionless.png"
image tomori default smile = "images/characters/tomori/tomori_default_smile.png"
image tomori default pensive = "images/characters/tomori/tomori_default_pensive.png"
image tomori default tears = "images/characters/tomori/tomori_default_tears.png"
image tomori default determined = "images/characters/tomori/tomori_default_determined.png"
image tomori default shy = "images/characters/tomori/tomori_default_shy.png"
image tomori default surprised = "images/characters/tomori/tomori_default_surprised.png"

image side tomori default expressionless = "images/characters/side/side_tomori_default_expressionless.png"
image side tomori default smile = "images/characters/side/side_tomori_default_smile.png"
image side tomori default pensive = "images/characters/side/side_tomori_default_pensive.png"
image side tomori default tears = "images/characters/side/side_tomori_default_tears.png"
image side tomori default determined = "images/characters/side/side_tomori_default_determined.png"
image side tomori default shy = "images/characters/side/side_tomori_default_shy.png"
image side tomori default surprised = "images/characters/side/side_tomori_default_surprised.png"
image side tomori default relieved = "images/characters/side/side_tomori_default_smile.png"

# 10 个代表性特写镜头 (bang dream! it's mygo!!!!! 风格，透明背景，2K采样)
image cg shot01 = "images/cg/cg_shot01_anon_hospital_awakening.png"
image cg shot02 = "images/cg/cg_closeup_anon_hosp_smug.png"
image cg shot03 = "images/cg/cg_closeup_anon_hosp_smile.png"
image cg shot04 = "images/cg/cg_closeup_rooftop.png"
image cg shot05 = "images/cg/cg_shot05_anon_bus_dawn.png"
image cg shot06 = "images/cg/cg_shot06_anon_arcade_penguin.png"
image cg shot07 = "images/cg/cg_shot07_anon_bedroom_tears.png"
image cg shot08 = "images/cg/cg_shot08_anon_bridge_kiss.png"
image cg shot09 = "images/cg/cg_shot09_anon_wedding_beach.png"
image cg shot10 = "images/cg/cg_closeup_reverse_rain.png"

# 若叶睦与长崎素世 (NovelAI V5 超清更新)
image mutsumi sad = "images/characters/mutsumi/mutsumi_expressionless.png"
image side mutsumi sad = "images/characters/side/side_mutsumi_sad.png"

# 特写表情矩阵 (NovelAI V5 Emotion Tool 特写)
image cg closeup anon hosp neutral = "images/cg/cg_closeup_anon_hosp_neutral.png"
image cg closeup anon hosp smile = "images/cg/cg_closeup_anon_hosp_smile.png"
image cg closeup anon hosp smug = "images/cg/cg_closeup_anon_hosp_smug.png"
image cg closeup anon hosp shy = "images/cg/cg_closeup_anon_hosp_smile.png"
image cg closeup anon hosp tears = "images/cg/cg_closeup_anon_hosp_tears.png"
image cg closeup anon hosp determined = "images/cg/cg_closeup_anon_hosp_smug.png"

image cg closeup anon def neutral = "images/cg/cg_closeup_anon_def_neutral.png"
image cg closeup anon def happy = "images/cg/cg_closeup_anon_def_happy.png"
image cg closeup anon def tears = "images/cg/cg_closeup_anon_def_tears.png"
image cg closeup anon def love = "images/cg/cg_closeup_anon_def_love.png"
image cg closeup anon def surprised = "images/cg/cg_closeup_anon_def_surprised.png"
image cg closeup anon def pout = "images/cg/cg_closeup_anon_def_pout.png"

image cg closeup anon wedding neutral = "images/cg/cg_closeup_anon_wedding_neutral.png"
image cg closeup anon wedding smile = "images/cg/cg_closeup_anon_wedding_smile.png"
image cg closeup anon wedding happy = "images/cg/cg_closeup_anon_wedding_happy.png"
image cg closeup anon wedding shy = "images/cg/cg_closeup_anon_wedding_shy.png"
image cg closeup anon wedding tears = "images/cg/cg_closeup_anon_wedding_tears.png"
image cg closeup anon wedding love = "images/cg/cg_closeup_anon_wedding_love.png"
image cg closeup anon wedding surprised = "images/cg/cg_closeup_anon_wedding_surprised.png"
image cg closeup anon wedding determined = "images/cg/cg_closeup_anon_wedding_determined.png"
image cg closeup anon wedding pout = "images/cg/cg_closeup_anon_wedding_pout.png"

image cg closeup tomori def neutral = "images/cg/cg_closeup_tomori_def_neutral.png"
image cg closeup tomori def smile = "images/cg/cg_closeup_tomori_def_smile.png"
image cg closeup tomori def pensive = "images/cg/cg_closeup_tomori_def_pensive.png"
image cg closeup tomori def tears = "images/cg/cg_closeup_tomori_def_tears.png"
image cg closeup tomori def determined = "images/cg/cg_closeup_tomori_def_pensive.png"
image cg closeup tomori def shy = "images/cg/cg_closeup_tomori_def_smile.png"

image cg closeup tomori wedding neutral = "images/cg/cg_closeup_tomori_wedding_neutral.png"
image cg closeup tomori wedding smile = "images/cg/cg_closeup_tomori_wedding_smile.png"
image cg closeup tomori wedding shy = "images/cg/cg_closeup_tomori_wedding_smile.png"
image cg closeup tomori wedding tears = "images/cg/cg_closeup_reverse_rain.png"






## ==============================================================================
## 《二手时间》标准视觉规范声明（依据规范文件.md 与 图片.rtf）
## ==============================================================================

## 1. 千早爱音（Anon）病房立绘差分
image anon hosp 01 smug = "images/characters/anon/anon_hosp_01_smug.png"
image anon hosp 02 boast = "images/characters/anon/anon_hosp_02_boast.png"
image anon hosp 03 curious_1 = "images/characters/anon/anon_hosp_03_curious_1.png"
image anon hosp 03 curious_2 = "images/characters/anon/anon_hosp_03_curious_2.png"
image anon hosp 03 curious_3 = "images/characters/anon/anon_hosp_03_curious_3.png"
image anon hosp 04 shy_1 = "images/characters/anon/anon_hosp_04_shy_1.png"
image anon hosp 04 shy_2 = "images/characters/anon/anon_hosp_04_shy_2.png"
image anon hosp 05 annoyed_1 = "images/characters/anon/anon_hosp_05_annoyed_1.png"
image anon hosp 05 annoyed_2 = "images/characters/anon/anon_hosp_05_annoyed_2.png"
image anon hosp 06 pain = "images/characters/anon/anon_hosp_06_pain.png"
image anon hosp 07 normal_1 = "images/characters/anon/anon_hosp_07_normal_1.png"
image anon hosp 07 normal_2 = "images/characters/anon/anon_hosp_07_normal_2.png"
image anon hosp 07 normal_3 = "images/characters/anon/anon_hosp_07_normal_3.png"
image anon hosp 08 gentle = "images/characters/anon/anon_hosp_08_gentle.png"
image anon hosp 09 confess = "images/characters/anon/anon_hosp_09_confess.png"
image anon hosp 10 tears = "images/characters/anon/anon_hosp_10_tears.png"

## 2. 椎名立希（Taki）立绘差分
image taki 01 glare = "images/characters/taki/taki_01_glare.png"
image taki 02 normal_1 = "images/characters/taki/taki_02_normal_1.png"
image taki 02 normal_2 = "images/characters/taki/taki_02_normal_2.png"
image taki 03 sad = "images/characters/taki/taki_03_sad.png"

## 3. 长崎素世（Soyo）立绘差分
image soyo 01 smile = "images/characters/soyo/soyo_01_smile.png"
image soyo 01 normal = "images/characters/soyo/soyo_01_normal.png"

## 4. 高松灯（Tomori）主视角 Side Image 头像差分（18 组情绪）
image side tomori ah = "images/characters/side/Side ah.png"
image side tomori an2 = "images/characters/side/Side an2.png"
image side tomori babble = "images/characters/side/Side babble.png"
image side tomori bitter = "images/characters/side/Side bitter.png"
image side tomori calm = "images/characters/side/Side calm.png"
image side tomori concern = "images/characters/side/Side concern.png"
image side tomori ehh = "images/characters/side/Side ehh.png"
image side tomori happy = "images/characters/side/Side happy.png"
image side tomori kya = "images/characters/side/Side kya.png"
image side tomori neutral = "images/characters/side/Side neutral.png"
image side tomori pout = "images/characters/side/Side pout.png"
image side tomori sad = "images/characters/side/Side sad.png"
image side tomori sadaway = "images/characters/side/Side sadaway.png"
image side tomori smile = "images/characters/side/Side smile.png"
image side tomori soft = "images/characters/side/Side soft.png"
image side tomori uff = "images/characters/side/Side uff.png"
image side tomori yay = "images/characters/side/Side yay.png"
image side tomori wtf = "images/characters/side/Side wtf.png"

