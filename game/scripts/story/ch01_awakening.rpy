## ch01_awakening.rpy - 第一章：苏醒与深海的余响
## 严格对标《规范文件.md》视觉素材规范与 11111.docx 对象修订终盘定稿
## 背景规范：hospital_bed_01_blue / hospital_exterior_01_blue / rehearsal_room_01_blue
## 立绘规范：taki 03 sad / soyo 01 normal / 主视角 Side Image 头像差分系统

label ch01_awakening:
    $ current_chapter = 1
    $ quick_menu = True

    # --------------------------------------------------------------------------
    # 序幕：意识的潜流与无声的宇宙
    # --------------------------------------------------------------------------
    scene black with fade
    play bgs bgs_rain volume 0.1 fadein 2.0 loop 
    play music bgm_opening fadein 1.5 loop
    show snow_white

    vn_white "其实，{w=0.5}自然界当中有感情的生物不止有人类一种。"
    vn_white "大象在死去的同伴前伫立，这是它们理解离去的方式。"
    vn_white "在太平洋某处，曾经有一位失去幼崽的虎鲸母亲。{w=0.5}
用额头顶着早已失去生机的孩子日夜不停地游曳上千公里。"
    vn_white "听说，{w=0.5}她一次又一次用脊背将不断下沉的躯体重新托出海面，{w=0.5}跨越了十七个昼夜。"
    vn_white "以此类推，{w=0.5}在广袤的天地之间，还有许许多多的生命和我们一样，{w=0.5}会为了无法挽回的失去而固执地抵抗遗忘。{w=0.5}
……这真是很浪漫的事情啊。"
    vn_white "这样说来，{w=0.5}在这个庞大而井井有条的地方，{w=0.5}我们似乎也没有那么孤独。"
    nvl clear

    vn_white "所以！{w=0.5}当你沉溺在痛苦与深情当中，{w=0.5}不妨摸摸自己的心脏吧！"
    vn_white "想象一下，{w=0.5}那里流淌的血液是所有真实活过的灵魂共同经历过的。"
    vn_white "当你摸到自己脉搏时，{w=0.5}尽管……{w=0.5}尽管你可能穿着校服，{w=0.5}还是什么其他的，都没有关系！"
    play sound sfx_impact
    vn_white "{b}你会听见海的声音！{/b}{w=0.5}那些仅仅存在于视野之外的灵魂，此刻正从你的身体里传出来……" with shake_h
    vn_white "这或许是某种很取巧的，可以看海的方法吧！"
    nvl clear

    vn_white "{b}当然{/b}，{w=0.5}我其实并不赞同什么，生命是无价的之类的观点。"
    vn_white "大家都在给它贴金，给生活贴金，给爱贴金，{w=0.5}把它们写成诗，拍成电影。"
    vn_white "我讨厌那些被包装的盛大而无坚不摧的奇迹。{w=0.5}至少，那些烂片的票房算不到我的帐上。{w=0.5}
这个世界不由那些宏大的词句构成！"
    vn_white "那么……{w=0.5}它到底是怎么运转下去的呢？"
    vn_white "曾经我在读到一本图鉴的时候，上面说过，{font=fonts/ChillHuoSong_F_Bold.otf}“世界依靠社会规范、共同信念与相互依赖维持”{/font}。"
    vn_white "……这好像在没有解决上一个问题的同时，{w=0.5}又提出了好多悬而未决的新的概念。"
    vn_white "什么可以被称作是规范？{w=0.5}什么是共同信念？"
    vn_white "我还是没看懂，{w=0.5}但是至少我们可以推己及人——"
    nvl clear

    # 黑屏转白，雪花倒转飘散，思维切换
    scene bg white with dissolve
    hide snow_white
    show snow_black_reverse

    vn_black "算了！……我为什么要在这里替他们找补？"
    vn_black "首先，我并不在乎。{w=0.5}
其次，拿我自己去揣测别人，本身就很难说清。"
    vn_black "不过，仅就{b}你{/b}而言，{w=0.5}其实是一颗特别奇怪的星星。"
    vn_black "归国转学生。{w=0.5}在年级里只占极少数，在少数人里也是个异类。"
    vn_black "吉他弹得很一般，{w=0.5}平平无奇。"
    vn_black "可就算这样，{w=0.5}你还是比任何人都更努力地、拼尽全力地想要发光。"
    vn_black "……我觉得这点，真的超可爱。" with shake_h
    nvl clear

    vn_black "也是在看着你的时候，{w=0.5}我才突然回过神来——我们能像现在这样并肩站着，本身就像一场奇迹。"
    vn_black "越想这些，{w=0.5}就越觉得不可思议。"
    vn_black "刚好在医院遇见，{w=0.5}刚好伸出了手，{w=0.5}刚好撞在一起组了乐队。"
    vn_black "或许会有人说这只是巧合，{w=0.5}但即使如此的话，这种巧合不也太经常出现了吗！"
    vn_black "例如……{w=0.5}两条完全不相干的平行线突然缠在了一起。"
    play sound sfx_strike
    vn_black "{b}假如偶然足够多，填满了所有的时间与空间，{w=0.5}那这种巧合怎么不能被视为是必然事件呢！{/b}"
    nvl clear

    vn_black "我可不信什么命中注定。{w=0.5}我没自大到以为你是为了拯救我才降临的，也不觉得你的努力只是为了博眼球。"
    vn_black "不过……{w=0.5}换个角度想呢？女孩向往人群，是因为按常理来说，我们以为认同来自外界。"
    vn_black "但如果这个女孩的心，{w=0.5}本身就是一整座空无一人的舞台呢？"
    vn_black "在她身后没有人为她鼓掌，{w=0.5}她只能一个人在上面拼尽全力，撑起自己全部的体面。{w=0.5}她需要用自己的方式来解释这一切……"
    vn_black "然后在独自表演的过程中，{w=0.5}慢慢萌生出了想要被真正看见的心愿——{w=0.5}
想被爱，想被认真注视。"
    vn_black "所以，{w=0.5}她才会不管不顾地把我也硬拽上这座舞台。"
    vn_black "唱得走调也没关系，{w=0.5}吉他弹得乱七八糟也没关系。"
    vn_black "因为她的世界，{w=0.5}从一开始就只有她自己啊！"
    vn_black "{b}只要我们站在这里，{w=0.5}她就已经替我否定了所有的否定……{/b}{w=0.5}{nw}"
    play sound sfx_impact
    extend "
这难道不超有意思吗！" with shake_h
    vn_black "我开心到几乎都要掉眼泪了，{w=0.5}真的。"
    vn_black "可是，{w=0.4}在真正睁开眼睛看见那颗粉色的星星之前，{w=0.4}我得先从那场坠落里醒过来。"
    vn_black "白色天顶的刺目亮光正隔着眼皮一点点压下来，{w=0.4}把刚才所有的声音都推回了很远的地方。"
    nvl clear
    window hide

    # --------------------------------------------------------------------------
    # 现实苏醒：单人病房铁架床（hospital_bed_01_blue）
    # 模拟睁眼、强烈对光反射与点滴声
    # --------------------------------------------------------------------------
    stop music fadeout 0.5
    stop bgs fadeout 1.0
    hide snow_black_reverse

    # 规范场景：hospital_bed_01_blue（冷峻沉重的单人铁架床）
    scene bg hospital_bed_01_blue
    show screen eyes_opening
    with cut_white_fade
    $ renpy.pause(2.4, hard=True)
    hide screen eyes_opening

    play sound sfx_iv_drip
    play bgs bgs_hospital fadein 1.5 loop

    nurse_a "{size=*1.5}医生！{w=0.4}3号床瞳孔出现对光反应了！{/size}"
    doctor "手电拿给我。"
    doctor "高松同学，{w=0.4}能听见我的声音吗？"

    # 灯虚弱呢喃（挂规范头像 Side an2）
    tomori an2 "……{w=0.4}"

    doctor "如果能听见，{w=0.4}试着眨一下眼睛。"
    tomori an2 "我没有眨眼。{w=0.1}{nw}"
    extend uff "很疼。"

    # 剧痛剧烈咳嗽（挂规范头像 Side uff）
    play sound sfx_cough_soft
    tomori uff "{size=*0.67}{cps=15}咳……{w=0.4}咳咳！{/cps}{/size}"
    nurse_a "{size=*1.2}侧过头！{w=0.3}别呛着！{/size}"
    "棉花擦过下巴。"
    nurse_b "我去叫门外的家属？"
    doctor "去吧，{w=0.3}一次只能进一个。"

    play sound sfx_door_slide
    "门被推开了一条缝。"
    nurse_b "高松先生？{w=0.3}高松太太？"
    nurse_b "病人醒了，{w=0.4}但情绪不太稳定。"
    mother "谢天谢地……{w=0.5}医生，真的太谢谢你们了！"
    father "给你们添麻烦了……{w=0.4}"
    nurse_b "小声点，{w=0.3}这里是重症监护区。"

    # --------------------------------------------------------------------------
    # 冰冷的病房自白：不可捉摸的人类生活
    # --------------------------------------------------------------------------
    play music reflection fadein 1.5 loop

    tomori calm "看起来他们真的打算在一个刚自杀完的病人床前，{w=0.1}{nw}"
    extend pout "扎堆开辩论会就是了。"

    tomori concern "虽然我跳楼之前确实没料到事情会演变成这么严肃又尴尬的局面，{w=0.1}{nw}"
    extend pout "但好歹让我安安静静待一会儿吧！"

    tomori babble "退一万步讲，{w=0.1}{nw}"
    extend bitter "我刚才只是在普通地睡个午觉，{w=0.1}{nw}"
    extend wtf "你们这样不打招呼就把人摇醒、{w=0.1}{nw}"
    extend babble "又是拿手电筒照瞳孔又是抽管子的，{w=0.1}{nw}"
    extend pout "未免也太不讲礼貌了吧？"

    tomori calm "我还活着。{w=0.1}{nw}"
    extend bitter "我当然会这样想。"

    tomori neutral "一切都会重新开始，{w=0.1}{nw}"
    extend sadaway "我会在这里呆上一段时间，直到医生认为我完全康复。"

    tomori calm "我会再次出院，{w=0.1}{nw}"
    extend sad "再次看到东京都的大街小巷、它的广场、车站、在路上上学放学的学生。"

    tomori sadaway "接着我也会继续重新开始，我会继续，过着一种充满耻辱的生活。{w=0.1}{nw}"
    extend bitter "{alpha=0.6}那种对我而言{/alpha}，{w=0.1}{nw}"
    extend sad "{alpha=0.4}从来就不可捉摸的人类的生活。{/alpha}"

    doctor "高松同学，{w=0.4}右手不要用力，针头会鼓包的。"

    tomori calm "我看着这一切。{w=0.1}{nw}"
    extend neutral "医生在一旁煞有介事地下医嘱，{w=0.1}{nw}"
    extend babble "护士在交头接耳、窃窃私语，{w=0.1}{nw}"
    extend sadaway "父母在门口像犯了滔天大罪一样对着空气连环鞠躬道歉。"
    play sound sfx_heartbeat
    camera at camera_heartbeat
    tomori sadaway "隔着半开的门缝，{w=0.3}我听见父亲压低声音向医生打听着千叶那边全封闭休养学校的手续，{w=0.1}{nw}"
    extend bitter "说等我身上的伤一养好，{w=0.3}就立刻带我办退学过去。"
    play sound sfx_clothes_rustle
    tomori sadaway "母亲用手帕捂着嘴连连点头，{w=0.3}像是只要把我锁进郊外那扇看不见的铁窗里，{w=0.1}{nw}"
    extend bitter "这场让他们抬不起头的麻烦就终于能体面地翻篇了。"

    # --------------------------------------------------------------------------
    # 护士们的交头接耳与雨棚回忆
    # --------------------------------------------------------------------------
    nurse_a "切……{w=0.4}现在的高中生到底在想什么啊……{w=0.4}"
    nurse_b "呃……{w=0.4}不知道。{w=0.3}谁知道呢。"
    nurse_a "哈……{w=0.4}真怪啊。"
    nurse_a "现在的小孩压力有这么大吗？"
    nurse_b "嘛……{w=0.4}也许是呢。"
    nurse_a "你听说是因为什么吗？"
    nurse_b "没。"
    nurse_a "我听警车那边的人说，{w=0.4}好像是跟学校里搞乐队的同学闹翻了。"
    intern_doctor "哈？{w=0.4}乐队吗？"
    intern_doctor "那你觉得她现在躺在这里，{w=0.4}过两天会不会有同队的小姑娘抱成一团哭着跑来探视？"
    nurse_b "哼……{w=0.4}怎么可能。"
    nurse_c "哎呀……{w=0.4}现在她们不都这样。{w=0.4}表面上好好的，背地里谁知道想的会是什么呢。"
    nurse_a "而且啊……{w=0.4}刚好砸在自行车棚的塑料顶棚上缓冲了嘛。"

    # 镜头转入医院大楼与被砸穿的雨棚（hospital_exterior_01_blue）
    scene bg hospital_exterior_01_blue with dissolve
    nurse_a "听说连雨棚都被砸穿了一个大窟窿，{w=0.4}物业今天早晨还在找学校索赔呢。"
    nurse_b "喂，小声点！"
    nurse_b "万一让家属听到又要投诉我们了。"
    play sound sfx_footsteps

    # 回到冷蓝病房
    scene bg hospital_bed_01_blue with dissolve
    play ambient_sfx sfx_trolley_wheels volume 0.7

    "走廊外的谈话声伴随着手推车轮子的吱呀声慢慢飘远。"

    # 灯自嘲自艾与乐队解散反思（细腻情绪差分）
    tomori calm "好无聊。{w=0.1}{nw}"
    extend bitter "他们的议论让我很不爽，{w=0.1}{nw}"
    extend pout "我也不知道为什么。"

    tomori neutral "倒也不是说他们在胡说八道。{w=0.1}{nw}"
    extend sadaway "我本来和他们描述的情况大差不差。"

    tomori sad "在学校里交不到朋友，{w=0.1}{nw}"
    extend bitter "在乐队里发不出声音。"

    tomori bitter "最后甚至连死都没能干脆地死成！{w=0.1}{nw}"
    extend pout "只知道像一袋垃圾一样砸穿学校的塑料雨棚。"

    tomori calm "我也没太把那些护士的闲话放在心上。{w=0.1}{nw}"
    extend soft "而且，{w=0.1}如果真的一切正如他们所说，也不是十足的坏事。"

    tomori calm "我没有理由觉得委屈。{w=0.1}{nw}"
    extend bitter "因为这意味着祥子她们现在同样觉得我恶心透顶。{w=0.1}{nw}"
    extend calm "那样再好不过。"

    tomori sad "不管旁人怎么议论，{w=0.1}{nw}"
    extend bitter "那支乐队确实是在我手里彻底粉碎的。"

    voice "audio/voice/vo_tomori_01_02.ogg"
    tomori sadaway "她们要是从此再也不理我，{w=0.1}{nw}"
    extend bitter "我一点也不会感到奇怪。{w=0.1}{nw}"
    extend sadaway "毕竟……{w=0.5}我就是这样一个只会给别人添麻烦的人啊。"

    tomori calm "……{w=0.4}{nw}"
    extend concern "可是，刚才那个年轻医生说的那些话……{w=0.1}{nw}"
    extend ah "{cps=*1.3}会有人抱着花哭着跑来医院看我吗？{/cps}"

    # --------------------------------------------------------------------------
    # 脑补爆发：漫画般的摇滚少女誓约（立希与素世的幻象展出）
    # --------------------------------------------------------------------------
    tomori calm "我从来没敢往这方面想过。{w=0.1}{nw}"
    extend ehh "那种跌跌撞撞冲进病房、{w=0.1}{nw}"
    extend kya "握着我的手抽泣着后悔的画面……"

    tomori wtf "哇。{w=0.1}{nw}"
    extend ehh "这么一说，{w=0.1}{nw}"
    extend yay "那简直……"

    # 规范立绘展出：taki 03 sad（悲伤动摇）与 soyo 01 normal（撕下假面的决绝）
    show taki 03 sad at left_standee with dissolve
    show soyo 01 normal at right_standee with dissolve

    tomori yay "{cps=*1.5}为了不成器的主唱、在大雨中反抗全世界的摇滚少女们……{/cps}{w=0.5}{nw}"
    play sound sfx_strike
    extend kya "{b}{cps=*1.6}\n禁忌的羁绊，被暴雨冲刷的誓约！{/cps}{/b}{w=0.5}{nw}" with shake_h
    extend yay "{b}\n简直像漫画里的情节一样！{/b}"

    tomori smile "如果有真的这种情节发生的话，{w=0.1}{nw}"
    extend yay "那么我现在在这里躺着这么长时间也不算浪费。"

    # --------------------------------------------------------------------------
    # 幻灭：地下排练室的尘埃与刻舟求剑（0.28s 焦橙负片快门瞬间烧碎漫画幻象）
    # --------------------------------------------------------------------------
    play sound sfx_impact
    $ photosnap(duration=0.28)
    hide taki
    hide soyo
    with ed_cut

    tomori calm "她们会说没关系，{w=0.1}{nw}"
    extend sadaway "只不过我让她们很失望。"

    tomori sad "她们会很快意识到，{w=0.1}{nw}"
    extend calm "没人愿意再把乐队组下去了。"

    tomori sadaway "没有人会愿意读我的日记，看完我写的歌词。{w=0.1}{nw}"
    extend babble "人们草草翻阅一通，然后将它们塞到我的病历最后，{w=0.1}{nw}"
    extend bitter "好像其得出的结论不过是，我是一个需加管控的多语症患者。"

    tomori calm "到末了，每个人总是自己独自行动，不再和任何人有关系——{w=0.1}{nw}"
    extend sadaway "只要死过一次，便可以看清这一点。"

    tomori calm "哪怕我真的死掉了，人们为我啼哭，为我伤心，悼念我一天、一个月，甚至一年；{w=0.1}{nw}"
    extend sadaway "然而消失的人终于还是消失了、离开了。{w=0.1}{nw}"
    extend calm "时间继续一天、一个月、一年地向前下去，头也不回。{w=0.1}{nw}"
    extend soft "人们最终也回到他们的时间去，不再刻舟求剑。"

    # 闪回地下排练室（rehearsal_room_01_blue）
    scene bg rehearsal_room_01_blue with dissolve
    tomori sad "白色的塑料门牌会剥落，{w=0.1}{nw}"
    extend sadaway "练习室里的歌谱会积满灰尘，{w=0.1}{nw}"
    extend calm "于是所有的人都会顺理成章地忘记我，后来连我的名字也会一起忘掉——{w=0.1}{nw}"
    extend soft "那，就随它去吧。"

    # 切回单人病房（hospital_bed_01_blue）
    scene bg hospital_bed_01_blue with dissolve

    tomori sad "但是另一方面，{w=0.1}{nw}"
    extend uff "我真的很……{w=0.1}{nw}"
    extend sad "\n难过。"

    tomori bitter "我这么想很蠢也很贪婪。{w=0.1}{nw}"
    extend calm "现实才不会有漫画里的奇迹。"

    tomori sad "如果祥子、立希和爽世真的彻底不要我了……{w=0.1}{nw}"
    extend sadaway "我就好像，{w=0.5}真的再也没有什么可以指望的了。"

    # 章节终结转场
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    scene black with slow_dissolve

    $ persistent.cleared_chapter_1 = True
    jump ch02_silence
