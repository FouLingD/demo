## 08_dev_shortcuts.rpy - 开发者测试专用快捷键与调试工具
## （正式发布上线前可直接删除此文件，或将 DEV_MODE 设为 False）

init -1 python:
    # 开发者调试总开关
    DEV_MODE = True

    # =========================================================================
    # 快进速率调节（每句对白文本停留时间，单位：毫秒 ms）
    # 数值越大越慢，数值越小越快：
    # - 50ms:  极快（每秒约 20 句）
    # - 100ms: 适中推荐（每秒约 10 句，能清晰看清说话人和对白内容，便于定位）
    # - 150ms: 平缓（每秒约 6~7 句）
    # =========================================================================
    DEV_SKIP_DELAY_MS = 100

    if DEV_MODE:
        # 1. 允许快进未读内容（方便开发测试随时快进跳转）
        config.allow_skipping = True
        config.fast_skipping = False # 不使用秒跳穿梭，保证对白正常渲染推进
        config.skip_delay = DEV_SKIP_DELAY_MS

        default_preferences = getattr(renpy.game, "preferences", None)
        if default_preferences:
            default_preferences.skip_unseen = True

        # 2. 滚轮下滑平稳快进检测逻辑
        import time
        _dev_wheel_time = 0.0
        _dev_wheel_count = 0

        def dev_wheel_down_action():
            global _dev_wheel_time, _dev_wheel_count

            # 保护检测：如果在存读档界面、设置页、历史日志或分支选项中，放行滚轮以供正常滚动查看
            active_screens = ["choice", "game_menu", "preferences", "history", "save", "load", "confirm", "about", "help"]
            for s in active_screens:
                if renpy.get_screen(s):
                    return

            now = time.time()
            # 0.35 秒内连续滚动判定为“快速下滑”
            if now - _dev_wheel_time < 0.35:
                _dev_wheel_count += 1
            else:
                _dev_wheel_count = 1
            _dev_wheel_time = now

            if _dev_wheel_count >= 2:
                # 连续快速下滑：启动平稳快进模式（按 DEV_SKIP_DELAY_MS 速率逐句推进）
                if not config.skipping:
                    config.skipping = "slow"
                    renpy.restart_interaction()

screen dev_wheel_fast_forward():
    zorder 999
    if DEV_MODE:
        key "mousedown_5" action Function(dev_wheel_down_action)

init python:
    if DEV_MODE and "dev_wheel_fast_forward" not in config.overlay_screens:
        config.overlay_screens.append("dev_wheel_fast_forward")
