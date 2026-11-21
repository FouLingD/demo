## ch11_proposal.rpy - 第十一章：二手时间与创口贴的誓言
## 严格对标《素材与视觉资产规范.md》与《图片.rtf》视觉素材规范
## 背景规范：bedroom_01_orange~rose~blue~purple~magenta / station_02_blue / road_02_blue / sea_01_orange / sea_02_blue / sea_03_blue~orange / cloud_02_blue~orange / sea_04_blue~orange / bg white / bg black
## 立绘规范：anon hosp 01~10 全套差分 / taki 02 normal_1~02 normal_2~03 sad
## 三层旁白与主视角差分系统：纯环境旁白（无立绘无头像） / 对方动作观察旁白（仅对方立绘无头像） / 高松灯主观心声与台词（tomori <emo> + 换行 extend + {nw} 疾奏）

label ch11_proposal:
    $ current_chapter = 11
    $ quick_menu = True

    # ==========================================
    # 1. 公寓午后的温存回忆与等待（海明威《永别了，武器》）
    # ==========================================
    scene bg bedroom_01_orange with fade
    camera at camera_gentle_sway
    play music bgm_routine fadein 2.0 loop
    show anon hosp 08 gentle at center_standee with dissolve

    tomori sadaway "我希望我们别总像罪犯一样生活。{w=0.2}{nw}"
    extend sad "\n我感觉自己像个罪犯，从乐队里逃跑了，也从学校里逃跑了。"

    show anon hosp 08 gentle at standee_step_in
    anon "亲爱的，别难过。你不会总像罪犯一样生活的，永远不会像罪犯一样生活，我们会过上好日子的。{w=0.2}{nw}"
    show anon hosp 07 normal_1 at standee_nod
    extend "\n清醒一点，小灯。那不是临阵脱逃，再说那只是一支已经解散的乐队。"

    play sound sfx_clothes_rustle
    show anon hosp 08 gentle at center_standee
    "她当时笑了，伸手摸了摸我的头发，对我说：“你是个好孩子，我们再躺会儿吧，在床上我就感觉很好。”{w=0.2}{nw}"
    extend "\n过了一会儿，她又低下头问我："

    show anon hosp 03 curious_2 at standee_step_in
    anon "你没有感觉自己像个罪犯，对吧？"
    tomori smile "是的。{w=0.15}{nw}"
    extend soft "\n和你在一起就没有那种感觉。"

    show anon hosp 01 smug at standee_nod
    anon "你真是个坏孩子。不过我会好好照顾你的。{w=0.2}{nw}"
    show anon hosp 09 confess at standee_step_in
    extend "\n你不明白自己遇到了一个多好的妻子。但我不在乎，我会把你带到她们谁也无法抓捕你的地方，那样我们就会过上幸福的生活了。"

    tomori soft "让我们去那里吧。"
    show anon hosp 08 gentle at standee_nod
    anon "我们会去的。只要你愿意，无论什么时候，去什么地方，我都愿意。{w=0.2}{nw}"
    extend "\n我们什么也不想了，好吗？"
    tomori calm "“好吧。”{w=0.15}{nw}"
    extend soft "我当时这样回答她。"

    # ==========================================
    # 2. 椎名立希的到访与告别之吻
    # ==========================================
    camera at default
    hide anon with dissolve
    scene bg bedroom_01_blue with dissolve
    play sound sfx_page_turn

    "沙发很软，我坐在阴影里翻看膝盖上那本写满了字句的旧笔记本，等着千早回来。{w=0.2}{nw}"
    extend "\n她那件粉色的旧外套就搭在沙发扶手上，我用双手紧紧握着袖子。"
    tomori calm "我终于开始读着笔记本上的词句，而且理解我所读的了。{w=0.2}{nw}"
    extend bitter "\n但是，读这些旧日写下的句子，就像是在追随某个陌生人的生活过程，这太叫人讨厌了。{w=0.2}{nw}"
    extend soft "\n我极想生活。过自己的生活。过一种新的生活。"

    stop music fadeout 1.0
    play ambient_sfx sfx_door_open_wood
    play sound sfx_footsteps_wood
    "就在这时，玄关的门被推开了。一股夹杂着潮湿水汽的穿堂风猛灌进来。{w=0.2}{nw}"
    extend "\n我抬起头，以为只是千早回来了，但站在玄关那里的，却是一个我无论如何也想不到会在此时此地出现的人。"

    show taki 02 normal_2 at left_standee with dissolve
    show anon hosp 06 pain at right_standee with dissolve
    "立希就站在走廊过道的暗影里，紧跟在千早身后。"
    tomori kya "她怎么会在这里？{w=0.15}{nw}"
    extend concern "\n她是怎么找到这间房间的？{w=0.15}{nw}"
    extend calm "\n谁也不出声。"

    play music bgm_above_the_mountains fadein 2.0 loop
    hide anon with dissolve
    show taki 02 normal_2 at center_standee

    "千早退到一旁，靠着墙壁垂下眼睛，把房间中央的空间留给了我和立希。"
    play sound sfx_footsteps
    show taki 03 sad at standee_step_in
    "立希向前走了一步，停在离沙发两米远的地方。{w=0.2}{nw}"
    extend "\n她看着我，眼里没有我预想中的愤怒与指责，只有一种深不见底的悲哀与温存——{w=0.2}{nw}"
    tomori calm "就在对上她眼睛的那一秒，我突然明白了：{w=0.15}{nw}"
    extend soft "\n千早已经把一切都告诉她了。她什么都知道了。"

    tomori soft "立希……你来了。"
    show taki 02 normal_2 at standee_nod
    taki "嗯。我来看看你。"

    play sound sfx_clothes_rustle
    "沉默。我抓紧了膝盖上的毛毯。"
    tomori concern "她……全都跟你说过了？"
    taki "说了。在车站那边说的。"
    tomori sadaway "你还在生我的气吗？"
    show taki 03 sad at center_standee
    taki "没有。从来没有。"
    tomori sad "对不起……"
    show taki 02 normal_2 at center_standee
    taki "为什么道歉？"
    tomori sadaway "因为以前乐队的事……因为我把一切都弄得一团糟。{w=0.2}{nw}"
    extend sad "\n如果大家都能听见就好了……我想向所有人道歉。"
    show taki 02 normal_1 at center_standee
    taki "用不着道歉，灯。{w=0.15}{nw}"
    extend "那些事早就过去了。"
    tomori soft "我从来没有讨厌过你，立希。"

    show taki 03 sad at standee_tremble
    "立希怔了一下，嘴唇微微颤抖。她没有接话。"
    tomori soft "不管从哪个角度……我都从来没有讨厌过你。"
    taki "我知道。"
    tomori sadaway "要是……"
    show taki 02 normal_2 at standee_nod
    taki "别说了，灯。{w=0.2}{nw}"
    show taki 03 sad at center_standee
    extend "是我自己要来的。"

    scene bg bedroom_01_purple with dissolve
    show taki 02 normal_2 at center_standee with dissolve
    "继之以沉默。{w=0.2}{nw}"
    extend "\n立希慢慢扫过这间昏暗的房间。她看见了丢在墙角的吉他盒，看见了桌上冷掉的红茶，最后停在衣架上那件雪白的蕾丝婚纱上。"

    taki "你们一直呆在这里？"
    tomori calm "嗯。"
    taki "那件衣服……就是她说的婚纱？"
    tomori soft "嗯。从旧货店买回来的。{w=0.15}{nw}"
    extend calm "是别人穿剩下的。"
    show taki 03 sad at standee_nod
    "立希望着那件婚纱，轻轻点了点头。"

    # NVL 文学独白：阿列克谢耶维奇《二手时间》与草莓创可贴婚戒
    hide taki
    scene bg white with dissolve
    nvl clear

    vn_black "我忽然意识到，无论是立希、千早还是我，我们都在使用二手词汇生活。"
    vn_black "用别人用过的词，表达别人感受过的痛苦，甚至连我们所经历的心碎、告别与爱，也像是从别人那里借来的。"
    vn_black "过去那支乐队早就在那个暴雨天散开了。我们站在淋湿的台阶上，两手空空，试图用剩下的零碎物件拼凑出自己的日子。时间仿佛不再是向前的洪流，而是一座安静的旧货市场——我们在里面翻找着旧唱片、旧吉他、磨毛了边的歌词本和别人穿剩下的白婚纱。我们以为自己在开始一段全新的生活，可在第一个音符弹响时，空气里回荡的依然是昨天的回音。"
    vn_black "在那些漫长寒冷的夜晚里，我们守在狭小的房间里直到天亮，桌上摆着冷掉的红茶，耳机里放着滋滋啦啦的杂音。我们好像不是生活在属于自己的时间里。"
    nvl clear
    window hide

    scene bg bedroom_01_rose with flash_warm
    camera:
        easein 0.8 zoom 1.06 yoffset 8
    tomori soft "可当我低下头，看见左手无名指根部贴着的那枚草莓图案创可贴——那是今天中午千早买不起戒指、从口袋里翻出来替我一圈圈缠在手指上的“婚戒”——{w=0.2}{nw}"
    tomori smile "指腹传来粗糙而暖和的触感，又让我觉得，至少指尖这一小块皮肤的温度，是完完全全属于我们自己的。"

    camera:
        easeout 0.6 zoom 1.0 yoffset 0
    scene bg bedroom_01_blue with dissolve
    show taki 02 normal_2 at center_standee with dissolve

    tomori calm "立希。"
    taki "怎么了？"
    tomori soft "我这两天写了一首歌。"
    "立希看着我手里的本子，没有动。"
    taki "新写的？"
    tomori smile "嗯。刚写完的。词和曲都写好了……{w=0.2}{nw}"
    extend soft "\n让我给你唱一下吧。"
    show taki 03 sad at center_standee
    taki "不用了。"
    tomori concern "很短的。只要两分钟……"
    taki "不用了，灯。{w=0.2}{nw}"
    extend "没有时间了。"
    tomori ehh "没有时间了？……"

    show taki 02 normal_2 at focus_standee_left
    show anon hosp 07 normal_2 at unfocus_standee_right with dissolve
    "她转过头，看了一眼百叶窗外愈发暗沉的天空，像是在提醒我，又像是在提醒靠在墙边的千早："
    taki "起风了。一会儿要下雨了。"
    show anon hosp 06 pain at focus_standee_right
    show taki 02 normal_2 at unfocus_standee_left
    anon "是啊……天已经黑下来了。"
    show taki 02 normal_1 at focus_standee_left
    show anon hosp 06 pain at unfocus_standee_right
    taki "你们不是还要出门吗？"
    tomori calm "嗯。要去海边。"
    taki "那就得快一点。趁雨还没下大。"
    tomori concern "那你呢？你要回去了？"
    show taki 02 normal_2 at focus_standee_left
    taki "我回去了。"
    tomori sad "我们……以后还会再见吗？"

    hide anon with dissolve
    show taki 03 sad at center_standee
    "立希没有回答这个问题。{w=0.2}{nw}"
    play sound sfx_train_horn volume 0.75
    extend "\n远处传来电车驶过铁桥的鸣笛声，低沉而悠长，像一声穿透整个城市平原的哀鸣。"
    play sound sfx_footsteps
    "立希转过身，准备朝玄关走去。{w=0.15}{nw}"
    extend "\n但在迈出房门之前，她忽然又回过身来找我。她在离我半步远的地方停住脚步。"

    show taki 03 sad at standee_step_in
    taki "您不介意我最后再吻你一下吧？"
    tomori ah "她突然又用了那个古怪的“您”字。"
    tomori soft "不介意……{w=0.2}{nw}"
    extend calm "我闭上了眼睛。"

    play sound sfx_clothes_rustle
    hide taki with dissolve
    play ambient_sfx sfx_footsteps
    play sound sfx_door_close
    "吻结束了。立希直起身，没有再看千早，也没有回头，快步走出玄关，轻轻带上了门。{w=0.3}{nw}"
    tomori sadaway "我再也没有见过她。"

    # ==========================================
    # 3. 穿上二手白婚纱与甜蜜的遗忘
    # ==========================================
    scene bg bedroom_01_rose with dissolve
    play music bgm_dialogue_warm fadein 2.0 loop

    "房间里重新安静下来。{w=0.2}{nw}"
    play sound sfx_thunder volume 0.8
    extend "\n窗外传来沉闷的雷声。我看着窗玻璃，随口说道："
    tomori calm "可能会下雨。"

    show anon hosp 02 boast at center_standee, standee_jump with dissolve
    anon "{cps=*1.5}但是就算下雨又怎么样呢？要抓紧时间啊，我们还来得及。{/cps}"

    play sound sfx_clothes_rustle
    show anon hosp 08 gentle at standee_step_in
    "千早脸上挂着大大的笑容。{w=0.15}{nw}"
    extend "\n她伸手帮我理了理脖子上的白头纱，又把一件针织开衫披在我肩上。"
    anon "外面很冷。裹紧一点。"
    tomori pout "呃，这种时候你还在操心这个？"
    show anon hosp 04 shy_2 at standee_nod
    anon "别撅嘴。我只是不想你着凉，仅此而已。"

    "我无可奈何地呼出一口气，看着她近在咫尺的笑脸。"
    tomori calm "你是我妈还是怎么的……"
    show anon hosp 01 smug at standee_jump
    anon "{cps=*1.5}哈哈，说不定是呢。这也说不准嘛。{/cps}{w=0.1}{nw}"
    show anon hosp 02 boast at standee_nod
    extend "\n{cps=*1.5}也许我天生丽质，长得显小呢。{/cps}"

    scene bg bedroom_01_magenta with dissolve
    camera at camera_gentle_sway
    tomori uff "额头上传来轻微的发晕，分不清是这两天淋雨落下的低烧，还是紧绷了太久的神经终于松懈了下来。{w=0.2}{nw}"
    tomori calm "我知道自己并不是真的失去了记忆，我只是太累了，像一个走完了漫长夜路的人，终于决定把背上那些沉重得压断脊梁的旧包裹一件件解开、丢在路边。{w=0.2}{nw}"
    tomori soft "只要我假装记不起那些把我们分开的名字、记不起千叶的铁窗和过去的学校，那些曾经把我逼上天台的东西就再也追不上我了。"

    tomori ah "我看着她，大脑变得晕头转向的。{w=0.2}{nw}"
    extend neutral "两步之前还显而易见的事，现在却成了谜。似乎有太多的东西正在滑落，滑落，滑落，滑落——以前的乐队、学校的名字、刚才哭过的理由，全都从指缝里溜走了。{w=0.2}{nw}"
    tomori smile "但唯独胸口那种感觉一点都没有减弱。那些不断形成的空缺地方并不会空置太久，因为那种温暖、美好的感觉会立刻涌进来，将它们填得满满当当。"

    show anon hosp 08 gentle at center_standee with dissolve
    "我歪过头，认真地问她："
    tomori soft "千早，我是什么时候遇见你的来着？{w=0.2}{nw}"
    extend smile "\n我忘记了……但是我记得我喜欢你。"

    show anon hosp 09 confess at standee_step_in
    anon "……这样啊。没关系。{w=0.2}{nw}"
    show anon hosp 08 gentle at standee_nod
    extend "\n你不记得也没关系。因为我感觉我已经认识你很久很久了。"

    tomori yay "{cps=*1.5}我也是！{/cps}{w=0.1}{nw}"
    extend smile "\n{cps=*1.5}这都不重要了。我们好长时间没见了！{/cps}"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.6}对，一点都不重要了！走吧，我们去看海！{/cps}"

    # ==========================================
    # 4. 穿衣镜、末班列车与暴风雨海滩（NVL 文学叙事段）
    # ==========================================
    camera at default
    hide anon with dissolve
    scene bg station_02_blue with push_right
    play music bgm_soaring fadein 2.0 loop
    play bgs bgs_train_overpass fadein 2.0 loop
    nvl clear

    vn_white "从穿衣镜里，我看到自己面色十分白净，周围是一片茫茫的夜色迷雾。对着镜子我自言自语道：“这就是我，高松灯，穿着新嫁衣，今夜就要去海边结婚了。”我几乎认不出自己来了，恍惚间觉得自己似乎变成了两个人。我曾在某本书里读到过，有人在死去时会穿着结婚的礼服被放进棺材；现在，我眼瞧着镜子里自己的身影，爱音站在我身后替我拉上背后的拉链，她从冰凉的镜子里伸出两臂环住我的脖颈，好像在轻轻地抚摸隐藏在我新娘头纱上的死神。"
    play sound sfx_footsteps_gravel volume 0.75
    vn_white "当我们提着裙摆从空无一人的街道和检票口穿过时，那缀有蕾丝花边的素白礼服发出窸窸窣窣的声音。我们跑着，我们两人都提着宽大的白纱跑着，接着末班列车的铁轨就出现在眼前。"
    vn_white "那是我所见到的最笔直的东西，笔直、空旷而又安静地穿过在夜色中开出的一条又长又空阔的通道，并且也穿过沉睡的大地。枕木被切割得又平整，又光滑，又干净，月光与信号灯照射在铁轨上，就像照在两条由蜘蛛吐出的银丝上，笔直伸向我们甚至都不能看到的远方。空荡荡的末班车厢摇晃着，那两条细丝看上去什么重量都承受不住，它们笔直、迅速又轻快地伸向黑暗的前方，就好像要带着穿着婚纱的我们不断加速，以便干净利落地跳出这个世界一般。"
    vn_white "一种想探索那片海域秘密的渴望，甚至彻底压倒了我对第七天午夜的害怕和无望。显然，这趟末班列车正载着我们驶向某个令人激动的领域——某种从未被揭示过的秘密，哪怕这种秘密的获得就是毁灭本身。"
    nvl clear
    window hide

    stop bgs fadeout 1.5
    call editorial_part6_sea_vow

    scene bg sea_01_orange with dissolve
    play bgs bgs_beach_night fadein 2.0 loop

    "太阳已经落山了。天边只剩下最后一点红晚霞，像一道未愈合的伤口横贯在海平面上。{w=0.2}{nw}"
    "空气变得异常清凉而湿润。在一条通往入海口的干涸河床旁边，成团成团白色的水汽正在荒草上方升腾、扩散，把远处的灌木林和废弃的船壳都笼罩进一片迷离的阴影之中。"
    tomori soft "整个大地仿佛在向深沉的梦乡滑落，所有的影子都在傍晚中融化。在这片广袤无垠的寂静中，人会突然感到自己是如此渺小，如此无依无靠；{w=0.2}{nw}"
    extend smile "但与此同时，一种与泥土、草木和海浪同呼吸的安详感，又会像甘霖一样浸透疲惫的心灵。"

    scene bg sea_02_blue with dissolve
    play bgs bgs_downpour fadein 1.5 loop

    "第一滴雨落在了我的鼻尖上。{w=0.2}{nw}"
    extend "\n紧接着，倾盆大雨泼向了整片海洋与荒滩。世界任何地方都没有这样垂直下落的大雨。"

    show anon hosp 02 boast at center_standee, standee_jump with dissolve
    "千早没有躲闪。她拖着湿透的白色婚纱，在布满卵石的海滩上跑来跑去，任凭暴雨凶狠地抽打着她的脸。{w=0.2}{nw}"
    extend "\n她的声音被呼啸的海浪淹没，可她还在咯咯傻笑，对着大海扯着嗓子大喊。"
    tomori yay "看着她，我也觉得好开心。{w=0.15}{nw}"
    extend smile "\n我走过去，向头顶的天空伸出手——天空感觉近在咫尺。"

    show anon hosp 02 boast at standee_jump
    anon "{size=*1.15}{cps=*1.6}嘿，小灯！过来！{/cps}{/size}{w=0.1}{nw}"
    show anon hosp 01 smug at standee_step_in
    extend "\n{cps=*1.5}这里就是我们的舞台了！差不多是时候了！{/cps}"

    tomori ah "舞台……？{w=0.2}{nw}"
    extend calm "\n对。我们是一支乐队。我还有最后一首歌要唱。"

    show anon hosp 07 normal_1 at standee_step_in
    anon "那你的歌词本呢？带草稿了吗？"

    tomori calm "没有。忘在房间里了。{w=0.2}{nw}"
    extend soft "\n不过我不需要歌词本。纸和笔没那么重要，它们只是载体。{w=0.2}{nw}"
    extend yay "\n当淹没我的情感如此强烈时，我确信，就算没有麦克风，就算没有音箱，我的声音也能击穿大气层，抵达终点。"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.6}说得对！本小姐也没有带吉他，但我的手还记得所有的和弦！{/cps}{w=0.1}{nw}"
    show anon hosp 08 gentle at standee_step_in
    extend "\n那你要把这最后一首歌唱给谁听呢，主唱大人？"

    # ==========================================
    # 5. 倒转的雨幕、撒向星空的石头与破晓的绝唱
    # ==========================================
    hide anon with dissolve
    "我环顾四周。{w=0.2}{nw}"
    play sound sfx_strike
    extend "\n就在这时，海滩、黑夜与沉闷的空气仿佛一道无形的墙壁，轰然倒塌了。"

    scene bg sea_03_blue with flash_warm
    show anon hosp 09 confess at center_standee, standee_step_in with dissolve
    camera:
        easein 0.8 zoom 1.08 yoffset 10
    "千早看着我，湿透的粉色长发贴在脸颊边，眼睛里却亮着一种纯粹而热切的笑。{w=0.2}{nw}"
    tomori smile "那笑声穿透了浓重的夜雾与大雨，让我胸口那些关于负罪、羞怯与生死的沉重想法，一下子全都散开了。"
    "雨水顺着她的下巴往下淌，她朝我伸出手，无名指上同样缠着一圈被雨水浸湿的白色创可贴。{w=0.2}{nw}"
    tomori soft "只要看着她那双毫无阴霾的眼睛，我就觉得过去所有为了一点碎裂的誓言而掉眼泪的日子，都已经远得像上辈子的事了。"

    camera:
        easeout 0.6 zoom 1.0 yoffset 0
    hide anon with dissolve
    stop bgs fadeout 1.2
    play sound sfx_reverse_rain
    scene bg cloud_02_blue with flash_cyan
    show snow_black_reverse

    tomori ah "所有的重力仿佛在这一刻退去。{w=0.2}{nw}"
    extend kya "漫天倾盆的大雨突然在半空中凝滞，然后开始倒转——成千上万颗晶莹的雨滴不再坠落，而是化作逆流的星辰，从漆黑的海面与卵石滩上腾空而起，向着幽暗的夜空倒飞上去。"
    play ambient_sfx sfx_clothes_rustle
    play sound sfx_pebble_scatter
    tomori yay "我从婚纱口袋里掏出我收集了整整一整个青春的所有石头，把它们像棋子一样全部撒向倒转的雨水与浩瀚的星空。"

    scene bg sea_04_blue with dissolve
    show snow_black_reverse
    "最后一滴雨水顺着我的睫毛滑落下来，滴在脚背上。{w=0.2}{nw}"
    extend "\n光线以不可思议的速度向着海岸推进，把昨夜残留的每一寸阴暗都照得纤毫毕现。"
    tomori smile "我站在原地，仿佛平生第一次真正睁开眼睛看见这个世界。{w=0.2}{nw}"
    extend yay "\n我从未感受到如此澄澈的幸福。{w=0.2}{nw}"
    extend smile "\n心里那些积压了十来年的羞怯与畏惧散得干干净净，胸腔里只剩下一种澄明而热烈的欢喜。"
    tomori kya "我睁大眼睛，望着倒流向天际的银色雨水，望着漫天旋转的星辰与海岸线破晓的刺目白光——{w=0.2}{nw}"
    extend yay "就像一个刚刚降生到世上的婴儿，平生第一次睁开眼睛，第一次看见这个鲜活、暴烈、毫无保留的世界。"

    scene bg cloud_02_orange with flash_warm
    show snow_black_reverse
    show anon hosp 08 gentle at center_standee, standee_step_in with dissolve
    "我转过头。{w=0.2}{nw}"
    extend "\n身边的女孩沐浴在倒飞的雨滴与暴烈的晨光之中。她的粉发与燃烧的天际同色，她的脸庞是如此熟悉、如此温暖，让我的胸口生疼。"
    tomori calm "我见过她的脸多少次？她又见过我的脸多少次？我说不上来。但我比地球上任何人都更了解她，而她也比任何人都更了解我。{w=0.2}{nw}"
    tomori soft "我知道，这双眼睛见过我最狼狈的模样；我只能祈祷，它们也曾映照出我最好的样子。即便目睹了我最怯懦、最难堪的时刻，她依然伫立在风暴中央，给予我如此真挚的笑容。"
    tomori smile "我喜欢看您笑。{w=0.2}{nw}"
    extend soft "\n您笑起来眼角弯弯的，真好看，所以我喜欢，所以我喜欢您呀。{w=0.2}{nw}"
    extend calm "\n我的歌是唱给谁听的？答案从来就只有一个。"

    scene bg sea_03_orange with dissolve
    show snow_black_reverse
    play music bgm_climax_phase1 fadein 2.0 loop
    show anon hosp 07 normal_1 at center_standee with dissolve

    tomori smile "千早……我有首歌要唱给你听。"

    show anon hosp 04 shy_2 at standee_jump
    anon "{cps=*1.6}什——什么？！只唱给我一个人听？！{/cps}"

    tomori smile "没错。只唱给你听！{w=0.1}{nw}"
    extend yay "{cps=*1.5}所以，调好你的弦！{/cps}{w=0.1}{nw}"
    extend calm "\n演出开始。倒数三……二……"

    show anon hosp 04 shy_1 at standee_shake_h
    anon "{cps=*1.6}等等，呃——好、好的！{/cps}{w=0.1}{nw}"
    show anon hosp 02 boast at standee_jump
    extend "\n{cps=*1.6}吉他手千早爱音，准备就绪！随时可以开始！{/cps}"

    scene bg sea_04_orange with flash_warm
    show snow_black_reverse
    show anon hosp 02 boast at center_standee, standee_jump
    tomori yay "{size=*1.35}一！！{/size}" with shake_h

    "爱音在虚空中用力挥下右手，拨响了那根看不见的琴弦。{w=0.2}{nw}"
    tomori yay "我的声音顺着海风冲出了喉咙，不再发颤，也不再躲闪，笔直地撞进漫天大雨与翻涌的海浪里。"
    hide anon with dissolve
    tomori calm "海浪中这千万种声音，今天听来显得格外新奇——我已经不能再区别这无数种声音，区别不出哭泣声中的欢笑声、绝境中的狂喜声。{w=0.2}{nw}"
    tomori soft "过去排练室里的争吵声、病房里的叹气声、天台上的呼喊声，愤怒的尖叫，濒死者的悲叹，在这一刻全都紧密联结在一起，一切都浑然一体，千百次地互相交错、消融在同一片轰鸣的海潮里。"
    "就在最后一个音符落下时，海平面那头那轮巨大的太阳轰然升起。"

    # ==========================================
    # 6. 破晓白光吞没万物与“您”的永恒终章（0.28s 焦橙负片过曝 + 摄影暖光晕掠过炸入白光）
    # ==========================================
    play ambient_sfx sfx_impact
    play sound sfx_whiteout_swell
    $ photosnap(duration=0.28)
    scene bg cloud_02_orange with flash_white
    show ed_ob_lightleak at ed_ob_flare_flash
    play music bgm_climax_phase4 fadein 2.0 loop

    "炫目的白光从大海深处喷薄而出，{w=0.15}{nw}"
    extend "地平线锯齿般的边缘燃起了漫天朝霞，染成红色、橙色和耀眼的玫瑰粉色。"

    scene bg white with slow_whiteout
    show snow_white
    nvl clear

    vn_black "破晓的太阳在视野里急剧膨胀，越来越大，越来越亮，占满了整片天空。翻涌的海浪、湿漉漉的卵石滩、远处的灯塔与身后的城市，全都在刺目的白光中融化了。"
    vn_black "漫天遍野的晨光正吞没整个世界。"
    vn_black "时间已不容我前思后想，已不容我拿不定主意。"
    vn_black "我穿着湿透的白色婚纱迈步朝那片刺目的白光深处追赶爱音，此外别无他法，因为我爱爱音。"
    vn_black "我像穿墙而过一样穿过轰鸣的风雨：湿透的裙摆拍打着脚踝，脚下是粗糙的卵石硬质感，迎面是海水一般的冷气与摇摆的时间。"
    vn_black "恍惚间，所有的记忆犹如水汽从海面上升腾起来。海是庞大的思念，倒飞的雨滴无声地悬浮在晨光里，漫长的时间化作巨大的光球浮于空中。"
    nvl clear

    vn_black "不再有两个人影的分别了。"
    vn_black "天空、大海、倒飞的雨滴、素白的婚纱，还有我和她交握的双手、无名指上湿透的创可贴，全都融化在同一片漫无边际的白光里。"
    vn_black "我在极度的光芒中扑进她的怀里，用尽全力抱紧她，用双手捧住她的脸，拼命地望着她，直到她失去一切世俗的意义，直到一切都融为一体。"
    vn_black "道路、城市、医院、铁轨，所有云彩的形状、那种光芒、那种红颜色的浓淡与过去的黑暗，全都失去了界限，各自在色彩和形态上变得一律平等了。"
    vn_black "也许创造星星、太阳和这片大海的就是我和千早爱音，可是我已经记不清楚了。"
    nvl clear
    window hide

    show anon hosp 09 confess at center_standee with dissolve
    "在万物被吞噬的轰鸣声中，我们贴着彼此的嘴唇，用只剩碎片的短句说话："

    tomori soft "好亮啊。"
    show anon hosp 08 gentle at center_standee
    anon "太阳掉下来了。"
    tomori calm "大海不见了。"
    anon "城市也不见了。地球要化掉了。"
    tomori concern "你还在吗？"
    show anon hosp 09 confess at standee_step_in
    anon "在。我抱着你呢。"
    tomori soft "好烫……你的手好烫。"
    show anon hosp 10 tears at standee_step_in
    anon "抓紧我。别松手。"
    tomori smile "不松手。一辈子。"
    show anon hosp 09 confess at standee_step_in
    anon "小灯，我爱你。"
    tomori soft "我喜欢您。{w=0.2}{nw}"
    extend smile "我也爱您，只爱您一个。"

    hide anon with slow_dissolve
    "白光吞没了我们的脚踝，{w=0.15}{nw}"
    extend "吞没了我们的腰肢，{w=0.15}{nw}"
    extend "吞没了我们交握的双手。"

    "？？？" "{cps=*0.85}您……您叫什么名字来着？{/cps}"
    "？？？" "{cps=*0.85}我不知道。我忘了。{/cps}"
    "？？？" "{cps=*0.8}您是谁来着？{/cps}"
    "？？？" "{cps=*0.8}抱歉，我想不起来了。{w=0.2}{nw}"
    extend "\n{cps=*0.8}那您呢？您是谁？{/cps}"
    "？？？" "{cps=*0.75}……我也忘了。{/cps}"
    "？？" "{alpha=0.88}{cps=*0.75}没关系。我只想听听您的声音。{/cps}{/alpha}"
    "？？" "{alpha=0.82}{cps=*0.75}没关系？{/cps}{/alpha}"
    "？" "{alpha=0.75}{cps=*0.7}嗯。是谁都没有关系了。{/cps}{/alpha}"
    "？" "{alpha=0.68}{cps=*0.7}可是我还在抱着您。{/cps}{/alpha}"
    "【 】" "{alpha=0.62}{cps=*0.65}对。我还在这里。{/cps}{/alpha}"
    "【 】" "{alpha=0.55}{cps=*0.65}我喜欢您。{/cps}{/alpha}"
    "【 】" "{alpha=0.50}{cps=*0.6}我爱您。{/cps}{/alpha}"
    centered "{size=+8}{color=#000000}我爱您。{w=0.4}我爱您。{w=0.4}我永远爱您。{/color}{/size}"

    stop music fadeout 3.0
    stop bgs fadeout 3.0
    scene bg black with slow_dissolve
    $ persistent.cleared_chapter_11 = True
    jump game_credits
