## ch08_nightbus.rpy - 第八章：空旷的商场与蓝色的金平糖
## 严格对标《素材与视觉资产规范.md》与《图片.rtf》视觉素材规范
## 背景规范：corridor_01_blue / corridor_01_orange / restaurant_01_blue / restaurant_01_orange / arcade_01_blue / arcade_01_orange / city_02_orange / road_01_orange / bg white / bg black
## 立绘规范：anon hosp 01~10 全套差分, taki 01 glare / 02 normal_1 / 02 normal_2 / 03 sad
## 三层旁白与主视角差分系统：纯环境旁白（无立绘无头像） / 对方动作观察旁白（仅对方立绘无头像） / 高松灯主观心声与台词（tomori <emo> + 换行 extend）

label ch08_nightbus:
    $ current_chapter = 8
    $ quick_menu = True

    # ==========================================
    # 1. 清晨空旷的大型商场
    # ==========================================
    scene bg corridor_01_blue with fade
    play music bgm_routine fadein 2.0 loop
    play bgs bgs_hospital fadein 2.0 loop

    "早班大巴在换乘枢纽站停靠休整的四十分钟里，{w=0.2}{nw}"
    extend "爱音摸了摸我冰凉的手腕，说去海边吹风之前必须先吃顿热乎的早饭，硬拉着我钻进了车站旁刚刚开门的大型商场。"
    "还没有什么人。{w=0.15}{nw}"
    extend "\n整座庞大的建筑呈现出一种清冷的空旷。"

    # Part 2：确立关系后的第一场戏（粉灰单人剪影交替 + 暗底“我已经活了十六年”独白）
    call editorial_part2

    scene bg corridor_01_orange with dissolve
    play sound sfx_footsteps
    show anon hosp 08 gentle at center_standee with dissolve
    "千早爱音拉着我的风衣袖子，我们两人走在空无一人的走廊正中央。{w=0.15}{nw}"
    tomori smile "现在，爱音来了。{w=0.15}{nw}"
    extend calm "\n我们要活下去，把剩下的时间全部烧成灰烬。"

    stop bgs fadeout 1.5

    # ==========================================
    # 2. 负一层面包房与蓝色的金平糖
    # ==========================================
    scene bg restaurant_01_blue with dissolve
    play music bgm_dialogue_warm fadein 1.5 loop

    show anon hosp 02 boast at anon_burst_in
    anon "{cps=*1.6}哇！负一层开门了！面包房！{/cps}{w=0.05}{nw}"
    show anon hosp 01 smug at standee_jump
    extend "\n{cps=*1.6}快来快来！草莓奶油三明治！两层厚奶油！{/cps}{w=0.05}{nw}"
    show anon hosp 07 normal_1 at standee_step_in
    extend "\n{cps=*1.5}小灯！吃这个！{/cps}"

    tomori pout "……太厚了。{w=0.15}{nw}"
    extend uff "咽不下去。"

    show anon hosp 07 normal_1 at center_standee
    anon "{cps=*1.5}哪会咽不下去啊！那这个呢？热牛奶！{/cps}{w=0.05}{nw}"
    show anon hosp 02 boast at standee_jump
    extend "\n{cps=*1.5}还有这个！小铁盒！不对，玻璃瓶！{/cps}"

    tomori ah "……星星。"

    show anon hosp 01 smug at standee_nod
    anon "{cps=*1.5}是金平糖啦！蓝色的！粉色的！硬糖！{/cps}{w=0.05}{nw}"
    show anon hosp 02 boast at standee_jump
    extend "\n{cps=*1.6}买！老板，结账！{/cps}"

    hide anon with dissolve
    "我们在扶梯边的长椅上坐下。{w=0.15}{nw}"
    extend "\n长椅很凉。奶瓶很烫。{w=0.15}{nw}"
    extend "\n瓶身直接贴在手心上，热气顺着手腕爬上来。"

    show anon hosp 07 normal_1 at center_standee with dissolve
    "爱音一口咬下去。{w=0.15}{nw}"
    extend "\n白色的奶油直接沾在了鼻尖上。"

    tomori calm "……鼻子。"

    show anon hosp 03 curious_3 at center_standee
    anon "哈？鼻子怎么了？"

    tomori smile "鼻尖上……有白色的奶油。{w=0.15}{nw}"
    extend soft "\n像小丑。"

    show anon hosp 05 annoyed_2 at standee_shake_h
    anon "{cps=*1.5}才不是小丑呢！{/cps}{w=0.05}{nw}"
    show anon hosp 07 normal_1 at standee_step_in
    extend "小灯也来一口！"

    tomori pout "不吃……"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.5}吃一口嘛！就一口！啊——！{/cps}"

    tomori pout "唔……{w=0.15}{nw}"
    extend calm "太甜了。"

    show anon hosp 01 smug at center_standee
    "爱音笑得整个人倒在椅背上。"
    play sound sfx_candy_jar
    "我拧开玻璃罐，倒出一颗蓝色的金平糖，塞进嘴里。"
    play sound sfx_candy_crunch
    "咔嚓。{w=0.15}{nw}"
    extend "咬碎了。"
    play sound sfx_candy_jar
    tomori soft "我把糖罐放进风衣内袋，贴着肋骨。{w=0.15}{nw}"
    extend calm "\n叮当，叮当。走动时有轻微的响动。"

    tomori soft "……很甜。"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.5}甜就对了！走！{/cps}"

    play sound sfx_running_corridor
    show anon hosp 07 normal_1 at standee_step_in
    "爱音没有多说什么，直接一把拽住我的手腕，拉着我快步冲上了三楼。"

    tomori uff "爱音……走太快了……"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.6}抓紧！到了！{/cps}"

    # ==========================================
    # 3. 三楼街机厅与企鹅玩偶
    # ==========================================
    scene bg arcade_01_blue with dissolve
    play music bgm_banter_boops fadein 1.5 loop
    play bgs bgs_arcade fadein 1.5 loop

    "三楼。大型室内游乐街机厅。{w=0.15}{nw}"
    extend "\n一出扶梯，五颜六色的霓虹灯光和电子音乐劈头盖脸砸过来。{w=0.15}{nw}"
    extend "\n跳舞机、推币机、赛车机。金属摇杆碰撞，硬币哗啦作响。"

    tomori calm "……我确实从来没有玩过这些。{w=0.15}{nw}"
    extend sadaway "\n十六年来，一次都没有。{w=0.15}{nw}"
    extend bitter "\n这些声音太吵了，光线太刺眼了。我以为这里只有正常人才能进来。"

    show anon hosp 01 smug at center_standee, standee_nod with dissolve
    anon "{cps=*1.5}少啰嗦！换硬币！{/cps}"

    play sound sfx_coin_insert
    "爱音往兑币机里塞了一千日元。{w=0.15}{nw}"
    extend "\n塑料盒里装满了沉甸甸的百元硬币。"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.5}看！橱窗里！{/cps}"

    tomori ah "……企鹅。"

    hide anon with dissolve
    "一只圆滚滚的黑白小企鹅玩偶歪倒在出物口的边缘，圆溜溜的塑料黑眼睛正对着我们。"
    play sound sfx_coin_insert
    show anon hosp 03 curious_1 at center_standee with dissolve
    "爱音把一枚枚硬币投进投币孔里，机器发出欢快的电子音乐。{w=0.15}{nw}"
    play ambient_sfx sfx_claw_whir
    extend "\n机械爪在玻璃箱里移动，落下去又抓空。"

    show anon hosp 05 annoyed_1 at standee_shake_h
    anon "{cps=*1.5}啊！又滑掉了！怎么这么松啊！{/cps}"

    tomori smile "……噗。"

    show anon hosp 05 annoyed_2 at standee_jump
    anon "{cps=*1.6}小灯你笑我！不服气，再来！{/cps}"

    "爱音屡次失手，气得直跺脚。{w=0.15}{nw}"
    play sound sfx_clothes_rustle
    show anon hosp 02 boast at standee_step_in
    extend "\n随后，爱音一把拉住我，把我推到了操作台正前方。"

    show anon hosp 01 smug at standee_step_in
    anon "{cps=*1.5}你来！本小姐给你护航！{/cps}"

    tomori sadaway "我……我不行的。"

    show anon hosp 07 normal_1 at standee_step_in
    anon "握住摇杆！"

    scene bg arcade_01_orange with flash_warm
    show anon hosp 08 gentle at center_standee, standee_step_in with dissolve
    camera:
        easein 0.8 zoom 1.08 yoffset 12
    "爱音从背后握住我的手，带着我的手指一起握紧了黑色的塑料摇杆。"
    tomori calm "我会变成什么。我害怕。{w=0.15}{nw}"
    extend soft "\n快来。快来我身边。快，给我一点您的力量。{w=0.15}{nw}"
    extend calm "\n我松开手。"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.6}就是现在！拍下去！{/cps}"

    play sound sfx_arcade_button
    hide anon with fast_dissolve
    "我用手掌用力拍下了红色的圆形按键。" with shake_v
    "三根机械爪笔直落下去，紧紧抓住了企鹅圆滚滚的肚子。{w=0.15}{nw}"
    extend "\n齿轮转动，小企鹅被一把捞起，晃晃悠悠地悬在半空中。"
    play sound sfx_plush_drop
    "啪嗒。{w=0.15}{nw}"
    extend "\n企鹅稳稳当当掉进了下方的出物口里。"

    camera:
        easeout 0.6 zoom 1.0 yoffset 0
    scene bg arcade_01_blue with dissolve
    show anon hosp 02 boast at center_standee, standee_jump
    anon "{cps=*1.6}哇啊啊啊！抓到了！抓到了！{/cps}"

    "爱音欢呼着原地跳了起来，两只手在半空中用力挥舞。"

    tomori yay "……抓到了。{w=0.15}{nw}"
    extend smile "爱音，我们抓到了。"

    show anon hosp 01 smug at standee_nod
    anon "{cps=*1.5}那是当然！{/cps}{w=0.05}{nw}"
    show anon hosp 02 boast at standee_step_in
    extend "\n{cps=*1.5}快抱好！这是我们的战利品！{/cps}"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.5}呼！{/cps}{w=0.05}{nw}"
    show anon hosp 07 normal_1 at center_standee
    extend "\n{cps=*1.5}四楼！家庭餐厅！吃热乎的去！{/cps}"

    # ==========================================
    # 4. 四楼家庭餐厅与立希相遇
    # ==========================================
    stop bgs fadeout 1.2
    scene bg restaurant_01_orange with dissolve
    play music bgm_reflection fadein 2.0 loop
    play bgs bgs_restaurant fadein 1.5 loop

    "我们在四楼的家庭餐厅坐下。{w=0.15}{nw}"
    extend "\n爱音点了加了熏三文鱼的意面，还有一大盘炸薯条。"

    show anon hosp 07 normal_1 at right_standee with dissolve
    anon "给！刚出锅的薯条！十六年没吃过什么的也太夸张了吧，快趁热拿一根！"

    tomori pout "那个……外皮看起来很硬。而且盘子边缘有小包的红色酱料……"

    menu:
        "爱音正期待地盯着托盘里的炸薯条。"
        "拿一根不蘸酱，小心咬一小口试试看":
            $ _fries_choice = "plain"
        "跟着爱音一起，直接蘸一大坨番茄酱":
            $ _fries_choice = "ketchup"

    if _fries_choice == "plain":
        tomori calm "{cps=*1.5}……唔。外面是脆的，里面是软的……好像刚烤熟的灰石头。{/cps}{w=0.25}{nw}"
    else:
        tomori kya "{cps=*1.5}……好酸！可是好烫！爱音，舌头要烫卷了——{/cps}{w=0.25}{nw}"

    show anon hosp 01 smug at right_standee, standee_jump
    anon "{cps=*1.7}哈哈哈哈哪有人形容炸薯条像灰石头的啦！烫到就哈气嘛哈气！{/cps}{w=0.2}{nw}"
    tomori smile "{cps=*1.7}呼——呼……可是，真的有土豆的香味。{/cps}{w=0.18}{nw}"
    show anon hosp 03 curious_3 at right_standee
    anon "{cps=*1.85}对吧对吧！那再试一根！不对——刚刚那根最长的明明是本小姐先看中的！{/cps}{w=0.15}{nw}"
    tomori ah "{cps=*1.9}啊，已经拿起来了……{/cps}{w=0.12}{nw}"
    anon "{cps=*2.0}喂！高松灯你这家伙居然会抢吃的了——{/cps}{w=0.1}{nw}"

    # 峰值一刀全断：DDLC 心理恐怖式切入（零渐弱、零过渡、瞬间失温）
    stop music
    stop bgs
    stop sound
    scene bg restaurant_01_blue
    show anon hosp 03 curious_2 at unfocus_standee_right
    show taki 01 glare at standee_duo_init_left, focus_standee_left(0.0)
    play sound sfx_strike volume 0.55

    taki "……灯？"

    $ renpy.pause(0.8, hard=True)
    play music bgm_at_the_sea fadein 1.5 loop
    play bgs bgs_restaurant fadein 2.0 loop volume 0.5

    "周围的嘈杂像是悬停了一下。{w=0.15}{nw}"
    extend "\n刀叉碰撞的声音、小孩子的哭闹声、服务员传菜的呼喊声，全都退到了很远的地方，却又依然喧闹地存在着。"
    "她手里端着一只灰色的塑料托盘。{w=0.15}{nw}"
    play sound sfx_cutlery_clink volume 0.7
    extend "\n托盘上放着一碗白色的杏仁豆腐，还有一罐印着黑白大熊猫图案的巧克力饮料。"

    tomori kya "……立希。"

    play sound sfx_clothes_rustle
    "我有些慌张地指了指对面的千早爱音，手指捏紧了膝盖上的纸餐巾。"

    tomori sadaway "那个……这是千早爱音同学。{w=0.15}{nw}"
    extend calm "\n爱音……这是立希……"

    show taki 02 normal_1 at focus_standee_left
    taki "我知道。同班的？{w=0.15}{nw}"
    extend "\n不对，在琴行还是哪里……"

    "立希冷淡地扫了爱音一眼，又看回卡座上那只圆滚滚的企鹅玩偶上，眉头习惯性地蹙起，但很快又移回到了我的脸上。{w=0.15}{nw}"
    extend "\n她端着托盘站在桌边，没有走，也没有坐下。"

    show anon hosp 07 normal_1 at focus_standee_right
    show taki 02 normal_1 at unfocus_standee_left
    anon "原来你们认识呀？要一起坐吗？"

    "爱音咬着叉子，好奇地看着她。{w=0.15}{nw}"
    extend "\n立希没有回答爱音。她只是看着我。"

    show taki 02 normal_2 at focus_standee_left
    show anon hosp 07 normal_2 at unfocus_standee_right
    taki "那之后……你还好吗？"

    tomori sadaway "对不起。"

    show taki 01 glare at standee_left_press
    taki "为什么是你道歉？{w=0.15}{nw}"
    extend "\n那天在练习室，说了重话的人是我。擅自发火的人也是我。"

    tomori bitter "不是的。是我没有唱好。{w=0.15}{nw}"
    extend sadaway "是我总是让大家……"

    show taki 02 normal_2 at focus_standee_left
    taki "你没有。{w=0.15}{nw}"
    show taki 03 sad at focus_standee_left
    extend "\n灯从来都没有错。错的是……算了。"

    "立希忽然盯住我搭在桌沿的右手腕上——{w=0.2}{nw}"
    extend "\n宽大的防风夹克袖口往上滑了一截，露出了底下还没有剪掉的医院塑料手环，还有里头条纹病号服的领口。"

    play sound sfx_table_slam
    show taki 01 glare at standee_left_press, standee_shake_h
    taki "{cps=*1.5}……你这手环是怎么回事？{/cps}{w=0.15}{nw}"
    extend "\n{cps=*1.6}你不是应该还在五楼住院吗？！{/cps}" with shake_h

    play sound sfx_clothes_rustle
    "立希脸一沉，一把搁下托盘，伸手就要来抓我的手腕。{w=0.15}{nw}"
    show anon hosp 02 boast at standee_right_burst
    show taki 01 glare at unfocus_standee_left
    extend "\n爱音眼疾手快地一步跨到桌前，抓起卡座上的小企鹅玩偶塞进我怀里，把我的手挡在身后，笑嘻嘻地打断她："

    anon "{cps=*1.6}哎呀，那是刚才三楼游乐场套票送的入场手环啦！{/cps}{w=0.1}{nw}"
    show anon hosp 03 curious_1 at focus_standee_right
    extend "\n{cps=*1.5}等等，你们刚才在说什么呀？什么练习室？什么道歉？{/cps}"

    "没有人向爱音解释。"

    show taki 02 normal_2 at focus_standee_left
    show anon hosp 07 normal_2 at unfocus_standee_right
    taki "我那时候……我只是想让你继续唱下去。{w=0.15}{nw}"
    show taki 03 sad at focus_standee_left
    extend "\n不管别人怎么说。"

    tomori soft "我知道。{w=0.15}{nw}"
    extend calm "对不起，立希。{w=0.15}{nw}"
    extend smile "但是谢谢你。"

    show taki 02 normal_2 at focus_standee_left
    taki "所以说了不用道歉啊。{w=0.15}{nw}"
    show taki 02 normal_1 at focus_standee_left
    extend "\n……你看起来比之前精神一点了。"

    tomori smile "嗯。刚才……我们抓到了这只企鹅。"

    show taki 01 glare at focus_standee_left
    taki "哈？企鹅？"

    show anon hosp 01 smug at focus_standee_right
    show taki 02 normal_1 at unfocus_standee_left
    anon "{cps=*1.5}是三楼的那个娃娃机啦！灯超级厉害的哦，最后拍下按键的时候——{/cps}"

    "她们开始说话了。{w=0.15}{nw}"
    extend "\n准确地说，是爱音在说，立希皱着眉头偶尔冷淡地回敬一两句。"
    tomori calm "立希离我远着呢。{w=0.15}{nw}"
    extend bitter "\n就像我小时候掉进水池里，眼前漆黑一片，不管怎么挣扎，什么也抓不住。那时候岸上的人，不知道在什么遥远的地方。"
    tomori sadaway "练习室也好，祥子也好，现在我想起来，反倒难过。{w=0.15}{nw}"
    extend calm "\n我们俩都是无辜之人。只是我现在已经时日无多了。"
    "立希最后还是没有坐下。{w=0.15}{nw}"
    extend "\n她端着她的杏仁豆腐和熊猫饮料走了，走之前对我说了一句话。"

    show taki 02 normal_1 at focus_standee_left
    taki "在学校遇到的话，打个招呼也没关系。"

    tomori soft "……嗯。"

    play sound sfx_footsteps
    hide taki with dissolve
    show anon hosp 07 normal_1 at center_standee with dissolve
    "我点点头。{w=0.15}{nw}"
    extend "什么都没有解决。"
    tomori soft "我又感到幸福。{w=0.15}{nw}"
    extend smile "这真是不可思议。"
    tomori calm "明明时间还在从地板缝里往上漫，明明那个致命的日子还在前面的某处等着我。{w=0.15}{nw}"
    extend bitter "\n我还是那个不会呼吸的怪物，还是那个连一句完整的道歉都说不明白的人。"
    tomori soft "但我刚才抓到了一只企鹅。{w=0.15}{nw}"
    extend soft "\n我喝到了热牛奶。{w=0.15}{nw}"
    extend smile "我把爱音介绍给了立希。"
    tomori calm "哪怕明天就要迎来休止符。{w=0.15}{nw}"
    extend soft "\n我热爱生活，哪怕它已经到了这个份上。"
    tomori calm "很好，我找到合适的词了。{w=0.15}{nw}"
    extend soft "\n热牛奶。红色的按钮。塑料桌布。{w=0.15}{nw}"
    extend smile "\n这毫无意义，但最终，我们相信了。{w=0.15}{nw}"
    extend soft "\n别管我。让我再在这个梦里多走几步。"

    # ==========================================
    # 5. 奔过斑马线
    # ==========================================
    stop bgs fadeout 1.2
    scene bg city_02_orange with dissolve
    play bgs bgs_crosswalk fadein 1.5 loop
    play sound sfx_footsteps

    tomori calm "快来。绿灯亮了。{w=0.15}{nw}"
    extend soft "我们过马路吧。"

    show anon hosp 02 boast at center_standee, standee_jump with dissolve
    anon "{cps=*1.6}小灯，快跟上！绿灯只有二十秒啦！{/cps}"

    tomori smile "……来了。"

    scene bg road_01_orange with flash_warm
    show anon hosp 08 gentle at center_standee, standee_step_in with dissolve
    play sound sfx_running_corridor
    "她转过身，抓住我的手。"
    tomori calm "快来，好走得更快。{w=0.15}{nw}"
    extend soft "快。就这样。快。{w=0.15}{nw}"
    extend smile "\n我们一起跑过了白色的斑马线。"

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    scene bg black with slow_dissolve

    $ persistent.cleared_chapter_8 = True
    jump ch09_haruhikage
