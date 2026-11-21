## ch06_verdict.rpy - 第六章：体检日病房与七天宣判
## 严格对标《规范文件.md》视觉素材规范与 11111.docx 对象修订终盘定稿
## 背景规范：hospital_bed_02_blue / hospital_bed_01_blue / hospital_bed_02_orange
## 立绘规范：anon hosp 01~10 规范病房立绘
## 演出规范：纯旁白（无头像无立绘 / 无头像仅对方立绘）与主视角 Side Image 差分 + 换行 extend / {nw} 组合

label ch06_verdict:
    $ current_chapter = 6
    $ quick_menu = True

    # 1. 四点四十阴天病房：被摇醒与细碎无助的对话（海明威式留白）
    scene black
    play bgs bgs_hospital fadein 1.5 loop
    play sound sfx_clothes_rustle

    # 【纯旁白：全黑无头像无立绘】
    "有人把手按在我的肩膀上，{w=0.3}隔着被单轻轻晃了晃。"
    anon "高松同学。{w=0.3}醒醒。"

    "我迷迷糊糊地晃了下脑袋，{w=0.3}把脸在臂弯里埋得更深了。"
    tomori an2 "……不干。{w=0.3}我哪儿也不去。"

    anon "别犯傻了，不是护士。{w=0.3}醒醒吧，小灯。"

    scene bg hospital_bed_02_blue with dissolve
    camera:
        blur 10.0
        warp ease_out_cubic 1.6 blur 0.0
    play music work fadein 2.0 loop

    # 【纯旁白：无头像，渐渐看清阴天病房】
    "我迟钝地眨了眨眼皮。{w=0.2}病房里没有开灯，下午四点过后的阴天光线灰蒙蒙地压在床尾。{w=0.2}{nw}"
    extend "\n我又拉起被单蒙住半张脸。"

    show anon hosp 07 normal_2 at center_standee with dissolve
    tomori an2 "……几点了？"
    anon "四点四十。"

    tomori calm "……天怎么这么暗。"
    show anon hosp 07 normal_3 at anon_wander
    anon "外面起云了。{w=0.3}{nw}"
    show anon hosp 07 normal_2 at center_standee
    extend "\n刚才你睡得很沉，我叫了你三声。"

    tomori sadaway "我喜欢蒙着被单说话。{w=0.2}{nw}"
    extend calm "在被单底下比较暖和。"

    # 【无头像，仅展示对方立绘动作】
    play sound sfx_glass_clink
    show anon hosp 08 gentle at anon_table
    "爱音站在我的铁床边，没有坐下。{w=0.2}她把床头柜上那杯凉掉的温水往我手边推了推。"

    anon "你要不要喝口水？"
    tomori calm "不渴。"
    show anon hosp 07 normal_2 at anon_table
    anon "你还是喝一点吧。{w=0.3}{nw}"
    extend "说不定会使你好过些。"

    play sound sfx_clothes_rustle
    show anon hosp 06 pain at standee_tremble
    "我撑起一点身子，没有碰杯子，{w=0.2}却看见她垂在身侧的右手正紧紧攥着衣角。"
    tomori concern "你的手怎么这么抖？"

    show anon hosp 06 pain at anon_retreat
    anon "走廊里开着窗，有点冷。"

    tomori calm "……你去过诊室了？"
    show anon hosp 07 normal_3 at anon_retreat
    "爱音看着地板，没有看我的眼睛。"

    show anon hosp 06 pain at standee_nod
    anon "去了。"
    tomori calm "门开着吗？"
    show anon hosp 07 normal_2 at anon_retreat
    anon "半掩着。{w=0.3}{nw}"
    extend "\n那个戴眼镜的主治医生在里面打电话，没注意门口。"
    tomori concern "……他在给谁打电话？"
    show anon hosp 06 pain at anon_retreat
    anon "你妈妈。"

    play sound sfx_clothes_rustle
    "我的手指在被单底下蜷缩了一下。"
    tomori concern "……那张评估单呢？"
    show anon hosp 07 normal_2 at center_standee
    anon "就压在诊室门口的分诊台角上。{w=0.3}{nw}"
    extend "\n我顺手抽出来，揣进兜里就跑回来了。"
    tomori calm "那上面……怎么写的？"

    show anon hosp 06 pain at standee_tremble
    "爱音低着头看着地板，嘴唇动了动，把话头顿住了。"
    anon "你并非真要——{w=0.1}{nw}"
    "她突然停住不说。我也看着地板。"

    tomori concern "是我……{w=0.2}明天一早就得跟家里人走吗？"
    show anon hosp 06 pain at standee_shake_h
    anon "不是出院的事情。"
    tomori smile "那是骨头还没有长好？"

    show anon hosp 06 pain at standee_tremble
    "爱音摇了摇头。她的声音又细又轻，像是一碰就会断掉。"
    anon "骨头长好了。"
    tomori ehh "……那是什么？"

    play sound sfx_heartbeat
    camera at camera_heartbeat
    show anon hosp 10 tears at standee_step_in
    anon "我刚才在门缝外听见医生在电话里跟你妈妈讲……{w=0.3}{nw}"
    extend "\n说你从四楼掉下来的时候，主动脉和心壁受了暗伤。"
    tomori ah "……暗伤？"
    show anon hosp 06 pain at standee_tremble
    anon "嗯。他说现在的平稳，只是靠每天点滴里的药物硬撑出来的。{w=0.3}{nw}"
    extend "\n使什么招儿也不管用了。"
    tomori concern "……还能撑多久？"
    show anon hosp 10 tears at standee_tremble
    anon "最多只能再维持一百六十八个小时。"

    tomori ah "……"

    play music bgm_back_to_start fadein 1.0 loop
    play sound sfx_strike
    show anon hosp 10 tears at standee_shake_h
    anon "高松灯……{w=0.2}{nw}"
    extend "你只剩下最后七天了。"

    # 2. 七天死刑宣判，认知崩塌与解离（冷青 X 光负片 0.26s 闪断 → 摄影漏光过载 → 黑屏）
    play sound sfx_strike
    $ photosnap_cyan(duration=0.26)
    hide anon
    scene bg black
    show ed_ob_lightleak at ed_ob_flare_flash
    play bgs bgs_white_noise fadein 1.0 loop
    nvl clear

    vn_white "最晚七天以后，除非出了意外。{w=0.3}\n那么说，没有任何希望了。毫无希望。"
    vn_white "是时候做点什么了。不能一边待着什么也不做。或许可以写点什么。"
    vn_white "沉默，之后。怎么做才能再多活一会儿，再活久一点。{w=0.2}就这样。"
    vn_white "现在我不再是我了。而是某个我不再认识的人。在我自己身上，突然出现了另一个人，她有我的面目，我的外观，但不是我。恰恰是这绝不能由他人替换的正身消失不见了。"
    vn_white "沉默，之后。你现在可以敞开心扉了。或许是我。为了让生活更甜美？"
    vn_white "谁也不知道。应该努力活着。不能投入死神的怀抱。就这样。这就是我要说的全部。"
    nvl clear

    vn_white "病房里即将吞没我的一切全都一动不动。"
    vn_white "爱音垂在身侧的手臂停滞在一个没有完成的姿势上。窗台上百合花在地板上的影子也固定不动。风像立正似的停住。"
    vn_white "我试图喊叫，发出声音，扭动一下手指，却明白自己动弹不得。我听不到这个受遏制的世界的最轻微的声息。我想：我在地狱里。"
    vn_white "我疯了。时间已经停滞。果真如此的话，那么我的思维也应该停滞。"
    vn_white "一百六十八个小时……{w=0.3}七天。"
    vn_white "我想躲开这一切。快来把我放在某个地方。"
    play ambient_sfx sfx_clock_tick volume 0.6
    vn_white "病房里只有墙上挂钟的声音。七天。在学校里是一周的时间。黑胶唱片放两百遍，七天就结束了。"
    vn_white "人们常说时间转瞬即逝，在一生最年轻的岁月、最可赞叹的年华，那时间来去匆匆，有时会突然让你感到震惊。{w=0.3}\n才十六岁，就已经是太迟了。我在十六岁的时候就已经走到了头。"
    nvl clear
    window hide

    stop bgs fadeout 1.2
    play bgs bgs_hospital fadein 1.5 loop
    scene bg hospital_bed_02_blue with dissolve
    show anon hosp 10 tears at center_standee, standee_shake_h with dissolve
    anon "对不起……灯，对不起……我本来不该当面告诉你的。{w=0.2}{nw}"
    extend "\n可是我做不到看着你被蒙在鼓里……在这张床上等到最后一秒。"

    # 【无头像，仅展示对方立绘】
    show anon hosp 06 pain at standee_tremble
    "爱音把脸埋在手心里。我看着她。"

    tomori calm "胸口原本沉重的地方，忽然变得很空。{w=0.2}{nw}"
    extend bitter "\n既然不再有任何希望，我反而感到解脱。这不过叫人难受罢了，没必要哭，现在谁也还没有死啊。"

    tomori calm "原来……{w=0.2}{nw}"
    extend bitter "只有七天了。"

    tomori sadaway "十六年里，我一直在向所有人道歉。{w=0.2}{nw}"
    extend bitter "\n向叹气的父母道歉，向觉得我怪异的老师道歉，向在雨里解散的乐队道歉。{w=0.2}{nw}"
    extend sad "\n我每天醒来，都在为了自己不能成为一个正常人类而难过。"
    tomori calm "但如果只剩下一百六十八个小时。{w=0.2}{nw}"
    extend soft "\n这个世界就再也没有理由要求我去变好了。"
    tomori calm "再也没有人会逼我回到教室，也没有人会对我露出失望的样子。{w=0.2}{nw}"
    extend smile "\n我拿到了一张可以提前离场的票。{w=0.2}{nw}"
    extend calm "\n死这个字，我已经无法把它和我的生命两相分开。它免除了我几乎所有的责任。"

    tomori soft "爱音……{w=0.2}{nw}"
    extend calm "不用说对不起的。{w=0.2}{nw}"
    extend smile "\n谢谢你把这个消息带给我。"

    show anon hosp 03 curious_1 at center_standee
    "爱音把脸抬起来，样子是疑惑的。{w=0.2}{nw}"
    extend "\n那不是看疯子的样子。那是一个闯了祸的孩子发现自己到头来根本没闯祸的样子。眼睛边缘泛着光。好像是要哭出来了。"

    anon "……为什么要谢我啊。"

    tomori calm "因为……{w=0.2}{nw}"
    extend sadaway "已经没有力气再去变好了。"

    show anon hosp 07 normal_2 at center_standee
    anon "……什么？"

    tomori calm "不用再回学校了。{w=0.2}{nw}"
    extend bitter "\n也不用再试着……去当一个合格的人了。{w=0.2}{nw}"
    extend calm "\n躺在这里就可以。我们什么也不等了。"

    show anon hosp 10 tears at standee_tremble
    anon "……高松灯。"

    tomori sadaway "我一直……做不好那些事。{w=0.2}{nw}"
    extend smile "\n现在终于不用做了。"

    show anon hosp 05 annoyed_2 at standee_jump
    anon "{cps=*1.6}笨蛋！大笨蛋！谁要你认错谁要你合格了啊！{/cps}" with shake_h

    play sound sfx_clothes_rustle
    show anon hosp 06 pain at anon_lean_in
    "爱音胡乱用毛衣袖子抹掉脸上的眼泪。"

    tomori calm "下午，晚些时候。我一点也不想再坚持了。{w=0.2}{nw}"
    extend bitter "\n我认为谁也不能说出这种恐慌。还不能。{w=0.2}{nw}"
    extend soft "\n我想叫住你，对你说，把你的嘴凑过来。快来，好走得更快。"

    show anon hosp 10 tears at standee_step_in
    anon "{cps=*1.5}只有七天了！{/cps}{w=0.1}{nw}"

    tomori calm "……嗯，我知道。"

    tomori calm "快。就这样。{w=0.2}{nw}"
    extend soft "\n我不会再做任何事来限制或扩展你的生活。"

    show anon hosp 10 tears at standee_shake_h
    anon "{cps=*1.5}你难道真的要在这里乖乖数着墙缝等死吗？！{/cps}"

    "我望着她被泪水浸湿的眼睛。"
    tomori soft "自从我们有了这事儿，我以为我的生活开始了。这是我平生第一次。{w=0.2}{nw}"
    extend bitter "\n我怎么知道的？我从这个，从我有时候想死，想受苦，想为了能爱她、能为她而痛苦，也为了想我将来还没做完的事情。"
    tomori calm "有一天我们会死的。棺材里将有爱情和尸体。{w=0.2}{nw}"
    extend soft "\n而棺材外面，要放着我们写下的歌。{w=0.2}{nw}"
    extend smile "不可能不是这样的。"

    # 3. 出逃决意与两个请求
    play sound sfx_heartbeat
    camera:
        warp ease_in_out_cubic 1.2 zoom 1.04 pos (0.5, 0.48)
    tomori calm "我不想留在这里。{w=0.2}{nw}"
    extend soft "\n我想在七天结束之前……做一件事。"
    tomori calm "……唯一的一件事。{w=0.2}{nw}"
    extend soft "\n我想把没有写完的那首歌……完整地唱给爱音听。"

    show anon hosp 03 curious_2 at standee_step_in
    anon "……歌？那本写满歌词的日记本？"

    tomori soft "嗯。"

    show anon hosp 04 shy_1 at standee_nod
    anon "……只唱给我听吗？"

    tomori smile "只唱给爱音一个人听。"

    scene bg hospital_bed_02_orange with dissolve
    play music bgm_dialogue_warm fadein 1.5 loop
    show anon hosp 01 smug at anon_burst_in
    anon "{cps=*1.6}那么，明天清晨五点，护士交接班的时候，我们就从这里逃跑！{/cps}"

    tomori ah "……逃跑？"

    tomori calm "那扇门通哪儿？通另一条街。逃跑用的。一扇用来逃跑的门。{w=0.2}{nw}"
    extend bitter "\n不能像你一样，这是让我遗憾的地方。{w=0.2}{nw}"
    extend soft "\n不过，既然爱音都说没关系了，那在这个世界上，就是真的再也没有任何关系了。"
    tomori calm "你就照这样活下去，永远不再听他们的话。我在心里对自己说，我答应你，永不。{w=0.2}{nw}"
    extend soft "\n我们还有那么漫长的几天，我们还有太多太多可以并肩去做的事情。"
    tomori smile "上天在最后收回了全部的苛责，并把千早爱音送到了我空无一人的病床前。{w=0.2}{nw}"
    extend soft "\n我在这荒芜的人世间，再也找不到比这更加浩大、更加纯粹的至高幸福了。{w=0.2}{nw}"
    extend smile "\n谢谢你。真的无尽感谢。无言以表。"

    show anon hosp 02 boast at standee_jump
    anon "{cps=*1.5}把手环扯掉，把难看的病号服扔了，坐上最早一班电车，去哪里都可以！{/cps}"

    tomori calm "去……{w=0.2}{nw}"
    extend soft "能看到海的地方。"

    "大海是没有证件、没有登记簿的地方。只有在海边或海上，一个没有归宿的人才感到最自在。"

    tomori calm "以及，爱音，我对你有两个请求。"

    show anon hosp 08 gentle at standee_step_in
    anon "你说。别说两个，一百个我也答应你。"

    tomori calm "第一，帮我找一点能提神的药，或者苦一点的黑咖啡，怎么都可以……{w=0.2}{nw}"
    extend sadaway "\n只要能让我一直醒着，只要能让我利用好我生命中最后的每一分钟就行。{w=0.2}{nw}"
    extend uff "我现在好困，爱音，可我不想再去睡觉了，我还有太多太多的事情要做。"

    show anon hosp 08 gentle at standee_nod
    anon "我明白。我不会让你睡过去的，我会一直在你耳边说话。{w=0.2}{nw}"
    show anon hosp 03 curious_1 at standee_step_in
    extend "\n那……第二个请求呢？"

    tomori calm "就像你刚才说的那样——带我离开这里，我要死在外面。{w=0.2}{nw}"
    extend soft "我需要再去一次那座人行天桥，再去一次阳光城的水族馆。以前我总是低着头匆匆走过那里，可却从来没有产生过要贴在玻璃上、从近处仔细看看那些水母和鱼群的好奇心。"

    show anon hosp 01 smug at standee_jump
    anon "{cps=*1.5}好，我们明天一早就去！{/cps}"

    show anon hosp 08 gentle at standee_step_in with flash_warm
    tomori calm "我还想不穿厚外套、不打伞走在深夜的冷风里，去体验一下特别寒冷的滋味。从前因为害怕感冒、害怕在练习室里发不出声音，我总是把自己裹得严严实实的。{w=0.2}{nw}"
    tomori smile "爱音，总而言之，我需要仰起脸去淋淋雨，需要向那些曾经对我伸出手的女孩们报以微笑，需要去你邀请我去的所有涉谷咖啡馆，"

    hide anon with dissolve
    "再过几个小时就天亮了。在天亮前一个小时，天气会很冷，但我们已经在路上了。"

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    camera at default
    scene black with slow_dissolve

    $ persistent.cleared_chapter_6 = True
    jump ch07_escape
