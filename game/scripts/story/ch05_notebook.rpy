## ch05_notebook.rpy - 第五章：活动室里的残缺笔记本
## 严格对标《规范文件.md》视觉素材规范与 11111.docx 对象修订终盘定稿
## 背景规范：hospital_interior_01_blue / corridor_01_blue / hospital_exterior_01_orange / cg starry_sky / cg closeup rooftop
## 立绘规范：anon hosp 01~10 规范病房立绘
## 主视角 Side Image 头像差分系统：高频切换 + extend 句子内微表情拆分

label ch05_notebook:
    $ current_chapter = 5
    $ quick_menu = True

    # 医院活动室，雨后黄昏（hospital_interior_01_blue）
    scene bg hospital_interior_01_blue with fade
    play bgs bgs_hospital fadein 2.0 loop
    play music autumn fadein 2.0 loop

    # 镜头微距沉浸运镜，聚焦窗前沉思
    camera:
        pos (0.5, 0.52) zoom 1.03
        warp ease_in_out_sine 8.0 pos (0.5, 0.49) zoom 1.0

    # NVL 全屏文学模式（vn_white）搭配静谧留白演出
    nvl clear
    vn_white "我很庆幸。{w=0.4}我很幸运。"
    vn_white "因为我知道，{w=0.4}那个总是踩着塑料拖鞋、大呼小叫的女孩，{w=0.4}随时都会推开这扇门。"
    vn_white "我会看到她粉色的头发，{w=0.3}我会看到她今天给我准备的礼物。"
    vn_white "哦对了，{w=0.3}我应该拿些什么东西来着……"
    vn_white "我从病号服的口袋里掏出了那本活页本。"
    vn_white "之前，{w=0.3}首先是一本精装日记本。"
    vn_white "这纸质真好，{w=0.3}甚至还有个让我写名字的扉页。"
    vn_white "扉页之后的那一页被我用力撕掉了，{w=0.4}留下参差不齐的毛边。"
    play sound sfx_pencil_write volume 0.75
    vn_white "我用铅笔在上面重重写下了那些句子。"
    vn_white "写下关于黑色的暴风雨，{w=0.4}那场雨你可能永远也遭遇不上……"
    nvl clear
    vn_white "这样想来，{w=0.3}如果你永远都不能和我感同身受的话，{w=0.4}那些文字还真的存在意义吗？"
    vn_white "或许你会讲，{w=0.3}文学本身的存在就是意义了！{w=0.5}就像我也会觉得爱音本身的存在就拥有十足的意义，{w=0.3}不需要解释。"
    vn_white "我是不是跑题了？{w=0.4}抱歉，{w=0.3}我不是故意一直要把话题往她的方向拐的……"
    vn_white "主要问题是，{w=0.3}我不知道自己为什么要写这些，{w=0.4}我的痛苦显得如此微不足道，{w=0.3}甚至有点娇气。"
    vn_white "我的文字如此无力，{w=0.3}我的歌声依旧含糊不清。"
    vn_white "我自己写着开心嘛，{w=0.4}也许我只是想给自己的残缺找一个可以安放的角落。"
    vn_white "可是无名的痛苦又怎样可以言说呢？"
    vn_white "我在寻找惟一一个词上面临的困难似乎是无法逾越的。"
    vn_white "如果我在生活中沉默不语，{w=0.4}那是因为在闪电打下来那会儿我相信这个词可能存在。{w=0.4}由于它现在不存在，{w=0.3}我就沉默着。"
    vn_white "这会是一个缺词，{w=0.3}一个空词，{w=0.4}在这个词中间掘了一个窟窿，{w=0.4}在这个窟窿中所有其他的词会被埋葬。"
    vn_white "也许不会说出它来，{w=0.4}但却可以让它响起来。"
    nvl clear

    camera at default

    # 爱音推门找到活动室
    play sound sfx_door_slide
    show anon hosp 08 gentle at anon_door
    $ renpy.pause(0.65, hard=True)
    play music banter fadein 0.5 loop
    anon "找到你啦，{w=0.4}高松同学！" with standee_shake_h

    tomori calm "爱音手里攥着一盒插着吸管的橙汁，大步流星地走过来，在我对面的单人沙发上坐下。"
    show anon hosp 07 normal_1 at anon_sit

    anon "你一个人在这里坐了多久啦……？{w=0.4}"

    tomori calm "……{w=0.4}不知道。{w=0.1}{nw}"
    extend neutral "从下午开始。"

    show anon hosp 03 curious_1 at anon_sit, standee_shake_h
    anon "哈？！一直坐着？{w=0.4}晚上，还有星期天，你平时在这里都做些什么呢？"

    tomori sadaway "我发呆……{w=0.4}睡觉……{w=0.4}我也不太清楚。{w=0.1}{nw}"
    extend calm "我有时间，{w=0.4}太长了。"

    tomori soft "她把橙汁放在玻璃茶几上，探着身子看向我膝盖上的本子。"

    show anon hosp 08 gentle at anon_sit
    anon "还在看这个本子啊？"
    extend " 借我再瞧瞧嘛……{w=0.4}"

    play music banter loop

    tomori calm "……{w=0.4}这是立希给我的。{w=0.1}{nw}"
    extend neutral "以前在乐队里的时候写歌用的……{w=0.4}"

    show anon hosp 03 curious_1
    anon "立希？就是昨天你跟我提过的那个鼓手……？{w=0.4}"

    tomori soft "……{w=0.4}嗯。立希其实人很好。"

    show anon hosp 07 normal_2
    anon "你们以前在乐队里的时候，{w=0.4}她也是一直守在你旁边的吗？"

    tomori calm "……{w=0.4}嗯。{w=0.1}{nw}"
    extend neutral "那天在排练室里，整整一个下午，她也一直在那儿，在我身边。"

    show anon hosp 03 curious_1
    anon "散伙的那天……？{w=0.4}"

    tomori sad "乐队停止了演奏。一曲终了。大家缓缓退出房间。{w=0.1}{nw}"
    extend sadaway "当时我甚至没有注意到演奏已经停止了。{w=0.4}我还在等待下一首曲子开始，可她们已经把乐器封闭在阴郁的琴盒里，一个一个地从我面前走过。{w=0.1}{nw}"
    extend calm "立希来看我的时候，我问过她：‘你会觉得和我搞乐队是开心的事情吗？告诉我，立希，我从来也不知道。’{w=0.1}{nw}"
    extend sadaway "以及那个本子写得很乱。要是看不懂也没关系的。"

    play music banter loop

    show anon hosp 01 smug at anon_sit
    anon "切……{w=0.4}怎么会看不懂！"
    show anon hosp 02 boast at anon_sit, standee_shake_h
    anon "行啦……{w=0.4}让我来看看未来的主唱大人到底写了什么传世名作！"
    show anon hosp 03 curious_1 at anon_sit
    anon "咦？{w=0.4}后面全都是空的啊？"

    tomori calm "……{w=0.4}嗯。因为……{w=0.4}写不出来了。{w=0.1}{nw}"
    extend sadaway "那天从排练室跑出来以后，脑子里就空掉了。{w=0.4}无论怎么想，都觉得后面再也不会有任何新的东西了。"

    show anon hosp 07 normal_1
    anon "为什么会空掉啊……？{w=0.4}"
    extend " 之前的乐队解散了，{w=0.4}再写新的不就好了吗？"

    stop music fadeout 0.8

    voice "audio/voice/vo_tomori_05_01.ogg"
    tomori sadaway "写不出来的……{w=0.4}我……{w=0.4}我根本不是能好好传达心意的人。{w=0.1}{nw}"
    extend bitter "连普通的对话都做不好，{w=0.3}只会把大家弄得痛苦……{w=0.1}{nw}"
    extend sad "以前大家在一起演奏的时候，{w=0.4}我以为自己终于抓住了什么。{w=0.1}{nw}"
    extend calm "……{w=0.4}我没有哭。{w=0.3}痛苦了吗？{w=0.3}我从来也不知道。{w=0.4}我不知道。{w=0.3}我不知道自己是否还在想着她们。{w=0.1}{nw}"
    extend sadaway "她们把乐谱拿走了，{w=0.4}就像把我的房子拆毁了一样。{w=0.5}人走后应该把房子拆毁，{w=0.3}有人就是这么做的。"

    show anon hosp 02 boast at anon_sit, standee_shake_h
    anon "拆掉就拆掉嘛！{w=0.4}旧的不去新的不来，我们可以盖一座更大的！"

    play sound sfx_page_turn
    tomori soft "爱音低头看着摊开的活页本。那些被划掉的横线、凌乱的标点。"

    show anon hosp 08 gentle at anon_lean_in
    anon "拜托了……{w=0.4}高松同学。"

    tomori soft "爱音把本子抱在胸前，眼睛直直地看着我。"

    play music vulnerable fadein 1.5 loop 

    show anon hosp 09 confess
    anon "我想和你两个人一起把最后一页写满。{w=0.4}我想和你两个人一起完成它。"

    tomori ah "……{w=0.4}哎？和我两个人……？{w=0.4}"

    show anon hosp 02 boast at anon_sit, standee_shake_h
    anon "对啊！{w=0.4}你看，这本本子后面还有这么多空页，空着多浪费啊！"

    tomori sadaway "但是……{w=0.4}我只会写这些乱七八糟的碎片……{w=0.1}{nw}"
    extend babble "字也写得很乱……{w=0.4}我也不会写吉他谱……{w=0.1}{nw}"
    extend uff "唱歌的时候，声音也经常发抖……{w=0.4}"

    show anon hosp 08 gentle at anon_sit
    anon "那又有什么关系嘛……{w=0.4}"

    tomori concern "为什么……{w=0.4}偏偏是我？"

    show anon hosp 01 smug at anon_sit
    anon "因为我选择了你呀……{w=0.4}"

    tomori calm "……{w=0.4}你一点也不了解我。"

    show anon hosp 02 boast at anon_sit, standee_shake_h
    anon "对你不了解，{w=0.4}不就已经是在了解你了吗！"

    tomori neutral "……{w=0.4}这种说法，我还是第一次听说。"

    show anon hosp 08 gentle
    anon "喂……{w=0.4}高松同学！"
    extend "
既然词都写得这么完整了，{w=0.4}你平时肯定自己试着哼过旋律吧？"
    show anon hosp 02 boast
    extend "
快！{w=0.4}现在就唱一句给我听听！"

    tomori ehh "……{w=0.4}欸？{w=0.1}{nw}"
    extend concern "唱、唱出来……？{w=0.4}"

    show anon hosp 08 gentle
    anon "对啊……{w=0.4}"
    extend "
反正活动室现在又没有别人，{w=0.4}护士站离这里隔着大半个走廊呢！"
    extend "
就唱两句！{w=0.4}如果不愿意的话，一句也可以的。"

    tomori uff "不……{w=0.4}不行的！"

    show anon hosp 01 smug at anon_sit
    anon "好啦好啦……{w=0.4}不唱就不唱嘛！"
    extend "
干嘛一副天都要塌下来的样子啊，{w=0.4}我又没有逼你上刑场！"

    tomori concern "那个……{w=0.4}爱音……{w=0.4}不生气吗？"

    show anon hosp 04 shy_1 at anon_sit, standee_shake_h
    anon "哈……{w=0.4}我生什么气啊，搞得好像我在欺负病人一样……{w=0.4}"

    show anon hosp 08 gentle at anon_lean_in
    anon "喏……{w=0.4}分你一半。既然你不唱，那就听听我的吧。"
    $ renpy.pause(0.5, hard=True)

    play sound sfx_earphone_plug
    tomori soft "我停了一下，伸手接过来，把那枚塑料耳塞放进右耳。她按亮手机屏幕，点开了一个绿色的图标。"

    # 播放白噪音音效
    play bgs bgs_white_noise fadein 1.5 loop
    play music dreams fadein 1.5 loop 

    tomori ehh "……{w=0.4}下雨了？"

    tomori calm "我转过头看向窗外。窗外的天色干涩，没有雨。"

    show anon hosp 08 gentle
    anon "不是外面啦……{w=0.4}是手机里录下来的声音。"
    extend "
雨打在窗户上的声音，还有海水退下去的声音。"
    show anon hosp 07 normal_2
    extend "
以前在国外住的时候，窗外整天都是这种动静。刚开始听着觉得烦，后来发现，只要耳朵里塞满这种声音，就不用去听别人都在聊些什么了。"

    show anon hosp 01 smug at anon_lean_in
    anon "怎么样……{w=0.4}把外面的声音全盖过去了吧？"

    tomori soft "……{w=0.4}嗯。真的听不见了。"

    show anon hosp 08 gentle at anon_sit
    anon "对吧？{w=0.4}"
    extend "
喂……{w=0.4}高松同学，要不要去个更好的地方？"

    tomori ehh "更好的地方……？{w=0.4}"

    show anon hosp 01 smug at anon_sit, standee_shake_h
    anon "秘密基地！{w=0.4}跟我来就是了！"

    # 离开活动室，两人被耳机线牵引着走在昏暗走廊中（corridor_01_blue）
    scene bg corridor_01_blue with push_right
    play sound sfx_footsteps

    tomori soft "我们一前一后走出了活动室。耳机线把我们拴在了一起，不能走得更快，也不能放慢脚步。{w=0.1}{nw}"
    extend calm "如果她停下来，我也停下来。有一次她停的时间有些长，我就安静地等着她。{w=0.1}{nw}"
    extend smile "她假装在领我走，我猜测，实际上她也不知道走廊那头通向哪里。"

    tomori neutral "……{w=0.4}我们向哪边走？"

    "她做了番努力，看了看我们刚走过的昏暗走廊的另一侧，但她没有指明。"

    show anon hosp 08 gentle at anon_wander
    anon "也就是说……{w=0.4}往高处走！"

    tomori concern "你在这里找什么东西吗？"

    show anon hosp 01 smug at anon_wander
    anon "切……{w=0.4}什么也不找。"

    tomori ehh "什么也不找……？{w=0.4}"

    show anon hosp 02 boast at anon_wander, standee_shake_h
    anon "对啊……{w=0.4}要是带着目的去找，那就不叫探险了吧！"

    tomori smile "她开始笑，我也跟着她笑，哪怕她并没有看见。到每一个楼梯的拐弯处，她都继续前行，不多不少，就像风遇到田野才刮起一样。"

    "综合医院六楼通往天台的消防铁门前。爱音手里攥着一根不知道从哪里捡来的细发卡，在门锁孔里来回拨弄着。"

    # 细发卡撬锁与重型铁门开启
    play ambient_sfx sfx_lock_pick
    $ renpy.pause(0.8, hard=True)
    play sound sfx_metal_door_open
    stop bgs fadeout 0.8
    play bgs bgs_rooftop_wind fadein 1.5 loop
    $ renpy.pause(0.8, hard=True)

    # 推门走上天台，黄昏金红晚霞扑面而来（hospital_exterior_01_orange）
    scene bg hospital_exterior_01_orange with dissolve
    camera:
        blur 14.0
        warp ease_out_cubic 2.0 blur 0.0
    play music happy fadein 2.0 loop
    $ renpy.pause(2.0, hard=True)

    show anon hosp 02 boast at anon_wander
    anon "搞定！{w=0.4}我就说这扇门的锁早就生锈松动了！"

    show anon hosp 08 gentle at anon_center
    anon "快上来呀……{w=0.4}高松同学！这里的视野超级棒的！"

    tomori ah "……{w=0.4}天台。"

    tomori soft "爱音踩着塑料拖鞋快步跑到了天台的铁丝防护网前，回过头朝我招手。"

    # NVL 全屏模式（vn_white）搭配倒流黑色雪花粒子特效
    show snow_black_reverse with dissolve
    camera:
        warp ease_in_out_sine 14.0 pos (0.5, 0.46) zoom 1.05
    nvl clear
    vn_white "闪闪发光。"
    vn_white "我现在大概明白爱音为什么执着于站在舞台最中间了，那不仅是虚荣，也是像我们这样的人唯一得以安身的地方。"
    vn_white "的确，有的人只有在远离人群的高处才觉得自如。"
    vn_white "在日常细节上，她都渴望登高望远：喜欢开阔的天台而不喜欢幽闭的单人病房，喜欢刺目的聚光灯而不喜欢角落里的阴影。"
    vn_white "讨厌逼仄的通道、沉闷的地下室以及深不见底的泥沼。"
    vn_white "她是吉他手，需要空间，若能站在四楼天台的铁丝网旁，远眺被落日染成金红色的街景，呼吸才会变得酣畅起来。"
    vn_white "尤其是当我们并肩站立在芸芸众生可望而不可即的高处，俯瞰着街道上蝼蚁般来去匆匆的人群，一种得救的安宁便在心头升起。"
    vn_white "所有的誓言与奇迹，似乎都只有在耀眼的高处才能被点燃。"
    vn_white "我们之所以拼命想要爬上最高峰，大声宣告着要组建轰动全校的乐队，不过是为了站得足够高，好让底下的人再也无法轻易审判我们的残缺。"
    nvl clear
    vn_white "对有些人来说，星空不可知是命运将我们与当下缝合的方式。"
    vn_white "对另一些人来说，这是惩罚的标记，是我们在此的整个存在最好被理解为一个缺陷或错误的确凿证据。"
    vn_white "对我来说，两者皆不是。这只是我们存在的方式。"
    vn_white "这场坠落是幸或不幸，大概更隶属于心境的问题，而不是其他问题。"
    vn_white "这样想就一切都清晰明了。"
    vn_white "你得站在那里，别为这个事实过于烦恼。"
    vn_white "很小的时候，有人带我去看旱季的黑夜。她要我好好看这天空，它在黑夜与白天一样碧蓝，看这明晃晃的大地，一直看到它的尽头。"
    vn_white "还要我仔细聆听黑夜的响声，人们的呼唤，以及同受死亡困扰的犬类哀怨的吠声，倾听所有这些同时诉说难以承受的孤独、和诉说这份孤独的歌声。"
    vn_white "人们通常对孩子们隐瞒的东西，相反应该告诉他们，如离别，不公正，孤独，死亡。"
    vn_white "我常要求大人们解释，这么说是什么意思。得到的回答总是不知道，谁也不知道。"
    vn_white "而且我们必须首先知道这一点：我们一无所知。身边这个对天空一无所知的女孩，反而比任何自以为无所不知的大人都更接近真相。"
    nvl clear

    hide snow_black_reverse with dissolve
    camera at default

    show anon hosp 08 gentle at anon_center
    anon "好啦……{w=0.4}别愣在门口吹冷风啦！快过来！"

    tomori calm "……{w=0.4}铁丝网很薄。"

    tomori soft "爱音回到我身边，拉着我挪到了那堵绿色的菱形防护网前。"

    show anon hosp 02 boast at anon_lean_in
    anon "你看……{w=0.4}这里有这么高、这么结实的铁丝网挡着呢，绝对掉不下去的！"

    tomori smile "……{w=0.4}好高。"

    tomori soft "爱音双手抓住铁丝网的网格，把脸贴在上面，两只眼睛倒映着天边燃烧的晚霞。"

    show anon hosp 08 gentle at anon_center
    anon "高才好啊……{w=0.4}"
    show anon hosp 02 boast
    extend "
站在最高的地方，{w=0.4}就能把所有讨厌的东西都踩在脚下了！"

    tomori neutral "……{w=0.4}踩在脚下？"

    tomori soft "爱音转过头看着我，风把她的刘海吹得凌乱不堪。"

    show anon hosp 08 gentle
    anon "对啊！{w=0.4}等我们出院了，组一个全新的乐队吧！"
    show anon hosp 02 boast
    extend "
我要去买一把最耀眼的粉红色电吉他……{w=0.4}"

    tomori soft "爱音整个人趴在铁丝网上，对着下方辽阔的城市大声描绘着她的宏图伟业。风把她的话语吹得七零八落，但她依然喊得极其卖力。"

    show anon hosp 08 gentle
    anon "我们要站在最华丽的舞台上，{w=0.4}聚光灯啪的一下打在我们身上！"

    tomori concern "……{w=0.4}台下会有人听吗？"

    show anon hosp 03 curious_1 at standee_shake_h
    anon "台下全都是为我们欢呼的观……{w=0.4}呃……{w=0.4}唔……！{w=0.4}" with shake_h

    $ renpy.music.set_pause(True, channel="music")
    $ renpy.pause(0.5, hard=True)

    tomori concern "爱音……？{w=0.4}{nw}"
    extend uff "\n你怎么了？{w=0.4}哪里不舒服吗？"

    show anon hosp 06 pain at standee_shake_h
    anon "没、没事……{w=0.4}呼……{w=0.4}就是突然抽筋了一下……{w=0.4}"

    tomori concern "我们快回去吧……！{w=0.4}"

    show anon hosp 05 annoyed_1
    anon "不要！{w=0.4}别去叫医生！"

    tomori concern "可是爱音的脸很难看……{w=0.4}"

    show anon hosp 04 shy_1
    anon "……{w=0.4}其实……{w=0.4}"
    tomori concern "她的声音在发颤。"

    tomori soft "……{w=0.4}爱音？"

    $ renpy.music.set_pause(False, channel="music")

    show anon hosp 10 tears at standee_shake_h
    anon "切……{w=0.4}才没哭呢！是天台的风太大了！"
    show anon hosp 08 gentle
    anon "喂……{w=0.4}高松同学！冲着下面大喊吧！"

    tomori soft "爱音把两只手拢在嘴边，做成喇叭的形状，她深吸了一大口气，把胸腔里的冷空气全部压进喉咙里。下一秒，一声极其响亮、带着一点破音的大喊划破了高空。"

    show anon hosp 10 tears at anon_center, standee_shake_h
    anon "{size=*1.25}伦敦的鬼天气去死吧————！虚荣心去死吧————！千早爱音才不会认输呢————！{/size}" with shake_h
    $ renpy.pause(1.0, hard=True)

    tomori ah "……！{w=0.4}"

    show anon hosp 08 gentle at anon_center
    anon "来……{w=0.4}轮到你了，高松同学！"

    stop music fadeout 1.2
    scene bg black with cut_white_fade
    $ renpy.pause(0.8, hard=True)

    # 视线重新聚焦，字重与情感迸发
    play music work fadein 2.5 loop
    scene bg hospital_exterior_01_orange with cut_black_fade
    camera:
        blur 10.0
        warp ease_out_cubic 1.8 blur 0.0
    $ renpy.pause(1.8, hard=True)

    tomori sadaway "在排练室里扯破乐谱的声音折磨着我直到今天。我心里清楚，那声求救还会在走廊和病房的每一个角落等着我，只要我依然活着。{w=0.1}{nw}"
    extend calm "可是站在这高高的天台上，俯瞰着脚下沉在傍晚里的屋顶与街道，我忽然明白自己不能再永远躲在自责的泥沼里了。{w=0.1}{nw}"
    extend soft "晚风中回荡的难道不是自己压抑太久的呼救吗？它催促着我做点什么。是啊，做点什么，还趁现在有大把的时间。{w=0.1}{nw}"
    extend calm "没有任何坚硬的物质把我们同其他人分隔开来。他们，他们不知道我们的存在。而我们，我们却可以觉察到他们的某些东西，听到他们全部的声音，看出他们的一些踪影。{w=0.1}{nw}"
    extend yay "于是我探出身子，朝着铁丝网下方的城市大声喊了出来——"

    play sound sfx_heartbeat
    camera:
        warp ease_in_out_cubic 0.8 pos (0.5, 0.45) zoom 1.06
    tomori yay "{size=*1.35}我想……{w=0.4}成为人类————！我想和爱音组乐队————！{/size}" with shake_h
    $ renpy.pause(1.2, hard=True)
    camera:
        warp ease_in_out_cubic 0.8 pos (0.5, 0.5) zoom 1.0

    tomori soft "我感受到，所有的房子似乎都变亮了。甚至连房子本来的灰色、黄色、灰绿色也都顿失其原有的阴郁。我看着她，人的心胸仿佛也豁然开朗，心灵似乎受到了震撼，或者就像有人用胳膊肘轻轻撞了你一下，使你产生新的观点和许多新想法……真是不可思议。{w=0.1}{nw}"
    extend calm "我扶着铁丝网打了个冷战，明白过来，我在这儿，我的声音在这儿，我的手还在这儿。{w=0.1}{nw}"
    extend soft "晚霞像软和的手指一样抚摸着我的后脑勺，身体又体验到了那种久违的感受——想融化在光里，投身于天空，让躯体消失，只留下一点能力，去感受身边这个人的温暖和呼吸。{w=0.1}{nw}"
    extend smile "当她的手伸过来拉住我的手时，我又一次在掌心里感觉到了她那只小巧、温暖的手的活力，手指寻觅着手指，手指交叉着手指。没什么办法，事情就这样发生了，就在天台的铁丝网旁。喜欢也好，害怕也好，全都一样，毫无办法，事情在那里发生了，真是不可思议。"

    tomori concern "糟糕……{w=0.4}两点半了，护士长该查房了。"

    show anon hosp 01 smug at standee_shake_h
    anon "切……{w=0.4}怕什么嘛！"

    tomori calm "我有些慌乱地想要转身朝消防门走去。爱音却一把拉住了我的手腕，用力把我拽了回来。"
    $ renpy.pause(0.5, hard=True)

    tomori concern "被抓到的话……{w=0.4}会被关禁闭的。"

    show anon hosp 08 gentle
    anon "回去又要被关在那个只能拉开一指宽细缝的小房间里，{w=0.4}多没劲啊！"

    tomori concern "可是时间已经到了……{w=0.4}"

    show anon hosp 01 smug at anon_sit
    anon "时间还早……{w=0.4}是医院的钟弄错了！"

    tomori calm "医院的钟……{w=0.4}不会错的。"

    show anon hosp 02 boast at anon_sit, standee_shake_h
    anon "行啦……{w=0.4}那就当成是夏令时弄错了！"
    extend "
总之……{w=0.4}在白日到来之前，谁也不准把我们分开！"

    tomori soft "爱音拉着我，背靠着天台的水泥矮墙坐了下来。她把我的双手塞进她宽大的开衫口袋里，两个人紧紧挨在一起取暖。"

    tomori neutral "那个……{w=0.4}那我们现在怎么办？"

    show anon hosp 08 gentle at anon_sit
    anon "既然都逃上来了，{w=0.4}不如就在这里看星星吧！"

    tomori calm "爱音抬起头，手指指向渐渐暗下来的深蓝色天穹。晚霞已经彻底褪去，天边升起了第一颗明亮而清冽的暮星。"

    show anon hosp 02 boast at anon_sit, standee_shake_h
    anon "对啊！{w=0.4}你看，第一颗星星已经出来了！"

    tomori soft "……{w=0.4}很亮。"

    tomori calm "天色完全暗了下来，天空变成了一片幽暗的深蓝色。"

    # 夜幕彻底降临，漫天星斗显现
    scene bg cloud_01_blue with Dissolve(2.0)
    camera:
        warp ease_in_out_cubic 2.5 zoom 1.05 pos (0.5, 0.47)
    play music the_dream fadein 2.0 loop
    $ renpy.pause(2.5, hard=True)

    tomori calm "铁丝网外面，城市的灯火与星光漫成一片，天地间浮着望不到头的微光。脚底下的重力好像一点点漏光了，让人觉得只要再往前迈出一步，整个人就会轻飘飘地坠进夜空里去。{w=0.2}{nw}"
    extend neutral "世界没有了景深，也没有了上下之分。盯得久了，那些亮光就像水潭里的颜料一样融化、漫出来，把远方群山的边缘蚀出一道珍珠白的亮圈……近得像是只要半步就能碰到。{w=0.3}{nw}"
    extend concern "只要半步。可是，如果真的迈出这半步的话……不，我得把心思从那道边缘上拉回来。{w=0.2}{nw}"
    extend sadaway "重不重蹈覆辙倒是小事，只是在喜欢的人面前死掉，无论如何都是太糟糕、太糟糕的事情了。{w=0.2}{nw}"
    extend calm "就拿这个理由劝自己吧。虽说去想象她流泪的样子并不让人讨厌——东京的夜色也未必就比伦敦好过多少——可坏就坏在，真到了那时候，我连看她一眼都做不到了。{w=0.3}{nw}"
    extend babble "我已经往那条河里跌过一次了，总不能老是踏进同一条河流里去……除非，是和喜欢蹚水的人一起。爱音会喜欢水吗？我是很喜欢的，假以时日，倒是很想牵着她一起去试试看。{w=0.2}{nw}"
    extend ehh "不过眼下还有更叫人在意的事——她对头顶这片天空简直一无所知。明明我们一直站在同一块夜空下面，她却像个刚刚搬来这里的陌生人。{w=0.2}{nw}"
    extend babble "一个对天空一无所知的女孩。哪怕是小孩子，也知道头顶上一直挂着太阳和月亮吧，她平时走路都不抬头看的吗？{w=0.2}{nw}"
    extend smile "又或者，她是昨天才刚刚降生、刚刚开始认识这个世界的呢……我真的一点也没法拒绝这个假设。只要这样想一想，就觉得她可爱得不得了。真的太可爱了，我的爱音。"

    tomori soft "高远夜空中的无数光点，仿佛静静落在了我们单薄的肩膀上。我慢慢抬起手臂，学着爱音的样子，慢慢朝着夜空伸开五指。哪怕踮起脚尖拼命伸手，也是不可能够得到那些遥远星辰的。伸出的指尖触碰到的只有初秋干燥的晚风。{w=0.1}{nw}"
    extend smile "但千早爱音依然仰着脸，一遍又一遍执拗地在虚空中虚握着手掌，试图把那些散落的光芒抓进掌心里。"

    show anon hosp 08 gentle
    anon "喂……{w=0.4}高松同学，你想要哪一颗星星？"
    extend "
要是让你选，{w=0.4}你想要哪一颗？"

    tomori calm "我……{w=0.4}{nw}"
    extend soft "我想要那一颗。{w=0.1}{nw}"
    extend calm "天顶附近，泛着白光、最亮的那一颗。"

    show anon hosp 02 boast
    anon "那一颗啊……！{w=0.4}"
    extend "
那我就要那条白白的、长长的带子……{w=0.4}"

    tomori ehh "……{w=0.4}为什么？"

    show anon hosp 08 gentle
    anon "你不觉得那条白色的光带很像刚刚出炉的长条奶油面包吗……？{w=0.4}"

    tomori calm "……{w=0.4}没有意见。{w=0.1}{nw}"
    extend neutral "刚才那一颗最亮的……是天琴座的织女星。{w=0.1}{nw}"
    extend calm "那是天鹰座的牛郎星。左边稍微靠后一点的那一颗，是天鹅座的天津四。{w=0.1}{nw}"
    extend soft "把这三颗连起来，在夜空里就成了一个三角形。叫作夏季大三角。"

    show anon hosp 02 boast at standee_shake_h
    anon "哇……！{w=0.4}真的连成三角形了！"

    tomori soft "爱音抱着膝盖在长椅边坐了下来，托着下巴看着头顶的星空。她明明连最基础的星座名字都叫不上来，却对这片夜空表现出了一种孩童般的热切与向往。{w=0.1}{nw}"
    extend smile "她仰着头的时候，眼睛里倒映着细碎的星光，整个人看起来毫无防备。这大概就是千早爱音的本质。她不关心那些深奥的宇宙规律，她只是单纯地向往一切明亮、耀眼、能够被人群注视的事物。为了得到这份注视，她愿意把整个天空都装扮进自己的梦想里。"

    show anon hosp 08 gentle
    anon "真好啊……{w=0.4}这里。"
    extend "
怎么就没早点发现这个天台呢……{w=0.4}"
    extend "
要是能一直这样坐在高处仰望星空就好了……{w=0.4}"

    tomori soft "那个……{w=0.4}爱音很喜欢星空吗？"

    # 切入天台依偎夜景特写，进入 NVL 诗意散文模式（vn_white）
    scene bg cloud_02_blue with dissolve
    play music spelunking fadein 2.0 loop
    $ renpy.pause(1.0, hard=True)

    nvl clear
    vn_white "黄昏退去，西边的晚霞原本还很明亮，但正渐渐变得暗淡，底下的街灯发着柔和的光亮。我和爱音并肩靠在天台的铁栏杆旁，远处的坡道和图书馆都在眼皮底下。"
    vn_white "在城市高楼的缝隙之间，可以瞥见地平线上泛起的薄暮。"
    vn_white "街道上行人稀少，夜市尚未喧闹起来，我们脚下踩着天台地面上残留的热气。"
    vn_white "有的人正进晚餐，而有的人准备休息。"
    vn_white "作息如此不同的两类人，就这样被马虎地分进同一个时区。"
    vn_white "天空渐渐布满繁星，若从一道微光望向另一道微光，便可瞥见它们在深蓝色的苍穹中映入眼帘的模样。"
    vn_white "我们正享受着病房喧扰之后的宁静，这清冽的夜色，以及渐显开阔的城市。"
    vn_white "我很满足。{w=0.4}真的。"
    nvl clear
    vn_white "我看见成群的白鸽。这些可爱的小动物终于下决心回落地面，它们以厚实洁白的羽毛遮掩着屋顶和水面，向着家家户户的玻璃窗翻飞扑打。"
    vn_white "到处都是啊！但愿它们带来好消息。"
    vn_white "果真如此，那么所有的人，不仅是出类拔萃者，都将得救！"
    vn_white "大家有福同享，有难同当。"
    nvl clear

    show anon hosp 08 gentle
    anon "好喜欢啊……！{w=0.4}"

    tomori soft "我想我没有必要补充“我也是”了。于是耐心等着爱音说完。"

    anon "因为不管你在下面过得有多狼狈，被别人怎样冷落……{w=0.4}"
    extend "
只要抬起头，这片天上的星星都一直都在那里闪闪发光，从来不会改变。"
    show anon hosp 07 normal_2
    anon "在英国的时候，{w=0.4}每当我一个人在公寓里难过得睡不着，就会推开窗户看天上的光点。"
    extend "
虽然伦敦老是下雨……{w=0.4}但偶尔放晴的夜晚，看到这些星星，就会觉得世界上还有别的东西在陪着我。"
    extend "
所以，在我练琴累了的时候，我会抬头看星星。"
    show anon hosp 08 gentle
    extend "
我不懂那些天文学之类的事情！不过如果它们都愿意当我的观众的话……"
    extend "
不也是……{w=0.4}我的福气吗！"

    tomori soft "她轻声说着这些话，声音里少见地没有了平时的浮夸与张扬。铁丝网外面的夜空安静地悬挂在头顶。上亿年前发出的微弱光芒穿透了漫长的时间与空间，落在我们两个人的身上。{w=0.1}{nw}"
    extend calm "天空确实没有改变。无论人世间经历了多少次破碎、解散与逃离，这片星空依然毫无改变地存在着。"

    show anon hosp 02 boast at standee_shake_h
    anon "等我们出院以后，不仅要组乐队，{w=0.4}还要一起去真正能看到满天星海的偏远海边！"
    extend "
到时候找一个最高的悬崖，{w=0.4}一边弹吉他一边把所有的星星看个够！"
    show anon hosp 08 gentle
    extend "
高松同学，你得陪我一起去哦……{w=0.4}"

    tomori soft "……{w=0.4}嗯。{w=0.1}{nw}"
    extend smile "我和爱音一起去……{w=0.4}"

    tomori sadaway "那个……{w=0.4}对不起。"

    show anon hosp 03 curious_1
    anon "嗯？{w=0.4}怎么了？"

    tomori sadaway "之前……{w=0.4}没有认识你。{w=0.1}{nw}"
    extend calm "我很抱歉……{w=0.4}"

    show anon hosp 08 gentle
    anon "哈……{w=0.4}说什么蠢话呢。"

    tomori sadaway "我知道……{w=0.4}可我还是很抱歉……{w=0.4}"

    anon "行啦……{w=0.4}这不是你的错。"

    tomori concern "那个……{w=0.4}如果那天我直接拒绝了你呢？让护士把你赶出去……{w=0.4}"

    show anon hosp 07 normal_1
    anon "干嘛这样问嘛……{w=0.4}"

    tomori sadaway "呃……{w=0.4}抱歉。"

    show anon hosp 01 smug
    anon "我会一直敲门吵你哦……{w=0.4}"
    extend "
到你来把我拉回病房。我的或者你的。"

    tomori calm "不会的……{w=0.4}我连站起来都很困难。{w=0.1}{nw}"
    extend sadaway "我会一直躺在床上，看着天花板。{w=0.1}{nw}"
    extend bitter "等明天下午的结果出来……{w=0.3}再被他们带到别的地方去。"

    show anon hosp 03 curious_1 at anon_lean_in
    anon "结果？{w=0.3}什么结果？"

    play sound sfx_paper_crinkle
    "我低下头，从病号服口袋里摸出那张被捏得发皱的粉色取报告凭条——{w=0.2}上面印着{font=fonts/ChillHuoSong_F_Bold.otf}【高松灯，明日16:30，主治医师诊室】{/font}。"
    tomori calm "明天下午四点半，{w=0.3}要去主治医生那里拿最终的评估单。{w=0.2}{nw}"
    extend bitter "\n所有人都觉得康复是一件好事，{w=0.3}可对我来说，康复就意味着必须重新回到父母叹气的眼皮底下，或者被送到更远的地方关起来……{w=0.2}{nw}"
    extend sadaway "\n我一点也不想去拿那张纸。"

    show anon hosp 07 normal_2 at standee_shake_h
    anon "你为什么总是在想这些丧气的事？{w=0.4}就为了这张小粉纸，从刚才起就一直垂头丧气的吗？"

    tomori calm "不……{w=0.4}你弄错了，不是这么回事。{w=0.2}{nw}"
    extend sadaway "\n我带着我的身体在走廊里走，可我一直不知道应该把它放在哪儿，才能让它停止抱怨。{w=0.2}{nw}"
    extend soft "\n我很长时间都没有把它放在它应该在的地方。{w=0.4}现在我觉得，我接近它会感到幸福的地方了……{w=0.2}{nw}"
    extend sadaway "\n所以我才害怕明天下午一到，又要从这里被赶出去。"

    play sound sfx_clothes_rustle
    show anon hosp 03 curious_2 at standee_step_in
    "爱音怔了一下，随即不由分说地伸出手，从我指间抽走了那张粉色的凭条，塞进她自己的口袋里。"

    show anon hosp 01 smug at standee_jump
    anon "{cps=*1.6}那就别去啦！{w=0.2}明天下午四点半是吧？这张评估单我替你去拿！{/cps}{w=0.1}{nw}"
    show anon hosp 02 boast at standee_nod
    extend "\n你就乖乖在病房里睡午觉，哪儿都不用去，等本小姐回来就行！"

    show anon hosp 04 shy_1 at standee_shake_h
    anon "{cps=*1.5}喂……{w=0.2}你突然之间在胡说八道些什么啊……{/cps}"

    tomori soft "我没有胡说。{w=0.4}千早同学使人产生活下去的愿望，你不觉得吗？"

    show anon hosp 03 curious_1 at standee_jump
    anon "{cps=*1.6}哈？！{w=0.2}我吗？{/cps}"

    tomori soft "嗯……{w=0.4}一看见你，我就想能把我的可憎之处给你，{w=0.1}{nw}"
    extend sadaway "因为我阴暗、是个只会给别人添麻烦的怪人，别人不会喜欢上我，{w=0.1}{nw}"
    extend smile "我想把它给你。"

    show anon hosp 08 gentle at standee_step_in
    anon "……{w=0.4}你已经给我啦。从你盯着我的草莓布丁发呆的时候就给我了。"

    play sound sfx_clothes_rustle
    tomori soft "我们一动不动地待着，我们的脸差不多碰到一起，一句话也不说，很长时间。远处干道上电车的声音融汇成一种喧嚣，我们听到了。我没有动，双唇微启，对她说："

    tomori soft "那个……{w=0.4}爱音。{w=0.1}{nw}"
    extend calm "刚才我不说话的时候……{w=0.4}脑子里其实什么都没有。{w=0.1}{nw}"
    extend sadaway "有时候就会变成那样。好像身体里的开关突然坏掉了，所有的感觉都会一下子散掉。{w=0.1}{nw}"
    extend calm "在那几分钟里，我甚至感觉不到自己喜欢你。哪怕你就坐在我旁边，我也突然感觉不到对你的好感。{w=0.1}{nw}"
    extend sadaway "什么感情都没有了。就连觉得爱音很好、很喜欢爱音这件事，也会突然感觉不到。……{w=0.4}你发现了吗？"

    show anon hosp 07 normal_2
    anon "发现了呀。你的眼一下子就跑远了，像在看一块不认识的石头。"

    tomori soft "然后我又重新开始呼吸。{w=0.1}{nw}"
    extend smile "一呼吸，就又喜欢你了。"

    show anon hosp 04 shy_1 at standee_shake_h
    anon "你这个人……{w=0.4}真是让人完全搞不懂啊！"

    tomori calm "如果以后我们死掉了……{w=0.4}棺材里会放着什么？"

    show anon hosp 03 curious_1 at standee_shake_h
    anon "哈？！{w=0.4}怎么又跳到棺材的话题去了？！"

    tomori calm "棺材里将有我们的乐队和尸体。{w=0.4}{nw}"
    extend soft "而棺材外面，要放着我们写满的笔记本。"

    show anon hosp 02 boast at standee_shake_h
    anon "噗……{w=0.4}那本子可得写厚一点才行，不然风一吹就跑了！"

    tomori soft "在我对海边的想象中……{w=0.4}我无法少了你。"

    show anon hosp 08 gentle
    anon "真的会去海边吗……？{w=0.4}"

    tomori smile "嗯……{w=0.4}真的会去。"

    anon "海边会很冷哦……{w=0.4}"

    tomori calm "我知道……{w=0.4}"

    show anon hosp 07 normal_2
    anon "而且坐慢车要好几个小时，{w=0.4}说不定到了那里，什么都不会发生。"

    tomori soft "我们走向某些东西。{w=0.4}即使什么都不发生，我们也是朝着某个目标前进。"

    show anon hosp 08 gentle
    anon "要是到了海边，{w=0.4}什么星星都看不到呢？"

    tomori calm "看着我的脸……{w=0.4}"

    show anon hosp 03 curious_1
    anon "欸？{w=0.4}看着呢，怎么了？"

    tomori soft "应该看得出来……{w=0.4}对我说：我们不能再退回那个小房间里去了。"

    show anon hosp 02 boast at standee_shake_h
    anon "看得出来！{w=0.4}我们绝对不能退回去！"

    tomori smile "你现在答应陪我去的，是一场别人都不要我去的旅行。{w=0.4}他们真蠢。"

    show anon hosp 01 smug at standee_shake_h
    anon "就是说啊……{w=0.4}他们什么都不懂！"

    tomori soft "那片海滩现在一定空无一人。海水很低，是平潮的时刻。大海终于涨潮的时候，海水会一块一块地淹没蓝色的沼泽。{w=0.1}{nw}"
    extend smile "我已经提前认出那片海了。我要和你待在一起，但要依我所愿。"

    play sound sfx_fence_rattle
    tomori calm "铁丝网发出轻微的撞击声。风从楼顶吹过去。{w=0.1}{nw}"
    extend soft "我们坐得很近，肩膀贴着肩膀。即使上面的光点隔着几亿年，我们谁也没有动。"

    camera:
        warp ease_in_out_cubic 2.5 pos (0.5, 0.46) zoom 1.04
    $ renpy.pause(2.5, hard=True)

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    camera at default
    scene black with slow_dissolve

    call editorial_part1

    $ persistent.cleared_chapter_5 = True
    jump ch06_verdict
