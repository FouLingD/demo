## ch02_silence.rpy - 第二章：无风的走廊与静止的尘埃
## 严格对标《规范文件.md》视觉素材规范与 11111.docx 对象修订终盘定稿
## 背景规范：hospital_bed_01_blue / corridor_01_blue
## 立绘规范：taki 01 glare / taki 02 normal_1 / soyo 01 smile / soyo 01 normal
## 主视角 Side Image 头像差分系统：频繁切换 + extend 句子内微表情拆分

label ch02_silence:
    $ current_chapter = 2
    $ quick_menu = True

    # 五楼单人病房，医院环境音与沉郁音乐（hospital_bed_01_blue）
    scene bg hospital_bed_01_blue with fade
    play bgs bgs_hospital fadein 2.0 loop
    play music bgm_relaxed fadein 2.5 loop

    tomori calm "从重症监护室转到单人病房，是在入院后的第三天。{w=0.1}{nw}"
    extend neutral "房间在五楼走廊最靠里的角落。"

    tomori calm "我躺在铁架床上，{w=0.1}{nw}"
    extend sadaway "心中对此却没有丝毫实感。我旁观着这一切。{w=0.1}{nw}"
    extend calm "好似这是别人的事情，好似在看着没有声音的电视画面。"

    nurse "高松同学，早餐放桌上了哦。"
    nurse "你看……{w=0.4}今天有热牛奶、白米粥和煮南瓜。"

    tomori calm "……{w=0.4}"

    nurse "昨天的南瓜汤，一口都没动呢。"
    tomori neutral "{cps=20}……{w=0.4}不饿。{/cps}"
    nurse "不饿也得吃一点啊。"

    tomori calm "这是不是前两天议论过我那个护士，我已经没印象了。{w=0.1}{nw}"
    extend babble "就像你刚睡醒，一定也会对刚发生的事情记忆不深刻吧？大梦初醒时总是缓不过来的，大脑还没反应过来要在这个世界做出什么反应呢。"

    tomori calm "周围的人都在劝我活下去，医生向我解释各种药物的作用，护士轻声哄我进食。"

    tomori calm "但是，他们根本就不明白。{w=0.1}{nw}"
    extend bitter "我并不是在同某个具体的人作对，我也不是在冲什么人发脾气，借此来缓和本来就不存在的女女情谊。"

    tomori sadaway "如果要发脾气，感到委屈了，我多可以有其他方式来排解。{w=0.1}{nw}"
    extend bitter "比如摔碎什么东西，{w=0.1}{nw}"
    extend sad "或者大哭一场。"

    tomori uff "灯管亮得晃眼，把我弄得昏昏沉沉的。{w=0.1}{nw}"
    extend sadaway "那些委屈现在只是别人的，而我只想在这张病床上耗尽最后一点力气，和接下来可能的一切说一声无声的再也不见。"

    tomori calm "有时候我长时间发空。我没有身份。{w=0.1}{nw}"
    extend soft "一开始会让人感到害怕。后来会变成一种幸福。仿佛我说话的时候我已经不在了。"

    nurse "医生说你今天的血糖指标又降了，胃一直空着会出问题的。"
    nurse "哪怕……{w=0.4}喝两口牛奶呢？"

    tomori sadaway "{cps=20}……{w=0.4}放着吧。{/cps}"
    nurse "呃……{w=0.4}为什么？"
    tomori concern "呃……{w=0.4}没什么。"
    nurse "医生说了，下午要是再不吃，就只能给你下鼻饲管了。"

    tomori uff "那个……{w=0.1}{nw}"
    extend sad "会很疼吗？"

    nurse "会有点难受。{w=0.5}所以，尽量自己吃两口吧。"

    # 走廊公共休息区（corridor_01_blue）
    scene bg corridor_01_blue with dissolve
    play sound sfx_footsteps

    tomori neutral "待她走后，我又把那碗早饭往窗边推了推。{w=0.1}{nw}"
    play ambient_sfx sfx_trolley_wheels volume 0.65
    extend calm "走廊里传来推车的轮子声。"

    tomori calm "我从床上坐起来，踩着塑料拖鞋，慢慢走到门外。{w=0.1}{nw}"
    extend neutral "走廊昏暗，阳光似乎怎么也照不进来，外人看来或许很难分辨这里是否禁止通行的地方。"

    tomori calm "没有风的走廊。没有钟表的走廊。没有人试图离开的走廊。{w=0.1}{nw}"
    extend sadaway "走廊尽头有一处小小的休息区。蓝色的塑料排椅摆放歪斜，电视了无生气挂在墙上。"

    tomori calm "电视里正重播上午的节目，我没有心情去分辨是悲剧还是喜剧。演员声音洪亮，妆容夸张，台词迅速，文字觉察到自身无聊而匆忙离场。"

    tomori neutral "有两个人坐在排椅上看电视。他们谁也不说话，只是盯着上面的笑话。"

    # 批注效果：“笑话”融化演变，流速逐步放缓，强制等待后直接 extend
    "{alpha=1.0}{cps=28}老套的笑话。不好笑的笑话。属于过去时代的笑话。令人感到困倦的笑话。二手的笑话。一个又一个笑话。{/cps}{/alpha}{w=0.6}{nw}"
    extend "\n{alpha=0.82}{cps=20}像灰尘一样从屏幕里掉出来、落在肩上、鞋上、随便哪里的笑话。为了掩盖沉默而制造出来，却让沉默更加沉默的笑话。{/cps}{/alpha}{w=0.9}{nw}"
    "{alpha=0.62}{cps=13}关于健康人的笑话。关于明天还会到来的笑话。关于这个世界依然完好无损的笑话。{/cps}{/alpha}{w=1.2}{nw}"
    extend "\n{alpha=0.40}{cps=7}没有人在笑的笑话。连笑话自己都忘记了为什么要发笑的笑话。{/cps}{/alpha}"

    grandpa "小姑娘，今天降温了啊。" with shake_h
    tomori neutral "……{w=0.4}嗯。"
    grandpa "这里的暖气总是不太热。习惯了就好。"
    tomori soft "……{w=0.4}好。"

    tomori calm "对话就这么简短地结束了。{w=0.1}{nw}"
    extend sadaway "节目依旧播放，剧情是女主角在面包店里打翻了面粉袋，所有人都在手忙脚乱地大笑。笑声回荡。"

    tomori calm "没有其他事情可做，也没有其他地方可去。{w=0.1}{nw}"
    extend sadaway "大家都在等时间它自己向前去，把未来全权交给它管控。{w=0.1}{nw}"
    extend calm "人的生病与住院，原来是这么平淡无奇的事情。"

    tomori bitter "电视机还在亮着。那两个人还在坐着。{w=0.1}{nw}"
    extend sadaway "看着他们看电视，我感觉自己也正在变成第三个笑话。"

    # 下午三点探视时间铃声，回到单人病房（hospital_bed_01_blue）
    play sound sfx_bell
    scene bg hospital_bed_01_blue with dissolve

    tomori calm "就这样，时间来到了三点，探视的铃声响了。{w=0.1}{nw}"
    extend neutral "我慢慢走回自己的病房，重新在铁架床上躺下。"

    tomori ehh "或许真的会有人前来探访我吧！{w=0.1}{nw}"
    extend yay "我想象着。就像是……下午放学的铃声刚刚打响，少女们把书包甩在肩头，没来得及整理衣服的褶皱，一路小跑。{w=0.1}{nw}"
    extend kya "{cps=*1.5}{b}两个人，三个人，或者更多人。{/b}{/cps}"

    "{cps=*2}推开鞋柜，换上外出的鞋子。——穿过开满八重樱的坡道，穿过电车道口的红色警示杆，穿过放学路上喧闹的人潮。{/cps}{nw}"
    "{cps=*2.5}怀里紧紧抱着从街角花店买来的花束，塑料包装纸在风里哗啦啦地响。{/cps}{nw}"
    "{cps=*3}气喘吁吁地冲进医院大厅，撞开电梯门，一路数着门牌号找过来。{/cps}{nw}"
    "{b}“灯！我们来看你了！”{/b}" with shake_h

    tomori yay "有人可能会忍不住当场哭出来，{w=0.1}{nw}"
    extend ehh "有人可能会数落我、气急败坏，{w=0.1}{nw}"
    extend kya "有人可能会笨手笨脚地把花瓶打翻。"

    tomori wtf "那种跌跌撞撞、热气腾腾的画面……{w=0.1}{nw}"
    extend ehh "哇。{w=0.1}{nw}"
    extend yay "会有的吧？"

    tomori sadaway "不会有的吧。" with shake_h

    tomori pout "光是脑子里冒出这种想法，我都觉得自己的脸颊在微微发烫。{w=0.1}{nw}"
    extend bitter "{b}我，{/b}{w=0.1}怎么能配得上这种级别的待遇？我以为我是谁呢？我以为我是她们的谁呢？"

    tomori sadaway "我是一个有病的人……{w=0.1}{nw}"
    extend bitter "我是一个心怀歹毒的人。{w=0.1}{nw}"
    extend babble "{cps=*1.5}我想我的肝脏有病。我想我应该落下了什么后遗症。{/cps}{w=0.1}{nw}"
    extend sadaway "但是我对自己的病一窍不通，甚至不清楚我到底患有什么病。"

    tomori calm "我不去看病，也从来没有看过病，虽然我很尊重医学和医生，但这不能让我成为一个健康的人。{w=0.1}{nw}"
    extend sadaway "既然自己已经认清了认定了这些事情，那就没有必要去确诊。确诊只是庸人自扰的手段。如果某样事物没有名称，它就从亟待确认的状态变成了黑箱中的猫。人们会更快地忘记它，它就真的不存在，也不会再有什么影响，然后就可以以假乱真，成为一个正常的健康的人了吧。"

    tomori calm "纵使有无数种维持生命的装置，药物也好，机器也好，它们可以修补坏掉的地方。{w=0.1}{nw}"
    extend sad "但如果一个人失去了希望，就如何、如何都修理不好了。"

    tomori soft "好在她们不一样。{w=0.1}{nw}"
    extend smile "她们还拥有完整的名字、完整的明天，以及变得更好的可能性。"

    tomori soft "所以，无论她们是不是会来，她们都是出自好心，没有人是坏人。{w=0.1}{nw}"
    extend calm "她们或许只是想更加健康，去呼吸更好的空气，去晒更明亮的太阳。"

    tomori calm "坏人是不存在的。于是乎，所谓人为的痛苦也是不存在的。想到这里，我的身体微微发暖——{w=0.1}{nw}"
    extend soft "我为她们的善良感到格外幸福。{w=0.1}{nw}"
    extend smile "我对这个世界的好意感到格外幸福。"

    tomori calm "{b}疼痛，那就让它疼好了。{/b}{w=0.1}{nw}"
    extend sadaway "我很早以前就这样生活了，十多年，马上二十年了。或许时间短点，总之这是我出生之后就在进行的事情。"

    # Crychic 队友探视：立希、爽世、睦登场（规范立绘：taki 02 normal_1 / soyo 01 smile）
    play sound sfx_door_slide
    play music bgm_daily fadein 2.0 loop

    show taki 02 normal_1 at left_standee
    show soyo 01 smile at right_standee
    with dissolve

    taki "……{w=0.4}灯。"

    tomori ah "啊！{w=0.1}{nw}"
    extend calm "她们来了。我才注意到走廊的声儿。似乎方才就有了，只是我没注意。"

    soyo "打扰了……{w=0.4}"
    tomori smile "没事。{w=0.4}正好我也没干什么。"

    taki "……{w=0.4}这房间还挺大。"
    taki "切……{w=0.4}五楼只有这一间是单人的吧？"
    tomori neutral "那个……{w=0.4}不知道。"

    soyo "那个……{w=0.4}我们在楼下问了护士台，{w=0.3}护士说在最里面这间。"
    soyo "电梯今天好像在检修，{w=0.3}我们走楼梯上来的。"
    soyo "有点热呢，{w=0.3}外面的风停了。"

    tomori neutral "雨已经停了吗？"
    taki "哈？{w=0.4}今天早上就停了，{w=0.4}你该不会刚醒没多久吧？"

    tomori calm "换做平常，我早就会说，我已经醒了很长时间了。或者，我才不会睡那么长时间。{w=0.1}{nw}"
    extend sadaway "但是即使是解释的话，也不可能会冰释前嫌对吗？所以，还不如节省点力气，在床上多蜷缩一会。"

    soyo "灯不想说话，{w=0.4}让她安静一会吧。"
    "爽世在一旁帮腔。她注意到了只能打开一个窄缝的窗户。"

    soyo "哎呀……{w=0.4}这窗户怎么只开这么一点？{w=0.4}房间里有点闷呢。"
    taki "切……{w=0.4}医院为了安全吧。"
    taki "高层病房都这样。"

    "素世把抱在怀里的花拿在手上，向前伸出。"
    soyo "那个……{w=0.4}花店的阿姨说百合花开得最久了。"
    "她的头偏向立希那儿去。"
    soyo "其实……{w=0.4}本来立希想买向日葵的。"
    soyo "不过……{w=0.4}这个季节的向日葵不太新鲜，{w=0.3}叶子都发黑了。"
    taki "嘛……{w=0.4}向日葵颜色亮一点。"
    soyo "不过……{w=0.4}病房里放太刺眼的颜色不太好吧？"
    soyo "白色的比较柔和，让人心情平静。"
    soyo "对吧，灯？"

    tomori calm "……{w=0.4}嗯。"

    tomori calm "白色的花。白色的墙壁。白色的床单。{w=0.1}{nw}"
    extend sadaway "所有的白色重叠在一起，让人分不清界限。{w=0.1}{nw}"
    extend calm "她们不再争论花的颜色了。也许是因为累了，也许是因为她们突然意识到，无论放什么花，这个房间都不会有任何改变。"

    "素世把花给安放到床头的花瓶里。这时，立希把一直拿在手上的袋子抬了起来。"
    taki "顺路在车站前面的便利店买的。"
    taki "两个装的草莓布丁。"
    taki "我说……{w=0.4}我记得你以前排练完了喜欢吃这个。"

    tomori smile "谢谢。"
    taki "喂……{w=0.4}今天吃了没？"
    tomori concern "呃……{w=0.4}吃过了。"

    tomori calm "她眼睛往旁边一瞥。我循着她的目光看去——啊，她发现了床头柜上那碟纹丝未动的南瓜粥托盘。"
    taki "真吃了？{w=0.4}"
    tomori sadaway "只……{w=0.4}喝了水。"

    "她瞪了我一眼。"
    tomori pout "你不知道，现在就算是喝水也要不少废我力气呢！"

    taki "行吧……{w=0.4}那就等会儿饿了再吃。"
    soyo "学校那边的事，{w=0.3}灯完全不用担心哦。"
    "爽世依旧是令人感到安心。"
    soyo "今天早上我和立希去羽丘交了请假申请单……{w=0.4}"

    tomori concern "那个……{w=0.4}不用麻烦爽世特地跑过来的。"
    soyo "哎呀……{w=0.4}说什么傻话呢，怎么会是麻烦？"
    soyo "我们大家……{w=0.5}都很挂念你啊。"

    tomori soft "说到这句话时，她的眼睫毛微微颤着，那是被上下摆动的眼皮带动的。她笑着，眼中透露出关怀和浅浅的忧虑。"

    taki "……{w=0.4}对了。"
    taki "月之森那边的乐器室，借用期延后了。"
    extend "老板说可以保留到下个月。"
    soyo "对呀……{w=0.4}所以灯酱只要安心养病就好了。"
    extend "等身体养好了，出院了，我们再去合练。"

    tomori ah "……{w=0.4}新曲子？"

    "见我有兴趣追问下去，素世的眼睛睁大了点，她直了直身子。"
    soyo "就是之前祥子写的那首啊……{w=0.4}"
    soyo "祥子今天虽然没来……{w=0.4}但她也是因为家里有事脱不开身。"
    soyo "她心里……{w=0.4}一定也一直在为你加油的。"

    tomori sadaway "我这才注意到祥子没有来。{w=0.1}{nw}"
    extend calm "午后的时间停滞不前。有些事情正在发生。它漫长、无法挽回。谁也没有说破。"
    stop music

    # 【双人争吵镜头流转系统】
    # 使用标准立绘：taki 01 glare / soyo 01 normal（素世撕下温柔假面）
    show taki 01 glare at focus_standee_left(0.8)
    show soyo 01 normal at unfocus_standee_right(0.8)
    with dissolve

    tomori concern "她的眉头紧锁，鼓起来的嘴唇是隐瞒不了她现在的心情的。"
    taki "……{w=0.4}爽世，别说了。"

    # 视线移向爽世（爽世进中景亮起，立希退避暗淡）
    show soyo 01 normal at focus_standee_right
    show taki 01 glare at unfocus_standee_left
    soyo "……{w=0.4}怎么了？我只是想让灯放宽心……{w=0.4}"

    # 视线移回立希
    show taki 01 glare at focus_standee_left
    show soyo 01 normal at unfocus_standee_right
    taki "祥子根本不会来了……{w=0.4}你心里很清楚吧。"
    taki "别再提什么新曲子了……{w=0.4}"

    # 视线移向爽世反问
    show soyo 01 normal at focus_standee_right
    show taki 01 glare at unfocus_standee_left
    tomori calm "素世的眉毛微微皱起来了。不过，是她的话，没那么容易被彻底激怒吧。凭我的了解是如此。"
    soyo "立希……{w=0.4}你非要在这种时候说这些吗？"
    soyo "这里是病房，灯才刚醒过来！"

    tomori concern "有点出乎意料。听起来像是某种不痛不痒的责备。她的眼睛想要告诉立希一些什么，但是立希压根不想往她那儿看。立希好像没听到那样，继续说了下去。"

    # 立希迫近病床质问灯
    show taki 01 glare at standee_left_press
    taki "……{w=0.4}灯。"
    taki "我就问一句话……{w=0.4}"
    taki "那天在天台上……{w=0.4}到底是为什么？" with shake_h
    tomori an2 "……{w=0.4}"

    # 爽世厉声喝止
    show soyo 01 normal at standee_right_burst with shake_h
    soyo "{size=*1.2}椎名立希！{/size}" with shake_h
    soyo "医生说了绝对不能刺激病人！"
    stop sound

    # 两人情绪平复回落，立希拿出歌词本
    show taki 02 normal_1 at focus_standee_left
    show soyo 01 normal at unfocus_standee_right
    taki "……{w=0.4}给。"

    tomori ah "……！{w=0.4}"
    tomori ehh "这、这个是……{w=0.4}"

    show soyo 01 normal at focus_standee_right
    show taki 02 normal_1 at unfocus_standee_left
    soyo "哈？！{w=0.4}立希？！你把那个本子拿来干什么？！"

    show taki 01 glare at focus_standee_left
    show soyo 01 normal at unfocus_standee_right
    taki "闭嘴，爽世！{w=0.4}这是灯自己的东西！"
    taki "……{w=0.4}不管你还唱不唱歌，也不管乐队以后怎么样。"
    taki "你写下来的东西，不准随随便便丢在那种地方让人踩。"
    taki "听见没有……{w=0.4}灯？"

    tomori soft "……{w=0.4}嗯。{w=0.1}{nw}"
    extend smile "谢谢你，立希。"

    play music memory fadein 2.0 loop

    tomori calm "房间里又安静下来了。急促的声音传进我的耳朵里，却全都被蒙上了一层棉花。{w=0.1}{nw}"
    extend sadaway "像是在水底听岸上的人说话。我可以使用这个比喻吗？虽然我很少游泳……{w=0.1}{nw}"
    extend soft "她们的难过是真的，眼泪是真的，手心里的汗水也是真的。至少，我不能妄下论断说她们此刻流露出来的感情是虚假的。"

    tomori calm "没有必要总是这样揣测人吧，这个世界上有三个人正为了我而痛苦着。这听起来其实挺暖和的。{w=0.1}{nw}"
    extend babble "虽然最近总是很少出太阳，可是怪就怪在，没有人能记录太阳本身的出勤率吧？{w=0.1}{nw}"
    extend sadaway "进一步想，如果完全没有人管着我的话，我或许也不知道会跑到那里去躲上一天了。{w=0.1}{nw}"
    extend calm "而且，虽然人们会抱怨”今天没有出太阳“，可是实际上，它就在那里，不增不减地散播着热量……"

    play sound sfx_piano_sting
    tomori soft "{b}当我们把地球仪转一圈就会发现，{w=0.4}其实只是我们自己躲到黑暗里面了！{w=0.4}这明明都是我们的选择。{/b}" with shake_h
    extend smile "\n{b}而我们就这样抱怨着太阳……{w=0.4}用责怪的语气表示着在意，这是一件多么幸福的事情啊！{/b}"

    # 睦走上前
    hide taki
    hide soyo
    with dissolve
    mutsumi "……{w=0.4}灯。"
    tomori neutral "……{w=0.4}睦？"
    mutsumi "……{w=0.4}对不起。"

    voice "audio/voice/vo_tomori_02_01.ogg"
    tomori sadaway "那个……{w=0.4}睦不用道歉的。{w=0.1}{nw}"
    extend calm "跳下去是我自己的决定。"

    play sound sfx_bell
    nurse "探视时间已经过了哦。"
    nurse "病人需要休息了，{w=0.4}同学们请先离开吧。"

    "爽世如释重负般松了口气，转过头看着我，挤出一个微笑。立希也从床边撤了半步，伸手要干什么。"
    show soyo 01 smile at right_standee
    show taki 02 normal_1 at left_standee
    with dissolve

    soyo "灯，那我们先回去了。"
    soyo "明天……{w=0.4}或者后天，等你有精神了，我们再来看你。"
    soyo "布丁记得吃哦……{w=0.4}"
    taki "……{w=0.4}走了。"

    "一直在一旁没开口的睦终于出声了。"
    mutsumi "……{w=0.4}再见。"

    tomori calm "她那张脸还是像镜湖一样，什么波动也没有。我想她还是有什么想说的吧，我知道她只是不善言辞。"
    tomori neutral "……{w=0.4}再见。"

    tomori soft "和她讲话反倒是最轻松的呢。{w=0.1}{nw}"
    extend calm "像机器收到指令一样，按照约定俗成的公式，输出声音就好。"

    # 探视结束，恢复冷清
    play sound sfx_door_close
    hide soyo
    hide taki
    with dissolve

    tomori calm "又只剩下我一个人了。我开始回想刚才的对话。{w=0.1}{nw}"
    extend neutral "向日葵、百合花、漫长的雨季。"

    tomori calm "大家都在很努力地找着无关痛痒的话题。{w=0.1}{nw}"
    extend sadaway "就像是在车站等车时偶遇同班同学，不得不硬凑出几句话来填补空白。{w=0.1}{nw}"
    extend calm "今天怎么样呢？昨天休息如何？"

    tomori calm "然而，我并没有感到被安慰。就像任何人都不会对公交车站的公式对话产生感动。{w=0.1}{nw}"
    extend sadaway "她们送来鲜花，送来水果，说着那些没什么意思的安慰话语。{w=0.1}{nw}"
    extend bitter "但我能从他们的眼睛里看到隐藏在关怀背后的恐慌与优越感。{w=0.1}{nw}"
    extend sadaway "这样说或许有点阴暗，但我总感觉，这就是我无法证明的事实，所以请允许我这样说。{w=0.1}{nw}"
    extend bitter "比起怜悯，她们在庆幸倒霉的不是自己。她们庆幸跳下去的不是自己。"

    tomori calm "“真可怜啊！”{w=0.1}{nw}"
    extend neutral "“为什么不早点和我们说呢？”{w=0.1}{nw}"
    extend bitter "同时又在为自己表现出的善良而得意。"

    tomori calm "这不怪她们。我没有任何责怪她们的意思。{w=0.1}{nw}"
    extend soft "想明白这一点后，我重新闭上眼睛。"

    stop music

    # 护士站谈论503病房千早爱音（corridor_01_blue）
    scene bg corridor_01_blue with dissolve

    nurse "我说医生啊……{w=0.4}隔壁503床的千早同学刚才又在护士站问东问西了。"
    extend "她一直在打听自动贩卖机什么时候会补货草莓牛奶。"

    tomori calm "啊，是那个女生。我之前还听说过她几次，但是具体印象什么的，倒是一点没有。{w=0.1}{nw}"
    extend neutral "我想，或许我之前见过她？"

    nurse "哈……{w=0.4}明明是在医院，却表现得像是在度假一样。"
    nurse "你看……{w=0.4}刚才还缠着实习医生问顶楼的天台能不能上去晒太阳呢。"
    nurse "说是病房里的光线太暗了，拍出来的照片不好看。"
    play music bgm_anon_playful loop

    # 【A 演出（升级版）：逆向《Oblivion 2666》Ch1 结尾 —— 无粉底、摄影漏光光晕 + 两处胶片损坏 + 局部粉字】
    window hide
    scene ed_hospital_right at gateweave(24, 0.5, 0.5) with ed_fade
    show ed_ob_filmdamage at ed_ob_damage_ambient
    show ed_ob_lightleak at ed_ob_flare_ambient

    ed_a_paper "这算是什么借口呢？\n啊，算了，管他呢。\n人总归是有各种各样奇怪的理由去做荒唐的事吧。"
    ed_a_paper "就像我为了不再弄脏大家而跳下天台一样，对别人来说肯定也是完全无法理解的怪事。\n这么一想，为了自拍好看想去天台晒太阳，反而显得挺{color=#FF8EB3}健康{/color}的？"

    ed_a_paper "我开始嫉妒这种{color=#FF8EB3}健康{/color}了，她的发色是{color=#FF8EB3}粉色{/color}，我的{color=#FF8EB3}草莓布丁{/color}也是{color=#FF8EB3}粉色{/color}。我可不会对还没会过的人的头发产生食欲！\n呃……我需要说清这一点。"

    ed_a_paper "如此，我爱上一个颜色——就眼前的状况来说，{color=#FF8EB3}粉色{/color}——好似中了魔咒。\n诚然，但那又如何？"
    ed_a_paper "也许你会说，这是一种自愿的错觉。\n你会说，每个{color=#FF8EB3}粉色{/color}的物体都可能是一丛准备开放的蔷薇，一段只有间谍能够破译的密码，一个地图上的X。"

    play sound sfx_marbles volume 0.8
    ed_a_paper "只是这幅地图太芜蔓，像我小时候趴在地板上拨弄的玻璃弹珠，一旦从盒子里撒出来，就各自滚进了再也找不到的墙角。"

    # 胶片损坏爆发 ①：极速快门负片反色闪光（0.30s）+ 强摄影漏光光晕过曝
    play sound sfx_impact
    $ photosnap(duration=0.30)
    show ed_ob_lightleak at ed_ob_flare_burst
    ed_a_paper "{b}我会努力给你解释。{w=0.4}假如有一个巨大的{color=#FF8EB3}草莓布丁{/color}在满医院寻找角度拍照，{w=0.4}换成谁都会觉得有意思吧！{/b}" with shake_h

    # 胶片损坏爆发 ②：极速冷青负片闪切（0.22s）→ 16mm 受损胶片卷缩进 + 摄影光晕快褪
    $ photosnap_cyan(duration=0.22)
    hide ed_ob_filmdamage
    scene ed_black_ink
    show ed_ob_filmroll_frame at ed_ob_filmroll_zoom
    show ed_ob_lightleak at ed_ob_flare_burst
    ed_a_paper "{color=#FF8EB3}草莓布丁……{/color}\n我承认，也许是我太孤单。\n可是这不能成为我的借口，即使这孤单会带来烧灼般的痛。"
    ed_a_paper "如果足够热，足够漫长，这痛便会开始模拟或者激发——\n——随你喜欢哪个词——对奇迹的领悟。"

    hide ed_ob_lightleak
    hide ed_ob_filmroll_frame
    window auto

    # 【VN 结束】：切回现实走廊与 ADV 对白
    scene bg corridor_01_blue with dissolve

    doctor "哈……{w=0.4}那孩子啊，看着挺开朗的。"
    doctor "高松同学，{w=0.4}你也许多向同龄人学学。"
    extend "隔壁的千早同学年纪和你差不多大。"
    doctor "等过两天身体恢复差不多了，你可以去走廊或者活动室坐坐，多和大家聊聊天。"

    tomori neutral "……{w=0.4}嗯。"

    # 【尾声演出】：医生护士离场，病房归于静谧，心尖浮现爱音名字的悸动
    play sound sfx_footsteps
    with dissolve
    play sound sfx_door_close
    "医生带着护士离开了。{w=0.4}\n门轻轻合上。"

    scene bg hospital_bed_01_blue with dissolve
    stop music fadeout 2.0

    tomori calm "千早爱音。{w=0.1}{nw}"
    extend soft "我在心里默默念着这个名字。"

    # 触动与温柔心境音乐缓缓流淌
    play music touched fadein 2.5 loop
    play sound sfx_wind_chime
    tomori soft "{cps=14}{color=#f49dae}千。{w=0.4}早。{w=0.4}爱。{w=0.4}音。{/color}{/cps}"

    tomori soft "像是一串挂在走廊窗户边上的彩色风铃。{w=0.1}{nw}"
    extend happy "粉色的头发，闪闪发亮的水晶，草莓牛奶，天台的自拍。"

    tomori ehh "在这个充满消毒水和病号服的五楼，{w=0.1}{nw}"
    extend yay "怎么会有人像是在度假一样生活呢？"

    tomori smile "真厉害呀。我不由得要对这个还没有见过面的人产生尊敬了……{w=0.1}{nw}"
    extend pout "哦，应该也用不上这么重的词！应该是，好感。"

    tomori concern "……可我这样的人，也会对别人产生好感吗？{w=0.1}{nw}"
    extend sadaway "明明连面对别人的力气都没有了，明明刚刚还在觉得自己已经不在了，{w=0.1}{nw}"
    extend pout "现在却躺在这里，擅自对一个连脸都没见过的女孩产生了好感。"

    tomori bitter "真是自相矛盾。脸皮也够厚的。{w=0.1}{nw}"
    extend sadaway "如果她推开门看见我，大概只会觉得我是这间病房件不太好看的家具吧。"

    tomori calm "一厢情愿的、不会打扰到任何人的好感。这样就很好。{w=0.1}{nw}"
    extend soft "这样就足够了。事到如今我不想再奢求什么我不应该得到的东西，如果一出戏剧注定要有一个由我见证的收场的话。"

    tomori soft "我闭上眼睛，粉色的名字留在舌尖上，吐不出来，也咽不下心去，像这样停留着就好了。{w=0.1}{nw}"
    extend calm "我这么想着，不知何时沉沉地睡了过去。"

    # 章节结束过渡
    stop music fadeout 3.0
    stop bgs fadeout 2.5
    scene black with slow_dissolve

    $ persistent.cleared_chapter_2 = True
    jump ch03_encounter
