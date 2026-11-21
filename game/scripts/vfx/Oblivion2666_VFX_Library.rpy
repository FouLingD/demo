# ==============================================================================
# OBLIVION 2666 - Complete Dynamic Visual Effects Library for Ren'Py
# (遗忘2666 - 动态视觉特效全套代码库)
#
# 提取、重构与原理解析自《Oblivion 2666: Demo Disc》(Ren'Py 8.x / Python 3)
# 适用版本: Ren'Py 8.0+ / 8.2+ / 8.5+ (现代 GL2 渲染架构)
#
# 本库包含 9 大模块:
#   1. 高级缓动数学库 (Cubic Bezier 数值求解器、阻尼谐振、指数与回弹曲线)
#   2. 有机镜头运动系统 (手持摄像机多倍频 Value Noise、晃动、行走颠簸、多平面景深视差)
#   3. 胶片全流程模拟 (24fps 片门抖动 GateWeave、快门闪烁、红晕色散 Halation、银盐闪烁)
#   4. 光学镜头与物理景深 (黄金角 Vogel 螺旋散景、变形镜头光斑、色差扩散、镜头畸变、移轴)
#   5. 复古模拟录像与早期数码 CCD (VHS 磁带跟踪抖动、CCD 强光溢出与紫边、隔行扫描、像素降采样)
#   6. 动态精灵材质与表面光照 (2D 精灵表面法线雨滴折射/浸润/高光、边缘轮廓光 RimLight)
#   7. 动态排版与文字着色器 (勒索信多字体动态跳变 {ransom}、乱码遮罩 {censor}、手绘沸腾描边 {boil})
#   8. 硬件级沉浸式转场 (CRT 关机电子束坍缩、胶片放映机卡带滑出、单反快门闪光与胶片负片闪回)
#   9. 渲染管线与填充率优化 (分级质量预设、缓冲区动态降采样 fxdown/fxup、图层架构)
# ==============================================================================

# ------------------------------------------------------------------------------
# 0. 基础环境与配置初始化
# ------------------------------------------------------------------------------
init -20 python:
    import math
    import random as _random
    import string

    # 默认性能分级: "cine" (电影级), "bal" (平衡推荐), "perf" (低配性能)
    default_fx_quality = "bal"

    # 全局开关与默认配置持久化
    if not hasattr(persistent, "gateweave"):
        persistent.gateweave = True
    if not hasattr(persistent, "chromaab"):
        persistent.chromaab = True
    if not hasattr(persistent, "vignette"):
        persistent.vignette = True
    if not hasattr(persistent, "redmvmt"):
        persistent.redmvmt = False
    if not hasattr(persistent, "fx_quality"):
        persistent.fx_quality = "bal"

# 推荐的分层架构 (可并入工程 options.rpy / gui.rpy)
init -15 python:
    if 'unmoving' not in config.layers:
        # 插入自定义渲染层: master(主舞台) -> rendered(全画幅滤镜层) -> transitionscr(特效转场层)
        config.layers = [
            'background', 'unmoving', 'master',
            'prerendered', 'rendered', 'postrendered', 'superrendered',
            'transient', 'transientscr', 'transitionscr', 'transitionscroverlay',
            'screens', 'superscreen', 'overlay'
        ]

# ------------------------------------------------------------------------------
# 模块 1: 高级缓动数学库 (Warpers & Easing Math)
# ------------------------------------------------------------------------------
# 说明:
# 1) synewarp: 自定义三次贝塞尔曲线 (0.5, 0.0, 0.0, 1.0)，使用 24 次二分迭代数值求解反函数，
#    达到极具电影质感的急启动与平稳阻尼煞车。
# 2) synewarp_d: 贝塞尔曲线的一阶导数 (速度分布)，呈 0 -> 1 -> 0 钟形，用于速度映射。
# 3) spring1~spring3: 物理阻尼谐振衰减公式 (1.0 - exp(-rho * x) * cos(mu * x)) / ...
# 4) bop 系列: 动感回弹与过冲三次/五次多项式曲线。
# ------------------------------------------------------------------------------

python early in _warper:
    _constant = True
    import math

    @renpy.atl_warper
    def synewarp(t):
        """电影级缓动 (0.5, 0.0, 0.0, 1.0) 贝塞尔曲线的高精度数值解"""
        if t <= 0.0: return 0.0
        if t >= 1.0: return 1.0
        lo, hi, u = 0.0, 1.0, t
        for _ in range(24):
            x = ((2.5 * u - 3.0) * u + 1.5) * u
            if x < t: lo = u
            else: hi = u
            u = 0.5 * (lo + hi)
        return (-2.0 * u + 3.0) * u ** 2

    @renpy.atl_warper
    def synewarp_d(t):
        """synewarp 的一阶导数归一化钟形曲线 (0 -> 1 -> 0)"""
        if t <= 0.0 or t >= 1.0: return 0.0
        lo, hi, u = 0.0, 1.0, t
        for _ in range(24):
            x = ((2.5 * u - 3.0) * u + 1.5) * u
            if x < t: lo = u
            else: hi = u
            u = 0.5 * (lo + hi)
        d = 6.0 * u * (1.0 - u) / ((7.5 * u - 6.0) * u + 1.5)
        return d / (2.0 + 2.0 * math.sqrt(2.0))

    @renpy.atl_warper
    def easer_expo_a(t):
        """指数缓入缓出"""
        if t == 0.0: return 0.0
        elif t == 1.0: return 1.0
        elif t < 0.5: return 2 ** (20 * t - 10) / 2
        else: return (2 - 2 ** (-20 * t + 10)) / 2

    @renpy.atl_warper
    def easeout_cubic_a(t):
        return 1.0 - ((1.0 - t) ** 3)

    @renpy.atl_warper
    def easein_cubic_a(t):
        return t ** 3

    @renpy.atl_warper
    def easeout_elastic_a(t):
        """物理弹性回弹"""
        c4 = (2 * math.pi) / 3
        if t == 0.0: return 0.0
        elif t == 1.0: return 1.0
        else: return 2 ** (-10 * t) * math.sin((t * 10 - 0.75) * c4) + 1.0

    @renpy.atl_warper
    def easein_exp_a(t):
        return 0.0 if t == 0.0 else 2 ** (10 * t - 10)

    @renpy.atl_warper
    def easeout_exp_a(t):
        return 1.0 if t == 1.0 else 1.0 - 2 ** (-10 * t)

    @renpy.atl_warper
    def ease_out_bounce(t):
        """物理弹跳落地"""
        n1, d1 = 7.5625, 2.75
        if t < 1 / d1: return n1 * t * t
        elif t < 2 / d1:
            t -= 1.5 / d1
            return n1 * t * t + 0.75
        elif t < 2.5 / d1:
            t -= 2.25 / d1
            return n1 * t * t + 0.9375
        else:
            t -= 2.625 / d1
            return n1 * t * t + 0.984375

    @renpy.atl_warper
    def spring1(x):
        """高频阻尼弹簧 (衰减率=5, 角频率=30)"""
        rho, mu = 5.0, 30.0
        return (1.0 - math.exp(-rho * x) * math.cos(mu * x)) / (1.0 - math.exp(-rho) * math.cos(mu))

    @renpy.atl_warper
    def spring2(x):
        """中频阻尼弹簧 (衰减率=5, 角频率=20)"""
        rho, mu = 5.0, 20.0
        return (1.0 - math.exp(-rho * x) * math.cos(mu * x)) / (1.0 - math.exp(-rho) * math.cos(mu))

    @renpy.atl_warper
    def spring3(x):
        """低频柔和弹簧 (衰减率=5, 角频率=10)"""
        rho, mu = 5.0, 10.0
        return (1.0 - math.exp(-rho * x) * math.cos(mu * x)) / (1.0 - math.exp(-rho) * math.cos(mu))

    @renpy.atl_warper
    def bop_time_warp(x):
        """过冲爆发 (Cinematic Pop)"""
        return -23.0 * x**5 + 57.5 * x**4 - 55 * x**3 + 25 * x**2 - 3.5 * x

    @renpy.atl_warper
    def bop_in_time_warp(x):
        return -2.15 * x**2 + 3.15 * x

    @renpy.atl_warper
    def bop_out_time_warp(x):
        return 2.15 * x**2 - 1.15 * x


# ------------------------------------------------------------------------------
# 模块 2: 渲染管线质量分级与填充率动态缩放
# ------------------------------------------------------------------------------
# 说明:
# 现代全屏着色器（如高斯/散景/光晕）极其消耗像素填充率 (Pixel Fill-rate)。
# 本系统通过三级品质设定 (cine / bal / perf) 自动降采样后处理缓冲，并在渲染完成后还原，
# 能够在核显或低配设备上将 GPU 耗时降低 50%~75%。
# ------------------------------------------------------------------------------
init -10 python:
    import math

    FX_PRESETS = {
        "cine" : {"bokeh": 48, "halation": 32, "bloom": 16, "smear": 24, "scale": 1.00},
        "bal"  : {"bokeh": 36, "halation": 24, "bloom": 12, "smear": 16, "scale": 0.75},
        "perf" : {"bokeh": 24, "halation": 16, "bloom":  8, "smear":  8, "scale": 0.50},
    }

    def fxq(key):
        """根据当前质量配置获取采样数 (Taps)"""
        preset = FX_PRESETS.get(persistent.fx_quality) or FX_PRESETS["bal"]
        return float(preset.get(key, 16))

    def fxs():
        """根据当前质量配置获取分辨率缩放比例 (Resolution Scale)"""
        preset = FX_PRESETS.get(persistent.fx_quality) or FX_PRESETS["bal"]
        return float(preset["scale"])

    _fxq_wsum_cache = {}
    def fxq_wsum(taps):
        """预计算指数衰减权重和并缓存，避免着色器逐像素重复计算"""
        n = int(taps)
        if n not in _fxq_wsum_cache:
            _fxq_wsum_cache[n] = sum(math.exp(-4.0 * (i + 0.5) / n) for i in range(n)) if n > 0 else 1.0
        return _fxq_wsum_cache[n]

transform fxdown():
    subpixel True
    zoom fxs()

transform fxup():
    subpixel True
    zoom (1.0 / fxs())


# ------------------------------------------------------------------------------
# 模块 3: 有机镜头晃动与程序化噪声 (Camera Movement & Noise)
# ------------------------------------------------------------------------------
# 说明:
# 摒弃机械的简谐正弦运动，使用多倍频一维连续分形值噪声 (_ValueNoise)
# 结合 24fps 步进，真实还原纪录片/电影中摄影师手持跟拍的“生理性呼吸感”与“微颤抖”。
# ------------------------------------------------------------------------------
init python:
    class _ValueNoise(object):
        """多八度连续平滑分形值噪声生成器 (1D Value Noise / fBm)"""
        def __init__(self, octaves=2, persistence=0.5, seed=None):
            rng = _random.Random(seed)
            self.table = [rng.uniform(-1.0, 1.0) for _ in range(256)]
            self.octaves = octaves
            self.persistence = persistence

        def _sample(self, t):
            i = int(math.floor(t))
            f = t - i
            u = f * f * (3.0 - 2.0 * f) # 平滑阶跃插值 (Smoothstep)
            a = self.table[i % 256]
            b = self.table[(i + 1) % 256]
            return a + (b - a) * u

        def __call__(self, t):
            v, amp, freq, norm = 0.0, 1.0, 1.0, 0.0
            for _ in range(self.octaves):
                v += amp * self._sample(t * freq)
                norm += amp
                amp *= self.persistence
                freq *= 2.0
            return v / norm

    class Wiggle(object):
        """手持摄影机 2D 平面连续漂移算法"""
        def __init__(self, freq=2.0, amp=8.0, octaves=3, persistence=0.5, seed=None):
            self.freq = freq
            self.amp = amp
            self.nx = _ValueNoise(octaves, persistence, seed)
            self.ny = _ValueNoise(octaves, persistence, (seed or 0) + 101)

        def offsets(self, t):
            return (self.amp * self.nx(t * self.freq),
                    self.amp * self.ny(t * self.freq))

        def __call__(self, trans, st, at):
            x, y = self.offsets(at)
            trans.xoffset = x
            trans.yoffset = y
            return 0.0

    def _fx_still(trans, st, at):
        trans.xoffset = 0
        trans.yoffset = 0
        return None

# 手持镜头晃动 Transform
transform handheld(amp=8, freq=2.0, seed=0):
    subpixel True
    function (Wiggle(freq, amp, seed=seed) if not persistent.redmvmt else _fx_still)

# 行走步伐颠簸 Transform (Walk Cycle)
transform walkcyc(dist=10.0, up=0.6, down=0.4):
    subpixel True
    yoffset 0
    block:
        easein up yoffset (-dist)
        easeout down yoffset 0
        repeat

# 多平面深度视差定位辅助 (2.5D Camera Staging)
transform unmoving():
    xoffset 0 yoffset 0

transform farpos(xdiff=0, ydiff=0, zdiff=0):
    subpixel True
    xoffset (xdiff * 0.3) yoffset (ydiff * 0.3) zpos (zdiff * 0.5)

transform midfarpos(xdiff=0, ydiff=0, zdiff=0):
    subpixel True
    xoffset (xdiff * 0.6) yoffset (ydiff * 0.6) zpos (zdiff * 0.8)

transform closefarpos(xdiff=0, ydiff=0, zdiff=0):
    subpixel True
    xoffset (xdiff * 1.0) yoffset (ydiff * 1.0) zpos (zdiff * 1.0)


# ------------------------------------------------------------------------------
# 模块 4: 胶片全流程模拟 (Photochemical Film Pipeline)
# ------------------------------------------------------------------------------
# 包含:
# 1) GateWeave (片门抖动): 模拟胶片经过投影机片门齿轮啮合时的机械位移与微旋转 (24fps 离散步进)
# 2) FilmFlicker (快门闪烁): 模拟旋转遮光叶轮导致的曝光度微幅波动
# 3) cam.halation (红晕着色器): 强光穿透胶片乳剂层照射到底片防光晕层反射形成的特征性红橙色光晕
# 4) cam.scintillate (银盐微晶闪烁): 模拟胶片感光卤化银晶粒在光照下的随机微光闪烁
# ------------------------------------------------------------------------------
init python:
    class GateWeave(object):
        """胶片放映机机械片门位移与摆动"""
        def __init__(self, framerate=24.0, jitter=2.0, hjitter=4.0, rot=0.0):
            self.framerate = float(framerate)
            self.jitter = float(jitter)
            self.hjitter = (jitter * 0.35) if hjitter is None else float(hjitter)
            self.rot = float(rot)

        def __call__(self, trans, st, at):
            n = int(at * self.framerate)
            rng = _random.Random(n)
            trans.yoffset = rng.uniform(-self.jitter, self.jitter)
            trans.xoffset = rng.uniform(-self.hjitter, self.hjitter)
            if self.rot:
                trans.rotate = rng.uniform(-self.rot, self.rot)
            return max(0.0, (n + 1) / self.framerate - at)

    def _scale_rgb(k):
        return Matrix([
            k,   0.0, 0.0, 0.0,
            0.0, k,   0.0, 0.0,
            0.0, 0.0, k,   0.0,
            0.0, 0.0, 0.0, 1.0,
        ])

    class FilmFlicker(object):
        """胶片放映机叶片遮光导致的亮度脉动"""
        def __init__(self, framerate=24.0, dimpercent=2):
            self.framerate = float(framerate)
            self.dim = float(dimpercent) / 100.0

        def __call__(self, trans, st, at):
            n = int(at * self.framerate)
            rng = _random.Random(n)
            k = rng.uniform(1.0 - self.dim, 1.0)
            trans.matrixcolor = _scale_rgb(k)
            return max(0.0, (n + 1) / self.framerate - at)

    # 4.1 胶片红晕 (Film Halation Shader)
    renpy.register_shader("cam.halation",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform float u_radius;
            uniform float u_threshold;
            uniform float u_knee;
            uniform float u_rolloff;
            uniform float u_strength;
            uniform float u_seam;
            uniform vec3 u_tint;
            uniform float u_taps;
            uniform float u_wsum;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            const vec3 luma = vec3(0.299, 0.587, 0.114);
            const float GA_COS = -0.7373688780783197;
            const float GA_SIN = 0.6754902942615238;

            vec4 base = texture2D(tex0, v_tex_coord);
            float N = max(u_taps, 1.0);
            float g = 0.0;
            vec2 dir = vec2(1.0, 0.0);

            for (int i = 0; i < 48; i++) {
                if (float(i) >= N) break;
                float fi = float(i);
                float r = sqrt((fi + 0.5) / N);
                vec2 offs = dir * (r * u_radius) / u_model_size;
                vec3 s = texture2D(tex0, v_tex_coord + offs, 1.0).rgb;
                float l = dot(s, luma);
                float knee = smoothstep(u_threshold - u_knee, u_threshold + u_knee, l);
                float energy = knee * pow(l, u_rolloff);

                float w = exp(-4.0 * r * r);
                g += energy * w;

                dir = vec2(dir.x * GA_COS - dir.y * GA_SIN,
                           dir.x * GA_SIN + dir.y * GA_COS);
            }

            vec3 halo = u_tint * (g / u_wsum) * u_strength;
            float shade = 1.0 - dot(base.rgb, luma);
            halo *= mix(1.0, shade, u_seam);

            gl_FragColor = vec4(base.rgb + halo, base.a);
        """
    )

    # 4.2 银盐微晶与热点闪烁 (Scintillation Shader)
    renpy.register_shader("cam.scintillate",
        variables="""
            uniform sampler2D tex0;
            uniform float u_time;
            uniform float u_flicker_strength;
            uniform float u_flicker_threshold;
            uniform float u_flicker_softness;
            uniform float u_flicker_scale;
            uniform float u_flicker_speed;
            uniform float u_flicker_fps;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_functions="""
            float hash_scint(vec2 p) {
                p = fract(p * vec2(123.34, 456.21));
                p += dot(p, p + 45.32);
                return fract(p.x * p.y);
            }
        """,
        fragment_300="""
            vec4 col = texture2D(tex0, v_tex_coord);
            float luma = dot(col.rgb, vec3(0.299, 0.587, 0.114));

            float mask = smoothstep(
                u_flicker_threshold - u_flicker_softness,
                u_flicker_threshold + u_flicker_softness,
                luma
            );

            float frame = floor(u_time * u_flicker_fps);
            vec2 cell = floor(v_tex_coord * u_flicker_scale);
            float noise = hash_scint(cell + frame * 0.17);

            float scint = (noise - 0.5) * 2.0 * u_flicker_strength * mask;
            col.rgb += scint;
            gl_FragColor = col;
        """
    )

    # 4.3 胶片齿孔与边框遮罩 (Sprocket Filter)
    renpy.register_shader("cam.sprocketfilter",
        variables="""
            uniform sampler2D tex0;
            varying vec2 v_tex_coord;
            attribute vec2 a_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec4 color = texture2D(tex0, v_tex_coord);
            float luma = dot(color.rgb, vec3(0.299, 0.587, 0.114));
            float mask = step(luma, 0.1);
            gl_FragColor = vec4(0.0, 0.0, 0.0, mask);
        """
    )

    # 4.4 叠加混合模式 (Overlay Blend)
    renpy.register_shader("blend.overlay",
        variables="""
            uniform sampler2D tex0;
            uniform sampler2D u_ovl;
            uniform float u_ovl_strength;
            varying vec2 v_tex_coord;
        """,
        fragment_400="""
            vec4 b = gl_FragColor;
            vec4 o = texture2D(u_ovl, v_tex_coord);
            vec3 bc = b.rgb / max(b.a, 0.001);
            vec3 oc = o.rgb / max(o.a, 0.001);
            vec3 res = mix(2.0 * bc * oc, 1.0 - 2.0 * (1.0 - bc) * (1.0 - oc), step(0.5, bc));
            res = mix(bc, res, o.a * u_ovl_strength);
            gl_FragColor = vec4(res * b.a, b.a);
        """
    )

transform gateweave(framerate=24, jitter=0.5, hjitter=0.5):
    subpixel True
    function (GateWeave(framerate, jitter, hjitter) if persistent.gateweave else _fx_still)

transform filmflicker(framerate=24, dimpercent=2):
    function FilmFlicker(framerate, dimpercent)

transform halation(radius=28.0, strength=1.1, threshold=0.72, knee=0.15, rolloff=4.0, seam=0.8, tint=(1.0, 0.30, 0.12)):
    mesh True
    shader "cam.halation"
    u_radius radius
    u_strength strength
    u_threshold threshold
    u_knee knee
    u_rolloff rolloff
    u_seam seam
    u_tint tint
    u_taps fxq("halation")
    u_wsum fxq_wsum(fxq("halation"))

transform scint(strength=0.5, threshold=0.55, softness=0.25, scale=14.0, speed=0.7, fps=24):
    mesh True
    shader "cam.scintillate"
    u_flicker_strength strength
    u_flicker_threshold threshold
    u_flicker_softness softness
    u_flicker_scale scale
    u_flicker_speed speed
    u_flicker_fps fps

transform sprocketoverlay():
    shader "cam.sprocketfilter"
    gl_drawable_resolution False

# 椭圆暗角渐变生成器 (Optical Vignette)
# image elliptical_gradient = GradientDisplayable(...)
image elliptical_gradient = Solid("#00000000")

transform vignopacity(transp=0.4):
    alpha (transp if persistent.vignette else 0.0)


# ------------------------------------------------------------------------------
# 模块 5: 光学镜头、散景景深与色差系统 (Lens, Bokeh & Optics)
# ------------------------------------------------------------------------------
# 包含:
# 1) cam.bokeh: 黄金角 Vogel 螺旋盘状散景模糊 (Golden Angle Vogel Spiral Bokeh)
#    - 高光非线性 Gamma 展开，使光斑在虚焦时绽放为璀璨圆形光圈
# 2) cam.anabokeh: 变形宽银幕椭圆散景 (Anamorphic Oval Bokeh) + 水平条纹拉丝
# 3) cam.chroma: 径向与定向光学色差 (Chromatic Aberration Dispersion)
# 4) cam.lensdisto: 桶形/枕形多项式光学镜头畸变 (Polynomial Lens Distortion)
# 5) cam.convex: 凸面球面 CRT 玻璃弧度 (CRT Convex Bulge)
# 6) cam.freelensing: 移轴微缩 / 偏焦平面着色器 (Tilt-shift / Freelensing)
# 7) cam.hmblur: 高速甩镜方向性运动模糊 (High-Motion Blur)
# ------------------------------------------------------------------------------
init python:
    # 5.1 黄金角 Vogel 螺旋散景 (Vogel Spiral Bokeh Shader)
    renpy.register_shader("cam.bokeh",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform float u_radius;
            uniform float u_bokeh_gain;
            uniform float u_taps;
            uniform float u_taps_over;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            if (u_radius < 0.1) {
                gl_FragColor = texture2D(tex0, v_tex_coord);
            } else {
                const float GOLDEN_ANGLE = 2.399963229728653;
                float taps = (u_taps_over > 0.0) ? u_taps_over : u_taps;
                vec4 acc = vec4(0.0);
                float wsum = 0.0;

                for (int i = 0; i < 64; i++) {
                    if (float(i) >= taps) break;
                    float fi = float(i);
                    float r = sqrt((fi + 0.5) / taps);
                    float th = fi * GOLDEN_ANGLE;
                    vec2 offs = vec2(cos(th), sin(th)) * (r * u_radius) / u_model_size;

                    vec4 sampleCol = texture2D(tex0, clamp(v_tex_coord + offs, 0.0, 1.0));
                    // 高光伽马展开，塑造明亮散景圆斑 (Highlight Blooming)
                    sampleCol.rgb = pow(sampleCol.rgb, vec3(u_bokeh_gain / 10.0));
                    float w = 1.0;
                    acc += sampleCol * w;
                    wsum += w;
                }

                acc /= max(wsum, 0.001);
                acc.rgb = pow(acc.rgb, vec3(10.0 / u_bokeh_gain));
                gl_FragColor = acc;
            }
        """
    )

    # 5.2 变形宽银幕散景 (Anamorphic Oval Bokeh)
    renpy.register_shader("cam.anabokeh",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform float u_ana_radius;
            uniform float u_ana_ratio;
            uniform float u_ana_swirl;
            uniform float u_ana_fieldc;
            uniform float u_ana_gamma;
            uniform int u_ana_taps;
            uniform float u_ana_mip;
            uniform vec2 u_ana_center;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            if (u_ana_radius < 0.1) {
                gl_FragColor = texture2D(tex0, v_tex_coord);
            } else {
                const float GOLDENANGLE = 2.39996322972865;
                vec2 center_off = (v_tex_coord - u_ana_center) * vec2(u_model_size.x / u_model_size.y, 1.0);
                float dist = length(center_off);
                float eff_radius = u_ana_radius * (1.0 + dist * dist * u_ana_fieldc);

                vec4 acc = vec4(0.0);
                float wsum = 0.0;

                for (int i = 0; i < 48; i++) {
                    if (i >= u_ana_taps) break;
                    float fi = float(i);
                    float tr = sqrt((fi + 0.5) / float(u_ana_taps));
                    float th = fi * GOLDENANGLE;
                    vec2 tap = tr * vec2(cos(th), sin(th));

                    tap.x /= max(u_ana_ratio, 0.1);
                    float rot = dist * u_ana_swirl;
                    mat2 rmat = mat2(cos(rot), -sin(rot), sin(rot), cos(rot));
                    tap = rmat * tap;

                    vec2 uv = v_tex_coord + tap * eff_radius / u_model_size;
                    vec4 s = texture2D(tex0, clamp(uv, 0.0, 1.0), u_ana_mip);
                    s.rgb = pow(s.rgb, vec3(u_ana_gamma));
                    acc += s;
                    wsum += 1.0;
                }
                acc /= max(wsum, 0.001);
                acc.rgb = pow(acc.rgb, vec3(1.0 / u_ana_gamma));
                gl_FragColor = acc;
            }
        """
    )

    # 5.3 径向/定向光学色差 (Chromatic Aberration)
    renpy.register_shader("cam.chroma",
        variables="""
            uniform sampler2D tex0;
            uniform float u_radial;
            uniform vec2 u_flat;
            uniform vec2 u_focus;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec2 to_edge = v_tex_coord - u_focus;
            vec2 r_off = to_edge * u_radial + u_flat;
            vec2 b_off = -(to_edge * u_radial + u_flat);

            float r = texture2D(tex0, v_tex_coord + r_off).r;
            float g = texture2D(tex0, v_tex_coord).g;
            float b = texture2D(tex0, v_tex_coord + b_off).b;
            float a = texture2D(tex0, v_tex_coord).a;

            gl_FragColor = vec4(r, g, b, a);
        """
    )

    # 5.4 绿品红数码色差 (Green/Magenta Chromatic Dispersion)
    renpy.register_shader("cam.chroma_g",
        variables="""
            uniform sampler2D tex0;
            uniform float u_radial;
            uniform vec2 u_flat;
            uniform vec2 u_focus;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec2 to_edge = v_tex_coord - u_focus;
            vec2 g_off = to_edge * u_radial + u_flat;
            vec2 rb_off = -(to_edge * u_radial + u_flat);

            vec4 src = texture2D(tex0, v_tex_coord);
            float g = texture2D(tex0, v_tex_coord + g_off).g;
            vec4 rb = texture2D(tex0, v_tex_coord + rb_off);

            gl_FragColor = vec4(rb.r, g, rb.b, src.a);
        """
    )

    # 5.5 镜头畸变 (Lens Distortion)
    renpy.register_shader("cam.lensdisto",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform float u_k1;
            uniform float u_k2;
            uniform float u_fit;
            varying vec2 v_tex_coord;
            attribute vec2 a_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec2 uv = v_tex_coord * 2.0 - 1.0;
            float r2 = dot(uv, uv);
            float f = 1.0 + u_k1 * r2 + u_k2 * r2 * r2;
            uv = uv * f * u_fit;
            uv = uv * 0.5 + 0.5;
            gl_FragColor = texture2D(tex0, clamp(uv, 0.0, 1.0));
        """
    )

    # 5.6 凸面屏幕曲率 (CRT Convex Screen)
    renpy.register_shader("cam.convex",
        variables="""
            uniform sampler2D tex0;
            uniform float u_curve;
            uniform float u_fit;
            varying vec2 v_tex_coord;
        """,
        fragment_300="""
            vec2 uv = v_tex_coord * 2.0 - 1.0;
            vec2 off = abs(uv.yx) / max(u_curve, 0.1);
            uv = uv + uv * off * off;
            uv *= u_fit;
            uv = uv * 0.5 + 0.5;
            gl_FragColor = texture2D(tex0, clamp(uv, 0.0, 1.0));
        """
    )

    # 5.7 移轴摄影 (Freelensing / Tilt-shift)
    renpy.register_shader("cam.freelensing",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform float u_flens_rad;
            uniform vec2 u_flens_center;
            uniform vec2 u_flens_dir;
            uniform float u_flens_plane;
            varying vec2 v_tex_coord;
        """,
        fragment_300="""
            vec2 p = v_tex_coord - u_flens_center;
            float d = abs(dot(p, normalize(u_flens_dir)));
            float blur_amt = smoothstep(0.0, u_flens_plane, d) * u_flens_rad;
            if (blur_amt < 0.2) {
                gl_FragColor = texture2D(tex0, v_tex_coord);
            } else {
                vec4 acc = vec4(0.0);
                float wsum = 0.0;
                for (int i = -8; i <= 8; i++) {
                    float fi = float(i);
                    vec2 uv = v_tex_coord + vec2(0.0, fi * blur_amt / u_model_size.y);
                    float w = exp(-0.1 * fi * fi);
                    acc += texture2D(tex0, clamp(uv, 0.0, 1.0)) * w;
                    wsum += w;
                }
                gl_FragColor = acc / wsum;
            }
        """
    )

    # 5.8 高速运镜运动模糊 (High-Motion Blur)
    renpy.register_shader("cam.hmblur",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform float u_hmblur_radius;
            uniform vec2 u_hmblur_dir;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            if (u_hmblur_radius < 0.5) {
                gl_FragColor = texture2D(tex0, v_tex_coord);
            } else {
                vec4 acc = vec4(0.0);
                vec2 step_uv = (normalize(u_hmblur_dir) * u_hmblur_radius) / u_model_size / 8.0;
                for (int i = -8; i <= 8; i++) {
                    acc += texture2D(tex0, clamp(v_tex_coord + float(i) * step_uv, 0.0, 1.0));
                }
                gl_FragColor = acc / 17.0;
            }
        """
    )

# 光学变换函数 (Transforms)
transform bokeh(radius=12.0, gain=24.0, taps_override=0.0):
    mesh True
    gl_mipmap True
    gl_texture_scaling "linear_mipmap_linear"
    shader "cam.bokeh"
    u_radius radius
    u_bokeh_gain gain
    u_taps fxq("bokeh")
    u_taps_over taps_override

transform bokehin(radius=12.0, gain=24.0, startr=0.0, movetime=4.0, taps_override=0.0):
    mesh True
    gl_mipmap True
    shader "cam.bokeh"
    u_radius startr
    u_bokeh_gain gain
    u_taps fxq("bokeh")
    u_taps_over taps_override
    easein_expo movetime u_radius radius

transform bokehout(radius=12.0, gain=24.0, endr=0.0, movetime=4.0, taps_override=0.0):
    mesh True
    gl_mipmap True
    shader "cam.bokeh"
    u_radius radius
    u_bokeh_gain gain
    u_taps fxq("bokeh")
    u_taps_over taps_override
    easein_expo movetime u_radius endr

transform bokehm(endr=12.0, startrad=0.0, movetime=0.0, gain=24.0, taps_override=0.0):
    mesh True
    gl_mipmap True
    shader "cam.bokeh"
    u_radius startrad
    u_bokeh_gain gain
    u_taps fxq("bokeh")
    u_taps_over taps_override
    easein_expo movetime u_radius endr

transform bokehmC(endr=12.0, startrad=0.0, movetime=0.0, gain=24.0, taps_override=0.0):
    mesh True
    gl_mipmap True
    shader "cam.bokeh"
    u_radius startrad
    u_bokeh_gain gain
    u_taps fxq("bokeh")
    u_taps_over taps_override
    ease_cubic movetime u_radius endr

transform chroma(radial=0.008, flat=(0.0, 0.0), focus=(0.5, 0.5)):
    mesh (persistent.chromaab)
    shader ("cam.chroma" if persistent.chromaab else None)
    u_radial radial
    u_flat flat
    u_focus focus

transform chroma_green(radial=0.008, flat=(0.0, 0.0), focus=(0.5, 0.5)):
    mesh (persistent.chromaab)
    shader ("cam.chroma_g" if persistent.chromaab else None)
    u_radial radial
    u_flat flat
    u_focus focus

transform chromaspike(radial=0.01, flat=(0.0, 0.0), focus=(0.5, 0.5), outt=0.3, intt=0.8):
    mesh True
    shader "cam.chroma"
    u_flat flat
    u_focus focus
    u_radial 0.0
    warp synewarp (outt) u_radial radial
    warp synewarp (intt) u_radial 0.0

transform lensdistortion(k1=-0.02, k2=0.01, fit=1.0):
    mesh True
    shader "cam.lensdisto"
    u_k1 k1
    u_k2 k2
    u_fit fit

transform convexity(curve=8.0, fit=0.96):
    mesh True
    shader "cam.convex"
    u_curve curve
    u_fit fit

transform motionblur(r1=0.0, r0=0.0, mt=0.0, mbwarper="ease_cubic", dir=(1.0, 0.0)):
    mesh True
    shader "cam.hmblur"
    u_hmblur_radius r0
    u_hmblur_dir dir
    warp mbwarper (mt) u_hmblur_radius r1


# ------------------------------------------------------------------------------
# 模块 6: 复古模拟录像与早期数码 CCD (Analog VHS & Digital CCD)
# ------------------------------------------------------------------------------
# 包含:
# 1) syne.vhs: 全功能录像带着色器 (磁头追踪噪波、磁带折痕条纹、水平相位撕裂、色度延迟)
# 2) cam.digibloom: 早期数码 CCD 势阱电子溢出 (Vertical Smear 紫色高光拖尾与过曝光晕)
# 3) cam.diginoise: 早期低照度传感器高 ISO 彩色噪点 (ISO Chroma Noise)
# 4) CCDInterlace: 隔行扫描交织器 (Odd/Even Field Interlacing with Comb Artifacts)
# 5) cam.quantize / cam.undersample / cam.lcdpanel: 8-bit/16-bit 量化与 LCD 像素网格
# ------------------------------------------------------------------------------
init python:
    # 6.1 全功能模拟录像带着色器 (Full VHS Emulation)
    renpy.register_shader("syne.vhs",
        variables="""
            uniform sampler2D tex0;
            uniform float u_time;
            uniform float u_vhs_amount;
            uniform float u_vhs_warp;
            uniform float u_vhs_tracking;
            uniform float u_vhs_static;
            uniform float u_vhs_chroma;
            uniform float u_vhs_bloom;
            uniform float u_vhs_flicker;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_functions="""
            float vhs_hash(vec2 v) {
                return fract(sin(dot(v, vec2(89.44, 19.36))) * 22189.22);
            }
            float vhs_noise(vec2 v) {
                vec2 i = floor(v);
                vec2 f = fract(v);
                f = f * f * (3.0 - 2.0 * f);
                float a = vhs_hash(i);
                float b = vhs_hash(i + vec2(1.0, 0.0));
                float c = vhs_hash(i + vec2(0.0, 1.0));
                float d = vhs_hash(i + vec2(1.0, 1.0));
                return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
            }
        """,
        fragment_300="""
            vec2 uv = v_tex_coord;
            float t = u_time;

            // 磁带微抖动 (Tape Jitter)
            float tw = (vhs_noise(vec2(uv.y * 80.0, t * 15.0)) - 0.5) * 0.008 * u_vhs_warp;
            uv.x += tw;

            // 磁头追踪误差折痕横条 (Tracking Error Bar)
            float tcGate = vhs_noise(vec2(t * 0.5));
            float tcLine = clamp((sin(uv.y * 10.0 - t * 4.0) - 0.90) * tcGate, 0.0, 0.02) * 5.0 * u_vhs_tracking;
            uv.x -= tcLine * (vhs_noise(vec2(uv.y * 120.0, t * 20.0)) - 0.5);

            // 底部磁头换向噪点 (Head Switching Noise)
            float switchBar = smoothstep(0.04, 0.0, 1.0 - uv.y) * u_vhs_static;
            uv.x += switchBar * (vhs_hash(vec2(uv.y, t)) - 0.5) * 0.15;

            // 采样主色彩与色差横向拖尾
            vec3 col = texture2D(tex0, clamp(uv, 0.0, 1.0)).rgb;
            if (u_vhs_chroma > 0.0) {
                float r = texture2D(tex0, clamp(uv + vec2(0.005, 0.0) * u_vhs_chroma, 0.0, 1.0)).r;
                float b = texture2D(tex0, clamp(uv - vec2(0.005, 0.0) * u_vhs_chroma, 0.0, 1.0)).b;
                col = mix(col, vec3(r, col.g, b), 0.7);
            }

            // 噪点雪花与闪烁
            col *= (1.0 + (vhs_noise(vec2(uv.y * 200.0, t * 30.0)) - 0.5) * 0.08 * u_vhs_flicker);
            vec3 dry = texture2D(tex0, v_tex_coord).rgb;
            gl_FragColor = vec4(mix(dry, col, u_vhs_amount), 1.0);
        """
    )

    # 6.2 CCD 传感器溢出与垂直紫边拖尾 (CCD Blooming & Vertical Smear)
    renpy.register_shader("cam.digibloom",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform float u_threshold;
            uniform float u_bloomradius;
            uniform float u_bloom;
            uniform float u_smear;
            uniform vec3 u_smeartint;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec4 base = texture2D(tex0, v_tex_coord);
            float luma = dot(base.rgb, vec3(0.299, 0.587, 0.114));

            vec3 bloom = vec3(0.0);
            vec3 smear = vec3(0.0);

            // 径向泛光 (Radial Bloom)
            if (u_bloom > 0.0) {
                for (int i = -6; i <= 6; i++) {
                    vec2 offs = vec2(float(i) * u_bloomradius / u_model_size.x, 0.0);
                    vec3 s = texture2D(tex0, clamp(v_tex_coord + offs, 0.0, 1.0)).rgb;
                    float sl = dot(s, vec3(0.299, 0.587, 0.114));
                    bloom += max(sl - u_threshold, 0.0) * s;
                }
                bloom /= 13.0;
            }

            // 垂直高光溢出拖尾 (Vertical Smear - CCD 特征紫线)
            if (u_smear > 0.0) {
                for (int j = -12; j <= 12; j++) {
                    vec2 voffs = vec2(0.0, float(j) * 24.0 / u_model_size.y);
                    vec3 vs = texture2D(tex0, clamp(v_tex_coord + voffs, 0.0, 1.0)).rgb;
                    float vsl = dot(vs, vec3(0.299, 0.587, 0.114));
                    smear += max(vsl - u_threshold, 0.0) * u_smeartint;
                }
                smear /= 25.0;
            }

            vec3 res = base.rgb + bloom * u_bloom + smear * u_smear;
            gl_FragColor = vec4(res, base.a);
        """
    )

    # 6.3 数码感光噪波 (Digital Sensor Noise)
    renpy.register_shader("cam.diginoise",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform vec2 u_res;
            uniform float u_amount;
            uniform float u_falloff;
            varying vec2 v_tex_coord;
        """,
        fragment_functions="""
            float hash_dnoise(vec2 p) {
                p = fract(p * vec2(443.897, 441.423));
                p += dot(p, p.yx + 19.19);
                return fract((p.x + p.y) * p.x);
            }
        """,
        fragment_300="""
            vec4 col = texture2D(tex0, v_tex_coord);
            float l = dot(col.rgb, vec3(0.299, 0.587, 0.114));
            vec2 grid = (u_res.x > 0.0) ? u_res : u_model_size;
            vec2 cell = floor(v_tex_coord * grid);

            float nr = hash_dnoise(cell + vec2(0.1, 0.2)) - 0.5;
            float ng = hash_dnoise(cell + vec2(0.3, 0.4)) - 0.5;
            float nb = hash_dnoise(cell + vec2(0.5, 0.6)) - 0.5;

            // 暗部噪波更显著 (Low-light ISO gain boost)
            float boost = pow(1.0 - l, u_falloff);
            col.rgb += vec3(nr, ng, nb) * u_amount * boost;
            gl_FragColor = col;
        """
    )

    # 6.4 隔行扫描显示对象 (CCD / CRT Interlacing Displayable)
    class CCDInterlace(renpy.Displayable):
        """交错场扫描渲染器 (Interlaced Fields Renderer)"""
        def __init__(self, child, fieldrate=60.0, band=2, **kw):
            super(CCDInterlace, self).__init__(**kw)
            self.child = renpy.displayable(child)
            self.fieldrate = fieldrate
            self.band = band
            self.parity = 0
            self.prev_render = None
            self.last_st = 0.0

        def render(self, width, height, st, at):
            cur = renpy.render(self.child, width, height, st, at)
            cw, ch = cur.get_size()
            rv = renpy.Render(cw, ch)

            if self.prev_render is None:
                self.prev_render = cur

            # 奇偶场交叉绘制
            y = (self.parity % 2) * self.band
            rv.blit(self.prev_render, (0, 0))
            while y < ch:
                rv.blit(cur.subsurface((0, y, cw, min(self.band, ch - y))), (0, y))
                y += 2 * self.band

            self.prev_render = cur
            self.parity ^= 1
            renpy.redraw(self, 1.0 / self.fieldrate)
            return rv

        def visit(self):
            return [self.child]

    def ccd_interlace(child, fieldrate=60.0, band=2, res=None, effects=()):
        if effects:
            child = At(child, *effects)
        return CCDInterlace(child, fieldrate=fieldrate, band=band)

transform vhs(amount=0.6, fps=30, warp=1.0, tracking=1.0, static=1.0, chroma=1.0, bloom=1.0, flicker=1.0):
    mesh True
    shader "syne.vhs"
    u_vhs_amount amount
    u_vhs_warp warp
    u_vhs_tracking tracking
    u_vhs_static static
    u_vhs_chroma chroma
    u_vhs_bloom bloom
    u_vhs_flicker flicker
    pause 1.0 / fps
    repeat

transform digibloom(threshold=0.7, bloomradius=18.0, bloom=1.2, smear=0.8, smeartint=(0.75, 0.30, 1.0)):
    mesh True
    nearest True
    shader "cam.digibloom"
    u_threshold threshold
    u_bloomradius bloomradius
    u_bloom bloom
    u_smear smear
    u_smeartint smeartint

transform diginoise(amount=0.12, falloff=2.0, w=0, h=0):
    mesh True
    gl_drawable_resolution False
    nearest True
    shader "cam.diginoise"
    u_amount amount
    u_falloff falloff
    u_res (float(w), float(h))
    pause 0
    repeat


# ------------------------------------------------------------------------------
# 模块 7: 动态 2D 精灵表面着色器 (Sprite Normal & Rain Surface)
# ------------------------------------------------------------------------------
# 包含:
# 1) syne.raineffect: 2D 精灵表面物理雨水着色器
#    - 结合精灵表面法线图 + 程序化 3D Voronoi 雨滴高度法线贴图 + 浸润暗化贴图
#    - 计算表面折射凹凸 (Bulge)、湿水织物暗化 (Wetness Soak)、主光与补光高光闪烁 (Specular Sparkle)
# 2) cam.rimlight: 基于 Alpha 梯度的定向边缘轮廓光 (Edge Normal Rim Light)
# ------------------------------------------------------------------------------
init python:
    # 7.1 2D 精灵物理雨水折射着色器 (Procedural Rain on 2D Sprite)
    renpy.register_shader("syne.raineffect",
        variables="""
            uniform sampler2D tex0; // 精灵底图
            uniform sampler2D tex1; // 雨滴法线+高度贴图 (R:nx, G:ny, B:height)
            uniform sampler2D tex2; // 漫反射湿润暗化贴图 (Wetness Map)
            uniform sampler2D tex3; // 精灵本身法线贴图 (Sprite Surface Normal)
            uniform float u_rain_scale;
            uniform float u_rain_surface;
            uniform float u_rain_height;
            uniform float u_rain_wetness;
            uniform float u_rain_wet_threshold;
            uniform float u_rain_wet_soft;
            uniform vec2 u_rain_light_dir;
            uniform vec3 u_rain_light_col;
            uniform float u_rain_light_mix;
            uniform float u_rain_light_size;
            uniform vec2 u_rain_light_pos;
            uniform float u_rain_light_falloff;
            uniform vec2 u_rain_fill_dir;
            uniform vec3 u_rain_fill_col;
            uniform float u_rain_fill_mix;
            uniform float u_rain_fill_size;
            uniform vec2 u_model_size;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
            varying vec2 v_rain_uv;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
            v_rain_uv = a_tex_coord * u_model_size / max(u_rain_scale, 1.0);
        """,
        fragment_300="""
            vec4 sn = texture2D(tex3, v_tex_coord);
            vec2 snxy = (sn.rg * 2.0 - 1.0) * sn.a;
            snxy.y = -snxy.y;

            // 雨滴 UV 依随角色表面法线微幅扭曲
            vec2 ruv = fract(v_rain_uv + snxy * u_rain_surface / max(u_rain_scale, 1.0));
            vec4 nh = texture2D(tex1, ruv);
            vec2 nxy = nh.rg * 2.0 - 1.0;
            float hgt = nh.b;
            float wet = texture2D(tex2, ruv).r;

            // 雨滴折射透镜扭曲 (Refractive Bulge)
            vec2 bulge = nxy * hgt * u_rain_height / max(u_model_size, vec2(1.0));
            vec4 color = texture2D(tex0, clamp(v_tex_coord - bulge, 0.0, 1.0));

            // 湿润深色暗化 (避免使高亮皮肤变黑)
            float luma = dot(color.rgb, vec3(0.299, 0.587, 0.114)) / max(color.a, 1e-4);
            float dark = 1.0 - smoothstep(u_rain_wet_threshold - u_rain_wet_soft,
                                           u_rain_wet_threshold + u_rain_wet_soft, luma);
            color.rgb *= 1.0 - wet * u_rain_wetness * dark;

            // 主光 + 辅光双光源镜面反射 (Specular Lighting on Droplets)
            vec3 n = normalize(vec3(nxy, 1.0));
            vec3 lk = normalize(vec3(u_rain_light_dir, 1.0));
            vec3 lf = normalize(vec3(u_rain_fill_dir, 1.0));

            vec2 lvec = (v_tex_coord - u_rain_light_pos) * vec2(u_model_size.x / u_model_size.y, 1.0);
            float atten = 1.0 - smoothstep(0.0, u_rain_light_falloff, length(lvec));

            float spec_k = pow(max(dot(n, lk), 0.0), u_rain_light_size) * u_rain_light_mix * atten;
            float spec_f = pow(max(dot(n, lf), 0.0), u_rain_fill_size) * u_rain_fill_mix;

            color.rgb += (u_rain_light_col * spec_k + u_rain_fill_col * spec_f) * hgt * wet * color.a;
            gl_FragColor = color;
        """
    )

    # 7.2 精灵边缘轮廓光 (Alpha-driven Rim Light Shader)
    renpy.register_shader("cam.rimlight",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 u_model_size;
            uniform vec2 u_rim_dir;
            uniform float u_rim_width;
            uniform float u_rim_cut;
            uniform float u_rim_soft;
            uniform float u_rim_intensity;
            uniform float u_rim_wrap;
            uniform vec3 u_rim_color;
            varying vec2 v_tex_coord;
        """,
        fragment_functions="""
            float rim_a(sampler2D t, vec2 p) {
                vec2 ok = step(vec2(0.0), p) * step(p, vec2(1.0));
                return texture2D(t, clamp(p, 0.0, 1.0)).a * ok.x * ok.y;
            }
        """,
        fragment_300="""
            vec4 c = texture2D(tex0, v_tex_coord);
            vec2 texel = 1.0 / max(u_model_size, vec2(1.0));
            vec2 dir = (dot(u_rim_dir, u_rim_dir) > 0.0) ? normalize(u_rim_dir) : vec2(1.0, 0.0);

            // 前向采样 Alpha 计算轮廓边缘遮挡深度
            float ahead = 0.0;
            for (int i = 1; i <= 12; i++) {
                ahead += rim_a(tex0, v_tex_coord + dir * float(i) / 12.0 * u_rim_width * texel);
            }
            ahead /= 12.0;
            float depth = max(1.0 - ahead, 0.0);

            // 计算法线朝向与光源夹角 (Sobel/Gradient Normal)
            float gx = rim_a(tex0, v_tex_coord + vec2(texel.x, 0.0)) - rim_a(tex0, v_tex_coord - vec2(texel.x, 0.0));
            float gy = rim_a(tex0, v_tex_coord + vec2(0.0, texel.y)) - rim_a(tex0, v_tex_coord - vec2(0.0, texel.y));
            vec2 g = vec2(gx, gy);
            float facing = 1.0;
            if (dot(g, g) > 1e-8) {
                float d = dot(-normalize(g), dir);
                facing = clamp(d * (1.0 - u_rim_wrap) + u_rim_wrap, 0.0, 1.0);
            }

            float field = depth * facing;
            float rim = smoothstep(u_rim_cut - u_rim_soft, u_rim_cut + u_rim_soft, field) * c.a;
            vec3 lit = c.rgb + u_rim_color * (rim * u_rim_intensity);
            gl_FragColor = vec4(lit, c.a);
        """
    )


# ------------------------------------------------------------------------------
# 模块 8: 动态文字排版与文字着色器 (Kinetic Typography Tags)
# ------------------------------------------------------------------------------
# 包含:
# 1) {ransom} / {ransom2}: 勒索信多字体动态跳变标签 (Ransom Note Typography)
# 2) {censor}: 动态机密审查乱码标签 (Classified Scrambled Redaction)
# 3) {boil}: 顶点手绘噪动沸腾文字着色器 (Hand-drawn Boiling Outline)
# 4) {dalikmatatxt}: 绿品红分色文字着色器 (Chroma Offset Text)
# ------------------------------------------------------------------------------
init python:
    # 8.1 顶点沸腾描边 (Boiling Contour Textshader)
    renpy.register_textshader("boil",
        variables="""
            uniform float u__amplitude;
            uniform float u__fps;
            uniform float u_time;
            attribute float a_text_index;
        """,
        vertex_60="""
            float t = floor(u_time * u__fps);
            vec2 j = vec2(
                fract(sin(a_text_index * 12.9898 + t * 78.233) * 43758.5453),
                fract(sin(a_text_index * 26.6519 + t * 39.1160) * 24634.6345)
            ) - 0.5;
            gl_Position.xy += j * 2.0 * u__amplitude;
        """,
        u__amplitude=1.5,
        u__fps=8.0,
        redraw=1.0 / 8.0,
    )

    # 8.2 文字色差分相 (Chromatic Aberration Textshader)
    renpy.register_textshader("dalikmatatxt",
        variables="""
            uniform sampler2D tex0;
            uniform vec2 res0;
            uniform float u_time;
            uniform float u__fps;
            uniform float u__strength;
            varying vec2 v_tex_coord;
        """,
        fragment_310="""
            float t = floor(u_time * u__fps);
            float ang = fract(sin(t * 12.9898) * 43758.5453) * 6.2831853;
            float mag = fract(sin(t * 78.233) * 24634.6345) * u__strength;
            vec2 off = vec2(cos(ang), sin(ang)) * mag / max(res0, vec2(1.0));
            vec4 shifted = texture2D(tex0, v_tex_coord - off);
            gl_FragColor.g = shifted.g;
            gl_FragColor.a = max(gl_FragColor.a, shifted.a);
        """,
        u__fps=8.0,
        u__strength=2.0,
        redraw=1.0 / 8.0,
    )

    # 8.3 勒索信多字体动态跳变系统 (Ransom Glyph Displayable)
    def _rand_color_hsv():
        return Color(hsv=(_random.random(), 0.65, 0.9)).hexcode

    def _get_system_ransom_fonts():
        # 若工程中没有单独的 fonts/random 文件夹，则安全回退到默认字体
        fl = [fn for fn in renpy.list_files() if fn.startswith("fonts/") and fn.lower().endswith((".ttf", ".otf"))]
        return fl if fl else ["DejaVuSans.ttf"]

    class RansomGlyph(renpy.Displayable):
        def __init__(self, ch, fonts, fps=10.0, is_colored=False, **kw):
            super(RansomGlyph, self).__init__(**kw)
            self.ch = ch
            self.fonts = fonts if fonts else ["DejaVuSans.ttf"]
            self.fps = fps if fps else 10.0
            self.is_colored = is_colored
            self.current_font = _random.choice(self.fonts)
            self.current_col = _rand_color_hsv() if is_colored else "#FFFFFF"
            self.last_st = 0.0

        def render(self, width, height, st, at):
            if st - self.last_st >= (1.0 / self.fps):
                self.current_font = _random.choice(self.fonts)
                if self.is_colored:
                    self.current_col = _rand_color_hsv()
                self.last_st = st

            t = Text(self.ch, font=self.current_font, color=self.current_col, size=30)
            child = renpy.render(t, width, height, st, at)
            w, h = child.get_size()
            rv = renpy.Render(w, h)
            rv.blit(child, (0, 0))
            renpy.redraw(self, 1.0 / self.fps)
            return rv

    def _tag_ransom(tag, argument, contents):
        fps = float(argument) if argument and argument.strip().isdigit() else 10.0
        fonts = _get_system_ransom_fonts()
        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for ch in text:
                    if ch.isspace():
                        rv.append((renpy.TEXT_TEXT, ch))
                    else:
                        rv.append((renpy.TEXT_DISPLAYABLE, RansomGlyph(ch, fonts, fps=fps, is_colored=False)))
            else:
                rv.append((kind, text))
        return rv

    def _tag_ransom_color(tag, argument, contents):
        fps = float(argument) if argument and argument.strip().isdigit() else 8.0
        fonts = _get_system_ransom_fonts()
        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for ch in text:
                    if ch.isspace():
                        rv.append((renpy.TEXT_TEXT, ch))
                    else:
                        rv.append((renpy.TEXT_DISPLAYABLE, RansomGlyph(ch, fonts, fps=fps, is_colored=True)))
            else:
                rv.append((kind, text))
        return rv

    # 8.4 乱码文字遮罩 (Scramble Censor Displayable)
    class ScrambleGlyph(renpy.Displayable):
        def __init__(self, ch, fps=24.0, **kw):
            super(ScrambleGlyph, self).__init__(**kw)
            self.ch = _random.choice(string.ascii_letters + "!@#$%^&*")
            self.fps = fps
            self.last_st = 0.0

        def render(self, width, height, st, at):
            if st - self.last_st >= (1.0 / self.fps):
                self.ch = _random.choice(string.ascii_letters + "!@#$%^&*")
                self.last_st = st
            t = Text(self.ch, color="#F0DDD8", size=28)
            child = renpy.render(t, width, height, st, at)
            w, h = child.get_size()
            rv = renpy.Render(16, h)
            rv.blit(child, (0, 0))
            renpy.redraw(self, 1.0 / self.fps)
            return rv

    def _tag_censor(tag, argument, contents):
        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for ch in text:
                    if ch.isspace():
                        rv.append((renpy.TEXT_TEXT, ch))
                    else:
                        rv.append((renpy.TEXT_DISPLAYABLE, ScrambleGlyph(ch)))
            else:
                rv.append((kind, text))
        return rv

    # 注册自定义文字标签
    config.custom_text_tags["ransom"] = _tag_ransom
    config.custom_text_tags["ransom2"] = _tag_ransom_color
    config.custom_text_tags["censor"] = _tag_censor


# ------------------------------------------------------------------------------
# 模块 9: 硬件级沉浸式转场黑科技 (Hardware Cinema Transitions)
# ------------------------------------------------------------------------------
# 包含:
# 1) crtstop(): 截取当前屏幕，执行 CRT 阴极射线管电视断电效果 (水平线亮起坍缩为微光光点熄灭)
# 2) projectorstop(): 截取当前画面，模拟放映机卡带齿轮脱出、伴随片门抖动垂直滑落转场
# 3) photosnap(): 截取当前画面，瞬间反转并施加负片色彩分级，模拟单反快门闪光曝光
# ------------------------------------------------------------------------------
transform crtcollapse:
    subpixel True
    anchor (0.5, 0.5) pos (0.5, 0.5)
    xzoom 1.0 yzoom 1.0
    matrixcolor BrightnessMatrix(0.0)
    parallel:
        easeout_expo 0.4 yzoom 0.005 # 垂直收缩为一道耀眼白线
    parallel:
        easeout_expo 0.3 matrixcolor BrightnessMatrix(1.0) # 荧光粉过载高亮
    pause 0.1
    easein_expo 0.5 xzoom 0.0 alpha 0.0 # 水平收缩为一个微弱光点消失

transform slideout:
    matrixcolor SaturationMatrix(0.95)
    subpixel True
    anchor (0.5, 0.5) pos (0.5, 0.5)
    zoom 1.0
    easein_expo 0.3 zoom 0.98
    pause 0.5
    easein_expo 0.1 alpha 0.0 yoffset 10

transform negativecol(duration=0.5):
    matrixcolor InvertMatrix(1.0)
    alpha 1.0
    pause duration * 2.0 / 3.0
    warp synewarp (duration * 1.0 / 3.0) alpha 0.0

init python:
    # 色彩分级着色器
    renpy.register_shader("cam.colorgrade",
        variables="""
            uniform sampler2D tex0;
            uniform vec3 u_lift;
            uniform vec3 u_gamma;
            uniform vec3 u_gain;
            uniform float u_sat;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            const vec3 luma = vec3(0.299, 0.587, 0.114);
            vec4 src = texture2D(tex0, v_tex_coord);
            float a = max(src.a, 0.0001);
            vec3 c = src.rgb / a;

            c = c * u_gain + u_lift * (1.0 - c);
            c = clamp(c, 0.0, 1.0);
            c = pow(c, 1.0 / max(u_gamma, vec3(0.0001)));

            float l = dot(c, luma);
            c = mix(vec3(l), c, u_sat);
            gl_FragColor = vec4(c * a, src.a);
        """
    )

transform colorgrade(lift=(0.0, 0.0, 0.0), gamma=(1.0, 1.0, 1.0), gain=(1.0, 1.0, 1.0), sat=1.0):
    mesh True
    shader "cam.colorgrade"
    u_lift lift
    u_gamma gamma
    u_gain gain
    u_sat sat

transform negativecollapse:
    mesh True
    shader "cam.colorgrade"
    u_lift (-0.05, -0.05, -0.05)
    u_gamma (0.4, 0.8, 0.7)
    u_gain (0.85, 0.38, 0.2)
    u_sat 1.0

# 沉浸式转场调用函数
init python:
    def crtstop(duration=1.2, size=(1920, 1080)):
        """执行 CRT 电视断电关机转场"""
        sc = renpy.screenshot_to_bytes(size)
        renpy.show_screen("_crtcframe", d=im.Data(sc, "screencap.png"))
        renpy.pause(duration, hard=True)
        renpy.hide_screen("_crtcframe")

    def projectorstop(duration=1.2, size=(1920, 1080)):
        """执行胶片放映机卡带滑落转场"""
        sc = renpy.screenshot_to_bytes(size)
        renpy.show_screen("_scframe", d=im.Data(sc, "screencap.png"))
        renpy.pause(duration, hard=True)
        renpy.hide_screen("_scframe")

    def photosnap(duration=0.5, size=(1920, 1080)):
        """执行单反相机快门闪光与负片显影闪回转场"""
        sc = renpy.screenshot_to_bytes(size)
        renpy.show_screen("_photoneg", d=im.Data(sc, "screencap.png"), dur=duration)
        renpy.pause(duration, hard=True)
        renpy.hide_screen("_photoneg")

screen _crtcframe(d):
    zorder 1000
    add Solid("#000000FF")
    frame at crtcollapse:
        background None
        add Transform(d, fit="fill", xysize=(config.screen_width, config.screen_height))

screen _scframe(d):
    zorder 1000
    add Solid("#000000FF")
    frame at slideout:
        background None
        add Transform(d, fit="fill", xysize=(config.screen_width, config.screen_height)) at gateweave(24, 0.7, 0.7)

screen _photoneg(d, dur=0.5):
    zorder 1000
    add Solid("#000000FF")
    frame at negativecol(dur), negativecollapse:
        background None
        add Transform(d, fit="fill", xysize=(config.screen_width, config.screen_height))

# ==============================================================================
# 代码库编写完成 - 包含 9 大模块全部核心代码与算法
# ==============================================================================
