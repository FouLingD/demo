## ch09_haruhikage.rpy - 第九章：爱音的房间与放声歌唱的春日影
## 严格对标《素材与视觉资产规范.md》与《图片.rtf》视觉素材规范
## 背景规范：sea_01_blue / sea_02_blue / corridor_01_blue / bedroom_01_blue~orange~purple~red~rose~magenta / rehearsal_room_01_blue~orange / station_02_blue / road_02_blue / bg white / bg black
## 立绘规范：anon hosp 01~10 全套差分 / soyo 01 smile~normal
## 三层旁白与主视角差分系统：纯环境旁白（无立绘无头像） / 对方动作观察旁白（仅对方立绘无头像） / 高松灯主观心声与台词（tomori <emo> + 换行 extend）

label ch09_haruhikage:
    $ current_chapter = 9
    $ quick_menu = True

    # ==========================================
    # 1. 闭馆前的水族馆长廊
    # ==========================================
    scene bg sea_01_blue with fade
    camera at camera_gentle_sway
    play music bgm_dreamy fadein 2.0 loop
    play bgs bgs_aquarium fadein 2.0 loop

    "在乘上列车后，我们去了很多地方。{w=0.2}{nw}"
    extend "\n我们像两个真正拥有大把时间可以挥霍的高中女生一样，在东京的夜晚漫无目的地换乘。"
    scene bg sea_02_blue with dissolve
    "后来，我们去了水族馆。{w=0.2}{nw}"
    extend "\n闭馆前的海底长廊空无一人。{w=0.2}{nw}"
    extend "\n人造的冷光从巨大的亚克力水箱顶部打下来，打到水箱里时，灯光看起来很像星星。"

    show anon hosp 07 normal_1 at center_standee with dissolve
    tomori soft "……爱音。{w=0.2}{nw}"
    extend smile "\n我们要不要办一张年卡呢？"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.5}年卡？好呀！只要来三次就回本了呢！{/cps}"

    tomori sadaway "但其实我心里清楚，好像已经没机会再来第二次了。"
    play sound sfx_clothes_rustle
    show anon hosp 08 gentle at standee_step_in
    "我把头靠在她的肩膀上。"
    tomori calm "为什么呢？我也说不清是怎样的想法。{w=0.15}{nw}"
    extend uff "\n只是觉得如果不靠着点什么，身体就会在列车到站前彻底散架。"
    "夜里十一点半。"

    # ==========================================
    # 2. 千早爱音的房间与伦敦日记本
    # ==========================================
    stop bgs fadeout 1.5
    camera at default
    scene bg corridor_01_blue with dissolve
    play ambient_sfx sfx_key_unlock
    play sound sfx_door_open_wood
    scene bg bedroom_01_blue with dissolve
    play music bgm_dialogue_warm fadein 2.0 loop

    "千早爱音的家。{w=0.2}{nw}"
    play sound sfx_footsteps_wood
    extend "\n玄关的感应灯亮起又熄灭，我们轻手轻脚地走上二楼，关上了她房间的门。"

    scene bg bedroom_01_orange with dissolve
    show anon hosp 07 normal_1 at center_standee with dissolve
    anon "病号服穿了那么长时间，肯定不舒服吧？"

    play sound sfx_clothes_rustle
    show anon hosp 02 boast at standee_step_in
    anon "{cps=*1.5}给，换上我的居家服！虽然尺码可能稍微大一点点。{/cps}{w=0.1}{nw}"
    show anon hosp 08 gentle at anon_door
    extend "\n我去楼下端两杯热饮上来，小灯你随便坐哦！"

    play sound sfx_door_close
    hide anon with dissolve
    "房门轻轻合上。{w=0.2}{nw}"
    play sound sfx_clothes_rustle
    extend "\n我在铺着毛绒地毯的书桌旁坐下，从书包里拿出自己那本边缘磨损的歌词本，摊开在桌面上。"
    "就在挪动笔筒的时候，我的指尖碰到了压在桌垫底下的一本粉色硬壳笔记本。{w=0.2}{nw}"
    extend "\n封皮上贴着伦敦巴士的贴纸。那是爱音的本子。"
    play sound sfx_page_turn
    tomori concern "我鬼使神差地伸出手，翻开了第一页。"

    play sound sfx_running_corridor
    show anon hosp 05 annoyed_2 at anon_burst_in
    anon "{size=*1.25}{cps=*1.6}——喂！小灯！{/cps}{/size}" with shake_h

    tomori kya "……啊。对不起。"

    play sound sfx_clothes_rustle
    show anon hosp 04 shy_2 at standee_step_in, standee_tremble
    "她低着头，把日记本紧紧护在胸口，我看着她的脸，她也正喘着气低头看着我。"

    show anon hosp 04 shy_2 at standee_shake_h
    anon "{cps=*1.6}讨厌啦！怎么可以随便偷看别人的东西！{/cps}{w=0.1}{nw}"
    show anon hosp 01 smug at standee_jump
    extend "\n{cps=*1.5}里面全都是我在伦敦大受欢迎的记录，小灯看了可是会嫉妒的哦！{/cps}"

    show anon hosp 02 boast at center_standee
    "她笑得比平时更欢。"
    play sound sfx_heartbeat
    camera at camera_heartbeat
    tomori sad "末了我发现，我胸口闷得没法，{w=0.15}{nw}"
    extend uff "眼睛里都噙满了眼泪。"

    # NVL 文学独白：陀思妥耶夫斯基《涅朵奇卡》式的狂热初恋剖析
    camera at default
    hide anon
    scene bg white with cut_white_fade
    nvl clear

    vn_black "我几乎不明白自己正在发生什么变化。一种新的、莫名其妙的感觉激荡着我的身心，我可以毫不夸大地说，我在为这一新的感情而苦闷，而烦恼。"
    vn_black "简单地说——请原谅我用这样的语汇——我爱上了我的爱音。"
    vn_black "是的，这是爱，真正的爱，伴有眼泪和欢欣的爱，热情洋溢的爱。"
    vn_black "她有哪一点吸引着我？怎么会产生这样的爱？"
    vn_black "她身上的一切都美；她的每一种坏脾气都不是和她一起诞生的，都是后来在异国的冷雨和孤独里染上的，而且始终处在挣扎与斗争状态。"
    vn_black "她生下来就幸运，她应当为幸福而生——这便是我和她在一起得到的最深的印象。也许，这是在我濒死的身体里第一次被唤起美的感觉，也是我对她产生爱的全部原因。"
    nvl clear

    vn_black "请相信我，没有一个人像我这样死心塌地、这样看着你。"
    vn_black "因为在世界上，没有什么东西可以比得上一个快要死去的孩子暗中怀有的、不为人所觉察的爱情。"
    vn_black "因为这种爱情不抱希望，低声下气，全神贯注，这和那些拥有漫长寿命的普通人完全不同。"
    vn_black "只有孤独的孩子才能把全部热情集聚起来，至于其他人，他们经常听人谈论喜欢，在流行歌里常常唱到爱情，他们玩弄感情，就像摆弄一个玩具，就像男孩抽了第一支香烟而洋洋得意。"
    vn_black "可我身边没有别人，我没法向别人诉说我的心事，没有人指点我、提醒我，我毫无阅历，毫无思想准备：我一头栽进我的命运，就像跌进一口深井。"
    nvl clear
    window hide

    scene bg bedroom_01_orange with dissolve
    show anon hosp 08 gentle at center_standee, standee_step_in with dissolve
    anon "……小灯？你哭什么呀？{w=0.15}{nw}"
    show anon hosp 03 curious_2 at standee_step_in
    extend "我又没有真的生你的气！"

    tomori sadaway "我没有哭……"

    show anon hosp 10 tears at standee_shake_h
    anon "{cps=*1.5}小灯！……我真是笨死了。其实我很早很早就喜欢上你了！{/cps}{w=0.1}{nw}"
    show anon hosp 09 confess at standee_step_in
    extend "\n你知道是打什么时候开始的吗？"

    tomori ah "……什么时候？"

    show anon hosp 10 tears at standee_jump
    anon "{cps=*1.4}打从你在天台上抓着栏杆，明明怕得发抖，却还是对我大声喊出心里话的那一次开始的……{/cps}{w=0.2}{nw}"
    show anon hosp 08 gentle at standee_step_in
    extend "\n傻——瓜——小——灯！"

    play sound sfx_clothes_rustle
    "她拉长了调子说着，额头抵在我的手背上，又是哭，又是笑。"
    tomori soft "爱音……"

    show anon hosp 08 gentle at standee_step_in
    anon "什么事？说呀，什么事？"

    tomori sad "为什么我们俩这么多时间一直……{w=0.3}一直……{w=0.1}{nw}"
    extend babble "\n{cps=*1.5}我没把这句话说完。为什么呢？为什么说不出来呢？是因为太多了吗？{/cps}{w=0.05}{nw}"
    extend kya "{cps=*1.6}那不是，更应该，像在公交车上时那样，拼尽全力地一口气通通说出来呢？这是要做什么？我在做什么？为什么呢？{/cps}"

    play sound sfx_clothes_rustle
    scene bg bedroom_01_rose with flash_warm
    show anon hosp 09 confess at center_standee, standee_step_in with dissolve
    camera:
        easein 0.8 zoom 1.08 yoffset 12
    "她从地毯上站起身，一把抱住我。{w=0.2}{nw}"
    extend "\n我们互相拥抱，足有三分钟一句话也不说。"

    camera:
        easeout 0.6 zoom 1.0 yoffset 0
    scene bg bedroom_01_orange with dissolve
    show anon hosp 04 shy_2 at center_standee with dissolve
    anon "你倒说说看，你对我是怎么想的？{w=0.15}{nw}"
    show anon hosp 04 shy_1 at center_standee
    extend "\n看到那个本子之后，是不是觉得我特别逊？"

    tomori calm "没有。并且，事实上，我什么都没看见。{w=0.15}{nw}"
    extend soft "\n不过我也能猜到里面的内容。{w=0.15}{nw}"
    extend smile "\n至于我想得可太多了，爱音。我老是在想，白天夜里都想。"

    show anon hosp 08 gentle at standee_nod
    anon "刚才在电车上睡着的时候，你还小声叫我名字来着，我听见过。"

    tomori kya "……真的？"

    show anon hosp 07 normal_1 at standee_step_in
    anon "还在病房里偷偷哭了不知多少次。我都看得出来。"

    tomori concern "那你为什么总是要装出一副什么都不在乎的样子？"

    show anon hosp 04 shy_2 at standee_shake_h
    anon "{cps=*1.5}因为我实在太蠢了，小灯！{/cps}{w=0.1}{nw}"
    show anon hosp 06 pain at center_standee
    extend "\n不知怎么的，我往往犯这样的毛病，完全没有旁的原因。有时候我甚至老是生你的气。"

    tomori ehh "为什么？"

    show anon hosp 01 smug at standee_nod
    anon "就为了我自己是个爱慕虚荣的坏东西呗！{w=0.2}{nw}"
    show anon hosp 10 tears at center_standee
    extend "\n先是因为你比我纯粹；后来因为不管走到哪里，像立希她们那样的人，眼里永远只有你。"
    show anon hosp 05 annoyed_2 at standee_shake_h
    anon "听着，有时候我很想对你好，后来看到你把心事全锁在本子里，我一下子又想生你的气！{w=0.1}{nw}"
    show anon hosp 02 boast at standee_jump
    extend "{cps=*1.5}可是后来我看到你离开了我根本没法在商场里走下去，我就在想：这个笨手笨脚的主唱，还得靠我千早爱音拉着才行！{/cps}"

    tomori smile "嗯。是的。我需要你啊。{w=0.15}{nw}"
    extend soft "爱音很勇敢。"

    show anon hosp 10 tears at standee_shake_h
    anon "{size=*1.15}{cps=*1.5}其实，我怕——得——要——死！{/cps}{/size}{w=0.1}{nw}"
    extend "\n{cps=*1.5}不管是在英国一个朋友都交不到的时候，还是第一次站在台上弹错和弦的时候，我都怕得要死！{/cps}{w=0.1}{nw}"
    show anon hosp 09 confess at standee_step_in
    anon "{cps=*1.6}你知道我为什么非要装出那么神气的样子吗？因为当时你在场！我看到你在旁边瞧着……懂吗？！所以我不管不顾地往前冲。{/cps}"
    show anon hosp 10 tears at standee_tremble
    anon "其实，我非常担心你认为我肤浅、认为我愚蠢！{w=0.15}{nw}"
    extend "\n你挺聪明，小灯，你写的每一句歌词都那么厉害，难道不是吗？"

    tomori kya "你说到哪儿去了，爱音……"

    show anon hosp 07 normal_1 at standee_nod
    anon "不，这我是知道的。{w=0.1}{nw}"
    play sound sfx_candy_jar
    show anon hosp 01 smug at standee_jump
    extend "\n{cps=*1.5}还有，今天我分给你的金平糖，你是不是连罐子都藏在怀里舍不得吃？真不害臊！这些我全都知道！{/cps}"

    show anon hosp 08 gentle at standee_step_in
    anon "小灯。再唱一遍吧。"

    tomori concern "……可是，我还没有写好。"

    show anon hosp 07 normal_1 at standee_nod
    anon "那也没关系。{w=0.2}{nw}"
    show anon hosp 08 gentle at standee_step_in
    extend "\n不用管练习室，也不用管以前的人。就在这个房间里，唱给我听。"

    tomori soft "……好。{w=0.2}{nw}"
    extend smile "我……唱给爱音听。"

    # ==========================================
    # 3. 熄灯与黑暗中的《春日影》/新歌清唱
    # ==========================================
    play sound sfx_clothes_rustle
    "我把手心里的黑皮笔记本攥得很紧，指节微曲，刚准备在暖黄的台灯下张开嘴。{w=0.2}{nw}"
    show anon hosp 02 boast at standee_jump
    extend "\n对面的爱音却突然从小地毯上跳了起来。"
    play sound sfx_footsteps
    hide anon with dissolve
    "她快步走到卧室门边，手指在墙壁的开关上啪嗒一按。"
    play sound sfx_light_switch
    scene bg bedroom_01_blue with fast_dissolve
    "紧接着，她又走回床头，啪嗒按熄了床头灯。"
    play sound sfx_light_switch
    scene bg bedroom_01_purple with fast_dissolve

    tomori ehh "……爱音？{w=0.2}{nw}"
    extend neutral "为什么要关灯？"

    show anon hosp 08 gentle at center_standee with dissolve
    anon "因为开着灯的话，小灯又会害羞得不敢看我了吧。{w=0.2}{nw}"
    show anon hosp 09 confess at standee_step_in
    extend "\n就这样，在黑夜里唱给我听。在黑夜里，什么都不用怕。"

    hide anon with dissolve
    "谁都没有再说话。{w=0.15}{nw}"
    extend "\n黑暗像温水一样漫过房间。"

    # NVL 独白：歌的诞生与主唱的尊严
    nvl clear
    vn_white "真要说起来，这首歌写下第一个字的时候，我并不知道之后要发生什么。"
    vn_white "也许有一场轰轰烈烈的初演，也许有一群能一直走到毕业的同伴，我也不知道它大概能唱多久，也许两分钟，也许四分钟，也许是一首长长的叙事曲？"
    vn_white "但是不知道为什么，我觉得这应该不是一首坏歌，而且我还意识到，也许这次我要费尽九牛二虎之力才能把它唱完，过去那种毫无挂碍的一挥而就再也无法复现了。"
    vn_white "这里面有太多和我骨头相连的东西，这里面有太多我一直未敢展示的自己的观察与呼喊，这里面有太多我从未尝试过的豁出去的发声方法，这里面有太多我不太成熟的但是又不甘放弃的对音乐的一点体会。"
    nvl clear

    vn_white "写到初春那场暴雨的时候，我意识到自己已经走到了荒凉的旷野里。"
    vn_white "远远看见几个旧日同伴的人影，可是她们只对我抱以客气的微笑，并没给我指路；回头望去，来处的排练室早已坍废断绝，无所归处。"
    vn_white "我拥有的只有我自己，这是可怕而孤独的时刻，我所能做的只有一样：努力维护自己作为主唱的尊严。"
    vn_white "关于这首歌本身，我并不想再说太多，属于歌声的，留给歌声。"
    vn_white "关于这首歌之外的，也许我想说一点。"
    vn_white "人是可悲的生物，想说一点，纯粹是为了牢记。世事变化得太快了，自以为永远铭记的诺言，说不定几个月之后就模糊了一半。"
    vn_white "这首歌从初稿到今天走过了漫长的旅程，我几次想要放弃，把歌词本撕碎扔进垃圾桶，而促使我留下稿子、扔掉垃圾桶的，是眼前这个在黑暗中把后背靠在床边的女孩。"
    vn_white "她给我的每一句话，我都牢记；她对我的信任，让我第一次觉得自己可以重新开口，也许原来她不应当这么信任我，但是现在可以。"
    nvl clear
    window hide

    play music bgm_dreamy fadein 2.0 loop
    scene bg bedroom_01_blue with dissolve

    centered "{size=+6}{color=#ffffff}人知れず\n肩落としてる君がいるのに\n碧すぎてる空ばかりが眩しい\n僕はどんな言葉を君に\n言えばいいのか\n君に何を{/color}{/size}"

    "窗帘边缘漏进来的夜空繁星闪烁，清新透明。{w=0.2}{nw}"
    tomori soft "举目一望，人会情不自禁地反问自己：在这样的天空底下，在这样澄净的黑夜里，难道还会有人怒气冲冲、喜怒无常吗？"

    centered "{size=+6}{color=#ffffff}脆くやわい こころで生きる\n僕らは 傷つく生き物で\nなのに 今日だって\n頑張ってる 十分 君はもう\n躓いて 転んだって\n立ち上がり来たんだ{/color}{/size}"

    tomori calm "这也是一个幼稚的问题，非常幼稚，但它总会在寂静中触动人的灵魂。{w=0.2}{nw}"
    extend sadaway "\n既然提到那些怒气冲冲、喜怒无常的同伴，我就不能不回想起自己在这一整天里的所作所为。"
    tomori sad "打从大清早跟着爱音翻出医院大门起，我就受到一种说不清的苦恼的折磨。{w=0.2}{nw}"
    extend bitter "\n我忽然觉得：我孤零零的，正在受到所有人的抛弃，所有的人都在离我而去。"
    tomori calm "当然，任何人都有权发问：这所有的人究竟是些什么人呢？{w=0.2}{nw}"
    extend sadaway "\n因为我在东京都生活了十六年，并没有结识过几个真正亲近的人。"

    centered "{size=+6}{color=#ffffff}頑張ってる いつでも\nここに立ってるだけで\n必死なんだから\nジタバタで ラクじゃないけれど\n迷っても 君と進んでみたいよ\nいいかな{/color}{/size}"

    tomori calm "不过，话得说回来，我要结识那么多人干什么呢？不结识我也熟悉东京的站台与天桥呀。{w=0.2}{nw}"
    extend sadaway "\n所以，一旦旧乐队的同伴各自散去、不再回头，我就觉得所有的人都要抛弃我了。{w=0.2}{nw}"
    extend sad "我觉得一个人孤单单地留下来，是很可怕的。"
    tomori sadaway "我怀着深深的忧伤，在从天台跌落后的日子里整整恍惚了几个月，根本不明白我到底出了什么事。{w=0.2}{nw}"
    tomori bitter "去学校的长廊也好，去月之森附近的茶馆也好，在平日经常路过的电车道口漫步也好，我惯常在某一时间、某一地点见到的那些旧同伴，一个也没有再见到。"

    centered "{size=+6}{color=#ffffff}誰かには\nちっぽけなものだったとしても\n君にとっては\nなにより大事なこと\n壊さないで 失わないで\n守りたいから\nとなりにいる{/color}{/size}"

    scene bg station_02_blue with dissolve
    "窗外远处的电车轨道与干线公路像一条发光的河流。{w=0.2}{nw}"
    extend "\n在东京生活的人们，按照各自的风格，围绕着城市里的河流与轨道打发时日。"
    tomori calm "有的仅仅是悠闲地漫步，有的则是遛狗。有人骑自行车，有人慢跑，或是愉快地踩着滑板在桥下穿行——{w=0.2}{nw}"
    extend babble "\n那样容易摔伤的东西如何能愉快地玩，老实说，我从来百思不得其解。"
    tomori calm "人们简直就像被某种磁力吸引来的一般，集中到这些亮着车灯的河畔。{w=0.2}{nw}"
    extend soft "\n也许，每天看见许多流动的水，或者看见像河流一样的车流，对人类具有重大意义。{w=0.2}{nw}"
    extend smile "啊啊，也许有点夸大其词，但对我来说算是一件重大的事情。"

    scene bg bedroom_01_purple with dissolve
    centered "{size=+6}{color=#ffffff}頑張ったよ 昨日の 君だって\n思うようにいかない\nそんな毎日だって\n頑張ったと 知ってる\n僕は知ってる だから{/color}{/size}"

    tomori calm "若是一段时间没有看到水，我便有一种渐渐失去生命力的干瘪心情。{w=0.2}{nw}"
    extend sadaway "\n同酷爱音乐的人却因了某种缘故长期远离乐器，感觉多少有些相似。{w=0.2}{nw}"
    extend soft "与我自幼喜欢收集水滴与湿润石头这一事实，或许多少也有干系。"
    "水面每天微妙地变化，改变颜色、波浪的形状和水流的流速。季节则确确实实地改变着环拥河川的植物和沿岸街景的众相。{w=0.2}{nw}"
    extend "\n大小不同形状各异的夜云随兴所至，突然现身遂又逝去。{w=0.2}{nw}"
    "光带承受着深夜高架桥的灯，将那白色车影的去来忽而鲜明忽而暖味地映在公寓天花板上。"
    tomori calm "根据季节的不同，简直有如切换开关，风向会发生变化。而根据触感、气味和风向，我们能明确地感受到季节推移的刻度。{w=0.2}{nw}"
    extend sadaway "在这样一种伴随着实感的流移变幻之中，我认识到自己在城市这巨大的马赛克当中，只不过一块微小的彩片；{w=0.2}{nw}"
    tomori calm "亦如河里的水，不过是流过桥下奔向大海的、随时可以被置换的一部分。{w=0.2}{nw}"
    scene bg bedroom_01_rose with flash_warm
    show anon hosp 08 gentle at center_standee with dissolve
    extend smile "\n但这块微小的彩片，此刻在这个房间里，被另一块彩片握住了手心。"

    hide anon with dissolve
    centered "{size=+6}{color=#ffffff}こころを隠さないでほしい\nらしさなんて\nまだわからないままだけど\nぶつかるたび痛んで\nでも浮かびあがる輪郭\nああ 見つける{/color}{/size}"

    # 闪回：月之森沙龙与排练室的篱笆（福克纳《喧哗与骚动》）
    scene bg rehearsal_room_01_blue with push_left
    show soyo 01 smile at right_standee with dissolve
    "“如果你知道自己是谁，你可以去任何地方。”{w=0.2}{nw}"
    extend "\n长崎爽世每次带我去月之森的沙龙茶室，总要微笑着对我说这个。"
    "“公立学校和街头那些搞地下乐队的人，大多数和我们不是一类，”爽世端着精致的茶杯，语气温和而从容，{w=0.15}{nw}"
    extend "“但我可以对任何人都客气周到。因为我知道自己是谁，我知道月之森的体面。”"

    centered "{size=+6}{color=#ffffff}頑張っても ダメだと 思う日も\nこの手をつなぐから\nぎゅっと 力込めて{/color}{/size}"

    show soyo 01 normal at right_standee
    "“她们根本不在乎你客不客气，”那时候丰川祥子坐在三角钢琴前，手指重重按在琴键上，冷淡地接上一句，{w=0.15}{nw}"
    extend "“知道自己是谁只对过去的名门有好处。现在，很多人根本就不知道自己是在什么地方，自己是谁。”"
    "爽世停下倒茶的手，看了祥子一眼。"
    "“我当然非常清楚自己是谁，”爽世轻声说，“丰川同学，要是你不知道自己是谁，我会为你感到不安。”"
    "“哈，少提那些。”祥子生硬地回道。"

    centered "{size=+6}{color=#ffffff}頑張ってる ひたすら 息してる\n当たり前に過ぎる\n一秒なんかないよ{/color}{/size}"

    show soyo 01 smile at right_standee
    "“你们丰川家一直是让人敬仰的名门，”爽世不紧不慢地说着，“从老宅到音乐厅，这座城市里谁不知道丰川家的门第。”"
    show soyo 01 normal at right_standee
    "“看看你的四周，”祥子烦躁地甩出胳膊，指了指排练室外狭窄潮湿的小巷，“你知道自己现在是在哪儿吗？那些旧门第能帮我们把眼下的音准合上吗？”"
    "“你怎么老是这个样子？”爽世说，“丰川家的大小姐本来就该站在聚光灯下。”"
    "“现在那些老宅子已经没意义了。”祥子恼怒地说。"
    "“过去的时候总是更体面的。”爽世低声说。"
    hide soyo with dissolve
    tomori calm "我知道爽世又要谈这个话题了，每隔几天，她就会绕到这上面来，就像准点的列车。{w=0.2}{nw}"
    extend sadaway "\n我知道沿途每一个交叉口，也知道在哪一点上，祥子最后的结论一定会庄严地滑进车站：{w=0.2}{nw}"
    tomori bitter "“荒诞。根本就不现实。用不用天生的嗓子唱下去，是你的自由；有些人试图跨过界限，这没错，但她们应该站在篱笆旁属于她们自己的那一侧。”"

    scene bg rehearsal_room_01_orange with flash_warm
    centered "{size=+6}{color=#ffffff}頑張ってる いつでも\nここに立ってるだけで\nたたかってるよ\n逃げてもいい 道が見えなくても\n迷っても 君と走っていたいんだよ\n一緒に{/color}{/size}"

    tomori calm "有些篱笆从一开始就在那里。"

    # ==========================================
    # 4. 破音与黑暗被窝里的相拥痛哭、畅想二十年
    # ==========================================
    scene bg bedroom_01_magenta with push_right
    show anon hosp 10 tears at center_standee, standee_shake_h with dissolve
    anon "{cps=*1.5}小灯……太犯规了……你这家伙，怎么能唱出这种歌啊……{/cps}{w=0.1}{nw}"
    show anon hosp 09 confess at standee_step_in
    extend "\n{cps=*1.5}我听见了……在黑暗里我全都听见了……什么篱笆，什么以前的人，全都去他的吧！{/cps}"

    tomori kya "爱音……你在哭吗？对不起，我最后一句唱破音了……{w=0.15}{nw}"
    extend babble "\n不对，我不是想说这个……我是想说，墙角见，爱音……我们刚才，是不是在墙角撞上了？"

    show anon hosp 10 tears at standee_jump
    anon "{cps=*1.6}什么墙角见啊，笨蛋小灯！你怎么在这种时候还在记我随口说的冷笑话啊……{/cps}"

    play sound sfx_clothes_rustle
    tomori sad "我也是……我的手也在抖，停不下来……{w=0.15}{nw}"
    extend smile "\n我以为唱完这首歌我就会死掉，可是没有……爱音，你还在这里，你真的在听……"

    "我们像两个突然丧失了语言能力的傻瓜，在漆黑的被窝里紧紧抱成一团，颠三倒四、语无伦次地抢着说话。{w=0.2}{nw}"
    extend "我们总是哭在一起，也不知道是因为激动、因为爱情，还是因为感叹彼此这狼狈不堪的身世。{w=0.2}{nw}"
    "狂喜和酸楚把我们的脑子搅成了一团浆糊，我们一连说了几十句毫无逻辑、没头没尾的傻话，一会儿隔着眼泪发疯似的大笑，一会儿又手忙脚乱地去擦对方脸上的泪水，结果把眼泪抹得满脸都是。"
    "直闹到两个人都哭得精疲力尽、嗓子发哑，胸口一起一伏，爱音才吸了吸鼻子。{w=0.2}{nw}"
    show anon hosp 02 boast at standee_step_in
    extend "\n为了镇住这股让人快要昏厥过去的激动，她双手按住我的肩膀，在黑暗中故作威严地提高了声音："

    play music bgm_dialogue_warm fadein 1.5 loop
    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.6}小灯！首先，今天晚上你不准回医院，明天也不准，后天也不行！就睡在我的床上！{/cps}{w=0.1}{nw}"
    show anon hosp 01 smug at standee_nod
    extend "\n{cps=*1.5}其次，我不喜欢你愁眉苦脸的样子！{/cps}{w=0.1}{nw}"
    show anon hosp 08 gentle at standee_step_in
    extend "\n啊，但愿明天快来吧！你困不困，小灯？"

    tomori smile "……不困。"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.6}那我们就谈吧！把接下来的词怎么写、把我们以后的事全都定下来！{/cps}"

    "于是我们并排躺在被窝里，扯了近两个钟头。{w=0.2}{nw}"
    extend "\n天知道还有什么我们没谈到。"
    tomori soft "爱音兴高采烈地向我介绍她对未来的全部设想，简直把我们今后二十年的生活都筹划好了。{w=0.2}{nw}"
    tomori smile "按照爱音出的点子，我们将这样过日子：一天由她这个队长向我发号施令，穿什么演出服、唱什么歌，我样样照办；第二天倒过来——由我发号施令，她百依百从，陪我去捡一整天的石头；以后我们俩平分秋色指挥对方；将来要是有人故意不服从命令，那时我们先吵一架做做姿态，然后赶快和解。{w=0.2}{nw}"
    tomori yay "总括为一句话：我们的未来无限幸福。"

    play sound sfx_heartbeat
    camera at camera_heartbeat
    tomori calm "二十年。{w=0.3}{nw}"
    extend sadaway "\n她说明天，说后天，说二十年。{w=0.2}{nw}"
    extend bitter "\n而我的口袋里，只剩下不到一百四十个小时了。"
    tomori calm "这毫无意义。{w=0.2}{nw}"
    extend smile "\n但此刻躺在这里，听着她的声音，我竟然像个白痴一样完完全全地相信了。{w=0.2}{nw}"
    extend soft "\n为了让生活更甜美？谁也不知道。应该努力活着。{w=0.2}{nw}"
    extend calm "\n就这样。"

    # Part 4：二楼卧室、140小时与卖掉粉色吉他（暗底磨损 + Blender 3D 渲染）
    camera at default
    call editorial_part4

    # ==========================================
    # 5. 卧室之夜与海涛声（杜拉斯《情人》《中国北方的情人》）
    # ==========================================
    camera at default
    stop music fadeout 2.0
    scene bg bedroom_01_red with dissolve
    play music bgm_above_the_mountains fadein 2.5 loop
    show anon hosp 08 gentle at center_standee with dissolve

    "说了整整两个钟头，爱音的声音渐渐低了下去。"

    show anon hosp 04 shy_1 at standee_step_in
    anon "呐，小灯……刚才你唱的那首歌，我还有几个地方没听懂呢。"

    tomori ehh "……哪里没听懂？"
    "爱音没有去拿本子。"

    show anon hosp 08 gentle at standee_step_in
    anon "你看，这一句——“每次相撞都会作痛，却也因此浮现出轮廓”。{w=0.2}{nw}"
    extend "\n小灯写这一句的时候，脑子里想的到底是什么呀？"

    tomori sadaway "唔……想的是，不知道该怎么和别人靠近……{w=0.2}{nw}"
    extend sad "\n每次靠近，都会把彼此弄疼……"

    play sound sfx_clothes_rustle
    show anon hosp 01 smug at standee_step_in
    "爱音低低地笑了一声。她贴着我的唇边和耳朵轻声耳语。{w=0.2}{nw}"
    extend "\n手指顺着我的衣领边缘探进去，轻轻摩挲着我颈窝下方凸起的肩线。"

    show anon hosp 04 shy_2 at standee_step_in
    anon "骗人。刚才我扑过来抱住你的时候，小灯明明就没有躲开。{w=0.2}{nw}"
    extend "\n那现在呢？在这么黑的地方，什么也看不见……小灯摸到我的样子了吗？"
    show anon hosp 08 gentle at standee_step_in
    anon "你在歌里不是唱了吗……“希望你不要把心藏起来”。{w=0.2}{nw}"
    extend "\n可是小灯现在还在发抖，扣子也系得这么紧，把什么都藏在衣服底下。"
    show anon hosp 09 confess at standee_step_in
    anon "小灯，你那些歌词，到底是写给我的脑子听的，还是写给我的身体听的？{w=0.2}{nw}"
    extend "\n如果我想把你写在本子里的每一个字，都在你身上亲手摸一遍呢？"

    tomori soft "写歌的人，身体也参与了她的写作。那些词句进入她的头脑，同时又在这一刻进入了我们的身体。{w=0.2}{nw}"
    extend calm "\n爱音……那句词后面，其实还有半句。"

    show anon hosp 04 shy_1 at standee_step_in
    anon "……哪半句？"

    tomori soft "啊，找到了。{w=0.2}{nw}"
    extend smile "\n我不藏了，爱音。你刚才听到的每一个字……全都是因为想要触碰你，才写出来的。"

    play sound sfx_heartbeat
    camera at camera_heartbeat
    scene bg bedroom_01_magenta with dissolve
    show anon hosp 09 confess at center_standee, standee_step_in with dissolve
    "房间里突然安静下来。{w=0.2}{nw}"
    extend "\n她望着我。在发晕里，我几乎忘了她是谁，然后又想起来了。{w=0.2}{nw}"
    extend "\n爱音撑起身子，居高临下地望着我。"

    anon "我现在就要你。"
    tomori soft "嗯。"

    # NVL 杜拉斯式身体叙事段（一）
    camera at default
    hide anon with dissolve
    nvl clear
    vn_white "我朝她靠近过去。我不言不语，不再望着她。"
    vn_white "我站在床边，她坐在我对面。我垂下眼睛。她从下端抄起我的连衣裙，为我脱掉。她移开我的手臂，以便看我的身体。以便看我。我不看。我垂下眼睛，我听任她看。"
    vn_white "她站起来。我依旧站在她面前。我在等待。她又坐下来。她轻轻爱抚我依然瘦弱的身体——微微凸起的锁骨，还有侧腹还没有完全消退的医用胶布印痕。她像个瞎子那样闭着眼睛。她停下来。她把手缩回去。她睁开眼睛，压低了声音："
    nvl clear
    window hide

    show anon hosp 06 pain at center_standee with dissolve
    anon "你才这个年纪，还在生病。{w=0.2}{nw}"
    extend "\n这怎么行呢。"

    hide anon with dissolve
    nvl clear
    vn_white "我不回答。她说：这事有点吓人。她不等待我的回答。她微笑，然后哭了。而我，我望着她，我在想——那张脸似笑如哭——可能我将会终生爱她。"
    vn_white "怀着某种担心，就像我是一件易碎的物品，也带着持续的急切，她把我抱起来，放在床上。一等我被平放在床上，听凭摆布，她还是望着我，此时她重又感到害怕。她闭上眼睛，她不说话。她不敢碰我了。"
    vn_white "于是我采取主动了。我闭着眼睛为她解开居家服的扣子，解开一个又一个，褪下袖子。"
    vn_white "她不帮我。她不动。与我一样闭上眼睛。"
    vn_white "我在看，看她单薄的肩膀，与一张毫无防备的脸同样陌生，与刚才搁在我身上的手同样古怪，同样令人爱怜。我一遍又一遍看着她，而她听之任之，她让我看个够。我低声说："
    nvl clear
    window hide

    show anon hosp 04 shy_2 at center_standee with dissolve
    tomori soft "爱音挺漂亮的。"

    play sound sfx_clothes_rustle
    show anon hosp 08 gentle at standee_step_in
    "我吻她。她在我身边。我闭着眼睛吻。我抓住她的双手，把它们贴在自己脸上。那双手。我抓住那双手，把它们贴在我自己的身上。{w=0.2}{nw}"
    "这时候她动弹了，她把我搂进怀抱，在我瘦小发颤的身体上方轻轻俯下身。正当她慢慢用自己的体温盖住我、还没有真正触碰到我的肌肤的时候，窗边关闭的百叶窗滤去了夜色。减弱了的市声传来，在黑暗的房间里听来十分遥远。而爱音的声音变得与她的双手一样贴近。"

    show anon hosp 09 confess at standee_step_in
    anon "我会弄疼你的。"
    tomori calm "我知道。"
    show anon hosp 10 tears at standee_step_in
    anon "我爱你，我不想跟你撒谎：这种疼痛，它以后不会再来，永远不会，真是这样的，我可以起誓。{w=0.2}{nw}"
    show anon hosp 09 confess at standee_step_in
    extend "\n闭上眼睛。我要做了。闭上眼睛，我的小灯。"
    tomori kya "不，不闭眼睛。{w=0.15}{nw}"
    extend soft "\n其他什么我都肯做，就是不能闭眼睛。"

    play sound sfx_clothes_rustle
    hide anon with dissolve
    "我试图往后缩。{w=0.2}{nw}"
    extend "她用手掌托住我的后背。{w=0.2}{nw}"
    extend "我不再企图挣脱。"

    # NVL 杜拉斯式高潮海涛交融段（二）
    play bgs bgs_beach_night fadein 3.0 loop
    scene bg bedroom_01_purple with slow_dissolve
    nvl clear

    vn_white "我常说我记得自己当时如何惧怕。就像我记得她的皮肤，她的温存。记得这番温存如何也带着惊恐。"
    vn_white "我闭着眼睛感受她的温存，我感受那暖和的肌肤，那嗓音，那怀有惧意的心脏，那悬在我上方、把我整个人严严实实拢在影子里的单薄身躯。我成了她的孩子，千早爱音的孩子了。她不吭气，她在哭，她怀着如此猛烈的爱情做这件事情，不由泪流满面。"
    vn_white "我感到她的嘴在燃烧，我们将彼此不分地搅在一起合二为一，不再能认出谁是谁，在前、在后还是在过程中，将在一起失去踪迹，失去名字，因为忘记了那个倒计时的死亡，一块一块地忘记，从一个时间到另一个时间，从一个名字到另一个名字。"
    vn_white "道路打开了。她放在我臂上的张开的手预示着一个多形状的、惟一的未来，这手光彩夺目，似羽毛一样轻飘，在我眼里似鲜艳的花朵。"
    vn_white "我们在最后的几声低唤里软了身子，喘气声逐渐变成甜蜜而喑哑的哭声，变成了互相交融的温暖身体，黑夜里的炙热呼吸。"
    nvl clear

    vn_white "我记得。我是最后一个还能回忆的人。我还能听见房间里的海涛声。我也记得曾经这样在笔记本上写过，说海涛声像街区的市声。我记得甚至写过这样的话，说那天大海就在情人们的房间里。"
    vn_white "情人们的床。"
    vn_white "我们可能睡着了。我们不知道。"
    vn_white "市声又回来了。它是连续的，浑成的。它无远不届。"
    vn_white "透过百叶窗，亮光投在床上。我们交握的手指上，那枚白色的创可贴已经卷起了边。"
    vn_white "门外是长长的过道，此刻空无一人；玄关处并排放着我们的两双鞋子，显得既孤独又亲切。"
    nvl clear
    window hide

    scene bg bedroom_01_rose with dissolve
    play sound sfx_clothes_rustle
    "我醒了。我看着她。百叶窗缝里漏进来的夜风有些凉，她睡梦中轻轻打了个寒噤，我伸手把搭在床尾的旧外套拉上来，严严实实地盖在她裸露的肩膀上。{w=0.2}{nw}"
    "这天夜里，但凡我们中间有一个人稍微翻身醒来，另一个人也会跟着睁开眼睛，因此谁也不会感到孤单。很多事情在黑夜里存在，到了白天便不复存在了。{w=0.2}{nw}"
    extend "外面的嘈杂声如此邻近，我们听到它在摩擦百叶窗，好像有人在房间里穿行似的。"
    show anon hosp 08 gentle at center_standee with dissolve
    "她醒了，但不动弹。她半睡半醒。她这样子像个少年。{w=0.2}{nw}"
    extend "\n沉默。{w=0.2}{nw}"
    "她凑到我身边，她一言不发。我指给她看那些植物，低声说话，很低，我微笑。而她，她说我不应该在意这些植物，说它们早就死了。说她老忘了给它们浇水。说她永远想不起来的。她的声音很低，就像防范街上的人听见似的。"

    show anon hosp 03 curious_2 at center_standee
    anon "你不开心。"

    "我微笑，做了个小小的手势："
    tomori calm "也许吧。"

    show anon hosp 08 gentle at standee_step_in
    anon "这是因为我们醒着做爱。到夜里就没事了。"

    "她望着我。我看到了。我垂下眼睛。{w=0.2}{nw}"
    extend "\n我也望着她。我看到她。我后退。我望着她瘦长、灵活、完美的身躯，与她的双手同样具有某种奇妙之美的身躯。"
    tomori smile "我从未见过你这么美。"

    "爱音盯着我看，好像我什么也没说似的。{w=0.15}{nw}"
    extend "\n她望着我，她只顾得上做这件事，望着我，以便日后，在她自己身上，保留一些属于这个站在她面前的女孩的东西。"

    show anon hosp 08 gentle at center_standee
    anon "你老有点不开心，不是吗……"

    "沉默。我微笑。"
    tomori calm "老有点不开心？……是的……{w=0.15}{nw}"
    extend sadaway "\n也许……我不知道……"
    show anon hosp 03 curious_2 at center_standee
    anon "……到底什么原因？"
    tomori sadaway "什么也不是……是我自己……{w=0.15}{nw}"
    extend sad "\n我就是这个样……"
    show anon hosp 06 pain at center_standee
    anon "是你家里人说的吧？"
    tomori calm "是的。"
    anon "他们怎么说的？"
    tomori bitter "他们说：让她安安静静呆着。{w=0.15}{nw}"
    extend sadaway "\n她就是这个样，她永远会是这个样。"

    show anon hosp 08 gentle at center_standee
    anon "你睡着了。我洗了个淋浴。"

    play sound sfx_glass_clink
    show anon hosp 10 tears at standee_step_in
    "她去给我倒一杯水。她动情地望着我，直至流泪。{w=0.2}{nw}"
    extend "\n她目不转睛望着我，她望着我身上的一切。我把杯子还给她，她把它放在茶几上。她又坐下来。她继续望着我。{w=0.2}{nw}"
    "我，可能我愿意她再说点话，但我没说出来。我一言不发。我再次让人难以猜到我到底在想什么。"

    show anon hosp 08 gentle at center_standee
    anon "你饿了吧。"

    "我点头：可能我饿了。是的，可能是饿了。我也闹不清。"
    tomori calm "出去吃饭太晚了。"
    show anon hosp 07 normal_1 at center_standee
    anon "有通宵营业的饭店。"
    tomori soft "那就随你吧。"

    hide anon with dissolve
    "我们相望，然后我们避开对方的眼睛。{w=0.2}{nw}"
    play ambient_sfx sfx_shower volume 0.55
    extend "\n我下床。我去淋浴。{w=0.2}{nw}"
    extend "\n她过来。她帮我洗，她用手掌，不擦肥皂，很慢很慢。"

    show anon hosp 08 gentle at standee_step_in with dissolve
    anon "你的皮肤像雨水一般柔滑。{w=0.15}{nw}"
    extend "\n你的手腕，还有脚踝也这么细巧，这挺怪的，你能解释吗……"
    tomori calm "我解释不了。"

    hide anon with dissolve
    nvl clear
    vn_white "我们相对微笑。欲望重又袭来。我们停止微笑。她帮我穿上衣服。然后依旧望着我。看着我。而我，我已经占据了爱音的心。我知道这个事实。我望着她，而且我第一次发现，她与我之间始终存在另一个空间。从我们第一眼看对方起。一个无边无际，不容侵犯，起着保护作用的别处。它将保护我们不受任何我不知晓的事情的伤害。我还发现我，自己，也在保护她免受各种事件的损害，如成年、死亡、夜晚的忧伤，还有爱情和欲望产生的孤独。"
    vn_white "我望着一切，我环顾这场所，这间屋子，这个情人，以及透过百叶窗看到的这个夜晚。我说天黑了，说天突然变冷了。"
    vn_white "我望着她。我感到一种无法克服的忧伤。"
    nvl clear
    window hide

    play sound sfx_clothes_rustle
    show anon hosp 08 gentle at standee_step_in with dissolve
    "爱音来到我身边，她把自己的身体贴上我的身体。"
    anon "我知道你此刻的感受，这种无望，这种难受。这不奇怪，有时候，在夜里某一时刻，人会感到慌乱不安，我知道人那时没着没落的。{w=0.2}{nw}"
    show anon hosp 09 confess at standee_step_in
    extend "在夜里，睡不着的时候，人人都会这样的。可能我们会相爱，不过现在还不知道。"

    "然后她听任我哭泣。{w=0.2}{nw}"
    extend "然后我说我也许饿了。{w=0.2}{nw}"
    extend "\n我跟她一同笑了。我慢慢地说："
    tomori smile "我早就爱上你了。{w=0.15}{nw}"
    extend soft "我永远不会忘记你。"

    show anon hosp 08 gentle at center_standee
    anon "我曾在某地听到别人跟我说同样的话……{w=0.15}{nw}"
    show anon hosp 07 normal_2 at center_standee
    extend "\n我记不清在什么地方了。可能在伦敦。"

    hide anon with dissolve
    "然后我望着她。久久地。望着她睡去的身体，她的双手，她的脸。我低声跟她说她疯了。就像跟她说我爱她一样。{w=0.2}{nw}"
    "晨曦将至、夜色未退的时候，我们在玄关的穿衣镜前拢了拢外套。我注意到我们在一夜之间好像都长大了许多。我们两个人在这短短一个不眠之夜里一起长了许多年纪，仿佛已经有几百岁了，长到了沉眠在疯人与流放者身上的那种古老的年纪。"
    show anon hosp 08 gentle at center_standee with dissolve
    "我望着她敞开的睡袍领口，望着她暖和的肌肤、手腕与颈窝，声音很轻："
    tomori soft "我渴望你。"

    "我们相对微笑。"
    show anon hosp 09 confess at standee_step_in
    anon "怎么又哭了呢？"
    tomori sadaway "没有，我想到很多事情。"
    show anon hosp 07 normal_1 at standee_nod
    anon "你可以说是被沙子吹的，但是这里没有风。"

    # ==========================================
    # 6. 砂堤外的海洋与去海边的约定
    # ==========================================
    scene bg bedroom_01_magenta with dissolve

    tomori calm "我听到一片海洋的声音，就在我身旁，只隔着爱音这间卧室的一道薄墙与砂堤。{w=0.2}{nw}"
    extend neutral "\n这片海洋到底是什么东西，之后要怎样摆布我，我连一点头绪都没有。{w=0.2}{nw}"
    tomori soft "我意识到，这片巨大的海浪早晚要从堤岸上翻涌过来，把一切淹没——那时……啊，那时才好呢，我就可以彻底快乐了。"
    tomori calm "只要静静听着它，给它宏大的声音催眠着，这几个月以来积压在胸口的零星悲痛与耻辱，就全都能平复下来；{w=0.2}{nw}"
    tomori soft "固然初中乐队散开的记忆依然使我伤心，可是再也没有那种被人唾弃的可耻与难堪的意味：在这间屋子里，一切都显得那么自然，差不多称得上是甜美的了。"

    tomori soft "我们一定要去海边一次，可以吗？"
    show anon hosp 08 gentle at center_standee with dissolve
    anon "为什么，一定要海边？"
    tomori calm "我听到了大海的声音。"

    "沉默。她没有觉得奇怪，也没有反驳我。{w=0.2}{nw}"
    extend "因为她也记得——就在刚才，当疼痛离开这具瘦小的身体、消失在陌生的幸福感里时，房间里确实回荡着轰鸣的海涛声。街区的市声摩擦着百叶窗，就像海浪拍打着海岸。{w=0.2}{nw}"
    "那天夜里，大海就在情人们的房间里。"

    show anon hosp 07 normal_1 at standee_step_in
    anon "好。我们去海边。{w=0.15}{nw}"
    show anon hosp 08 gentle at standee_nod
    extend "\n随你的意，什么时候去都可以。"
    tomori sadaway "我还是忘不了之前的乐队。"
    show anon hosp 01 smug at standee_nod
    anon "让我去解决吧。"

    hide anon with dissolve
    call editorial_part6_suitcase
    call editorial_part6_cathedral

    nvl clear
    vn_white "是的，爱音，哪怕明知道只剩下最后一百四十个小时，哪怕明知道这一切建立在一场谎言之上，人也会不由自主地相信：“真正的、诚挚的激动是能够彻底触动灵魂的；”"
    vn_white "在这原本无血无肉、飘渺的幻想之中，是有着可以感触得到的、活生生的东西的。"
    vn_white "哪怕直到最后一分钟我们依然双手空空，我也甘愿同她一起沉溺在这场空想之中。纵令明天醒来还有死亡的苦恼，此刻也全都忘光了；在她的声音里，我依然贪婪地做着关于明天、关于后天、关于漫长未来的另一个梦，另一个片断的梦。"
    nvl clear
    window hide

    stop music fadeout 2.5
    stop bgs fadeout 2.5
    scene bg black with slow_dissolve
    $ persistent.cleared_chapter_9 = True
    jump ch10_wedding
