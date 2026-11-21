## ch10_wedding.rpy - 第十章：白色的二手婚纱与死刑的真相
## 严格对标《素材与视觉资产规范.md》与《图片.rtf》视觉素材规范
## 视角说明：本章为千早爱音第一人称视角（“我”=千早爱音）
## 背景规范：bedroom_01_blue~magenta~purple~rose~red~orange / corridor_04_blue~orange / corridor_01_orange / rehearsal_room_01_blue~orange / station_01_blue~orange / station_02_orange~blue / cloud_01_orange / bg black
## 立绘规范：anon hosp 01~10 全套差分 / taki 01 glare~02 normal_1~02 normal_2~03 sad
## 三层旁白与高密度演出系统：纯环境旁白（无立绘无头像） / 对方动作观察旁白（仅立绘无头像） / 角色台词与高松灯头像差分（换行 extend + {nw} 疾奏）

label ch10_wedding:
    $ current_chapter = 10
    $ quick_menu = True

    # ==========================================
    # 1. 黎明前的凝视与假死刑判决书的真相（三岛由纪夫《金阁寺》+ 陀思妥耶夫斯基《白夜》）
    # ==========================================
    scene bg bedroom_01_blue with fade
    camera at camera_gentle_sway
    play music bgm_above_the_mountains fadein 2.0 loop
    play bgs bgs_beach_night fadein 2.5 loop

    "我听到一片海洋的声音，就在我身旁，只隔着一道砂堤。{w=0.2}{nw}"
    extend "\n那是在伦敦。阴冷的雨季，狭小的寄宿房间。这片海洋是什么东西，要把我怎样摆布，那时的我连一点观念都没有。{w=0.2}{nw}"
    "我只意识到这海洋要从堤岸上翻过来，那时……啊，那时才好呢，我就可以完全快乐了。"

    stop bgs fadeout 2.0
    camera at default
    scene bg bedroom_01_magenta with dissolve
    play sound sfx_clothes_rustle
    camera:
        easein 1.2 zoom 1.06 yoffset 8

    "小灯终于睡熟了。{w=0.15}{nw}"
    extend "\n她松开了乱蓬蓬的短发，一只手背搭在另一边脸颊和嘴唇上，这使她的脸显得更小。{w=0.2}{nw}"
    extend "虽说是手背，手指却是舒展着的，较长的中指直伸到下巴颏下面。她的右手放在被头边上，手指轻柔地抓着被头，一点也没有防备。"

    show anon hosp 08 gentle at center_standee with dissolve
    "我撑起酸痛的胳膊，低头看着枕边高松灯熟睡的脸。{w=0.2}{nw}"
    extend "\n时间越是流逝，昨夜这间狭小的天地越是远离开去，我便越是怀疑这几个昼夜发生的一切是否实有其事。{w=0.2}{nw}"
    show anon hosp 06 pain at center_standee
    "若以为是幻觉便似乎是幻觉；但就幻觉而论，她呼吸的细节又过于宛然在目，而如果实有其事，她此刻毫无防备地蜷缩在我怀里的模样，又过于完美无缺。"

    hide anon with dissolve
    play sound sfx_heartbeat
    camera at camera_heartbeat
    "我将一只胳膊肘支在枕头上，一边盯着小灯的手，一边在心里喃喃自语：“简直是一只活手嘛。”{w=0.2}{nw}"
    extend "活着这个事实当然摆在眼前，但这句话一经在脑海里冒出来，又留下了令人毛骨悚然的弦外之音。"

    # 【D 演出：黑底白字紧缩压迫独白 → 诊室真相纯白黑字负片反色硬切（无人物剪影）】
    camera at default
    window hide
    scene ed_d_dark_ink with dissolve

    ed_d_black "被我用“只剩七天”的谎言哄骗着、此刻熟睡得不省人事的小灯，就算不是停止，也是被我亲手截断了原本正常的时间，沉入了只属于我一个人的暗井里，难道不是吗？"
    ed_d_black "对走投无路的我来说，也许她就是生命本身，是可以放心地去触摸、去独占的生命。\n当看见她颈窝与侧腹上残留的微红印记时，我终于翻然觉悟到了那种从不曾拥有过的对存在的确信。"
    ed_d_black "这里存在着她年轻而易碎的身体，存在着不得不通过欺骗来留住她的、来自我的念想。她的身体接纳了我那种走投无路的爱的情感，从而将我与所有的存在之环铆接成一体。\n要留住熟睡的她并不费吹灰之力，她恐怕不会反抗。黑暗的空落与狂喜同时在我心里扩展。"

    ed_d_black "我费力地搜寻这两天的记忆，就像为重新粘好一个破旧瓷罐的裂缝而用一把镊子把瓷器的碎片捡在一起一样。\n其实我看到的不是我自己，看到的是另外一个人在做这些胆大包天的事儿，一个叫千早爱音的骗子，而不是我。"
    ed_d_black "看着她熟睡的脸庞，听着她轻浅的呼吸，一想到只要这个谎言被戳穿，我就再也看不见这双黄褐色的眼睛毫无阴霾地对我睁开了，再也听不见她对我说“喜欢”了，这多痛心啊！多让人胆寒啊！\n如果一切都按照理智进行就好了，可是相反，好像一切都不由我们，而是由着某种疯狂的惯性在进行着。"
    ed_d_black "就仿佛我用一张假死刑判决书偷窃了她的生命和爱情——是的，不要否认，所有人准都会这样谴责我的。\n我这十六年里做了不少蠢事、逃避了不少丢脸的丑事，但是其中只有拐走高松灯这一件，我不后悔，而且死也不可能后悔。"
    ed_d_black "哪怕从定义上说，那“最后七天”就是彻头彻尾的谎言，是一种非实在的伪装现实，是一场类似马戏团或剧场里蹩脚魔术师制造的海市蜃楼；可为了留住她，我已经接纳了来自内心的恶念，并且心甘情愿按照自己的全部实力为这个恶念服务。"
    window auto

    scene bg bedroom_01_blue with dissolve
    show anon hosp 06 pain at center_standee with dissolve
    "我支起胳膊肘，把脸贴近她的脸，听着她深沉的鼻息——{w=0.2}{nw}"
    extend "因为我比谁都清楚，两天前下午四点半在医院走廊那头，隔着半掩的诊室门，我听见那个戴眼镜的主治医生对着电话那头说的究竟是什么——"

    # 闪回：医院走廊诊室门口的真相（0.22s 焦橙底片负片定格 → 刺眼纯白诊室真相三连疾切）
    hide anon
    window hide
    play sound sfx_strike
    $ photosnap(duration=0.22)
    scene ed_d_clinical_white with flash_white
    ed_d_white "“高松太太，您放心，501床的复查结果没有任何问题，\n那孩子只是贫血和神经性低热，身体已经完全康复了。”"

    window auto
    scene bg corridor_04_blue with ed_cut
    camera:
        easein 0.5 zoom 1.05

    show anon hosp 03 curious_3 at center_standee, standee_step_back with dissolve
    anon "……完全康复了？"

    hide anon
    camera at default
    scene bg bedroom_01_rose with dissolve
    nvl clear

    vn_white "真的，要是在另一个时候，我会相信，这全部生活并不是感情冲动的结果，不是海市蜃楼，不是想象力的欺骗，而所有这一切都是现实，真真切切，实实在在。"
    vn_white "小灯，请告诉我，为什么在这样的时刻，精神反而受到压抑？为什么我的两颊在发烧？为什么我全身感到那么难以形容的高兴？"
    vn_white "为什么这一个不眠之夜在无穷的愉快和幸福之中就像一眨眼，一眨眼就过去了，而在朝霞映在百叶窗上，闪烁出玫瑰色的光芒，梦幻似的游移不定的晨光，照亮东京这里阴暗的房间时，我已经精疲力尽，疲惫不堪，倒在床上，灵魂高兴不已，但心里却带着甜丝丝的、令人疲倦的隐痛？"
    vn_white "是的，小灯，一旦上当受骗，我就会情不自禁地相信：真正的、诚挚的激动是能够触动灵魂的，还会情不自禁地相信，在我那无血无肉、虚无飘缈的幻想之中，是有着可以感触得到的、活生生的东西的。"
    nvl clear
    window hide

    scene bg corridor_04_orange with fast_dissolve
    doctor "是啊，死神早就退场啦！{w=0.2}{nw}"
    extend "\n您和她父亲听说没有后遗症，这下总算可以松一口气了。"

    scene bg bedroom_01_rose with fast_dissolve
    show anon hosp 09 confess at center_standee with dissolve
    "小灯，这就是为什么当我第一次遇见你的时候，我会那样发疯似的高兴。{w=0.2}{nw}"
    show anon hosp 10 tears at center_standee
    extend "\n我还记得那时候要向你开口有多难，多残忍。想要抓住你的欲念太强烈，简直找不到话来表达。{w=0.2}{nw}"
    "这个躲躲闪闪的游戏、这番幼稚的欲言又止和你的眼泪，这一切本应该使人想到，这就是爱情。{w=0.2}{nw}"
    show anon hosp 08 gentle at center_standee
    extend "\n一个爱情故事，一场令人目眩的爱情。始终没有结束。永远没被遗忘。"

    hide anon
    play sound sfx_heartbeat
    camera at camera_heartbeat
    scene bg corridor_04_blue with fast_dissolve
    doctor "说是为了防止她回学校再做傻事，明天上午十点办完出院手续，千叶那边的专车就直接把她接过去，让她彻彻底底静下心来封闭改造半年。{w=0.2}{nw}"
    extend "\n评估单我签好字放在外头分诊台上了……"

    camera at default
    scene bg bedroom_01_purple with dissolve
    nvl clear

    vn_white "然后，有一次这事情发生了——你上了我的床。"
    vn_white "我们原本是两个毫无瓜葛的女孩，对彼此的身体是陌生人。自从我听说了你以前在那个乐队里受过的伤，看到你在人群里瑟瑟发抖的样子，从那时候起，我就害怕外面的世界会杀了你。"
    vn_white "可是，不，幸好，你把一切都忘了，把过去的乐队、把外面的暴雨全都忘了。你感到那么幸福，你哭了。我也哭了。这就像过节一样，不过更深刻——你看，小灯，人们不笑，反而会哭。"
    vn_white "连我自己也很难原谅我自己。这是理所应当的吧？"
    vn_white "谁都会撒了谎之后心虚。我也为撒谎感到害怕。可我不能自制，好比人老想到死，嗯，有点像。"
    vn_white "我哄骗了你，也哄骗了我自己——我告诉你，我们的生活只剩下最后这几天了，过了这几天一切就都结束了。"
    vn_white "我不知道，靠着向你灌输这种绝境、靠着这种谎言从你身上换来的温存与交付，到底算不算正确。"
    vn_white "这感觉就像是一场偷窃。我把你从她们身边偷出来，又从你手里偷走了这几天的生命，像个小偷一样独自守在昏暗的房间里清点赃物。我为此感到羞耻，感到心惊肉跳；可是小灯，请你原谅我——除了撒谎，除了做这个卑劣的小偷之外，我已经没有任何别的办法能留住你了。这一别就不知道下一次该怎么再认识你了。我会因为单恋而发狂的。"
    nvl clear
    window hide

    # ==========================================
    # 2. 晨光百叶窗与“我想为你穿一次婚纱”
    # ==========================================
    scene bg bedroom_01_orange with dissolve
    play music bgm_dialogue_warm fadein 2.0 loop

    "晨光透过百叶窗缝落在床单上。这像是旋转过后的监狱栏杆。{w=0.2}{nw}"
    extend "\n街道又要苏醒了呢。阳光把它的光和热撒到所有阴影所不及处。驱赶走夜晚长久累积下来的冷气。"

    show anon hosp 06 pain at center_standee with dissolve
    "我看着她那张脸。毫无戒备。本来也手无寸铁。{w=0.2}{nw}"
    "现在，小灯的心里面，也会有类似的感觉吗？可是我欺骗了她。她就是再怎么让身心都暴露到阳光下，都会因为一举一动都在搅动清冷的空气，借由寒风无处不在的提醒意识到自己时日无多这件事。{w=0.2}{nw}"
    "我带她逃离了窗户只能拉开一指宽的监狱，然后把她带进了更加令人无望的境地里。"
    show anon hosp 10 tears at standee_tremble
    "千早爱音，你怎么能坏成这样？{w=0.2}{nw}"
    show anon hosp 08 gentle at center_standee
    extend "\n好想叹一口气。呼不出来。也许是因为怀里有个人，胸腔的起伏会惊扰到她的。{w=0.2}{nw}"
    extend "\n我低头看去——"

    play sound sfx_clothes_rustle
    "小灯醒着。{w=0.15}{nw}"
    extend "\n她把脸贴在我的胸口，手指一下下数着我的发梢。"

    tomori calm "学校里的那些女孩子那么饶舌，你以前的乐队、还有我以前的乐队，她们很快就会知道我们的事情。{w=0.2}{nw}"
    extend sadaway "\n她们会痛苦的。可能她们已经知道了。{w=0.2}{nw}"
    extend soft "\n正因为我使你们痛苦，我们也该结婚了。"

    show anon hosp 08 gentle at standee_nod
    anon "是的。"

    tomori smile "我想为你穿一次婚纱。"

    show anon hosp 03 curious_3 at standee_jump
    "……出于某种本能，我的身子往前微微弯了一下，而我仿佛下一秒就要脱口而出一声“哈？！”。{w=0.2}{nw}"
    show anon hosp 08 gentle at center_standee
    extend "\n但是，没有。现在不需要表演那些东西。"

    show anon hosp 09 confess at standee_step_in
    anon "好啊。从第一夜起……我就很怕这个事……{w=0.2}{nw}"
    show anon hosp 04 shy_2 at standee_step_in
    extend "\n怕我做不好你的新娘，也怕做不好你的新郎。"

    "她没有回答这句话，只是顺着自己的幻想往下说："
    tomori soft "然后我们就去漫游世界。"
    show anon hosp 08 gentle at standee_nod
    anon "没错。是这样的。到那时候，我们已经坐上离开这里的船了。{w=0.2}{nw}"
    extend "\n就该是这样的。"

    hide anon with dissolve
    "……{w=0.2}{nw}"
    extend "沉默。{w=0.2}{nw}"
    extend "她问："

    show anon hosp 07 normal_1 at center_standee with dissolve
    tomori ehh "那时候船在什么地方？"
    anon "东京湾中。"
    tomori neutral "为什么在那儿？"
    show anon hosp 01 smug at standee_nod
    anon "我随便一说。"

    play sound sfx_clothes_rustle
    scene bg bedroom_01_rose with flash_warm
    show anon hosp 02 boast at center_standee, standee_step_in with dissolve
    camera:
        easein 0.6 zoom 1.08 yoffset 10
    "她噗嗤一声笑了出来，伸手捶了一下我的肩膀。{w=0.15}{nw}"
    extend "\n我顺势抓住她的手腕，把她整个人翻过来按在被窝里，低头去挠她的痒，然后贴着她的耳朵一遍又一遍地念叨："

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.5}我喜欢你，小灯。我喜欢你。{/cps}{w=0.05}{nw}"
    show anon hosp 01 smug at standee_step_in
    extend "\n{cps=*1.5}你没有一口手提箱重，我能把你扔到床上，像一口小箱子。我喜欢你，听见没有？{/cps}"
    tomori kya "{cps=*1.4}听见了……好痒……{/cps}{w=0.05}{nw}"
    extend smile "\n{cps=*1.4}我也喜欢你，爱音……喜欢你……{/cps}"

    show anon hosp 08 gentle at center_standee
    "我们在被单上滚作一团，她喘着气笑个不停，直到眼角又沁出泪花。{w=0.2}{nw}"
    extend "\n我停下来，用双手撑在她身体上方，低头吻了吻她的鼻尖。{w=0.2}{nw}"
    extend "\n沉默重新降临。我说："

    camera:
        easeout 0.6 zoom 1.0 yoffset 0
    scene bg bedroom_01_orange with dissolve
    show anon hosp 08 gentle at center_standee with dissolve
    anon "我们到海边去吧。{w=0.15}{nw}"
    show anon hosp 07 normal_1 at center_standee
    extend "\n就在九十九里滨那边，我订了一个看得到海的房间。"
    tomori neutral "什么时候去？"
    show anon hosp 08 gentle at standee_nod
    anon "随你的意。今天晚上。今天夜里。{w=0.15}{nw}"
    extend "\n或者今天白天也可以。"
    tomori concern "那么学校呢？还有其他人……"

    show anon hosp 01 smug at standee_step_in
    "我忽然改口用起了敬语，故意逗她："
    anon "这不要紧。就是以前，您也不是每天上学。{w=0.15}{nw}"
    show anon hosp 07 normal_1 at standee_nod
    extend "\n您经常一个人跑到水族馆和天文部去。我打听过。"

    play sound sfx_clothes_rustle
    hide anon with dissolve
    "小灯稍稍后退了一点，缩进枕头那边。她忽然显得有些害怕。{w=0.2}{nw}"
    show anon hosp 06 pain at center_standee with dissolve
    extend "我使劲盯着她看，接着我想到终究会失去她，想到她口袋里所剩无几的时间，感到无法忍受，遂闭上眼睛，好像只要什么都看不到的话，时间就不再流逝。"

    show anon hosp 10 tears at standee_tremble
    anon "一想到要与你别离，我就感到我的心就掉进了胃里，一点一点被腐蚀被灼烧……{w=0.2}{nw}"
    show anon hosp 09 confess at standee_step_in
    extend "\n我快疯了……我不能离开你，这不可能，可是总有一天会变成那样，我知道。"

    show anon hosp 08 gentle at center_standee
    "我不再望着她。我闭着眼睛抚摩她的头发。{w=0.15}{nw}"
    extend "\n她更加后退，抱紧膝盖坐在床角。我问："
    show anon hosp 03 curious_2 at center_standee
    anon "为什么你突然害怕那片海滩？{w=0.15}{nw}"
    extend "\n不是你说想去海边的吗？"

    scene bg bedroom_01_purple with dissolve
    show anon hosp 06 pain at center_standee with dissolve
    tomori sadaway "我小时候跟家里人去过海边，有一次我可是吓着了……{w=0.2}{nw}"
    extend concern "\n海滩上一片荒凉，什么也没有，没有村庄，没有……任何东西，任何人……{w=0.2}{nw}"
    tomori sad "只有几个疯子，几个流浪汉，在防波堤下面游荡……还有女人，从城里赶出来的女人，夜里在海滩上又哭又笑。"

    show anon hosp 08 gentle at standee_step_in
    "小灯闭上眼睛，脸无血色。我挪过去，贴到她身边。"
    anon "你最害怕什么，大海还是人？"
    "她说，她几乎是喊叫出来："
    tomori kya "{cps=*1.5}怕人。怕你。{/cps}{w=0.1}{nw}"
    extend sad "{cps=*1.5}你，千早爱音。{/cps}"

    show anon hosp 06 pain at standee_step_back
    "我久久沉默。那会儿她仿佛认不出我来了。{w=0.2}{nw}"
    extend "\n她缩在那里，好像一只小兔子，走投无路，只得任人摆布。是我不好。我吓到你了呢。我问："
    show anon hosp 08 gentle at center_standee
    anon "那些又哭又笑的女人，她们从哪里来的？"
    "小灯其实不太知道。于是她就编造了，信口开河。"

    tomori babble "她们是从海上过来的……藏在帆船里……{w=0.2}{nw}"
    extend sadaway "她们完全丧失了理智，整个儿疯了，由于过度害怕，由于烈日、森林，由于搞砸了一切，被所有人抛弃，每天夜里边哭边笑，长篇大论地说话，还唱歌……"
    "说着，她真的轻轻哼起了一段不成调的、像摇篮曲又像挽歌一样的旋律。"
    tomori soft "你瞧……我记得这首摇篮曲……"

    play sound sfx_clothes_rustle
    scene bg bedroom_01_orange with dissolve
    show anon hosp 08 gentle at center_standee, standee_step_in with dissolve
    "我笑了，把她重新揽回怀里，用额头抵着她的额头。"
    anon "你在编……这不说明任何问题。{w=0.15}{nw}"
    show anon hosp 07 normal_1 at standee_step_in
    extend "\n你怎么知道这些事情的？是谁跟你讲的？"
    tomori sadaway "为了引起你的兴趣……{w=0.15}{nw}"
    extend soft "我想到什么说什么……"
    show anon hosp 09 confess at standee_nod
    anon "傻瓜。不用编故事，我也已经对你着迷到无可救药了。"

    hide anon with dissolve
    call editorial_part5a
    scene bg bedroom_01_orange with dissolve

    "她似乎筋疲力尽，把脸埋在我颈窝里，闭上眼睛想睡觉。{w=0.2}{nw}"
    extend "\n午后的热气漫进房间，她的呼吸渐渐变得绵长而均匀，终于沉沉睡去。"
    show anon hosp 08 gentle at center_standee with dissolve
    play ambient_sfx sfx_clock_tick volume 0.45
    "我看了看床头的闹钟，轻轻抽出手臂，替她掖好被角。{w=0.2}{nw}"
    extend "\n她迷迷糊糊地睁开一线眼皮，抓着我的衣袖问我要去哪儿。我俯下身吻了吻她的发顶，笑着跟她说："

    show anon hosp 07 normal_1 at standee_nod
    anon "你不是说想为我穿一次婚纱吗？{w=0.15}{nw}"
    show anon hosp 08 gentle at standee_step_in
    extend "\n趁你睡午觉，我出门去买点婚礼道具——头纱、戒指，还有今晚去海边要带的东西。乖乖等我回来。"

    hide anon with dissolve
    "她安心地“嗯”了一声，翻了个身，把脸埋在留有我气味的枕头里，重又坠入梦乡。{w=0.2}{nw}"
    scene bg corridor_01_orange with dissolve
    play sound sfx_door_close
    extend "\n我拿起包，轻轻带上房门。"

    # ==========================================
    # 3. 池袋 Livehouse RiNG：与椎名立希的对峙与真相爆发
    # ==========================================
    stop music fadeout 1.5
    scene bg rehearsal_room_01_blue with dissolve
    play ambient_sfx sfx_metal_door_open
    play sound sfx_footsteps
    play music bgm_at_the_sea fadein 1.5 loop

    "我推开池袋 Livehouse RiNG 的大门，顺着台阶走下去。{w=0.2}{nw}"
    extend "\n下午的地下演出厅空空荡荡，只有吧台那边亮着几盏射灯。{w=0.2}{nw}"
    extend "椎名立希就站在吧台后面。自从灯从医院失踪后，她显然没有睡过一个好觉。{w=0.2}{nw}"
    "我在她面前几步远的地方站定。场面僵住了。"

    show taki 01 glare at anon_burst_in
    "我怀着按捺不住的好奇心看她。{w=0.15}{nw}"
    extend "\n她抬起头，认出了我，一把撑住吧台冲了出来："

    taki "{size=*1.15}{cps=*1.6}……千早爱音？！你是干什么来的，你？！{/cps}{/size}" with shake_h

    show taki 01 glare at unfocus_standee_left
    show anon hosp 07 normal_2 at focus_standee_right with dissolve
    anon "我以为你是知道的。事关高松灯。"

    show taki 01 glare at standee_left_press, standee_shake_h
    show anon hosp 07 normal_2 at unfocus_standee_right
    taki "{cps=*1.5}灯？！你把灯拐到哪里去了？！她才刚从医院抢救过来，你这个突然冒出来的家伙到底对她灌了什么迷魂汤？！{/cps}{w=0.1}{nw}"
    extend "\n{cps=*1.6}我警告你，你要是敢耍什么花样——说到动手，我随时奉陪！{/cps}" with shake_h

    show taki 01 glare at focus_standee_left, standee_tremble
    "她攥紧了拳头，因为极度的担忧和愤怒，声音都在发抖，嘴唇扯出一个狰狞的冷笑。{w=0.2}{nw}"
    show anon hosp 08 gentle at focus_standee_right
    show taki 01 glare at unfocus_standee_left
    extend "\n我看着她的脸，平静、温和地说："

    anon "别摆出这副要吃人的样子嘛，椎名同学。{w=0.15}{nw}"
    show anon hosp 07 normal_1 at focus_standee_right
    extend "\n我今天专门坐了一个半小时电车过来，可不是为了跟你打架的。"
    "她越是冲我吼，我反而越能看出来——{w=0.15}{nw}"
    extend "\n只有她自己相信她在发火，其实她手心攥得那么紧，只是因为害怕得快要死了。"

    show taki 01 glare at focus_standee_left, standee_shake_h
    show anon hosp 07 normal_2 at unfocus_standee_right
    taki "{cps=*1.5}你这家伙……把自己当成什么人了？！{/cps}{w=0.1}{nw}"
    extend "\n{cps=*1.5}灯现在到底在哪儿？！她是不是受了什么刺激？！{/cps}"

    show anon hosp 08 gentle at focus_standee_right
    show taki 01 glare at unfocus_standee_left
    anon "她在我那里。睡在我的床上。很安全。{w=0.2}{nw}"
    show anon hosp 07 normal_2 at focus_standee_right
    extend "\n我来这儿，是因为昨天夜里她哭着跟我说，她还是忘不了之前的乐队。"

    show taki 02 normal_2 at focus_standee_left
    show anon hosp 07 normal_2 at unfocus_standee_right
    "立希怔住了，像是被这句话迎面击中，攥紧的拳头僵在半空。{w=0.2}{nw}"
    play sound sfx_footsteps
    show anon hosp 07 normal_3 at standee_right_burst
    show taki 02 normal_2 at unfocus_standee_left
    extend "\n我走近一步，目不转睛地盯着她："

    anon "我要你对我说真话，事关小灯……{w=0.15}{nw}"
    extend "\n在之前的乐队里，你们是不是有时候在折磨她？"

    show taki 01 glare at standee_left_press, standee_shake_h
    show anon hosp 07 normal_3 at unfocus_standee_right
    taki "{cps=*1.5}胡说八道什么！谁会折磨她！我一直都在保护她！{/cps}{w=0.1}{nw}"
    show taki 03 sad at focus_standee_left, standee_tremble
    extend "\n{cps=*1.4}是祥子那家伙……是那场荒唐的解散把她逼成这样的！如果我不看着她，她那种人根本没法在普通人堆里活下去！{/cps}"

    show anon hosp 05 annoyed_1 at focus_standee_right
    show taki 03 sad at unfocus_standee_left
    anon "你说她“没法活下去”，就像大人说一个孩子“没治了”一样。{w=0.2}{nw}"
    show anon hosp 03 curious_2 at focus_standee_right
    extend "\n她是你的什么人？她跟你说起过我吗？"

    show taki 02 normal_2 at focus_standee_left, standee_step_back
    show anon hosp 07 normal_2 at unfocus_standee_right
    "立希盯着我，呼吸急促。她大概从我那种满不在乎又过于笃定的神态里察觉到了什么，脸一点点发白："
    taki "……你们到底发展到哪一步了？"
    show anon hosp 01 smug at focus_standee_right
    show taki 02 normal_2 at unfocus_standee_left
    anon "我以为你已经猜到了。{w=0.15}{nw}"
    show anon hosp 09 confess at focus_standee_right
    extend "我成了她的情人。"

    play sound sfx_strike
    show taki 01 glare at standee_left_press, standee_shake_h
    show anon hosp 09 confess at unfocus_standee_right
    taki "{cps=*1.6}你疯了？！她才多大，而且她刚从鬼门关回来，脑子根本不清醒！{/cps}{w=0.1}{nw}"
    extend "\n{cps=*1.5}你这种轻浮的家伙，根本不知道她有多脆弱，她随时都会——{/cps}" with shake_h

    show anon hosp 08 gentle at focus_standee_right
    show taki 01 glare at unfocus_standee_left
    anon "我知道。从第一天起我就知道。"
    "因为她老怀着一种儿童才有的畏惧心理——一种无时无刻不在的害怕和戒备。害怕一切，怕雷雨、黑暗、人群、大海……怕你们，也怕我，怕一切。{w=0.2}{nw}"
    show anon hosp 09 confess at focus_standee_right
    extend "可即便她像你们说的那样“没治了”，我也爱她一辈子。"

    hide anon with dissolve
    show taki 02 normal_2 at center_standee
    "沉默。{w=0.2}{nw}"
    extend "\n地下室的空调发出低沉的嗡鸣。立希看着我，在她紧绷的唇际和眼里，我看到了和我一模一样的无望与恐慌。{w=0.2}{nw}"
    show taki 03 sad at standee_step_back
    extend "\n她的肩膀一点点垮了下来，扶着吧台边缘，声音哑得不像话："

    taki "……你那么爱她？{w=0.15}{nw}"
    extend "\n凭什么……你才认识她几天？"
    show taki 03 sad at unfocus_standee_left
    show anon hosp 08 gentle at focus_standee_right with dissolve
    anon "那时候她是什么样子——在遇到我之前，在你们那个乐队里的时候，她是什么样子？{w=0.2}{nw}"
    extend "\n我一点也不知道。"

    show taki 02 normal_2 at focus_standee_left
    show anon hosp 08 gentle at unfocus_standee_right
    "立希愣住了。她没想到我坐了一个半小时的电车找上门来，竟然会问她这个问题。{w=0.2}{nw}"
    extend "\n过了许久，她像被抽干了力气一样，低声回答："

    show taki 03 sad at focus_standee_left
    taki "……她唱起歌来的时候，比谁都耀眼。{w=0.2}{nw}"
    extend "\n虽然平时连话都说不利索，总是低着头捡石头、写些奇怪的句子，但只要她在台上，所有人都以为我们会一直那样下去。{w=0.2}{nw}"
    extend "\n完美无缺……可惜人事无常。"

    show anon hosp 08 gentle at focus_standee_right
    show taki 03 sad at unfocus_standee_left
    anon "是的，无常。{w=0.2}{nw}"
    extend "\n刚才我跟你顶嘴，请你原谅。其实我来找你，不是为了跟你吵架，是因为我很想了解你……由于她，由于小灯。{w=0.2}{nw}"
    show anon hosp 07 normal_2 at focus_standee_right
    extend "她知道自己的一切了吗？是的。不过她还不知道，我今天下午上你这儿来了。我骗她说，我是出来买婚礼道具的。"

    show taki 02 normal_2 at focus_standee_left, standee_step_in
    show anon hosp 07 normal_2 at unfocus_standee_right
    taki "……婚礼道具？你们要干什么？你要带她去哪儿？"
    show anon hosp 08 gentle at focus_standee_right
    show taki 02 normal_2 at unfocus_standee_left
    anon "去海边。今晚就去。{w=0.2}{nw}"
    show anon hosp 09 confess at focus_standee_right
    extend "\n你应该知道，椎名同学，人爱的即便是世上最奇怪、最易碎的生物，那份爱也是神圣的。{w=0.2}{nw}"
    extend "\n人有这个权利——它和生存的权利一样神圣——有权不对任何人解释这种爱。"

    hide anon with dissolve
    show taki 03 sad at center_standee, standee_tremble
    "立希垂下眼睛，眼眶通红。她咬着牙，半晌才从喉咙里挤出一句话："
    taki "……那你到底为什么要来告诉我这些？既然你已经把她带走了，为什么还要跑来跟我说这些？！{w=0.2}{nw}"
    show taki 01 glare at standee_step_in
    extend "\n过来。看着我。{w=0.2}{nw}"
    extend "\n她什么时候走？马上告诉我日期。"

    show taki 01 glare at unfocus_standee_left
    show anon hosp 06 pain at focus_standee_right with dissolve
    anon "就在这几天。她只有最后几天了。"
    show taki 02 normal_2 at focus_standee_left
    show anon hosp 06 pain at unfocus_standee_right
    taki "确切说，是哪一天？"
    show anon hosp 07 normal_2 at focus_standee_right
    show taki 02 normal_2 at unfocus_standee_left
    anon "最晚六天以后，除非出了意外。"

    hide anon with dissolve
    "沉默。{w=0.2}{nw}"
    show taki 03 sad at center_standee
    extend "\n立希灰心丧气，但保持平静。"
    taki "那么说，没有任何希望了……"
    anon "毫无希望。"

    "立希合上眼睛，好像就要睡着似的。她闭着眼睛说："
    taki "你怎么可能知道？……"
    anon "我知道的……就跟知道人总有一死一样。"

    show taki 03 sad at standee_tremble
    "立希低声哭泣。她边哭边说："
    taki "这算什么事啊……我的天哪……什么事啊……"

    play sound sfx_heartbeat
    camera at camera_heartbeat
    "说出这句话的时候，我的胸膛里响起剧烈的嗵嗵声，好像心脏已经一整天没跳了，现在要当着椎名立希的面拼命跳动一番。{w=0.2}{nw}"
    "我逼迫自己昂起头，不向她让半步——因为我比谁都清楚，所有事情中最最卑劣的就是在别人盯着看的时候感到害怕。{w=0.2}{nw}"
    "如果要拯救高松灯，我就必须永远忘掉害怕；哪怕全世界都说这是一场荒唐的诱拐，我也必须捍卫她的尊严、她的同情和她向死而生的幻梦。"

    camera at default
    show taki 03 sad at unfocus_standee_left
    show anon hosp 06 pain at focus_standee_right with dissolve
    anon "……我多么希望这是真的。{w=0.3}{nw}"
    show anon hosp 10 tears at focus_standee_right
    extend "\n可是并不是。"

    show taki 02 normal_2 at focus_standee_left
    show anon hosp 10 tears at unfocus_standee_right
    taki "……你说什么？"

    show anon hosp 06 pain at focus_standee_right
    show taki 02 normal_2 at unfocus_standee_left
    anon "我说，根本没有什么后遗症。{w=0.2}{nw}"
    extend "\n医院的复查报告单现在就揣在我的口袋里——上面写着她只是贫血和神经性低热，身体早就康复了。{w=0.2}{nw}"
    show anon hosp 10 tears at focus_standee_right
    extend "我多么希望她真的只剩下最后六天，那样她就永远只属于我一个人了……可是并不是。"

    play sound sfx_strike
    scene bg rehearsal_room_01_orange with flash_red
    show taki 01 glare at center_standee, standee_step_in, standee_shake_h
    taki "{size=*1.25}{cps=*1.6}千早爱音——！！你他妈在耍我吗？！{/cps}{/size}" with shake_h
    taki "{cps=*1.5}既然不是真的，那你为什么欺骗她？！{/cps}{w=0.1}{nw}"
    extend "\n{cps=*1.5}你知不知道她每天都在数着钟表过日子？！你竟然拿死刑这种混账话去骗一个刚从天台上跳下来的病人，你到底安的什么心？！{/cps}"

    show taki 01 glare at unfocus_standee_left
    show anon hosp 10 tears at standee_right_burst, standee_shake_h with dissolve
    anon "{cps=*1.6}对不起……对不起，我没有其他办法！！{/cps}"
    show taki 01 glare at standee_left_press, standee_shake_h
    show anon hosp 10 tears at unfocus_standee_right
    taki "{cps=*1.6}你说什么？！{/cps}"

    show anon hosp 10 tears at focus_standee_right, standee_shake_h
    show taki 01 glare at unfocus_standee_left
    anon "{cps=*1.6}除了骗她，我还能怎么办啊？！椎名立希，你告诉我，我到底还能怎么办啊？！{/cps}{w=0.08}{nw}"
    show anon hosp 06 pain at focus_standee_right
    extend "\n{cps=*1.5}那天下午在诊室门口，医生笑眯眯地跟我说“死神退场啦，她明天就能出院啦”，然后呢？！{/cps}{w=0.08}{nw}"
    show anon hosp 05 annoyed_2 at focus_standee_right, standee_shake_h
    anon "{cps=*1.5}她妈妈已经在千叶乡下找好了全封闭式的矫正机构，只要第二天上午十点一到，就会收走她的笔记本，把她像关疯子一样锁进铁窗里！{/cps}{w=0.08}{nw}"
    show anon hosp 10 tears at focus_standee_right
    anon "{cps=*1.5}就算不去那里，让她回到羽丘的教室，回到你们那间撕碎了乐谱的排练室，回到所有人小心翼翼又充满嫌弃的叹气声里——你觉得她能撑过三天吗？！{/cps}"

    show anon hosp 06 pain at focus_standee_right
    anon "我自私透顶，我卑劣得像个小偷，我靠着这个谎言才偷来了她这几天的温存……{w=0.2}{nw}"
    show anon hosp 10 tears at focus_standee_right
    extend "\n可是，立希。"
    "我大吸一口气，好把我最脆弱最不堪的想法一次性吐露出来。"
    show anon hosp 10 tears at standee_right_burst
    anon "{cps=*1.6}对不起，我真的没有其他办法了！{/cps}{w=0.1}{nw}"
    extend "\n{cps=*1.5}如果不把这个谎撒到底，我们两个人都会烂死在五楼的病房里的！{/cps}"

    hide anon with dissolve
    "本应羞愧得无地自容，结果却说了这么一大通话。{w=0.2}{nw}"
    show taki 02 normal_2 at center_standee
    extend "\n立希像是第一次真正看清我的长相。"

    taki "……你疯了，千早。{w=0.2}{nw}"
    extend "你们两个全都是疯子。"
    anon "是啊，我早就疯了。"

    "自首完毕，她再怎么说也伤不到我了。{w=0.2}{nw}"
    show taki 03 sad at center_standee
    extend "\n她的嘴张开来，好像要说什么，似乎微微抽动了几下。{w=0.2}{nw}"
    extend "她的肩膀松懈下去了。虽然依旧是那副凶狠模样，不过想必她肯定认真地想过我说的那些，灯的下场。"

    scene bg rehearsal_room_01_blue with dissolve
    show taki 03 sad at unfocus_standee_left
    show anon hosp 08 gentle at focus_standee_right with dissolve
    taki "……那等这七天过去呢？"
    anon "今晚我就带她去九十九里滨的海边。{w=0.2}{nw}"
    show anon hosp 09 confess at focus_standee_right
    extend "\n等她把那首新歌唱给大海听，等最后的一秒钟走完……{w=0.2}{nw}"
    extend "\n如果她还是想死，我就陪她一起跳进海里；如果她愿意活下去，我就带她逃到谁也找不到的地方去。"

    hide anon with dissolve
    "沉默。"
    show taki 03 sad at center_standee, standee_nod
    taki "……带我去看看她吧。"
    anon "你要去揭穿我吗？"
    show taki 02 normal_2 at center_standee
    taki "如果揭穿你，她现在就会崩溃吧。{w=0.2}{nw}"
    extend "\n我不提报告单的事，也不提以前乐队的事。我发誓。{w=0.2}{nw}"
    show taki 03 sad at standee_step_in
    extend "\n哪怕只是站在门外看她一眼……让我去跟她道个别，千早。"

    "我们相视。我们不再说话。"

    # ==========================================
    # 4. 车站天桥上的和解与远望（杜拉斯《广岛之恋》《副领事》）
    # ==========================================
    stop music fadeout 1.5
    scene bg station_01_blue with dissolve
    play music bgm_reflection fadein 2.0 loop
    play bgs bgs_train_overpass fadein 2.0 loop
    show taki 02 normal_1 at unfocus_standee_left with dissolve
    show anon hosp 07 normal_1 at focus_standee_right with dissolve

    anon "立希，在这边的屋檐下等我五分钟。{w=0.2}{nw}"
    show anon hosp 08 gentle at focus_standee_right
    extend "\n我出门的时候骗小灯说，我是出来买婚礼道具的。如果我两手空空地把你带回去，她会起疑心的。"

    play sound sfx_footsteps
    show taki 02 normal_2 at focus_standee_left
    show anon hosp 08 gentle at unfocus_standee_right
    taki "走吧，千早。{w=0.2}{nw}"
    show taki 03 sad at focus_standee_left
    extend "\n虽然是你让她笑出来的……但这件事，我这辈子都不会原谅你的。"

    show anon hosp 08 gentle at focus_standee_right
    show taki 03 sad at unfocus_standee_left
    anon "……嗯。{w=0.2}{nw}"
    extend "我不需要你原谅。{w=0.2}{nw}"
    show anon hosp 06 pain at focus_standee_right
    extend "\n应该道歉的是我……我本不该那样跟你说话。我们也不能再吵了。{w=0.2}{nw}"
    show anon hosp 08 gentle at focus_standee_right
    extend "\n我们，我们是朋友……"

    hide anon with dissolve
    show taki 02 normal_1 at center_standee, standee_nod
    "立希微微一笑，对这一点，她不如我那么确信。"
    taki "真的吗？"
    anon "真的。"

    "她微笑。{w=0.2}{nw}"
    extend "沉默。{w=0.2}{nw}"
    show taki 03 sad at standee_step_in
    extend "\n她望着我。她看到我的痛苦。她说话的样子突然变得很动人："

    taki "灯让你很痛苦。"
    "我对立希微笑。"
    show taki 03 sad at unfocus_standee_left
    show anon hosp 08 gentle at focus_standee_right with dissolve
    anon "是的。她带给我的痛苦超过我的忍受力。{w=0.2}{nw}"
    extend "\n昨天夜里我们谈起过你。她说她非常、非常喜欢你，她说我是知道的。{w=0.2}{nw}"
    show anon hosp 09 confess at focus_standee_right
    anon "我也很喜欢你，不可能不喜欢你。我不讨厌你。真的，灯也不讨厌你。我还要替她谢谢你。见了你，人家就想疼她，疼你一直护着的那个孩子。"

    show taki 02 normal_2 at focus_standee_left
    show anon hosp 08 gentle at unfocus_standee_right
    "立希不再是一开始那副戒备满级的模样了。"
    taki "这想必可怕，我相信你……{w=0.2}{nw}"
    extend "\n不过你能跟我谈起她，那么真诚，我很领情……我们俩可以谈上好几夜，你不以为……"
    show anon hosp 08 gentle at focus_standee_right
    show taki 02 normal_2 at unfocus_standee_left
    anon "是的，是真的。我们可以谈她，谈你。"

    hide anon with dissolve
    "立希不再听我说话。她目不转睛盯着我。"
    show taki 01 glare at center_standee
    taki "真奇怪，见了你还是想揍你……原谅我。{w=0.2}{nw}"
    show taki 03 sad at center_standee
    extend "\n灯想必跟你说过之前乐队的事……我没把她照顾好，受到最大惩罚的是我。可是就算这样，我还是不能原谅你。"
    anon "我请你原谅。"

    hide taki with dissolve
    "继之以沉默。{w=0.2}{nw}"
    extend "\n我在城里是孤独的，在生活里也是。我满心爱着那个女孩，而女孩将要走了，永远离开我，远离我的身体。{w=0.2}{nw}"
    extend "\n我心里像在居丧。而站在我对面的立希知道这个。"

    scene bg station_01_orange with dissolve
    play sound sfx_footsteps
    show taki 03 sad at center_standee, standee_step_in with dissolve
    "立希走近一步。"
    taki "千早。"
    anon "我在听。"
    taki "对不起。{w=0.2}{nw}"
    show taki 02 normal_2 at center_standee
    extend "\n刚才在下面，我不该那样对你大吼大叫。我不该骂你轻浮，也不该说你想把灯毁掉。"
    show taki 03 sad at standee_tremble
    taki "还有以前的事情……我也该道歉。{w=0.2}{nw}"
    extend "\n是我太没用了。在之前的乐队里，当祥子说要退出的那天，我只会像个蠢货一样冲着她大喊大叫，逼问她到底算什么。{w=0.2}{nw}"
    extend "但我什么也没有挽回。我什么也做不到。{w=0.2}{nw}"
    taki "我看着灯一个人站在暴雨里，浑身湿透，哭着把本子递给别人，可是没有任何人接过来。{w=0.2}{nw}"
    extend "\n后来在学校里、在练习室里，我也只是把自己的焦虑塞给她，逼着她快点走出来，逼着她练习……{w=0.2}{nw}"
    taki "我自以为是在保护她，自以为比世界上任何人都懂她、都在乎她。其实我根本不懂她。是我害了她。对不起。"

    show taki 03 sad at unfocus_standee_left
    show anon hosp 08 gentle at focus_standee_right with dissolve
    anon "你什么也不知道，立希。你必须知道这一点。你一无所知。{w=0.2}{nw}"
    extend "\n你只知道她以前在乐队里的样子，只知道她唱歌时的样子。{w=0.2}{nw}"
    show anon hosp 06 pain at focus_standee_right
    extend "有关小灯为什么一直生活在恐慌里，有关她到底害怕什么，有关我和她的事情，你什么也不知道。{w=0.2}{nw}"
    show anon hosp 08 gentle at focus_standee_right
    anon "这不是你的错。事情生来就是这样。这没什么。没什么。你不必因此责备自己。"

    "立希没有打断我。她听任我说下去。"

    show anon hosp 06 pain at focus_standee_right
    anon "刚才在店里，我对你摆出的那副高傲、笃定的样子，全都是装出来的。{w=0.2}{nw}"
    extend "\n其实我自私透顶。我在英国搞砸了一切，灰溜溜地逃回日本，每天都在假装自己过得光鲜亮丽。{w=0.2}{nw}"
    anon "我接近小灯，一开始不过是想拉她组个乐队，好让我自己在学校里出风头，好遮掩我那一文不值的自卑。{w=0.2}{nw}"
    show anon hosp 10 tears at focus_standee_right
    extend "我甚至在利用她的脆弱，利用她对我的依恋，自私地想要留住她、想要成为她生命里唯一的依靠。{w=0.2}{nw}"
    anon "我把她从你们身边带走，却根本承担不起她的未来。我才是那个最可耻的人。{w=0.2}{nw}"
    extend "\n对不起……让你一个人在台后担惊受怕，让你为她掉这么多眼泪。"

    hide anon with dissolve
    scene bg station_02_orange with dissolve
    show taki 02 normal_1 at center_standee with dissolve
    "立希摇了摇头。{w=0.2}{nw}"
    extend "\n阳光在桥面上移动，把我们的影子拉得很淡。"

    taki "但她笑了。{w=0.2}{nw}"
    show taki 03 sad at center_standee
    extend "\n自从那支乐队解散之后，我再也没见她笑过。可是在你的公寓里，她睡得那么安稳，还想着要为你穿婚纱。{w=0.2}{nw}"
    show taki 02 normal_1 at center_standee
    extend "千早，虽然我还是很难喜欢你……但至少你让她活过来了。哪怕只有这几天。"

    scene bg cloud_01_orange with dissolve
    "她望着远处的铁路线。列车正进站。{w=0.2}{nw}"
    extend "\n立希忽然问我："

    taki "如果你说的是真的，如果她真的只有接下来几天了，那之后呢？{w=0.2}{nw}"
    extend "\n我们会怎么样？我们会忘掉吗？"
    anon "不会忘掉。永远不会。"
    taki "我们会回到各自的学校。我们会重新加入别的乐队，跟别的人一起弹琴、唱歌。{w=0.2}{nw}"
    extend "\n然后有一天，我们会爱上别的人。"
    anon "会的。生活会逼着我们往前走。"
    taki "然后，在很久以后，当别人问起我们高中时的事情，我们会说起小灯，说起那个喜欢捡石头的女孩子。{w=0.2}{nw}"
    extend "\n再晚些时候，也许还会有人把这些事写成书。"
    anon "也许吧。但即便过去几十年，这世上也再不会有第二个高松灯了。"
    taki "是的。再也不会有了。{w=0.3}{nw}"
    extend "还好这一切不是真的。"

    scene bg station_02_blue with dissolve
    show taki 02 normal_2 at center_standee with dissolve
    play sound sfx_footsteps

    taki "走吧。电车要开了。{w=0.2}{nw}"
    extend "带我去看她。"

    call editorial_part5b_taki

    stop music fadeout 2.5
    stop bgs fadeout 2.5
    scene bg black with slow_dissolve
    $ persistent.cleared_chapter_10 = True
    jump ch11_proposal
