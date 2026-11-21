## ch03_encounter.rpy - 第三章：走廊的哭声与逃兵的驻足
## 严格对标《规范文件.md》视觉素材规范与 11111.docx 对象修订终盘定稿
## 背景规范：hospital_bed_01_blue
## 立绘规范：anon hosp 01~10 规范病房立绘
## 主视角 Side Image 头像差分系统：高频切换 + extend 句子内微表情拆分

label ch03_encounter:
    $ current_chapter = 3

    # 一开始先是全黑与环境音
    scene black
    $ quick_menu = False
    play bgs bgs_hospital fadein 2.0 loop

    play sound sfx_door_slide
    $ renpy.pause(0.8, hard=True)

    # NV 模式下全黑画面出现一行神秘呼唤
    nvl clear
    vn_white "“哟。{w=0.4}醒啦？”"
    nvl clear
    window hide

    # 睁眼：高斯模糊与眼睑开合严密绑定非线性动作曲线（hospital_bed_01_blue）
    $ quick_menu = True
    scene bg hospital_bed_01_blue
    show anon hosp 01 smug at center_standee
    play music dreams fadein 1.5 loop

    camera at waking_camera_intro
    show screen eyes_opening
    $ renpy.pause(3.05, hard=True)
    hide screen eyes_opening

    tomori ah "……！{w=0.4}"

    tomori ah "{alpha=0.75}视野里撞进了一大片毫无道理的粉色。{/alpha}{w=0.1}{nw}"
    extend ehh "{alpha=0.75}谁？{/alpha}{w=0.1}{nw}"
    extend calm "{alpha=0.75}我盯着她看了好几秒，努力在空荡荡的脑海里翻箱倒柜，试图找出能和眼前这个人贴合的标签。{/alpha}{w=0.1}{nw}"
    extend neutral "{alpha=0.75}走错房间的访客？{w=0.3}不对，她穿着病号服。{/alpha}{w=0.1}{nw}"
    extend babble "{alpha=0.75}新来的护工？{w=0.3}护工不会用这种像熟人串门一样随性的语气打招呼。{/alpha}{w=0.1}{nw}"
    extend soft "{alpha=0.75}草莓牛奶。{w=0.4}503病房。{w=0.4}外国转院。{w=0.4}天台的自拍。{/alpha}"

    # 念出“千早爱音”那四个字时，高斯模糊度通过动作曲线回归正常，镜头平滑回正，切换回爱音曲
    camera at waking_focus_restore(1.6)
    play music anon fadein 1.5 loop

    tomori ah "啊。{w=0.1}{nw}"
    extend smile "是千早爱音。"

    tomori calm "那个我睡前明明才在心里郑重其事地产生过好感、结果一觉睡醒就忘得一干二净的千早爱音。{w=0.1}{nw}"
    extend babble "我下次应该记忆力再好一点，我敢打赌她认为医生也早就把她介绍给我了。{w=0.1}{nw}"
    extend pout "等我终于把这四个字重新安装回她的头顶上时，我已经直勾勾地盯了人家快半分钟了。再配合上我的睡姿估计有够糟糕的，希望不要产生太糟糕的初印象吧！"

    unknown "喂喂，{w=0.4}你干嘛用那种看外星人似的看我啊？"
    unknown "我又不会咬人。"

    tomori concern "……{w=0.4}你、{w=0.3}你是谁？"
    unknown "诶？原来还需要我给你介绍吗？"

    tomori neutral "……{w=0.4}千早同学。"

    tomori calm "她心安理得地接受了我不知从哪里得知她名字的设定。对她来说，被人认识似乎是一件理所当然的事。"

    voice "audio/voice/vo_anon_03_01.ogg"
    show anon hosp 01 smug at standee_shake_h
    anon "叫爱音就好啦！"
    show anon hosp 07 normal_1
    anon "千早同学听起来太生疏了，{w=0.4}像教导主任点名一样。"

    tomori neutral "……{w=0.4}千早同学。"
    show anon hosp 08 gentle
    anon "行吧行吧……{w=0.4}随你高兴。"
    anon "话说过来……{w=0.4}高松同学……{w=0.4}{nw}"

    tomori ah "……{w=0.4}你认识我？" with shake_h

    tomori calm "她是怎么知道我的名字的？我心里庆幸，好在刚才花了半天终于想起她的名字。"

    show anon hosp 03 curious_1
    anon "咦？这有什么好惊讶的吗？"

    "她伸出手指，示意我看床头柜上方。"
    "501室，高松灯。"

    show anon hosp 01 smug
    anon "你看，{w=0.4}门口有，床头也有。想不知道都很困难吧？"
    show anon hosp 08 gentle
    anon "而且啊……{w=0.4}我还站在这儿观察了半天呢。高松同学，你的睡相还真是有够老实的。"

    tomori sadaway "……{w=0.4}对不起。"

    show anon hosp 07 normal_2
    anon "哎呀……{w=0.4}没必要突然道歉的呀，"
    anon "睡相像展品又不是什么违反院规的事……{w=0.4}就算真的有那回事的话。"
    extend "\n你这个人平时在学校也是这样动不动就向人认错的吗？"
    extend "\n一直这样的话，{w=0.4}会很辛苦的。"

    tomori calm "或许她说的是对的，我是说……或许我该对她的建议表个态，就是“嗯”一声出来也好。可是我好像做不到。{w=0.1}{nw}"
    extend babble "如果一开始就没打算要采纳，不出声是很正常的吧？可以拿我还是个虚弱的病号这个客观条件来掩盖过去，相信她肯定会自然而然地这么来替我解释的。虽然她也是病号。{w=0.1}{nw}"
    extend concern "可是，看她这副样子，真能想到这一层去吗？"

    "她东张西望地找了找病房里的空位，挑了个地方坐了下来。"
    show anon hosp 04 shy_1 at anon_sit
    anon "哈……{w=0.4}真是个怪人。"
    show anon hosp 04 shy_2
    anon "不过算了……{w=0.4}反正五楼全是一帮无聊透顶的怪人。"

    tomori ehh "那个……{w=0.4}千早同学，为什么会在我的病房里？"

    show anon hosp 08 gentle
    anon "这个嘛……{w=0.4}"
    anon "因为啊……{w=0.4}我那间病房太闷了！"

    tomori neutral "……{w=0.4}闷？"

    show anon hosp 05 annoyed_1
    anon "对啊！电视机只能收到三个台，全是无聊的老年养生节目。"
    anon "你看……{w=0.4}隔壁床那个阿姨一直在跟护工抱怨腰疼。"
    show anon hosp 06 pain
    anon "走廊里又冷得要死，护士长还整天盯着我不让我到处乱跑。"
    show anon hosp 07 normal_1
    anon "我本来想去活动室找人聊天的，结果活动室里只有两个大爷在下将棋，{w=0.4}连个能说话的人都没有！"

    tomori calm "可是……{w=0.4}这里是单人病房。"

    show anon hosp 02 boast at standee_shake_h
    anon "就是因为是单人病房我才溜进来的啊！"

    tomori ehh "……？{w=0.4}"

    show anon hosp 08 gentle
    anon "你想想看嘛……{w=0.4}要是多人病房，我推门进去多引人注目啊。"
    anon "这里就你一个人。还是个同龄人呢！"
    show anon hosp 03 curious_1
    anon "而且啊……{w=0.4}早上护士说，501住着一个从来不开口说话、一口饭都不肯吃的人。"
    anon "我一听就超级好奇好不好……{w=0.4}"

    tomori neutral "……{w=0.4}神秘？"

    show anon hosp 02 boast
    anon "对吧？{w=0.4}听起来超有故事的感觉！"
    anon "比如什么落难的财阀大小姐，或者背负着秘密的阴郁系大人物之类的。"
    show anon hosp 07 normal_1
    anon "结果推门进来只发现了一个人。盖着被子，很不舒服的样子。只有你。高松同学。"

    "可能是坐的姿势不舒服了，她站起身来，在我的病房里四处转悠。"
    show anon hosp 07 normal_3 at anon_wander

    call editorial_part3
    scene bg hospital_bed_01_blue with ed_fade
    show anon hosp 07 normal_3 at anon_wander

    tomori babble "啊啊，她是不是无聊了？现在是轮到我来接话茬了。可是，可是，我有什么好说的呢？{w=0.1}{nw}"
    extend concern "我飞快地回忆了一下她刚才说的那几句话是什么……"

    tomori sadaway "我……{w=0.4}我不是大人物。"

    show anon hosp 08 gentle
    anon "咳……{w=0.4}这我看得出来啦！"

    "她走到床头柜旁，盯上了那束白花。"
    show anon hosp 03 curious_1 at anon_table

    tomori calm "她随口说出了其他人不敢说破的事实……然后她就把花忘了。她又看上了花瓶旁边的塑料盒子上。"

    show anon hosp 02 boast at anon_table, standee_shake_h
    anon "哇……！{w=0.4}草莓布丁！"

    tomori soft "像是发现了什么稀奇事，爱音的眼睛一下子亮了起来。{w=0.1}{nw}"
    extend calm "她伸出手指，戳了戳塑料盒表面那层透明的封膜，我差点担心她把它给戳破了，不过显然这种担心是多余的。明明都是女孩子，本来应该了解这一点的。粗枝大叶的人并不多。"

    show anon hosp 08 gentle
    anon "喂……{w=0.4}高松同学。"
    anon "你……{w=0.4}吃不吃这个啊？"

    tomori neutral "……{w=0.4}千早同学想吃吗？"

    show anon hosp 04 shy_1 at standee_shake_h
    anon "切……{w=0.4}谁、谁想吃了！"

    play music dialogue fadein 2.0 loop

    tomori calm "但是，明眼人都能看出来，明明是她被揭穿了吧。不过，似乎是我太直接了呢。{w=0.1}{nw}"
    extend babble "像一只发现零食的企鹅？但是企鹅又是分成很多种的……{w=0.1}{nw}"
    extend ehh "如果是企鹅科里的十八个物种，到底更接近哪一种呢？{w=0.1}{nw}"
    extend neutral "肯定不是皇帝企鹅。皇帝企鹅的身高超过一米一，她看起来大约一米六的样子？{w=0.1}{nw}"
    extend calm "主要不是身高的问题，我是说，我认为她应该不会那么庄重？那么死板？{w=0.1}{nw}"
    extend babble "王企鹅也不像。那么是阿德利企鹅吗？{w=0.1}{nw}"
    extend soft "对。阿德利企鹅性格凶悍又极度爱面子，喜欢偷偷摸摸衔走邻居巢穴里的鹅卵石来炫耀。{w=0.1}{nw}"
    extend ehh "或者……更像是一只小蓝企鹅，或者是跳岩企鹅？{w=0.1}{nw}"
    extend calm "而且，企鹅应该也见不到任何零食。从生物演化的常识来看，这个比喻从源头上就是不成立的。{w=0.1}{nw}"
    extend neutral "野生企鹅主要的食物来源是南极磷虾一类的东西。如果有谁突发奇想，丢下一整包拆开的饼干或者膨化薯片，一只路过的企鹅最多只会出于好奇去啄一啄包装袋。{w=0.1}{nw}"
    extend calm "所以，这世上根本就不存在“发现零食的企鹅”。"

    tomori calm "我大概盯着她看了太久。粉色的长发垂在她白皙脸庞的两侧。{w=0.1}{nw}"
    extend smile "但当她试图掩饰自己的心思时，整张脸又显得滑稽、神气活现而又可怜兮兮。她十岁时，那双眼睛肯定就是如此：就像一枝突然闯进病房的花朵，她的出现甚至不是为了博得他人的美誉，她的意义只是为了说明，红色。{w=0.1}{nw}"
    extend soft "而现在，这抹红色正在她的脸上蔓延开来。随着耳根漫开红晕，她终于忍无可忍地跺了跺脚。双臂往后用力地小幅度甩了甩，两只拳头握紧了，这好像叫恼羞成怒。"

    show anon hosp 05 annoyed_2 at anon_table, standee_shake_h
    anon "喂……{w=0.4}你一直板着脸盯着我发什么呆啊！"

    tomori calm "阿德利企鹅，喜欢偷石头。"

    show anon hosp 03 curious_2 at anon_table, standee_shake_h
    anon "哈？！{w=0.4}这跟石头到底有什么关系啊！"
    show anon hosp 04 shy_2
    anon "行啦……{w=0.4}我只是看它放在这里快要过期了，好心提醒你一句而已！"

    tomori neutral "保质期到后天。"

    show anon hosp 04 shy_1
    anon "……{w=0.4}"

    tomori calm "她脸上的神气有点古怪。可能是在绞尽脑汁地想该怎么把话给圆回去。大概她自己没想这么多吧，谁知道一个假命题要用更多句话来弥补回来呢。真是越描越黑。{w=0.1}{nw}"
    extend babble "啊，现在应该是我把话题往别处引才对。"

    tomori neutral "朋友买的。{w=0.1}{nw}"
    extend calm "买来就是给别人吃的。{w=0.1}{nw}"
    extend smile "千早同学想吃的话……{w=0.4}拿去吃也可以。"

    show anon hosp 03 curious_1
    anon "哈？{w=0.4}真的？"

    tomori calm "我看起来很护食吗？这就是她一开始的心思吧。"

    show anon hosp 01 smug
    anon "你不会等会儿跟护士告状说我偷你东西吧？{w=0.4}"

    tomori ehh "这家伙看着大大咧咧，居然在这种地方这么谨慎吗……"

    tomori neutral "不会。{w=0.1}{nw}"
    extend calm "我不喜欢告状。"

    show anon hosp 08 gentle
    anon "那我就不客气啦……{w=0.4}"

    play sound sfx_pudding_peel
    "她撕开塑料封膜，掰开附赠的小塑料勺。挖了一大勺布丁塞进嘴里。眼睛眯起来了。看来她觉得很好吃。"

    show anon hosp 02 boast at anon_table, standee_shake_h
    anon "唔！活过来了！"
    anon "甜食果然是世界上最伟大的发明！"
    show anon hosp 07 normal_1
    anon "在英国的时候，那边的甜点太甜了，还是东京的布丁最合我的口味！"

    tomori ah "……{w=0.4}英国？"

    show anon hosp 08 gentle at anon_center
    anon "……{w=0.4}对啊。"
    show anon hosp 02 boast
    anon "其实……{w=0.4}我之前在伦敦留学来着。"

    tomori neutral "伦敦……{w=0.4}远吗？"

    show anon hosp 08 gentle
    anon "当然远啦……{w=0.4}坐飞机要飞十几个小时呢！"
    show anon hosp 02 boast at standee_shake_h
    anon "大本钟、伦敦眼、泰晤士河！"

    tomori smile "她的手指在空中停不下来了喂。"

    show anon hosp 08 gentle
    anon "满大街都是红色的双层巴士，超级洋气的！"

    tomori soft "……{w=0.4}听起来很厉害。"

    show anon hosp 01 smug
    anon "那是当然……{w=0.4}"
    anon "我在那边天天都和大家一起喝正统的英式下午茶！"

    tomori ah "哇……{w=0.4}{nw}"
    extend ehh "\n……红茶，很苦吗？"

    tomori concern "她一副拿我没办法的样子。呃，一不小心就脱口而出了。可是我真的不知道啊……"

    show anon hosp 08 gentle
    anon "你看……{w=0.4}放两块方糖，再加一小勺鲜牛奶，一点都不苦。"
    show anon hosp 02 boast
    anon "每次我和同学们去茶室，我都会拍好多好看的照片发动态！"
    anon "大家都在评论区里给我点赞呢！"

    tomori soft "看起来她并没有什么多余的嫌弃之类的意思。太好了。她刚刚说的所有东西……我都在心里一一记下了。"

    tomori soft "……{w=0.4}千早同学的朋友很多呢。"

    show anon hosp 01 smug
    anon "那当然啦……{w=0.4}"
    anon "班上的外国同学经常围着我转呢！"
    show anon hosp 02 boast
    anon "如果有机会的话，{w=0.4}你也一定要去一次才可以！"

    play music sunny fadein 2.0 loop

    tomori soft "国外。真好啊。我在心里咀嚼着这几个字。{w=0.1}{nw}"
    extend calm "在那个离东京坐飞机要十几个小时的地方，街上全都是不认识的人，到处都是听不懂的语言。{w=0.1}{nw}"
    extend sadaway "我突然想说，那你可以带我去吗？{w=0.1}{nw}"
    extend soft "把我塞进你的行李箱里，或者拉着我的衣袖，再或者，直接握着我的手腕——带我离开东京，去到那个只要保持沉默就不会被苛责的世界去。"

    tomori bitter "毕竟，如果只是口头支持的话，那不就是在炫耀自己的经历吗？“如果有机会的话，你也一定要去一次才可以！”{w=0.1}{nw}"
    extend calm "健康又体面的人们总是喜欢这么说。今天去这里，明天去那里，好像到哪里生活对于他们而言，只是在地图上指指点点就能完成的事情。"

    tomori soft "不过，这也不能完全怪她啦。如果换成我是她的话，应该也会忍不住让别人流露出，“你好厉害！”这样的眼光吧。{w=0.1}{nw}"
    extend concern "糟糕，我不应该把她想的那么坏的。对不起，我不应翻来覆去想这些用不着的东西。"

    tomori calm "我想，她也许只是无聊了。我现在还不能下床……呃，其实这只是一句借口。我当然可以下床。不过，即使能下床，我也对同样的楼层中住着什么人没有兴趣。我巴不得所有人都当我不存在。{w=0.1}{nw}"
    extend soft "然而她不是这样，跋涉了那么遥远的路途，见识过那么多我没见过的风景，却还是受不了在这个冷清的五楼被人遗忘。{w=0.1}{nw}"
    extend smile "依然想要被夸奖，想要成为焦点，想要证明自己的特别……{w=0.1}{nw}"
    extend soft "这种心情，即便是我这样孤僻的人，其实也是能够模糊理解的。"

    tomori babble "不知道为什么她停下来不讲了。啊，糟糕，肯定是因为我刚才走神了……我想，再继续听她说。说什么都好。想想有什么想知道的……"

    tomori neutral "外国同学……{w=0.4}会讲日语吗？"

    show anon hosp 03 curious_1
    anon "呃……{w=0.4}怎么可能！"
    show anon hosp 02 boast
    anon "在伦敦当然全讲英文啦……{w=0.4}"

    tomori calm "好蠢的问题。这种事情想也知道吧。"

    tomori neutral "千早同学的英文……{w=0.4}很厉害吧。"

    "她朝窗外看去。外面什么都没有，她刚检查过了。"

    show anon hosp 04 shy_1
    anon "咳……{w=0.4}还、还行吧！"
    anon "日常交流完全没问题……{w=0.4}"

    tomori ehh "那在学校上课的时候……{w=0.4}大家都在聊些什么？"

    "她用塑料叉子戳着布丁边缘。这么快就吃完了吗？不禁让人感叹她的进食速度。"

    show anon hosp 07 normal_1
    anon "就……{w=0.4}就聊流行音乐啊。"
    anon "还有周末去哪里逛街，哪家店的裙子好看之类的……{w=0.4}"

    tomori smile "听起来……{w=0.4}好热闹。"

    play sound sfx_heartbeat
    show anon hosp 08 gentle
    anon "……{w=0.4}嗯。"
    anon "挺热闹的……{w=0.4}"

    stop music

    "病房里突然安静下来。"

    tomori concern "……{w=0.4}千早同学？"

    show anon hosp 03 curious_1
    anon "哈？{w=0.4}怎么了？"

    tomori calm "她好像和我刚才一样，走神了。"

    tomori concern "千早同学……{w=0.4}怎么会突然回东京了？"

    show anon hosp 04 shy_1 at anon_retreat
    anon "呃……{w=0.4}这个嘛……{w=0.4}"
    anon "就、就放假了回国看看嘛……{w=0.4}"
    anon "东京都内那么多好玩的地方，偶尔也想回来逛逛街嘛！"

    tomori calm "可是……{w=0.4}千早同学现在住在503病房。"

    show anon hosp 05 annoyed_1 at standee_jump
    anon "{cps=*1.6}哈……{w=0.2}那、那是意外！{/cps}{w=0.1}{nw}"
    show anon hosp 04 shy_2 at standee_shake_h
    anon "{cps=*1.5}突发情况懂不懂嘛……{/cps}"

    tomori ehh "……{w=0.4}意外？"

    show anon hosp 04 shy_2 at standee_nod
    anon "……{w=0.4}就、就是水土不服而已啦！"
    show anon hosp 07 normal_2 at anon_center
    anon "伦敦的天气天天都在下雨，到处都是灰蒙蒙的冷风，吃的东西又不适应，一下子受不了就病倒了。"
    show anon hosp 01 smug at standee_nod
    anon "这还是医生说需要回国静养一段时间，{w=0.4}我才回来的！"

    play music sunny loop

    tomori calm "……{w=0.4}下雨。"

    show anon hosp 03 curious_1
    anon "嗯？{w=0.4}怎么了？"

    tomori sadaway "下雨天……{w=0.4}确实很让人讨厌。{w=0.1}{nw}"
    extend bitter "衣服会湿透，鞋子里全都是泥水。{w=0.1}{nw}"
    extend uff "浑身冷冰冰的。"

    show anon hosp 02 boast at standee_shake_h
    anon "对吧？{w=0.4}你也这么觉得对吧！"
    anon "伦敦的雨下起来根本没完没了，连打伞都没用，风一吹伞全被掀翻了！"
    show anon hosp 06 pain
    anon "讨厌死了……{w=0.4}"

    tomori soft "……{w=0.4}嗯。"

    tomori calm "刚才那个没那么聒噪的她是不是我看走眼了？"

    play sound sfx_cutlery_clink
    "她用勺子把盒底最后一点布丁刮干净，心情似乎又好了一点。"
    "她{b}说话心虚时总爱把两只手合拢又分开{/b}，{w=0.2}捏着那柄小塑料勺转来转去。\n"
    extend "她装出漫不经心、高高在上的模样，然而这副模样只是面具而已，要掩盖的是想要摆脱长期心情紧张与孤立无援的强烈愿望。"

    tomori soft "当听到我顺着她的话说出“下雨天确实很让人讨厌”时，她抬起眼看我——这已全然不是刚进门时那张带着浮夸炫耀的脸，全然不是刚才那种防备的样子了。{w=0.1}{nw}"
    extend smile "她看过来时是柔和的，同时又是信任的、软和的、羞怯的。孩子们往往就是这样看着他们极其喜欢并对其有所求的人。"

    show anon hosp 08 gentle at anon_lean_in
    anon "不过话说回来……{w=0.4}高松同学你又是怎么进来的啊？"

    tomori concern "她一边在我的病床上东张西望，一边好奇地探着脑袋。{w=0.1}{nw}"
    extend uff "我的心揪紧了，余光瞥向枕头边那个摊开的黑色活页笔记本。{w=0.1}{nw}"
    extend babble "本子里密密麻麻写满了像咒语一样碎裂的词句，关于西瓜虫，关于一种别的孩子避之不及的动物，关于沉在水底发不出声音的石头，全都是我最见不得人的奇怪自言自语。"

    tomori pout "我祈祷她不会看到那些本子上奇怪的东西！……好吧，照她这种把别人的病房当成自家后花园、到处乱晃乱看的自来熟性格，她一定会看到的。{w=0.1}{nw}"
    extend babble "我还不如祈祷点别的。比如祈祷外面的大雨突然把整栋大楼冲走，或者祈祷天花板现在就掉下来把我砸晕过去。{w=0.1}{nw}"
    extend kya "晕过去就好了！眼前一黑，陷入彻底的昏迷，医生和护士就会惊慌失措地推着仪器冲进房间，把我的本子顺手放在桌子上。"

    play sound sfx_paper_crinkle volume 0.8
    tomori wtf "完了。她已经看到了。她一把拿过去，先是合上它，然后好奇地翻看封皮。"

    show anon hosp 03 curious_1
    anon "这是什么？"

    tomori concern "虽然说自己提起来未免尴尬，但是果然不想要被她注意到那个本子然后细细研读啊。所以，我其实已经没得选了。这种时候只能当机立断。"

    tomori calm "我……{w=0.4}{nw}"
    extend sadaway "从高处掉下来了。"

    "她的眼睛从本子挪回到我的身上。"
    stop music

    show anon hosp 07 normal_1
    anon "高处？{w=0.4}楼梯吗？"

    tomori calm "……{w=0.4}学校的天台。"

    play sound sfx_heartbeat
    show anon hosp 03 curious_1 at anon_lean_in, standee_shake_h
    anon "{size=*1.45}天、天台？！{/size}"

    "她愣在原地，手里紧紧攥着刚才合上的本子。"

    tomori calm "……{w=0.4}嗯。四楼。"

    show anon hosp 03 curious_2 at anon_lean_in, standee_shake_h
    anon "{size=*1.45}真的假的？！{/size}"

    tomori neutral "嗯……{w=0.4}真的。"

    show anon hosp 06 pain
    anon "这、这也太夸张了吧……{w=0.4}"
    anon "你是不小心踩空了吗……？{w=0.4}"

    tomori calm "……{w=0.4}不是。"

    show anon hosp 03 curious_3
    anon "那难道是……{w=0.4}"
    anon "……{w=0.4}你自己跳的？"

    tomori calm "……{w=0.4}嗯。"

    show anon hosp 06 pain
    anon "为什么啊……？！{w=0.4}"

    tomori calm "……{w=0.4}"

    show anon hosp 08 gentle
    anon "……{w=0.4}很疼吗？"

    tomori ehh "……{w=0.4}什么？"

    show anon hosp 06 pain
    anon "从四楼跳下来……{w=0.4}"
    anon "摔在塑料棚上的时候，{w=0.4}很疼吗？"

    tomori sad "{cps=20}……{w=0.4}其实，跳下去的时候不疼。{/cps}{w=0.1}{nw}"
    extend calm "风很大……{w=0.4}{nw}"
    extend uff "\n在医院醒过来的时候……浑身都很疼。"

    "千早爱音原本晃来晃去的动作彻底停住了。但很快，她用力拍了拍自己的脸颊。"

    play music anon fadein 1.5 loop
    show anon hosp 08 gentle at anon_center

    anon "那、那就说明你超走运的嘛……{w=0.4}"
    anon "四楼掉下来居然还能好端端地在这里跟我说话，{w=0.4}神明大人肯定在暗中保佑你呢！"
    show anon hosp 02 boast at standee_shake_h
    anon "俗话不是说嘛……{w=0.4}大难不死，必有后福！"
    anon "以后肯定会有超级棒的事情发生在你身上的……{w=0.4}"

    tomori ehh "……{w=0.4}那，千早同学什么时候带我去伦敦呢？{nw}"
    stop music

    show anon hosp 04 shy_1 at anon_center, standee_shake_h
    anon "咳！{w=0.2}咳咳咳……！{w=0.4}"

    tomori concern "……{w=0.4}千早同学？"

    show anon hosp 03 curious_1 at anon_center, standee_shake_h
    anon "哈？！{w=0.4}"
    show anon hosp 04 shy_2
    anon "伦、伦敦？！"
    anon "你……{w=0.4}你怎么突然问起这个啊！"

    tomori neutral "千早同学刚才说……{w=0.4}如果有机会的话，一定要去一次才可以。"
    tomori ehh "所以……{w=0.4}我想知道什么时候可以去。"

    show anon hosp 04 shy_1
    anon "这、这种事……{w=0.4}当然要等以后啦！"
    anon "去英国要办很多手续的！{w=0.4}护照啊，签证啊，机票也超级贵的！"
    show anon hosp 01 smug
    anon "至少……{w=0.4}至少也要等我们都高中毕业以后吧！"
    anon "不对！{w=0.4}要等本小姐什么时候有空了才行！"

    play music anon fadein 2.0 loop

    tomori calm "她一口气说了很长一串话，最后几个字时她自己也开始信不过了，声音渐隐。{w=0.1}{nw}"
    extend soft "我想，这只不过是她随口胡诌的一句场面话罢了。{w=0.1}{nw}"
    extend smile "可即便明知是假的，我还是顺着她的描述，在脑海里勾勒出了那个遥远的国度——仿佛那里真的每样东西都精致整洁，仿佛在美好的一天结束时真能听到红色的双层巴士驶过钟楼的歌声。\n仿佛那里真的存在着一个充满友善与浪漫的、连我也被允许踏足的世界。"

    tomori soft "……{w=0.4}好。{w=0.1}{nw}"
    extend smile "那我等千早同学有空……{w=0.4}"

    show anon hosp 04 shy_2 at standee_shake_h
    anon "喂……{w=0.4}你干嘛这么一本正经地说这种话啊！"
    anon "切……{w=0.4}真是个超级麻烦的家伙……！"

    tomori calm "……{w=0.4}"

    show anon hosp 03 curious_1
    anon "哇……！{w=0.4}你刚才是不是笑了？！"
    show anon hosp 01 smug
    anon "高松同学你绝对笑了对吧？{w=0.4}"

    tomori smile "……{w=0.4}没有笑。{w=0.1}{nw}"
    extend neutral "因为千早同学头上的呆毛……{w=0.4}一直在晃。"

    show anon hosp 03 curious_2 at anon_center, standee_shake_h
    anon "哈？！{w=0.4}呆、呆毛？！"
    show anon hosp 05 annoyed_1
    anon "这才不是呆毛！{w=0.4}这是今年最流行的空气感造型好不好！{w=0.4}刚从床上爬起来乱了一点而已！"

    tomori soft "她气鼓鼓地去按那撮头发，可是刚按下去，松开手，又倔强地弹了回来。"

    tomori smile "……{w=0.4}又弹起来了。"

    show anon hosp 04 shy_1 at standee_shake_h
    anon "哎呀……{w=0.4}不许看啦！快把头转过去！"

    "她伸出两只手，作势要来捂我的眼睛，走廊外传来推车声。"
    "503床的千早同学？千早同学人呢？又跑哪去了？"

    play sound sfx_footsteps
    show anon hosp 01 smug at anon_door
    anon "好啦好啦……{w=0.4}"
    show anon hosp 08 gentle
    anon "高松同学，我先撤了……{w=0.4}"
    anon "明天下午要是没被抓，我再来找你玩哦……{w=0.4}"
    anon "草莓布丁超好吃的，谢啦……{w=0.4}"

    tomori neutral "……{w=0.4}千早同学。"

    "她停在门边，回头对我眨了眨右眼，比了个剪刀手。"

    show anon hosp 01 smug
    anon "行啦……{w=0.4}都说了叫我爱音啦！"
    show anon hosp 08 gentle
    anon "明天见，{w=0.4}灯！"

    play sound sfx_door_close
    hide anon with dissolve

    tomori soft "门被迅速拉开，又轻轻关上。病房里重新只剩下我一个人。{w=0.1}{nw}"
    extend smile "她真是一个{b}{w=0.1}可爱的{/b}，{w=0.1}十足可爱的人。{w=0.1}{nw}"
    extend soft "可爱到，足以让我第一次没有满脑子想着“为什么我还没有死掉”。"

    tomori calm "什么时候带我去伦敦？是啊，什么时候呢。{w=0.1}{nw}"
    extend soft "连我自己都搞不清楚，那究竟只是为了配合她的随口附和，还是真的想去看看。{w=0.1}{nw}"
    extend babble "我甚至开始在脑海里默默编造着明天的对话。因为看来事情不仅必须跟我所期待的一致，而且还必须和她自己的兴致相吻合才行。要是她明天又偷跑过来，我该对她说些什么？"

    tomori sadaway "我意识到她并不了解我，并且将永远了解不了我。\n{w=0.2}她不知道我是多么浅薄、多么乏味，也不懂得我根本没有能力去绕那么多圈子把她留住，这一点我将永远也办不到。只有我心里是明白的。{w=0.1}{nw}"
    extend sad "{cps=*2}到了一定的时候，她就会像所有的人那样{b}离开{/b}。我们对彼此来说，大局已定。{/cps}"

    tomori uff "这种无望的想法已经超出了我所能承受的，而我却不能对此表示理解，更不能逆来顺受。{w=0.1}{nw}"
    extend babble "{cps=*3}万一她明天睡醒就忘了呢？\n万一她发现我其实沉闷又无趣，木头一桩、连一句讨人喜欢的话都挤不出来呢？{/cps}"

    tomori soft "我不是在说她麻烦！相反，说是期待还来不及呢。我在等待，等待明天到来，等待她再一次推开门，对我说：我不可能不来。{w=0.1}{nw}"
    extend sadaway "但我知道这不过是一种自我安慰的幻觉。不能这样。我必须避免这种情况。"

    play sound sfx_impact
    tomori bitter "{b}她不能走。我不能让她失望。她那么好。她在乎我，{w=0.4}哪怕是虚假的，也是在乎我！{/b}" with shake_h

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    camera at default
    scene black with slow_dissolve

    $ persistent.cleared_chapter_3 = True
    jump ch04_intrusion
