## ch04_intrusion.rpy - 第四章：越界的闯入与窗外的阴天
## 严格对标《规范文件.md》视觉素材规范与 11111.docx 对象修订终盘定稿
## 背景规范：hospital_bed_01_blue / corridor_01_blue
## 立绘规范：anon hosp 01~10 规范病房立绘
## 主视角 Side Image 头像差分系统：高频切换 + extend 句子内微表情拆分

label ch04_intrusion:
    $ current_chapter = 4
    $ quick_menu = True

    # 阴天病房，爱音的越界闯入（hospital_bed_01_blue）
    scene bg hospital_bed_01_blue with fade
    play bgs bgs_hospital fadein 2.0 loop
    play music searching fadein 2.0 loop

    tomori calm "真奇怪。{w=0.1}{nw}"
    extend sadaway "一天前，{w=0.4}我还一心盼着自己的内脏慢慢停止跳动。"

    tomori neutral "“你不想知道自己的检查结果吗？”{w=0.4}那时一个护士这样对我说。{w=0.1}{nw}"
    extend calm "我摇了摇头，{w=0.3}不算肯定也不算否定，{w=0.3}我的身体情况我自然清楚不过。"

    tomori calm "我心里清楚。{w=0.4}或许那些仪表能很好地反映我的身体在发生什么，{w=0.3}但是它们无法解释我心里发生着什么。{w=0.1}{nw}"
    extend bitter "虽然我写下的话向来缺少分量，{w=0.4}但我还是准备好了在尚有一点力气的时候离开，{w=0.3}最好的时间是一天前，{w=0.3}其次就是现在。"

    tomori uff "那时候，{w=0.3}我讨厌任何递到嘴边的热气，{w=0.3}讨厌护士换药时撕开胶布的声音，{w=0.3}更讨厌窗外透进来的每一缕光线。{w=0.1}{nw}"
    extend soft "可是今天中午，{w=0.4}当护士把那一小碗南瓜粥端进来的时候，{w=0.3}我居然握着勺子，慢慢把它喝完了。甚至连医生查房时递过来的温水，{w=0.3}我也乖乖喝了半杯。"

    tomori calm "因为我在心里悄悄算着时间。如果我不吃东西，{w=0.3}护士就会一直在房间里念叨，{w=0.3}下午的探视时间就会被各种各样的检查占满。{w=0.1}{nw}"
    extend concern "那样的话……{w=0.4}千早爱音推门进来的时候，我就没有力气和她说话了。"

    tomori sadaway "如果她完全不期待和我说话，{w=0.3}但愿如此，这只是我自作多情。{w=0.1}{nw}"
    extend soft "不过，但凡她真的顺着楼梯溜下来了，哪怕只有万分之一的可能，{w=0.3}她推开门想要找个人聊聊天，而我却因为没有吃饱饭而昏昏沉沉地背对着她，{w=0.3}我辜负了她的心意，就太不应该了。"

    tomori soft "她比我好上千倍万倍，如果我都能得到垂怜，那么她也一样。我的脑子里还是一遍又一遍地排演那些场景。{w=0.1}{nw}"
    extend babble "在喝那半杯温水的时候，又或者只是靠在铁床边漫无目的地消磨时间，我都会忍不住开始想。"

    tomori concern "要是她问我今天感觉怎么样，我是该回答“还好”，还是该告诉她“肋骨没有前两天那么疼了”？{w=0.1}{nw}"
    extend ehh "要是她又开始吹嘘伦敦的大本钟和红茶，我是该安静地听着，还是该问她司康饼到底是什么味道？{nw}"

    # 快乐boop小曲配合爱音进门
    play sound sfx_door_slide
    play music banter fadein 0.5 loop
    show anon hosp 08 gentle at anon_burst_in
    $ renpy.pause(0.65, hard=True)

    anon "哈喽……{w=0.4}高松同学！" with standee_shake_h
    show anon hosp 02 boast
    anon "哎呀……{w=0.4}今天精神看起来不错嘛！"

    tomori calm "她很自然把门反手关上了。"

    tomori neutral "……{w=0.4}千早同学。"

    show anon hosp 01 smug at standee_shake_h
    anon "行啦……{w=0.4}都说了多少遍啦，叫我爱音！"
    show anon hosp 02 boast
    anon "你看……{w=0.4}我今天冒着被护士长抓包的危险，去自动贩卖机抢到的战利品！"

    tomori ehh "……{w=0.4}草莓牛奶？"

    voice "audio/voice/vo_anon_04_01.ogg"
    show anon hosp 08 gentle at standee_shake_h
    anon "两瓶！刚好是最后两瓶哦……{w=0.4}"

    tomori soft "还没等到我拒绝，她就给牛奶插上吸管，把玻璃瓶塞到了我手里。"

    tomori smile "……{w=0.4}谢谢爱音。"

    tomori soft "听到“爱音”两个字，她的唇边满意地翘起来，露出右边那颗虎牙。"

    show anon hosp 08 gentle at anon_sit
    tomori calm "她吸了一大口牛奶，两只脚在椅子下面晃来晃去。爱音喝着牛奶，她看起来是个好人。{w=0.1}{nw}"
    extend soft "起初我还想过她是不是想耍我，或者搞什么恶作剧，但现在看来并非如此。不要再与世界作对，我建议自己，去爱现实。{w=0.1}{nw}"
    extend smile "爱音没有和我这么说，但是我渐渐要把自己说服了。"

    show anon hosp 03 curious_1
    anon "对了高松同学……{w=0.4}我昨天看你病历卡上写着16岁，你是在哪所学校念书啊？"

    tomori neutral "那个……{w=0.4}羽丘女子学园。"

    show anon hosp 03 curious_2 at anon_sit, standee_shake_h
    anon "羽丘？！"
    anon "{size=*1.45}真的假的？！{/size}"
    show anon hosp 02 boast
    anon "其实……{w=0.4}我回国之后办转学手续，家里安排的也是羽丘诶！"

    tomori ah "……{w=0.4}真的吗？"

    show anon hosp 01 smug
    anon "对吧？{w=0.4}当然是真的啦！"
    show anon hosp 08 gentle
    anon "本来我还担心回国插班会跟不上大家，{w=0.4}没想到居然在医院里先遇到了未来的同校同学！"
    show anon hosp 02 boast at anon_sit, standee_shake_h
    anon "那我们以后不就是同级的校友了吗！{w=0.4}好耶——"

    tomori soft "她趴在病床边的铁栏杆上，我能闻到她身上洗发水的气味。"

    show anon hosp 08 gentle
    anon "喂……{w=0.4}高松同学，羽丘的校风怎么样？"

    tomori concern "我……{w=0.4}不太清楚。"

    show anon hosp 03 curious_1
    anon "诶，比如说就是，大家平时下课都会去哪里玩啊……？{w=0.4}"

    tomori sadaway "我很少出去玩的……{w=0.4}有的时候我就喜欢自己一个人呆着。"

    show anon hosp 08 gentle
    anon "我怎么听起来不像是真的呢，那你平时的爱好会是？"

    tomori calm "下课的时候……{w=0.4}我一般都在教室角落里坐着。{w=0.1}{nw}"
    extend neutral "或者……{w=0.4}去操场边上看落叶。"

    show anon hosp 03 curious_1
    anon "哈？{w=0.4}看落叶？"
    anon "你平时在学校都不和别人聊天的吗……？{w=0.4}"

    tomori sadaway "……{w=0.4}不太会聊天。{w=0.1}{nw}"
    extend neutral "大家聊的话题……{w=0.4}我都听不懂。"

    show anon hosp 08 gentle
    anon "那又怎样嘛……{w=0.4}你是挺怪的，但我就喜欢你这点——"
    show anon hosp 02 boast
    anon "反正……{w=0.4}等我去了羽丘，和我一起玩就够了嘛。"

    tomori ah "……{w=0.4}"

    tomori soft "我有多久没像这样跟人聊天了？感觉像是过了好几个世纪。爱音啊……{w=0.1}{nw}"
    extend smile "真的，我好久没试过这么轻松地跟人说话了。之前我都在干什么呢？这可怪罪不到其他人头上。"

    tomori concern "爱音往床头柜上扫了一圈，突然停在了那昨天没有看完的本子上。{w=0.1}{nw}"
    extend uff "警报在我的脑子里拉响了。"

    # 搞笑抖包袱效果：急促战斗曲、警报音效与立绘迫近
    play sound sfx_impact
    play music tense1
    show anon hosp 03 curious_1 at anon_table

    anon "咦？{w=0.4}这是什么？"
    anon "昨天我就想问了……{w=0.4}日记本？还是作业？"

    tomori concern "只要我说是数学错题集，她肯定连碰都不会碰一下。{w=0.1}{nw}"
    extend kya "{cps=30}快说那是数学错题集啊！{/cps}{w=0.1}{nw}"
    extend uff "可是我的嘴唇完全不听大脑的指挥。"

    tomori babble "……{w=0.4}是写歌词的本子。"

    tomori pout "糟糕透顶……我为什么要说实话。爱音整个人像是被点着了一样，眼睛亮起来。"

    # 罐头闪烁音效 + 切入更夸张的战斗曲tense2
    play sound sfx_sparkle
    play music tense2
    show anon hosp 02 boast at anon_table, standee_shake_h

    anon "哈？！{w=0.4}歌词？！"
    anon "音乐？！{w=0.4}"
    anon "高松同学你居然在写歌词？！{w=0.4}"

    tomori calm "……{w=0.4}以前写的。{w=0.1}{nw}"
    extend neutral "现在……{w=0.4}不写了。"

    tomori concern "我试图用最直接、最直白、最不绕弯子的语气把这件事糊弄过去。距离本子还有十公分。五公分。两公分。{w=0.1}{nw}"
    play sound sfx_page_turn
    extend pout "然而她完全没有理会我的后半句话，兴致勃勃地翻开封皮。也许那句话其实并不能起任何作用就是了。"

    show anon hosp 08 gentle
    anon "行啦……{w=0.4}我看看我看看！"
    anon "哇……{w=0.4}字写得还挺工整的嘛……{w=0.4}"

    tomori calm "病房里一下子安静了下来。爱音低着头，手指按在活页本的纸张边缘。她盯着本子看了好几秒钟，慢慢把散落的粉色碎发撩到耳后。"

    # 翻阅高潮罐头音效 + 切入tense4
    play sound sfx_sparkle
    play music tense4
    show anon hosp 03 curious_2 at anon_table, standee_shake_h

    tomori uff "我祈祷她看不见那些内容！不行！我急忙伸出手去，想要把它从爱音手里抢回来。爱音稍微刚好避开了我伸过去的手。"

    show anon hosp 05 annoyed_1
    anon "喂……{w=0.4}别乱动嘛，病人就给我好好躺着！"

    tomori concern "她后退到我够不着的地方去了。她的眼睛上下翻飞，左右跳跃着，我希望她赶紧停下来，可是我知道我叫不住她的。我只能无可奈何地看着她那张脸，和她眉飞色舞地讲话的时候没什么两样。我好害怕。她那样，我分辨不出来，究竟是在挑选有意思的片段，还是搜寻笑料。毕竟，女生们走在一起说说笑笑的样子就是像她这样的。"

    "她突然凑过来。"
    show anon hosp 03 curious_1 at anon_table
    anon "……{w=0.4}等一下，这一行写的是什么？"

    tomori uff "她把本子递到我面前，手指指着某一行歌词。好羞耻。这些东西就这样示人了……那些字……光是扫一眼就要了我的命了。我忍不了了。"

    tomori babble "快……{w=0.4}快给我！"

    stop music
    tomori calm "爱音停住了。预想中的尖叫和嘲笑并没有落下来。抵在我脑门上的两根手指收了回去，她啪的一声合上本子，用一种像是刚看完卢浮宫名画一样的深沉样子看着我。"

    show anon hosp 08 gentle
    anon "其实……{w=0.4}你的歌词很酷。"
    anon "写得很有意思……{w=0.4}"

    tomori ehh "……{w=0.4}啊？"

    stop music fadeout 1.0
    play music summer fadein 1.5 loop

    tomori soft "她把本子抱在怀里，歪着脑袋，若有所思地盯着床头柜上的那束白百合花。"

    show anon hosp 01 smug
    anon "我刚不就这意思嘛！{w=0.4}我说真的……{w=0.4}不要质疑我的眼光！"
    anon "写了又不给人看，{w=0.4}那还有什么意义？"
    show anon hosp 03 curious_1
    anon "不过话说回来……{w=0.4}"
    anon "高松同学，前两天来病房看你的那几个人……{w=0.4}该不会就是你之前的乐队队友吧？"

    tomori neutral "爱音……{w=0.4}看见她们了？"

    show anon hosp 08 gentle
    anon "当然看到了……{w=0.4}那天下午我正好在走廊里晃悠呢！"

    tomori calm "……{w=0.4}嗯。{w=0.1}{nw}"
    extend neutral "是立希买给我的花……{w=0.4}{nw}"
    extend sadaway "\n她们……确实是我以前的队友。"

    show anon hosp 03 curious_1
    anon "哈……{w=0.4}原来是这样吗？"
    anon "那后来怎么不玩了……？{w=0.4}"
    anon "是吵架了吗？{w=0.4}还是音乐理念不同什么的呢？"

    stop music

    tomori sadaway "是我……{w=0.4}"

    tomori calm "我低着头，不敢看爱音的眼睛。离别没有来临，但未来确实会来。这一次我汲取了教训。我停止奢望。也许，我最终也会停止追赶你。"

    tomori sadaway "{cps=30}因为我唱得太差了。{w=0.35}{nw}"
    extend bitter "{cps=35}在舞台上发不出声音……{w=0.2}连一句完整的歌词都唱不出来。{w=0.35}{nw}"
    extend sad "{cps=40}大家为了照顾我，{w=0.2}付出了那么多努力。{w=0.35}{nw}"
    extend uff "{cps=45}可是我却把演出全毁了……{w=0.35}{nw}"
    extend bitter "{cps=50}祥子把乐谱撕掉了，{w=0.2}立希和大家吵架了……{w=0.35}{nw}"
    extend sadaway "{cps=56}全都是因为我。{w=0.35}{nw}"
    extend sad "{cps=62}如果不是因为我……{w=0.2}大家就不会解散了。{w=0.4}{nw}"
    extend uff "{cps=68}{alpha=0.75}对不起……{w=0.2}{/alpha}{alpha=0.45}真的对不起……{/alpha}"

    play music summer loop

    show anon hosp 03 curious_1 at anon_table, standee_shake_h
    anon "哈？！" with shake_h
    show anon hosp 07 normal_1
    anon "你道什么歉啊……？！{w=0.4}"
    anon "行啦……{w=0.4}你也不需要道歉的！"
    anon "那事跟你又没关系嘛……{w=0.4}"

    tomori ehh "我抬起头，满脸茫然。"

    tomori ehh "……{w=0.4}啊？{w=0.1}{nw}"
    extend concern "也……没关系？"

    "她翻了个大大的白眼，气呼呼地抱起手臂。"

    show anon hosp 05 annoyed_1 at anon_pace_right
    anon "切……{w=0.4}废话！"
    anon "乐队是好几个人一起玩的东西吧……？{w=0.4}"
    anon "演出出了状况，{w=0.4}大家一起想办法解决不就好了吗！"

    show anon hosp 05 annoyed_2 at anon_pace_left
    anon "凭什么一个人撕了乐谱跑掉，{w=0.4}所有责任就全变成你的错了啊？"
    anon "他们会以此为借口，{w=0.4}彻底把事情甩到一边！"
    anon "那些动不动就把责任推给别人、搞得大家都不开心的家伙，{w=0.4}光是听着就让人心烦！"

    tomori concern "……{w=0.4}心烦？"

    show anon hosp 07 normal_2 at anon_lean_in
    anon "对吧？{w=0.4}超烦的！"
    anon "最讨厌这种动不动就甩脸子搞得全天下都欠她一样的做派了……{w=0.4}"
    show anon hosp 05 annoyed_1 at anon_lean_in, standee_shake_h
    anon "高松同学你也是，{w=0.4}干嘛把什么黑锅都往自己身上揽啊！"
    anon "你又不是垃圾桶……！{w=0.4}"

    tomori calm "看着我发呆的样子，爱音有些不自然地咳了一声。"

    show anon hosp 04 shy_1 at anon_retreat
    anon "咳……{w=0.4}"
    show anon hosp 01 smug
    anon "好啦……{w=0.4}过去的事情就让它过去嘛！"
    show anon hosp 02 boast
    anon "反正等我去了羽丘，{w=0.4}我肯定是要组一支全校最闪耀的女子乐队的！"

    tomori neutral "……{w=0.4}爱音要组乐队？"

    "她站起身来，得意洋洋地比划着弹吉他的姿势。"
    show anon hosp 02 boast at anon_center

    anon "当然啦……{w=0.4}"
    anon "我在英国的时候就看中了一把超好看的粉色电吉他哦……{w=0.4}"
    anon "回国之后我一定要买下来……{w=0.4}"
    anon "到时候，{w=0.4}我要站在舞台最中间！"
    anon "高松同学，你既然会写词，那等我组了乐队，{w=0.4}你就来给我当主唱！"

    tomori ah "我……？{w=0.4}"
    tomori sadaway "我不行的……{w=0.4}我真的唱不好……{w=0.4}"

    tomori calm "主唱。在舞台中央发出声音。像是发现了什么不得了的事情一样，爱音突然凑近过来，上下瞅着我。"

    show anon hosp 03 curious_1 at anon_lean_in
    play music joyful fadein 1.5 loop

    anon "喂……{w=0.4}高松同学。"
    show anon hosp 08 gentle
    anon "你看……{w=0.4}你今天气色真的比前两天好多了诶！"
    anon "脸上都有血色了，{w=0.4}刚才说话声音也比昨天大了一点点！"
    show anon hosp 02 boast
    anon "你看你……{w=0.4}草莓牛奶都快喝完大半瓶了！"

    tomori calm "我顿了两秒。可能还眨了两下眼睛。"

    tomori ehh "……{w=0.4}有吗？"

    show anon hosp 01 smug
    anon "有啊……{w=0.4}绝对有！"

    tomori smile "她好细心啊。"

    "她双手叉腰，在床前转了个圈。"
    show anon hosp 08 gentle

    anon "我说啊……{w=0.4}你总是应该下床走走的。"

    tomori concern "散、散步……？{w=0.4}{nw}"
    extend neutral "可是……护士说还要静养……{w=0.4}{nw}"
    extend uff "\n我……站不太稳。脚底下……没有力气。"

    tomori calm "爱音掀开我的被角，把塑料拖鞋踢到床沿下面。"

    show anon hosp 01 smug
    anon "切……{w=0.4}怕什么！有我扶着你呢！"
    show anon hosp 08 gentle
    anon "来……{w=0.4}把脚放下来！"

    tomori calm "脑子还是晕乎乎的，但起码能自己站起来了。我从床沿撑起来，借着她的支撑直起膝盖——"

    tomori uff "……{w=0.4}唔。"

    tomori sadaway "算了。还是站不稳。"

    show anon hosp 06 pain
    anon "哇——哇……！{w=0.4}"
    anon "小心点啦……{w=0.4}"

    show anon hosp 08 gentle at stand_up_stagger
    with shake_h
    $ renpy.pause(1.05, hard=True)
    anon "慢点起……{w=0.4}一、二、三，起！"

    tomori soft "在我摔到地上前，她接住了我。"
    play sound sfx_clothes_rustle
    "她把我的左手臂搭在她自己的肩膀上，另一只手揽住我的腰。"

    camera:
        warp ease_in_out_cubic 1.2 zoom 1.08 pos (0.5, 0.48) rotate -1.5
    $ renpy.pause(1.2, hard=True)

    tomori soft "怀着某种担心，{w=0.3}就像我是一件易碎的物品，{w=0.4}……我真不想承认，{w=0.3}但她是正确的。{w=0.1}{nw}"
    extend smile "有人扶着……{w=0.3}确实很有帮助。"

    tomori calm "当我的双脚重新踩在坚硬的地板上时，{w=0.4}整个世界的分量好像一下子全都压了回来。{w=0.1}{nw}"
    extend soft "可这一次，{w=0.3}这分量不再让我感到害怕，{w=0.4}因为有一半的重量……{w=0.4}正落在她的肩膀上。"

    tomori sadaway "几天前，{w=0.4}我站在天台边缘任由身体向下坠落；{w=0.1}{nw}"
    extend soft "爱音的出现，{w=0.3}是不是因为世界需要阻止我，{w=0.3}好去成就什么更重要的事情呢？还是说，是因为我潜意识里渴望着什么东西——任何东西——来阻止我？"

    tomori calm "而且，{w=0.3}我其实并不在乎伦敦的红茶到底是什么滋味，{w=0.4}但我拼命假装我在乎，{w=0.3}我顺着她的话点头，{w=0.4}想问她什么时候能带我去看大本钟。"

    play sound sfx_heartbeat
    tomori calm "我不知道。{w=0.5}她的头发蹭过我的脖颈时，{w=0.4}我产生了错觉，{w=0.4}和我从四楼跳下来时同样强烈。{w=0.1}{nw}"
    extend soft "仿佛我经年累月费尽心力，{w=0.3}从高高的地方一跃而下——然后熬过那些夜晚，仅仅是为了在这一刻……倒进她的怀里。"

    tomori soft "我们认识还不到两天。在昨天以前，我甚至不知道世界上存在着千早爱音这个人。{w=0.1}{nw}"
    extend calm "在一周以前，她大概正背着吉他盒走在我不认识的街道上，在更早以前，她甚至还在大洋彼岸的另一座城市里。{w=0.1}{nw}"
    extend soft "可现在，我却觉得我好像已经在渡船上等了她整整一辈子。"

    tomori soft "尽管在那漫长的十六年里，我们从来没有过哪怕一秒钟的交集。{w=0.1}{nw}"
    extend smile "但只是因为她也喜欢被人羡慕、也因为我也在做着同样的事情——拼尽全力，想要让她觉得我是一个可以交谈的朋友。{w=0.1}{nw}"
    extend kya "这种巧合……让我脸红。"

    camera:
        warp ease_in_out_cubic 0.8 zoom 1.0 pos (0.5, 0.5) rotate 0.0
    $ renpy.pause(0.8, hard=True)

    show anon hosp 08 gentle
    anon "呼……{w=0.4}高松同学，你看着瘦瘦小小的，怎么骨头还挺沉的嘛！"
    anon "站稳了没有……？{w=0.4}"

    tomori sadaway "……{w=0.4}对不起……{w=0.4}压疼你了吧？"

    "她没好气地敲了一下我的脑门。"

    show anon hosp 07 normal_1
    anon "好啦……{w=0.4}你没必要总是道歉的。"

    tomori smile "……{w=0.4}好。"

    show anon hosp 08 gentle
    anon "嘘……{w=0.4}小声点！"

    tomori soft "这不奇怪。听她这么个吵吵嚷嚷的女孩子嘱咐得这么认真，还是令人莞尔的。"

    anon "护士站就在前面转角，{w=0.4}要是被护士长看到我们私自出来溜达，肯定又要被抓去写检讨了！"

    tomori ehh "……{w=0.4}检讨？"

    show anon hosp 04 shy_1
    anon "对啊……{w=0.4}昨天我被她训了半个小时，还要我保证不在走廊里大声喧哗！"

    tomori soft "看着她小心翼翼踮着脚尖走路的滑稽模样，我轻声开口。"

    tomori calm "……{w=0.4}爱音很像小偷。"

    "她差点脚下一滑，瞪着我。"

    show anon hosp 05 annoyed_1 at standee_shake_h
    anon "切……{w=0.4}哪有这样的小偷啊！"

    tomori calm "阿德利企鹅……{w=0.4}"

    show anon hosp 08 gentle
    anon "我知道啦……{w=0.4}你说过的！喜欢偷石头。"

    tomori ah "诶……？{w=0.4}原来爱音能记住的吗？"

    "爱音翻了个白眼。"
    tomori smile "好吧。其实我心里是开心的。本来不是什么很值得奇怪的事情，但是记住我说过的话并不是任何人的义务。而现在眼前这个人做到了。"

    stop music 

    # 两人并肩走在走廊（corridor_01_blue）
    scene bg corridor_01_blue with push_right
    play sound sfx_footsteps
    $ renpy.pause(0.8, hard=True)

    tomori calm "我们这样走过了二十米长的走廊。终于挪到了走廊尽头的那扇大窗户前。"

    camera:
        blur 16.0
        warp ease_out_cubic 2.2 blur 0.0
    play music lily fadein 2.0 loop
    $ renpy.pause(2.2, hard=True)

    tomori soft "好了。视野变清晰了一些。窗外是秋日午后淡金色的天空。阳光透过玻璃照在我的脸上，暖洋洋的。窗缝里漏进来的微风吹动着我的额发，带着室外干爽的气息。我双手扶着窗台，低头看着医院外面的街道。"

    tomori calm "……{w=0.4}嗯。"

    tomori calm "从五楼往下看。我能看清人行道了，还有建筑物、天空和灯光。听到的，是城市的噪声，无休无止、低沉喑哑、无边无际的嘈杂。{w=0.1}{nw}"
    extend neutral "他们要么就是在回家，要么就是在睡觉，要么就什么都没做。楼下的马路上，汽车慢慢移动着。穿着制服的初中生走过人行道，路边的银杏树叶子已经开始泛出金黄色。{w=0.1}{nw}"
    extend soft "那是活着的世界。周围的一切都很友善。一切都很美。真好。这些都是值得一看、值得一想的美好事物。"

    "爱音顺着我往外看下去，忽然指着远处的一栋红砖大楼。"

    show anon hosp 03 curious_1 at right_standee with dissolve
    anon "喂……{w=0.4}高松同学，你看那边！"
    anon "那栋楼是不是羽丘的校舍啊……？{w=0.4}"

    tomori calm "……{w=0.4}不是。{w=0.1}{nw}"
    extend neutral "那是图书馆……{w=0.4}{nw}"
    extend calm "\n羽丘在更往右边的坡道上面……"

    show anon hosp 08 gentle
    anon "切……{w=0.4}长得真像。"
    show anon hosp 02 boast
    anon "等我们出院了，{w=0.4}一起去羽丘上学吧！"

    tomori concern "那个……{w=0.4}爱音，真的想和我一起组乐队吗？"

    show anon hosp 01 smug at standee_jump
    anon "{cps=*1.5}对吧？{w=0.2}当然是真的啦！{/cps}"

    tomori soft "她伸出小拇指，递到我面前。"

    show anon hosp 08 gentle at standee_step_in
    anon "来……{w=0.4}拉钩！"

    show anon hosp 04 shy_2 at standee_step_in with flash_warm
    "看着她白皙的小拇指，我顿了一下，慢慢伸出自己的小指，轻轻勾住了她的手指。"

    tomori smile "……{w=0.4}拉钩。"

    show anon hosp 08 gentle at anon_center, standee_shake_h
    "她用力摇了摇我们勾在一起的手指。走廊另一头突然传来了护士长严厉的喊声。"

    play sound sfx_footsteps
    nurse_head "{size=*1.3}喂！那边的两个病号！{/size}" with shake_h
    nurse_head "千早同学！高松同学！你们两个怎么跑到窗户那去了？！"
    nurse_head "不是说了高松同学不能剧烈运动吗？！快回病房！"

    "爱音吓得缩了缩脖子，飞快地拉住我的手。我被她拉着手，拖鞋在地上啪嗒啪嗒地响着。"

    scene bg hospital_bed_01_blue with PushMove(0.35, "pushleft")
    show anon hosp 08 gentle at anon_door

    tomori soft "爱音把我一路拉回病房，{w=0.3}帮我把歪掉的毛巾重新搭回铁床栏杆上。{w=0.1}{nw}"
    extend calm "走廊外护士长的脚步越来越近，{w=0.3}她朝我吐了吐舌头，{w=0.3}退到门边，握着门把手小声说："

    show anon hosp 01 smug at anon_door
    anon "先溜啦！{w=0.3}明天老时间，我再溜下来找你——{w=0.3}要是那本笔记本你还没藏好，{w=0.3}我可就接着往下看咯！"

    hide anon with dissolve

    # 门关上，病房重回孤独清寂（hospital_bed_01_blue）
    play sound sfx_door_close
    play bgs bgs_hospital fadein 2.0 loop
    play music reflection fadein 2.0 loop

    tomori calm "门轻轻合上，{w=0.3}病房里重新安静下来。{w=0.1}{nw}"
    extend soft "甚至在她把门关上以后，{w=0.3}我似乎还能看见她站在门缝那儿朝里张望的样子。"

    play sound sfx_clothes_rustle
    tomori soft "我在床上慢慢躺下来，{w=0.4}把脸贴在还留着一点草莓牛奶甜味的枕头上。{w=0.1}{nw}"
    extend calm "床头柜被她随手擦得很干净，{w=0.3}白色的水杯端端正正地摆在正中间。"

    camera:
        warp ease_in_out_cubic 2.2 pos (0.5, 0.48) zoom 1.04
    $ renpy.pause(2.2, hard=True)

    tomori smile "我看着天花板，{w=0.4}看着刚才她站过的那块地板，{w=0.4}看着被她碰过的窗台，{w=0.4}第一次没有再去数墙上的裂缝。{w=0.2}{nw}"
    extend soft "一闭上眼睛，我就开始想您，{w=0.3}而且只想您一个人。{w=0.2}我会整夜、整个星期都想您。{w=0.3}{nw}"
    extend smile "明天您一定要到这里来，{w=0.3}我要再见到您，{w=0.2}一次一次地再见到您。"

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    camera at default
    scene black with slow_dissolve

    $ persistent.cleared_chapter_4 = True
    jump ch05_notebook
