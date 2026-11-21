# ==============================================================================
# turbulent_moire_fx.rpy
# 基于 3×3 拼贴莫尔纹贴图 (images/vfx/moire_pattern_3x3.png)
# + 零形变、超缓速伪湍流明暗呼吸（仅作用于低调暗部，中高调保持纯净）
# ------------------------------------------------------------------------------
# 用法示例：
#   show expression MoireTurbulentBG("images/bg/station_01_blue.png")
#   show expression MoireTurbulentBG("images/bg/sea_04_blue.png", speed=0.10)
#   show expression MoireTurbulentBG("images/bg/bedroom_01_orange.png", luma_cutoff=0.42)
# ==============================================================================

init -5 python:
    renpy.register_shader("fx.turbulent_moire_tex",
        variables="""
            uniform sampler2D tex0;
            uniform sampler2D tex1;
            uniform vec2 u_model_size;
            uniform float u_time;
            uniform float u_disp_amp;
            uniform float u_turb_speed;
            uniform float u_turb_scale;
            uniform float u_luma_low;
            uniform float u_luma_high;
            uniform float u_lift_gain;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            const vec3 LUMA_W = vec3(0.299, 0.587, 0.114);

            vec2 px = 1.0 / max(u_model_size, vec2(1.0));
            vec2 uv = v_tex_coord;

            // 超缓速低频 4-octave fBm 明暗场（不扭曲原图几何形状）
            float n1 = 0.0;
            float n2 = 0.0;
            float amp = 0.5;
            float freq = max(u_turb_scale, 0.5);
            float t = u_time * u_turb_speed;

            for (int i = 0; i < 4; i++) {
                float fi = float(i);
                vec2 p1 = uv * freq + vec2(t * (0.14 + 0.06 * fi), t * (0.10 - 0.04 * fi));
                vec2 p2 = uv * freq + vec2(t * (0.14 + 0.06 * fi) + 17.3, t * (0.10 - 0.04 * fi) + 9.7);

                vec2 i1 = floor(p1); vec2 f1 = fract(p1); vec2 u1 = f1 * f1 * (3.0 - 2.0 * f1);
                float a1 = fract(sin(dot(i1, vec2(127.1, 311.7))) * 43758.5453);
                float b1 = fract(sin(dot(i1 + vec2(1.0, 0.0), vec2(127.1, 311.7))) * 43758.5453);
                float c1 = fract(sin(dot(i1 + vec2(0.0, 1.0), vec2(127.1, 311.7))) * 43758.5453);
                float d1 = fract(sin(dot(i1 + vec2(1.0, 1.0), vec2(127.1, 311.7))) * 43758.5453);
                n1 += amp * mix(mix(a1, b1, u1.x), mix(c1, d1, u1.x), u1.y);

                vec2 i2 = floor(p2); vec2 f2 = fract(p2); vec2 u2 = f2 * f2 * (3.0 - 2.0 * f2);
                float a2 = fract(sin(dot(i2, vec2(127.1, 311.7))) * 43758.5453);
                float b2 = fract(sin(dot(i2 + vec2(1.0, 0.0), vec2(127.1, 311.7))) * 43758.5453);
                float c2 = fract(sin(dot(i2 + vec2(0.0, 1.0), vec2(127.1, 311.7))) * 43758.5453);
                float d2 = fract(sin(dot(i2 + vec2(1.0, 1.0), vec2(127.1, 311.7))) * 43758.5453);
                n2 += amp * mix(mix(a2, b2, u2.x), mix(c2, d2, u2.x), u2.y);

                freq *= 2.0;
                amp *= 0.5;
            }

            float turb_energy = clamp(n1 * 0.65 + n2 * 0.35, 0.0, 1.0);
            float turb_wave = smoothstep(0.28, 0.72, turb_energy);

            // 原图零形变采样，保持建筑/天际线绝对笔直
            vec4 base = texture2D(tex0, uv);

            // 仅对莫尔纹贴图允许极微弱偏移（默认 0.0 为纯明暗呼吸）
            vec2 pat_uv = clamp(uv + vec2(n1 - 0.5, n2 - 0.5) * 2.0 * u_disp_amp * px, 0.0, 1.0);
            float pat_raw = texture2D(tex1, pat_uv).r;
            float pat = clamp((pat_raw - 0.15) / 0.72, 0.0, 1.0);
            float pat_mod = 0.20 + 0.80 * pat;

            // 5-tap 宏观亮度平滑采样，绕过原图自带 Bayer 抖动网点
            float l_c = dot(base.rgb, LUMA_W);
            float l_1 = dot(texture2D(tex0, clamp(uv + vec2(2.0, 0.0) * px, 0.0, 1.0)).rgb, LUMA_W);
            float l_2 = dot(texture2D(tex0, clamp(uv - vec2(2.0, 0.0) * px, 0.0, 1.0)).rgb, LUMA_W);
            float l_3 = dot(texture2D(tex0, clamp(uv + vec2(0.0, 2.0) * px, 0.0, 1.0)).rgb, LUMA_W);
            float l_4 = dot(texture2D(tex0, clamp(uv - vec2(0.0, 2.0) * px, 0.0, 1.0)).rgb, LUMA_W);
            float macro_luma = (l_c + l_1 + l_2 + l_3 + l_4) * 0.2;
            float struct_luma = mix(macro_luma, l_c, 0.28);

            // 沿用原图单一色调
            float ch_max = max(max(base.r, base.g), base.b);
            vec3 tint = (ch_max > 0.02) ? (base.rgb / ch_max) : vec3(0.85, 0.90, 1.0);

            // 严格限制仅低调暗部受影响，中高调 (struct_luma >= u_luma_high) 完全保留原样
            float lowkey_mask = 1.0 - smoothstep(u_luma_low, u_luma_high, struct_luma);

            vec3 lowkey_dark = base.rgb * 0.45;
            vec3 lift_tone = max(base.rgb, tint * 0.24) * u_lift_gain;
            vec3 lowkey_moire = lift_tone * pat_mod;

            vec3 shadow_mod = mix(lowkey_dark, lowkey_moire, turb_wave);
            vec3 out_rgb = mix(base.rgb, shadow_mod, lowkey_mask);

            gl_FragColor = vec4(clamp(out_rgb, 0.0, 1.0) * base.a, base.a);
        """
    )

    def MoireTurbulentBG(bg_path, speed=0.10, scale=2.0, disp_amp=0.0, luma_low=0.16, luma_high=0.42, lift_gain=1.15, pattern_path="images/vfx/moire_pattern_3x3.png"):
        m = Model()
        m.texture(bg_path)
        m.texture(pattern_path)
        m.shader("fx.turbulent_moire_tex")
        m.property("u_disp_amp", float(disp_amp))
        m.property("u_turb_speed", float(speed))
        m.property("u_turb_scale", float(scale))
        m.property("u_luma_low", float(luma_low))
        m.property("u_luma_high", float(luma_high))
        m.property("u_lift_gain", float(lift_gain))
        return m
