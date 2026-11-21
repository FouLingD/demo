## ch07_escape.rpy - 第七章：清晨的出逃与脱轨的早班电车
## 严格对标《规范文件.md》视觉素材规范与 11111.docx 对象修订终盘定稿
## 背景规范：hospital_bed_01_blue / corridor_05_blue / hospital_exterior_01_blue / road_01_blue / station_01_blue / car_window_01_blue~orange / city_01_orange
## 立绘规范：anon hosp 01~10 规范立绘
## 演出规范：纯旁白（无头像无立绘 / 无头像仅对方立绘）与主视角 Side Image 差分 + 换行 extend / {nw} 组合

label ch07_escape:
    $ current_chapter = 7
    $ quick_menu = True

    # 1. 清晨五点病房醒来
    scene bg hospital_bed_01_blue with fade
    play bgs bgs_hospital fadein 2.0 loop

    # 【纯旁白：无头像无立绘】
    "我整夜没有合眼。{w=0.2}{nw}"
    extend "\n耳朵里反复响着昨天下午千早爱音说出的那句话。"
    "‘医生说……你只剩最后七天了。’"

    tomori calm "主治医生让我老老实实待在病房里，去选择一个能够安静闭上双眼的地方。{w=0.2}{nw}"
    extend soft "但是，当我在清晨看到千早爱音蜷缩在陪护椅上熟睡的时候，我彻底明白了什么是我离开这个世界时想要看到的画面——{w=0.2}{nw}"
    tomori smile "千早爱音的那张脸。所以我决定不再消极等死了。"

    voice "audio/voice/vo_tomori_06_01.ogg"
    tomori an2 "……千早同学。"

    show anon hosp 07 normal_1 at center_standee with dissolve
    "陪护椅上的粉发少女睫毛动了动，慢慢睁开眼睛。{w=0.2}{nw}"
    show anon hosp 03 curious_1 at center_standee
    extend "\n她揉着眼睛，有些吃力地把脑袋从椅背上抬起来，发懵。"

    anon "呜……嗯？{w=0.4}灯……？{w=0.2}{nw}"
    show anon hosp 01 smug at standee_nod
    extend "\n怎么突然又叫回千早同学了，昨天不是叫爱音叫得挺顺口的嘛……"
    show anon hosp 03 curious_2 at standee_jump
    anon "{cps=*1.5}现在才五点不到！这么早就走嘛？{/cps}"

    play sound sfx_heartbeat
    camera at camera_heartbeat
    tomori calm "当你在深夜疲惫入睡的时候，我的胸口又抽痛了一次，我真切地以为我的死期已经到了。{w=0.2}{nw}"
    extend bitter "\n它不讲理地提前到来，就算它本身就不合理。心脏的疼不过是它大发慈悲地给我一点提醒。{w=0.2}{nw}"
    tomori soft "我借着晨光看着你的脸，试图猜测出你隐瞒的所有委屈与孤单，并且准备平静地走向终点。"

    tomori calm "现在就走吧。"

    show anon hosp 03 curious_2 at anon_lean_in
    anon "这就出发了？"

    tomori calm "但是时间还在走动，我的心脏依然在胸膛里倔强地跳动着，也许是因为我心里还有未完成的愿望。"
    show anon hosp 07 normal_2 at center_standee
    "千早爱音低下了头。"
    tomori soft "你不要因为我的任性而感到为难。{w=0.2}{nw}"
    extend calm "\n我不会对千早同学提出任何过分的要求，仅仅是要你允许我喜欢你，允许我再为你唱完整整一首歌，如果我的喉咙还能发出声音的话。"
    tomori calm "作为交换，我只要求你答应我一件事：{w=0.2}{nw}"
    extend soft "\n如果你听到医生说我就要死了，请你带我走出这所综合医院的高墙，去看看外面的树木和天空，去呼吸清晨新鲜的空气。"

    show anon hosp 07 normal_3 at anon_retreat
    "千早爱音许久没有讲话。我以为她又又拿不定主意了，不想如此早地面对外界。{w=0.2}{nw}"
    extend "\n我望着医院围墙外边的晨光。"

    show anon hosp 08 gentle at standee_step_in
    anon "如果你想离开这里，我就带你出去。{w=0.2}{nw}"
    show anon hosp 01 smug at standee_nod
    extend "\n只是给我几分钟时间，让我去拿外套和钱包，然后我们两个人立刻就走。"

    tomori calm "千早同学，我们在一起的时间不多了，这你是明白的。"

    show anon hosp 07 normal_2 at anon_wander
    "千早爱音没有回答。{w=0.2}{nw}"
    show anon hosp 08 gentle at standee_step_in
    extend "\n她迅速从椅背上抓起防风夹克，将充电线、钱包和围巾塞进大衣口袋里，快步走到了病床前。"
    play ambient_sfx sfx_clothes_rustle
    play sound sfx_zipper
    "她把衣服罩在我的条纹病号服外面，拉链唰的一声拉到领口。"

    stop bgs fadeout 1.5
    stop music fadeout 1.5
    play sound sfx_strike
    show anon hosp 02 boast at anon_burst_in

    anon "{size=+3}{b}高松灯，我们会一起去看海，要比在这间千篇一律的病房里度过的日日夜夜还要长久。{/b}{/size}" with shake_h
    show anon hosp 01 smug at standee_jump
    anon "{cps=*1.6}我们走吧，逃兵就要做疯狂的事！{/cps}"

    # 2. 逃出医院奔跑与站台
    hide anon
    scene bg corridor_05_blue with dissolve
    play ambient_sfx sfx_door_slide
    play sound sfx_running_corridor
    play music bgm_soaring fadein 2.0 loop

    "她抓紧了我的手腕。{w=0.2}{nw}"
    extend "\n病房的门锁被轻轻拧开，我们在清晨五点不到空无一人的走廊里奔跑起来。{w=0.2}{nw}"
    extend "\n没有回头看一眼那张空下来的病床。"

    scene bg hospital_exterior_01_blue with PushMove(0.40, "pushright")

    tomori calm "推开医院侧门的时候，天还没有亮透。我不知道，也不曾想过上哪里去；{w=0.2}{nw}"
    extend bitter "\n我只知道一点：这一切必须就在今天改变，一次性地改变，立即改变；否则我决不回那间病房，因为我不愿意如此死去。"

    scene bg road_01_blue with dissolve
    play sound sfx_running_corridor

    "我尽量不去看医院高高的围墙，急切切地跟着爱音往车站的方向赶去。{w=0.2}{nw}"
    extend "\n我们一路奔跑，穿过清冷无人的街道，赶到了早班车的站台前。"

    scene bg station_01_blue with dissolve
    show anon hosp 08 gentle at center_standee with dissolve

    "清晨的寒气在呼吸间化作白雾。{w=0.2}{nw}"
    extend "\n我顿了顿，环顾站台，然后转过身来朝拉着我的粉发少女点头。"
    tomori calm "明摆着，我们是同伴。{w=0.2}{nw}"
    extend soft "两人都穿着宽大的外套，一样的狼狈。"
    show anon hosp 06 pain at standee_tremble
    "爱音套着一件深色防风夹克，而这衣服使她的肩膀显得单薄，有些发抖。{w=0.2}{nw}"
    extend "\n我自己呢，里面还裹着条纹病号服。"

    # 3. 登上长途大巴
    hide anon
    scene bg car_window_01_blue with dissolve
    camera at camera_gentle_sway
    play sound sfx_bus_door
    play bgs bgs_bus_ride fadein 2.0 loop

    "我们离巴士车门很近。转瞬之间夜色与我们相融又相隔。{w=0.2}{nw}"
    extend "\n拉着行李箱的爱音正走到底层车厢的正中央。"
    "我紧跟着走上前去，往前挪了几步，{w=0.2}{nw}"
    extend "停在离爱音半步的地方，看着车窗外的黑暗。"
    tomori uff "我从检票口紧挨着走过来，朝千早爱音靠过去，在她背后停下来，像她一样喘息。{w=0.2}{nw}"
    extend calm "\n车窗玻璃上映出了我们的影子。"
    tomori calm "这个女孩为什么拉着我？她要去哪里？谁也没有问。{w=0.2}{nw}"
    extend concern "\n我看着她。千早爱音没有回过头来，她看着前路，等待着发车，像个赌徒一样站在昏黄车灯下。"
    "售票员朝我们走过来。我发凉的手指抓住了千早爱音的风衣衣角，一声不吭。{w=0.2}{nw}"
    extend "\n引擎声低吼着，又震动起来了。是一辆长途大巴，驶向海边。"
    play sound sfx_clothes_rustle
    show anon hosp 08 gentle at standee_step_in with dissolve
    "冷风穿过开启的单向车门，朝车厢吹来。{w=0.2}{nw}"
    extend "\n大巴驶出了站台。爱音转过头看着我，伸出手来，没有松开我的手，把手覆在我发冷的手背上。"
    "车轮开始转动。我坐在座位上，一动不动。窗外飞速倒退的街景从眼前滑过，像黑色的河水一样。"

    show anon hosp 07 normal_1 at center_standee
    "车窗玻璃上两人的影子晃动着。{w=0.2}{nw}"
    show anon hosp 08 gentle at anon_sit
    extend "\n爱音整个人陷在座椅里，两只手揣在宽大的口袋里，侧过脸看着我。{w=0.2}{nw}"
    show anon hosp 03 curious_1 at anon_sit
    extend "\n她不再像刚才在医院里那样紧绷，眉梢眼角浮现出浅浅的轻松，甚至带着些许好奇。"

    show anon hosp 08 gentle at anon_lean_in
    anon "灯。"

    tomori calm "……嗯？"

    show anon hosp 08 gentle at standee_step_in
    anon "我想更多了解你。"

    tomori ah "我愣在座位上。{w=0.2}{nw}"
    extend bitter "\n在生命走到头时，在这个只剩下一百五十五个小时的早晨，我才突然反应过来：{w=0.2}{nw}"
    extend calm "\n我对身边的千早爱音，几乎一无所知。{w=0.2}{nw}"
    extend soft "\n而她却把自己的一切押在了一个快要死掉的人身上。"

    show anon hosp 03 curious_2 at center_standee
    anon "昨晚你说的那个乐队……叫CRYCHIC对吧？{w=0.2}{nw}"
    show anon hosp 07 normal_2 at center_standee
    extend "\n还有你本子里写到的那些人，立希，还有那个叫祥子的女孩。"
    show anon hosp 08 gentle at anon_lean_in
    anon "你们以前也是这样，坐着车去演出或者练习吗？"

    tomori sadaway "祥子……{w=0.2}{nw}"
    extend bitter "立希……"

    # 4. 高松灯的解离体验与心痛（0.24s 冷青负片快切 → C 演出：超宽车窗窄条视窗）
    stop music fadeout 1.2
    play sound sfx_heartbeat
    $ photosnap_cyan(duration=0.24)
    camera at default
    hide anon
    window hide
    scene ed_c_bus_window_strip with ed_cut
    show ed_c_bus_poles_tile at ed_c_poles_pass
    show ed_ob_filmdamage at ed_ob_damage_ambient
    play music work fadein 2.0 loop

    ed_c_top "雨的声音砸下来。把窗户关上。外面的光太亮了，我已经没有力气再去辨认那些树影。"
    ed_c_bottom "看哪，这就是我们剩下的全部时间。这么短，甚至来不及喝完一杯冷掉的水。"
    ed_c_top "你在这里。你却又离我这么远。不要说话。一旦开口，那些词就会碎在地板上，像干枯的叶子。"
    ed_c_bottom "我写了一辈子，最后只剩下一个词。但我把它弄丢了。{w=0.2}冷。从脚趾开始的冷。"

    hide ed_ob_filmdamage
    hide ed_c_bus_poles_tile
    window auto

    scene bg car_window_01_blue with dissolve
    camera at camera_gentle_sway
    play sound sfx_book_drop
    "怀里的黑色笔记本啪的一声滑落在地上。"

    show anon hosp 06 pain at center_standee, standee_shake_h
    anon "灯？灯？"

    tomori uff "爱音，把你的手给我。不，算了，你的手太热了，像某种我不熟悉的生命。{w=0.2}{nw}"
    extend calm "\n来帮我把笔记本捡起来，我没有什么可写的了。我从未扔掉一块石头。"
    tomori sadaway "所有人都很耀眼。{w=0.2}{nw}"
    extend bitter "\n……一个连怎样呼吸都做不好的女孩。这就是我。如此而已。"
    tomori sad "别松开我的手，求求你们。{w=0.2}{nw}"
    extend sadaway "\n别管我，我本来就应该一个人待在角落里。"

    show anon hosp 08 gentle at standee_step_in with flash_warm
    "我的目光落在她伸过来的右手食指上——{w=0.2}指节背面贴着一枚草莓图案的创可贴，边缘因为刚才在医院侧门翻铁栏杆时蹭破了皮，正渗着一点点血渍。{w=0.2}{nw}"
    extend "我伸出冰凉的指尖，轻轻碰了碰那枚翘起边角的创可贴。"
    tomori bitter "祥子，我要向你道歉，但我不知道自己做错了什么。{w=0.2}{nw}"
    extend sadaway "\n我那么喜欢你们。而现在我要掉队了。{w=0.2}{nw}"
    extend calm "\n到头了。结束了。这是终点。太突然了。终结让我感到迷惑。"
    tomori uff "我浑身发冷：时间。真让人害怕。{w=0.2}{nw}"
    extend sadaway "\n企鹅停止了游动。我很害怕。"

    show anon hosp 06 pain at standee_step_in
    anon "是不是胸口又疼了？还是呼吸不上来？"

    tomori calm "我不甘心。我感觉自己路过了你的一生，却没有推开过你的门。{w=0.2}{nw}"
    extend sadaway "\n一无所知。除了你的名字和温度，我一无所知。"
    tomori calm "我不能什么也不知道地闭上眼睛。{w=0.2}{nw}"
    extend bitter "\n我一直以为还有很多时间。没有办法，我一直以为“一辈子”是很久很久。"
    tomori calm "你从来不说你自己的事。这是某种迁就。我呢，我理所当然地躲在你的体贴里。{w=0.2}{nw}"
    extend babble "\n{cps=*1.5}就一句话，快。告诉我你最讨厌的颜色。我们交换。快。{/cps}"

    tomori an2 "我喜欢……"

    tomori soft "我其实……我那么爱你。不是作为乐队的主唱，也不是作为迷路的孩子。{w=0.2}{nw}"
    extend calm "\n我真不知道原来爱一个人……是可以连她几点睡觉都不知道的。"
    tomori soft "有几秒钟我摸到了你手指上的茧。{w=0.2}{nw}"
    extend calm "\n从我自己的世界里走出来，这让人发晕。有时候你的眼睛深得让人害怕。"
    tomori calm "我厌倦了只谈论我自己。{w=0.2}{nw}"
    extend soft "\n我想写一首只有你的名字的歌。哪怕一个韵脚都没有。不管是喜欢还是爱。{w=0.2}{nw}"
    extend smile "\n快来。在一切停下之前，告诉我你的全部。我要现在开始喜欢你。"

    show anon hosp 03 curious_1 at center_standee
    anon "……嗯？喜欢什么？这首前奏吗？"

    scene bg car_window_01_orange with dissolve
    camera at camera_gentle_sway
    show anon hosp 08 gentle at standee_step_in with dissolve

    "我看着匀称呼吸着的爱音。这一百六十八个小时燃尽之前，我不打算再回到那张白色的病床上去了——一秒钟也不打算。"
    tomori calm "打定主意，下定决心，不分日夜，我的脑海里只剩下这一个无比清晰的意念：{w=0.2}{nw}"
    extend soft "\n不要求向这个世界取得什么原谅，只求在天亮之前，牵着她的手从当前的处境中彻底脱身而去。"

    "那根细细的白色耳机线把我们的脑袋连在一起。{w=0.2}{nw}"
    extend "\n耳机里传出的微弱沙沙声仿佛是在说：放心好了，不会让你出事儿的。"
    tomori soft "好像是她在说她知道有一个好地方，那里一年过两回圣诞节，从秋天起就过，而且过一整个冬天再过到春天和夏天——{w=0.2}{nw}"
    extend smile "\n只要我和她待在这根耳机线的两端，我是会平安无事的。"

    # 5. 车厢深处告白与“喜欢和你玩”
    stop music fadeout 1.5

    tomori calm "我喜欢你。"

    show anon hosp 03 curious_1 at center_standee, standee_jump
    anon "……诶？{w=0.3}{nw}"
    show anon hosp 04 shy_2 at standee_shake_h
    extend "\n{cps=*1.5}等、等等……高松同学，你冷不丁地说什么呢？{/cps}{w=0.3}"
    show anon hosp 01 smug at standee_nod
    anon "{cps=*1.4}我当然知道啦！我也超喜欢小灯的，毕竟我们现在是搭档嘛——{/cps}"

    play music bgm_dialogue_warm fadein 1.5 loop

    tomori calm "不是那个。"

    show anon hosp 03 curious_2 at center_standee
    anon "……哎？"

    tomori calm "不是搭档。{w=0.2}{nw}"
    extend sadaway "也不是主唱对吉他手。{w=0.2}{nw}"
    play sound sfx_heartbeat
    extend soft "\n就是喜欢。千早爱音，我喜欢你。"

    show anon hosp 04 shy_2 at standee_shake_h
    anon "{cps=*1.6}什、什么叫‘就是喜欢’啊……小声点啦，前面还有人睡觉呢……{/cps}{w=0.2}{nw}"
    show anon hosp 04 shy_1 at anon_retreat
    extend "\n你这个人，平时半天都憋不出一句话，怎么一开口就这么突然啊……{w=0.3}"
    show anon hosp 07 normal_2 at anon_lean_in
    anon "而且，你说的喜欢……到底是哪种喜欢？小灯真的弄明白这两个字是什么意思了吗？"

    play sound sfx_clothes_rustle
    "平时总是卡在喉咙里、需要一个字一个字慢慢找的语言，就在她发问的这一秒，突然涌了出来。{w=0.2}{nw}"
    "我怕自己一停下来就会重新变回那个发不出声音的哑巴，于是只能抓着她的袖子，压低声音，像背诵写满整页的歌词一样急促地、一口气往外说——"

    tomori sadaway "{cps=*1.5}我以前不明白……{w=0.05}{nw}"
    extend bitter "{cps=*1.5}我以前从来不明白，{w=0.05}{nw}"
    extend sad "{cps=*1.5}但现在我比谁都清楚。{/cps}{w=0.1}{nw}"
    extend "\n{cps=*1.6}这件感情太新了，来得太快，一想到几天之后就要和你分开，我就觉得好可怕……{/cps}{w=0.1}{nw}"

    tomori soft "{cps=*1.6}我想知道你平时几点睡觉，{/cps}{w=0.05}{nw}"
    extend babble "{cps=*1.6}想知道你最讨厌什么颜色，想知道你在伦敦的雨夜里偷偷哭过几次，想知道你早起的时候头发是不是也会翘起来。{/cps}{w=0.1}{nw}"

    show anon hosp 03 curious_1 at standee_jump
    anon "{cps=*1.6}小、小灯……？{/cps}{w=0.1}{nw}"

    tomori calm "{cps=*1.6}为什么你总是只听我说，却从来不跟我讲你的事呢？{w=0.05}{nw}"
    extend soft "{cps=*1.6}你告诉我吧，趁现在告诉我……{/cps}{w=0.1}{nw}"
    extend sadaway "\n{cps=*1.6}在遇到你之前，我连什么是难过、什么是活着都分不清，我以为我知道，其实我什么都不懂。{/cps}{w=0.1}{nw}"

    show anon hosp 04 shy_2 at standee_shake_h
    anon "{cps=*1.6}慢一点……你一下说太快了，小灯，你先喘口气——{/cps}{w=0.1}{nw}"

    "她什么样子？我没去注意看。请让我短暂地把重心挪回到自己身上吧！{w=0.1}{nw}"

    tomori sad "{cps=*1.6}我怕停下来就说不出来了。如果不趁现在全部告诉你，时间就不够用了。{/cps}{w=0.1}{nw}"
    extend sadaway "{cps=*1.5}我有一点羡慕所有比我更早认识你的人。羡慕你在英国的同学，羡慕你初中的朋友，也羡慕……等以后我不在了，还能陪在你身边的那些人。{/cps}{w=0.1}{nw}"

    tomori sadaway "{cps=*1.4}我不想让你太快忘记我。{w=0.1}{nw}"
    extend sad "{cps=*1.4}哪怕我知道人总是会忘的。{/cps}{w=0.1}{nw}"
    extend soft "\n我想完完整整地记住你。记住你爱逞强的样子，记住你嘴硬的样子，记住你明明那么贴心、自己却一点都不知道的样子。"

    tomori soft "这就是我的喜欢。{w=0.2}{nw}"
    extend calm "\n除了爱音，我这辈子不会再有别的喜欢了。"

    show anon hosp 10 tears at standee_shake_h
    anon "……你这是犯规啊，高松灯。{w=0.3}{nw}"
    show anon hosp 04 shy_2 at standee_step_in
    extend "\n哪有人大清早在巴士后排突然说这些的……一口气倒出来这么多，我都接不住了啦……"

    tomori calm "……那你听懂了吗？"

    show anon hosp 09 confess at standee_nod
    anon "{cps=*1.5}听懂了啦！笨蛋，贴得那么近，怎么可能听不懂嘛……{/cps}"

    tomori smile "其实，总结起来只有一句。"

    show anon hosp 03 curious_1 at center_standee
    anon "……哪一句？"

    tomori smile "……我喜欢和你玩。"

    show anon hosp 03 curious_2 at standee_jump
    anon "诶？{w=0.3}{nw}"
    show anon hosp 04 shy_2 at standee_shake_h
    extend "\n绕了一大圈，最后怎么又变回小孩子一样的发言了啊？真是的……害我白白紧张了半天，心脏都快跳出来了。{w=0.3}{nw}"
    show anon hosp 08 gentle at standee_nod
    extend "\n哪有人把别人弄哭了之后，最后的总结陈词是‘喜欢和你玩’的啊……"

    scene bg city_01_orange with flash_warm
    camera at camera_gentle_sway
    show anon hosp 08 gentle at standee_step_in with dissolve

    "我们俩就这样并排坐着，在一种幸福的迷雾中坐着。{w=0.2}{nw}"
    extend "\n她用一只手揽着我的肩膀，另一只手握着我的手，在宽大的风衣口袋里，我通过那只手感触到整个的她。"
    tomori soft "我的灵魂又开始在胸腔里呼吸，我的眼睛又明亮了。时间只属于我们，只为我们两个人的逃亡而存在。"
    tomori calm "“我喜欢……”"
    "你转过头来看我了。"
    tomori smile "……我喜欢和你玩。一个将要把我留在原地的女孩。{w=0.2}{nw}"
    extend calm "\n除此以外，在舞台上或角落里，在我呼吸之前或停止之后，都无所谓。"
    tomori soft "我爱你。{w=0.2}{nw}"
    extend calm "\n人类是可以靠这种微小的动作活下去的。"

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    camera at default
    scene black with slow_dissolve

    $ persistent.cleared_chapter_7 = True
    jump ch08_nightbus
