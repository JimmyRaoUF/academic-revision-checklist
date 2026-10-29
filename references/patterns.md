# 66 种修改和检查

这些规则来自一篇英文博士论文（人机交互方向，2026 年答辩）五周、60 多轮的修改记录。每一条都是先在一个具体的句子上卡住，修好，再抽象成一条能拿去检查的规则，然后带着它把全文查一遍。

每条的格式：

- **规则**：一句话能检查的做法；
- **例子**：论文里真改过的句子，`改前` 和 `改后` 都是原文；
- **怎么查**：全文找这一类的办法。标了「脚本」的，可以先用 `scripts/flag_candidates.py` 列出候选，再逐处读；其余的只能靠读。

编号和 `checklist.md` 一致，八组是：

1. 句子：读者读到这里要停下（P1–P13）
2. 词和术语：一个名字只指一样东西（P14–P24）
3. 结论、数字和来源：说到证据为止（P25–P33）
4. 段落和整篇的结构（P34–P44）
5. 标题（P45–P47）
6. 图、表和排版（P48–P56）
7. 语气和文风：读起来像机器写的（P57–P64）
8. 成套的方法（P65–P66）

---

## 第一组　句子：读者读到这里要停下

### P1 第一次读的人要读两遍

- **规则**：读者第一次读就要能读懂。凡是要读两遍的句子都算问题，并说出原因：太长记不住，用了没解释的词，指向读者还没见过的东西，走进花园路径（P5），要点不清，或者和前一句接不上。说不出原因的，先别改。
- **例子**：`stays learning` 先被读成动词短语。
  > 改前：and its purpose stays learning
  > 改后：and learning stays its purpose
- **怎么查**：只能读。从第一句读到最后一句，每句问一次「我要不要读两遍」。最好请一个没读过这篇论文的人（或一个没有背景的模型）只做这一件事：标出要读两遍的句子。

### P2 一句话装了两个结果

- **规则**：一句只报告一个结果。两个结果放在一句里，读者要同时记住两件事，还容易弄不清哪个统计量属于哪个结果。
- **例子**：
  > 改前：Word count correlates with the unit count (r = .29) and not significantly with any outcome on its own (r = -.12 to .24).
  > 改后：Word count correlates with the unit count at r = .29. On its own, it does not correlate significantly with any outcome (r = -.12 to .24).
- **怎么查**：读结果部分和所有总结结果的地方（摘要、引言、讨论、结论）。看到 `whereas`、`while`、`and` 连着两个统计量，就停下来。

### P3 从句层层嵌套，或一句串起几个主张

- **规则**：一句里不套几层从句。一句很长、又用 `and`、`which` 接上第二个主张时，拆成两句。只拆确实串起了不同主张的句子，不为拆而拆。
- **例子**：
  > 改前：A direct question elicits what a student can say about an interest on demand, which is how they feel about it, what they do, and why, and not the knowledge of the interest's domain that surfaced when the interest was used
  > 改后：A direct question elicits what a student can say about an interest on demand: how they feel about it, what they do, and why. It does not elicit the knowledge of the interest's domain, which surfaced when the interest was used
- **怎么查**：脚本可以数每句的从句引导词（which、that、because、while、whereas……），列出三个以上的句子，再逐句读。拿本领域一篇通过答辩的论文的比例作参照，比凭感觉准。
- **教训**：我试过 ASD-STE100（给技术手册用的受控英语）。盲评的结论是 "Most of STE100 makes your text read less human."，最后只留下一条：一句长过约 30 个词、又串起第二个主张时才拆。

### P4 主语是抽象的东西，或名词堆在一起

- **规则**：主语尽量是做事的人或物（导师、学生、这项研究），动作写成动词。不要让 `the account`、`identification` 这类抽象名词去做动作，也不要把几个名词堆成一串。
- **例子**：
  > 改前：Obtaining each student's interests, however, is a barrier to IBL's reach in practice.
  > 改后：A major barrier is that interests have to be identified before anything can be built around them, separately for every student.

  改前这句有三个毛病：`however` 开启一节，前面却没有可转折的东西；主语是一个看不出谁在做的动作；句子停在 `in practice` 这个虚词上。
- **怎么查**：只能读。审阅模型的一句诊断很好用："The weakest sentences replace those actors with "the account," "the proposition," or several linked what-clauses. Keep the theory; make its subject and action explicit."

### P5 花园路径：读到后面才发现前面读错了

- **规则**：压缩的短语会让读者先按错误的结构去读，读到后面才发现，只好回头。补上 `that`、介词或动词，让结构一眼就清楚。
- **例子**：`phase teaching` 先被读成一个名词短语，读到 `starts` 才知道读错了。
  > 改前：Matching the source to the phase teaching starts from.
  > 改后：Matching the source to the phase that teaching starts from.
- **怎么查**：只能读，最好出声读。摘要的第一句 "Contextualize what is taught to topics" 也是这样被我自己读出来的（先读成 taught to）。

### P6 指代词离它指的东西太远

- **规则**：`these two`、`both`、`the former`、`this`、`the second`、`the difference` 这类词，如果所指的东西在两句以前，中间又隔着别的可能对象，或者原文是用别的说法提到的，就直接写出所指的东西。
- **例子**：我读到这句时的原话是 "are the 2 features that easy for readers to know which 2? I don't know"。
  > 改前：Because of these two features, the framework treats interests at every phase as candidates for identification
  > 改后：Because an interest can be at any phase at the moment a system tries to identify it, and a student may not recognize an interest in its early phases, the framework treats interests at every phase as candidates for identification
- **怎么查**：读。找出每个 `this`、`these`、`the first` 一类的词，问它指的东西在不在前一句里。可以让第二个人逐条试着证明「其实很清楚」，证明不了的才改。

### P7 读者不知道所指的名词

- **规则**：带 `the` 的名词（`the name`、`the label`、`the framework`、`the pipeline`），如果同一句或前一句没有交代是谁的、是哪一个，读者就要自己去补。直接写出来。
- **例子**：
  > 改前：The tutor's opening question obtained little beyond the name
  > 改后：The tutor's opening question obtained little beyond the interest's name
- **怎么查**：脚本找出每一个 `the name`、`the label` 这类词，逐个在上下文里读。注意：改写别的句子时，它会悄悄写回来。我的论文里 `the name` 改了 34 处，后来的重写又写回来两次。

### P8 比较缺了另一边

- **规则**：写 `higher`、`more`、`more common`、`larger` 时，写出和什么比。
- **例子**：
  > 改前：also rated the content higher.
  > 改后：also rated the content higher than the other participants did.
- **怎么查**：脚本（P8）列出没有 `than` 的比较级，逐个读。修一个问题时新写的句子，也要按这条再查一遍。我有两处按审阅意见改过的句子，改完仍然只写了一边，过了两天才发现。

### P9 统计词或数字挂错对象，或缺了名词

- **规则**：显著性只能说一个差异、一个关联或一个检验，不能说一个比例或一个平均数（A difference, association or test can be significant. A share or a mean cannot.）。百分比要说清是谁的百分比。p 值要写出 `p value`，不能只写 `below .05`。
- **例子**（一位母语是英语的朋友在旁边写了 "Very long sentence + a bit confusing"，这一句同时有 P2、P8、P9 三个问题）：
  > 改前：Both situational phases were significantly more common among browsing history's interests, whereas the larger share of well-developed interests among posts was not significant
  > 改后：Both situational phases were significantly more common among browsing history's interests than among those from posts. Well-developed interests made up a larger share of those from posts than of those from browsing history, but that difference was not significant

  缺名词的一处：
  > 改前：per unit and stayed below .05 in all but one case.
  > 改后：per unit, and its p value stayed below .05 in all but one case.
- **怎么查**：脚本（P9）列出 `significant` 附近有 share、percentage、mean 的句子；再读每一个孤立的 `p`、`.05`。

### P10 句尾拖着出处和建议

- **规则**：一句话讲的是 A，句尾却接上「某某作者建议……」，读者要自己把出处挪回去。给出处单独一句，或者把出处放到句首。
- **例子**：
  > 改前：Talk about what one likes and does belongs to a different tier of disclosure from talk about beliefs and vulnerabilities, a distinction drawn from users' conversations with a companion chatbot
  > 改后：In a study of users' conversations with a companion chatbot, talk about what one likes and does belonged to a different tier of disclosure from talk about beliefs and vulnerabilities
- **怎么查**：读每个句尾的 `, as X advise`、`, a distinction drawn from`、`, following X`。拆句时要把出处一起挪，否则问题还在。

### P11 引文和句子接不上

- **规则**：引文要能接进句子：引文里的代词在句子里要有所指，语法要接得上，句子对引文的描述要和引文一致。
- **例子**：引文里的 `them` 在原句里没有所指。
  > 改前：as Hidi and Renninger advise for the early phases, in which "providing them with questions to answer may be essential"
  > 改后：Hidi and Renninger write that while students are in the early phases of interest development, "providing them with questions to answer may be essential"
- **怎么查**：读每一处引文，连同它前面的半句一起读。

### P12 一个词能读成另一个意思，或撞上文中的术语

- **规则**：一个普通词如果在这个位置有第二种读法，或者和论文自己定义的术语重名，就换一个词。
- **例子**：朋友在 `in other forms` 上方写了 "forums?"；而 `form` 在前一段指自我报告问卷。
  > 改前：their posts may differ in form and audience.
  > 改后：their posts may differ in format and audience.

  撞术语的一处（`individual` 是论文所用理论模型里的一个阶段名）：
  > 改前：to that student's individual interests.
  > 改后：to that student's own interests.
- **怎么查**：先列出论文自己定义的术语，再在全文找这些词的普通用法。只能读。

### P13 评价词或含糊的说法代替了结果

- **规则**：写出发现了什么，而不是给一个评价（`proved efficient`）或一个含糊的方向（`pointed the same way`、`went with`）。`enough` 要说清够什么。
- **例子**：我朗读摘要时问："What do you mean exactly by proved efficient?"
  > 改前：Asking proved efficient but narrow, obtaining a name, a feeling, and an activity
  > 改后：One question reliably returned the name of an interest, a feeling about it, and an activity, and almost never what the student knew about it.
- **怎么查**：在全文找 `efficient`、`effective`、`pointed`、`went with`、孤立的 `enough`，逐处读。

---

## 第二组　词和术语：一个名字只指一样东西

### P14 一样东西有两个名字

- **规则**：同一个概念在正文、表格和图里用同一个名字。名字太长可以用定义过的简称，但不能有两个名字。
- **例子**：图里叫 `direct channel`，正文叫 `directly elicited`。我朗读时的原话："I feel like it should be the same if it's too long. You can use abbreviation. But you should not have different name okay."
  > 改前：The directly elicited disclosure is the participant's reply to the interest question.
  > 改后：The participant's reply to the interest question is the direct channel, the interest information the tutor obtained by asking
- **怎么查**：先数清每个名字在全文出现几次，选已经用得最多的那个；再把每一处在句子里读一遍后替换。结果变量最容易出这个问题，我的一个结果变量曾有四个名字。
- **反过来也成立**：两样东西不能合用一个名字。我想把图里的 `routes` 全换成 `data sources`，读完 50 处才发现它们是两样东西（route 包括提问，data source 不包括），所以没改。

### P15 一个词有两个意思

- **规则**：一个词在全文只用一个意思。尤其要避免普通词和论文定义的术语重名，以及同一个词在相邻句子里换了意思。
- **例子**：`material` 既指学生说的话和数据，又指导师用来教的内容。
  > 改前：Grounding is the extent to which the student's own material supports what the description asserts.
  > 改后：Grounding is the extent to which the student's own words or data support what the description asserts.
- **怎么查**：在全文找出这个词的每一处，按意思分组，一组保留原词，另一组换词。改名之后要再查新名字，`benchmark` 改成 `threshold` 后，又撞上了论文说「没有找到」的那种阈值，只好再分出一个 `cut point`。

### P16 数据的名字要按实际交上来的东西叫

- **规则**：研究用的数据，按参与者实际提交的东西来叫。例如交上来的是帖子，就叫 `social media posts`，不叫 `social media activity`（点赞也是活动，但点赞没有语言）。也不要用 `records`、`traces` 这类笼统的词指你的数据源。
- **例子**：
  > 改前：These findings motivate considering records as complements to asking
  > 改后：considering the data sources as complements to asking
- **怎么查**：全文检索后逐处读，包括图的源文件、表注和标题。

### P17 样本里的人和泛指的角色分开叫

- **规则**：写数据、方法和结果时，研究里的人是 `participants`；讲一般的学习者、讲设计或理论时用 `student`（或你领域的对应词）。
- **例子**：
  > 改前：nearly half of the information asserted about students was not visibly supported
  > 改后：nearly half of the information asserted about participants was not visibly supported
- **怎么查**：每次编译后报告各章两个词的数量；结果部分出现 `students`、理论部分出现 `participants` 的，逐处读。

### P18 自造的词和别扭的标签

- **规则**：说研究里的东西（导师、提问、会话、学生给出的内容）时，用这个领域已经在用的词。新词只留给确实新的构念（Reserve invented vocabulary for the constructs that are actually new.）。
- **例子**：我朗读时在几个自造的短语上停下："If this is so weird, I don't like that."
  > 改前：to a machine addressee
  > 改后：to a tutor rather than to an interviewer
- **怎么查**：拿本领域一篇写得好的论文（我用的是实验室里一篇刚通过答辩的论文）建一个词库，写成脚本跑全文；自己的构念放进保护名单。

### P19 作者和领域都不用的词

- **规则**：用你会用的词和你这个领域会用的词，尤其是动词。拿不准时，先查范文和所引的文献里有没有这个词。
- **例子**：
  > 改前：Study 2 reads its two data sources through the scheme's categories.
  > 改后：Study 2 analyzes its two data sources with the scheme's categories.

  `yield` 在我的论文里出现过 88 次，改到只剩 2 次。`lay in` 这个我读着就别扭的说法，过了大约十二轮检查都没人发现，我当时问的是："'lay in' felt unnatural to me, and why you didn't catch it?"
  > 改前：What went wrong lay in how it was used and in how the student experienced that use.
  > 改后：What went wrong was how it was used and how the student experienced that use.
- **怎么查**：脚本按范文里每个动词的出现次数，标出范文里没有、你却常用的动词；再用全部参考文献作语料，标出「所引文献里从没出现过的词」。之后每改一个说法，都在全文找同一个习语。

### P20 术语先用后定义，经典理论没有解释

- **规则**：每个术语、标签、缩写、统计量和编码类别，都在读者第一次读到它的地方定义或解释（Define before use, for an outside reader.）。经典的理论和定律，即使委员会都熟悉，第一次用时也要描述一句。
- **例子**：我问 "is extractor clearly defined, and natural to use here?"
  > 改前：For an extractor, Accuracy is measured by two established metrics.
  > 改后：When interests are proposed by an extractor, a system that infers them from a data source, Accuracy is measured by two established metrics.

  经典理论的一处：
  > 改前：tend to give the minimum adequate answer, and the more work a question demands
  > 改后：tend to give the minimum adequate answer, a tendency known as satisficing, and the more work
- **怎么查**：列出每个术语第一次出现的页码和定义所在的页码，两者不一致的就改。

### P21 缩写、简称、有名的模型没写全

- **规则**：用准确的全称，不用省掉一个词的简称（large language models 不是 language models）。缩写在摘要、第一章和相关章节第一次出现时都展开。属于一个有名模型的构念，写出模型的名字和作者。
- **例子**：我朗读时说："You need to be more specific because large language models are different than language models. And check this type of issue throughout the whole dissertation."
  > 改前：Language models are already being used to teach through a student's interests
  > 改后：Large language models are already being used to teach through a student's interests
- **怎么查**：脚本能查三件事：省略了一个词的术语，第一次出现时有没有展开，同一章里有没有重复展开。

### P22 借来的专业词换了意思

- **规则**：从别的领域借来的词（信息论的 channel、capacity、noise，质性研究的 coding cycle），只在它原来的意思上用。研究没有测量的东西，不用那个领域的词。
- **例子**：
  > 改前：The behavioral trace is expected to be broader and noisier.
  > 改后：The behavioral trace is expected to be broader and less precise.

  导师指出过另一处，second coding cycle 在质性研究里指把数据再编一遍码，而我叫作第二轮的，只是把两位编码者的码对照、合并。
  > 改前：The Two First-Cycle Passes
  > 改后：The Two Initial Coding Passes
- **怎么查**：在全文检索这些借来的词，逐处读。

### P23 名字跟着构念走，没有跟着测量走

- **规则**：结果变量按量表实际测的东西命名，不按它代表的构念命名（Use the word for what the instrument measured, not the construct it stands for.）。构念是要判断的性质，测量是判断它的方法，两者分开定义。
- **例子**：那个量表叫 Value/Usefulness，正文却写成 relevant。
  > 改前：the more relevant they rated the interest-based session's content
  > 改后：the more useful they rated the interest-based session's content
- **怎么查**：对照每个量表的名字和题目，读每一处提到这个结果的句子。导师的一句话可以当检查问题：你有没有把构念和测量混在一起？

### P24 能用常用词的地方用了生僻词

- **规则**：一个词如果不在 TOEFL 词表或常用词表里，又有一个常用词能保持原意，就换成常用词。领域术语、论文定义的术语和人名保留。
- **例子**：
  > 改前：an analogy that presupposes something about the participant
  > 改后：an analogy that assumes something about the participant

  > 改前：This dissertation adopts the reciprocal view
  > 改后：This dissertation adopts the two-way view
- **怎么查**：脚本把全文每个不同的词和词表比对，列出表外的词，再逐个判断。我那一轮标出 307 个词，最后改了 38 处，其余都写了保留的理由。

---

## 第三组　结论、数字和来源：说到证据为止

### P25 引用的来源不支持这句话

- **规则**：每个引用都要支持它所在的句子，而且要打开原文核对，不靠摘要或别人的转述。数据、结论和案例必须能核实，不编造来源；没有直接出处的说法，标出来让作者决定。
- **例子**：
  > 改前：problems written in the context of students' own interests have raised interest
  > 改后：problems matched to the interest categories students endorsed on a survey have raised interest
- **怎么查**：只能读。打开每一个被引用的 PDF，找到支持这句话的那一段。我第一次这样核对一篇被引用的论文，就发现三处引用错误；第 1 到 3 章另有 18 句和所引来源不符。

### P26 数字不能从数据重现，或前后不一致

- **规则**：正文里依靠的每个数字，都要能用研究的数据文件和脚本重新算出来；没有人核对过的计数，要么删掉，要么重新数。两处数字不一致时，先查清各自是哪天、按什么写的，再决定改哪一处。改数字要有数据依据。
- **例子**（两处均值对不上：这里用了整场会话的均值，该用只算回答的均值）：
  > 改前：a name from everyone, a mean of 3.4 units,
  > 改后：a name from everyone, a mean of 2.5 units,
- **怎么查**：在本地用原始数据和脚本重跑每一个数字。参与者的数据不离开本机，不发给任何外部服务。

### P27 概括比结果说得宽、强或弱

- **规则**：摘要、引言、讨论和结论里的概括，只说结果支持的那么多，带上结果的范围和条件。文献空白只说到「本文综述过的研究」为止。反过来，自己做到的也要说足，不因为怕说过头而含糊。我的原话："I don't want to overclaim, but please claim exactly what I did, with no hold back."
- **例子**：
  > 改前：Asking always found the right interest yet often gave the tutor little to build from.
  > 改后：In Study 1, every participant named an interest, while many disclosed little detail about it.

  文献空白的一处：
  > 改前：None of these works examines where the interest data come from.
  > 改后：These studies do not compare alternative sources of interest information.
- **怎么查**：把每个总结性的句子和报告这个结果的那一章对照着读。

### P28 因果、不显著和平均的说法不准

- **规则**：相关的结果不用 `made`、`caused`、`drove`、`raised` 这类因果动词；不显著的结果写 `was not significantly associated`，不写成「没有关系」或「关系很弱」；组的平均数要写 `on average`，不写成每个参与者都如此。
- **例子**：
  > 改前：was only weakly related to the count (ρ = .34, p = .053)
  > 改后：was not significantly related to the count (ρ = .34, p = .053)

  > 改前：Participants who disclosed three units or fewer rated the content of the interest-based session no higher than they rated their generic session
  > 改后：On average, participants who disclosed three units or fewer rated the content of the interest-based session no higher than that of their generic session
- **怎么查**：在结果和讨论里找因果动词和 `weakly`、`no relation`；读每一句关于组的结论。

### P29 计数被当成发现

- **规则**：描述性的计数只是对这个样本、这个问题的描述。换一批学生、换一个问题，计数就会不同，所以不能单凭计数推出结论。回答「说了什么」这类问题，先用文字和例子回答，计数留给后面的相关分析。
- **例子**：
  > 改前：from everyone and little more: a median of three IIUs over the session, with only 12 students'
  > 改后：When asked, students named interests but most said little more.

  新加在计数后面的一句：
  > These counts answer RQ1.1 for this sample and for the questions the tutor asked.
- **教训**：这句话后来被「段尾不写空洞总结」的规则删掉一半，又被另一轮理解错了一次，丢了「换一个问题，计数就会不同」这一半。两条规则撞在同一句上时，要回头看前一条规则当初为什么要写这句话。

### P30 没检验过的设计被写成前提

- **规则**：研究没有检验过的设计，不写成前提或要求（`the tutor should receive`）。`should` 只出现在从结果推出的建议里，而且要标明它没有被检验。
- **例子**：导师看到这类句子时问的是：谁说它应该这样？
  > 改前：It follows that raw data should not reach a tutor and that the tutor should receive only a description the student has reviewed
  > 改后：These findings support a design in which raw data do not reach a tutor and the tutor receives only a description the student has reviewed
- **怎么查**：在全文找 `should`、`must`、`needs to`，逐处问：这是结果推出的，还是我假定的？

### P31 结果出现得太早

- **规则**：研究问题、方法、文献和理论框架这些章节，任务是提问、描述或说明，不报告结果，也不用预设了结果的说法。结果出来以后才写的「预期」，不当作预测。
- **例子**：我朗读研究问题那一节时说："I don't know if you should report rq2.3 results here because this is just research question, right?"
  > 改前：The differences it finds are differences in what each source produced under one extraction procedure.
  > 改后：Any differences it finds are differences in what each source produced under one extraction procedure.
- **怎么查**：脚本可以在研究问题和方法部分找结果用语（found、showed、higher、significant……），作为每次编译必须为 0 的一关；再逐句读第 1 到 4 章里提到研究和数字的句子。

### P32 统计术语没有解释，或加了先例没有的限定词

- **规则**：统计量和统计术语在第一次出现的地方用平白的话解释。总结性的地方（摘要、引言、结论）只给普通的统计量，技术性的限定词留在结果章节。不加本领域先例里没有用过的限定词。
- **例子**：我朗读时说："Okay, this is very weird... explain what is uncorrected test."
  > 改前：The association is a qualified one, holding on the uncorrected test and falling just outside it once the four outcomes are corrected as a family
  > 改后：The association is a qualified one: it holds when that outcome is tested on its own (p = .014), and it falls just outside .05 once the p value is adjusted for the four outcomes tested together
- **怎么查**：列出每个统计量第一次出现的页码和解释所在的页码。拿不准一个限定词要不要加，就查本领域通过答辩的论文用没用过。

### P33 参与者引文和转写不一致

- **规则**：引用参与者的话要和转写逐字一致，省略处用省略号标出；采用什么约定（是否改正拼写），在方法部分写明。
- **例子**（写进方法部分的约定）：
  > Quotations are verbatim, including the participants' spelling and capitalization, and an ellipsis marks an omission.
- **怎么查**：把每一处参与者引文和它的转写逐一对照。在本机上做，参与者材料不发给外部服务。

---

## 第四组　段落和整篇的结构

### P34 一段讲了两个主张，或太长

- **规则**：一段一个主张。我的段落规则是："Treating the 150-word cap as a governor rather than a strict law preserves narrative momentum: keep the default at 120–150 words, allow the occasional 180-word synthesis, and ruthlessly cut any paragraph attempting to support two independent claims." 这里的 cut，是在两个主张的接缝处分段，不删句子。
- **怎么查**：脚本（P34）列出超过上限的段落，逐段读，找接缝。之后每一轮修改都检查改过的段落有没有超过上限。

### P35 建立在后文之上

- **规则**：Build on what came before, never on what comes later. 一节只能用前面已经交代过的定义、表格、设计和结果。可以保留三种向后的指引：本章的路线图、章末交给下一章的过渡、指向附录。
- **例子**：
  > 改前：That is an expectation the literature supports rather than a result, and Chapter 6 is where it is put to the test: RQ2.2 compares the phase distributions the two sources produce.
  > 改后：That is an expectation the literature supports rather than a result.
- **怎么查**：脚本列出所有指向后文的交叉引用（我的论文里有 207 个），逐个读，凡是借用了后文的定义、表格、设计或结果的，改写或删去。

### P36 段落开头接不上前一段

- **规则**：每段的开头要从前一段接过来；`however`、`this premise` 这类连接词，前面要真的有可以转折或指回的东西。
- **例子**：
  > 改前：This premise has substantial empirical support: students who study mathematics
  > 改后：Studies in several subjects support that promise: students who study mathematics

  > 改前：Conversational tutors predate the LLM.
  > 改后：Earlier conversational tutors show the authoring effort that preceded LLM-based instruction.
- **怎么查**：只读每一个段落和小节的衔接处：上一段的最后一句，下一段的第一句。

### P37 推理少了一步

- **规则**：句子之间的推理不能留一步让读者自己补。每一句都要从前一句推出来。宣布「有意义」的句子，要说出是什么意义。
- **例子**：
  > 改前：Read against that model, the descriptive results have a specific meaning.
  > 改后：Read against that model, stored knowledge made up one-tenth of what asking obtained, and the other three components nine-tenths
- **怎么查**：讨论和结论部分按顺序逐句读，问：这一句是从前一句推出来的吗？

### P38 开头讲文档，或以别人的结论开头

- **规则**：章节的第一句讲主题本身，不讲这一节为读者做什么。段落和小节也不以前人的结论开头，先讲本研究自己的观点，再引用。我朗读时说："We don't spell it out. In such obvious way like this section sets out what a reader needs in order to follow the problem."
- **例子**：
  > 改前：The first decision concerns what is being identified.
  > 改后：What is being identified is an interest, and in the four-phase model
- **怎么查**：脚本取出每一章、节、小节下面的第一句，标出以读者为主语、描述本节用途、空洞铺垫的写法；再逐段读每一段的第一句。

### P39 同样的内容出现几次

- **规则**：每一种内容只有一个家（Give each kind of material one home.）：文献综述报告别人发现了什么，理论框架讲你的理论，结果部分报告，讨论部分解释。删去重复时，保证留下的那一份完整。一个数字第一次报告之后，再提到时用指引，不再复述。
- **怎么查**：逐句对照容易重复的两处（研究问题一章和各研究开头、结果和讨论）；脚本列出出现五次以上的数字，再逐处判断。

### P40 前后说法不一致，或旧说法没跟着改

- **规则**：后面的章节转述前面的结果时，数字、限定词、术语和指引都要和报告结果的那一章相同。一个决定改变了文档，就找出所有还按旧状态写的句子。
- **例子**（和另一章 "not in degree along one scale" 的说法矛盾）：
  > 改前：and the two data sources make moves of different sizes.
  > 改后：and the two data sources make different moves.
- **怎么查**：结论、讨论、摘要和引言，逐句和报告结果的章节对照。每做一个决定（改名、改分析、删一节），就把旧说法写成检索词查一遍。

### P41 带来的疑问多于价值的内容

- **规则**：一段内容、一项分析或附录的一部分，只有在某个结果或论证依赖它时才保留。它引出的疑问多于它带来的价值，就删掉，或者移到附录。理由是读者的负担，不是页数。我当时的话大意是：有些部分带来的困惑和疑问，多于它的价值。
- **怎么查**：按节估算篇幅，和本领域一篇通过答辩的论文的目录对照；每部分写出保留或删去的理由，作者批准后再动。

### P42 论文在讲自己是怎么写成的

- **规则**：论文写研究现在的状态。导师看到我在正文里交代研究问题是怎么改出来的，说这不是一个讲论文怎么变过来的故事。举一反三，还要找三类：交代工作先后顺序的句子，评论文章自己怎么写的句子，提前回应读者反驳的句子。`now`、`previously`、`originally` 这类表示修改史的词也不用。
- **例子**（评论文章自己的一处）：
  > 改前：Two patterns are worth recording, with their limits.
  > 改后：Two patterns appear, each with its limits.

  修改史用词的一处：
  > 改前：since a tutor can now generate an interest-based example
  > 改后：since a tutor can generate an interest-based example
- **怎么查**：脚本（P42）找 `now`、`originally`、`revised`、`turned out`、`added later` 这类词；再按三类逐句读。

### P43 方法细节散在各处

- **规则**：谁编的码、用什么工具，在方法部分交代一次；其他地方只写 `coded`，不写 `human-coded`、`machine-coded`。我朗读时的原话："Say it was coded and don't specify who coded it."
- **例子**：
  > 改前：scored under two different arrangements of machine and human effort, which makes it less likely to be an artifact of either arrangement.
  > 改后：scored under two different procedures, which makes it less likely to be an artifact of either.
- **怎么查**：在全文找 `human`、`machine`、`AI-coded`、`LLM-coded`、工具名，逐处读。

### P44 引言没有从空白一步步推到方法

- **规则**：引言的每一步都由上一步推出：问题，前人做了什么，还缺什么，从哪里切入，核心想法，方法，贡献。至少用一两句说清前人做了什么、还缺什么、本研究从哪里切入。结果只说方向和意义，具体数字留给结果章和结论章。贡献不说过头。
- **例子**（先给核心想法，再引出测量）：
  > 改前：This dissertation builds a way to measure what a student's reply and the two data sources reveal about the student's interest,
  > 改后：In the account this dissertation develops, a tutor teaches not from the interest itself but from the information about it that reaches the tutor. The dissertation therefore builds a way to measure what a student's reply and the two data sources reveal about the student's interest,
- **怎么查**：只读引言，把每一段标成上面七步中的哪一步，看顺序有没有跳。

---

## 第五组　标题

### P45 标题读成另一个意思、冒号两边接不上、术语用得太早

- **规则**：每个标题先在目录里读一遍，再到正文的位置读一遍，问三个问题。一，脱离上下文，它会不会被读成这一节没有做的事？二，`X: Y` 这样的标题，能不能用一句话说清 Y 和 X 是什么关系？三，标题里的术语是不是已经介绍过，用的是不是论文定义的意思？改的时候，先用本节路线图句或第一句里的原话。
- **例子**：我读 PDF 时问："before and after the : seems to be relevant but not direct link?"
  > 改前：The Scaling Problem: From Traditional Methods to Automated Identification
  > 改后：Traditional Methods and Why They Do Not Scale
- **怎么查**：只能读，按顺序一个一个读，每个都对照本节的开头。做法见 `reading-protocols.md`。

### P46 标题写了结论、问题或分析的状态

- **规则**：学位论文的标题说这一节讲什么，不说这一节发现了什么；不写成问句；不用 `Exploratory` 这类分析的状态代替内容。同一层的标题形式平行。期刊或会议有自己的惯例时，按惯例，但全文统一。
- **例子**：
  > 改前：Direct Elicitation Obtained Little Beyond the Name of the Interest
  > 改后：What Direct Elicitation Obtained

  > 改前：Exploratory Analyses of Phase
  > 改后：Phase Evidence and the Four Outcomes（"exploratory" 移到这一节的第一句）
- **教训**：我曾按一篇范文把讨论部分的标题改成结论句，五天后又按「标题写内容」改回来。同一个对象，两条规则给出了相反的做法，要先定下用哪一条。

### P47 粗体引导语是残句、用词别扭或指代不清

- **规则**：段首的粗体引导语如果是一句话，就写成完整的句子，不留残句；里面的词要自然，代词要有所指。
- **例子**：我读局限部分时说："I feel like each limitation. The bold. It should be a complete sentence. For example, you cannot just. Power."
  > 改前：Power.
  > 改后：Because of the sample size, statistical power is limited.
- **怎么查**：列出所有粗体引导语，在上下文里读，问四个问题：词自然吗，形式对吗，能用平白的话说出意思吗，代词指什么。

---

## 第六组　图、表和排版

### P48 图注太长

- **规则**：概念图的图注只说图里有什么、各部分怎么连起来，一两句话，约 30 词；论证放进正文。统计图的图注按本领域论文的一般长度。
- **例子**：一张图的图注从约 140 词缩到约 50 词。
  > 改后：Dissertation scope. Upper tier, Study 1 (blue): what the agent obtains by asking. Middle tier, Study 2 (orange): what an LLM extracts from two data sources the student already produces.
- **教训**：缩短也可能删掉读者需要的东西。一张图的图注一度只剩 "The horizontal line marks no difference."，我读的时候说 "is very confusing"，只好补回每个点和这条线的含义。
- **怎么查**：数一数本领域论文的图注长度作参照；请一个读者把每张图表单独读一遍，看不读正文能不能看懂。

### P49 坐标轴不分图表类型

- **规则**：柱状图的长度表示数值，所以从零开始；点、线和箱线图表示的是位置，坐标轴可以按数据收紧。改了坐标轴，就要改描述坐标轴的图注和替代文字。
- **怎么查**：把每张图按类型分好，数据图用脚本重画；再读每一处描述坐标轴的图注和替代文字。

### P50 图表里的字太小

- **规则**：图表里的字不小于正文（12 磅），图不缩小。
- **怎么查**：在 PDF 上量每张图里的字号；列出所有用小字排的表。

### P51 正文里用了粗体

- **规则**：粗体只留在标题、段首引导语、列表标签，以及定义构念的地方。句子里定义的术语用斜体；正文里其他的粗体改成普通字。正文里的数字不加粗。句首加粗的几个词，会让普通的句子看起来像自造术语的词汇表。
- **怎么查**：脚本列出全部 `\textbf`、`**`，逐处读。

### P52 用斜体来强调

- **规则**：In APA-style writing, italics normally mark terms and titles, not whole sentences for emphasis. 不用斜体强调，不把整句设成斜体，引号里的内容不再加斜体。
- **怎么查**：脚本列出全部斜体，每一处读过、归类，再按类修改。

### P53 引号、标点、拼写不统一

- **规则**：引号用弯引号（“ ” 和 ‘ ’）；逗号和句号放在后引号里面（美式）；人名的拼写和参考文献一致；同一个复合修饰语全文只用一种写法。
- **例子**：
  > 改前：Social-media platforms market themselves
  > 改后：Social media platforms market themselves
- **注意**：LaTeX 里的 ` `` '' ` 在有的字体下会印成两道细线，看起来像两个单引号；直接输入弯引号最稳。
- **怎么查**：在 PDF 里数引号；复合修饰语全部数过，按多数的写法统一。

### P54 引文缺出处位置

- **规则**：书一类的长来源（专著、学位论文、法规），或者同一来源在文中别处已经给过页码时，引文才给页码或节号。
- **例子**：
  > 改前：for which they are processed"~\cite{gdpr2016}.
  > 改后：for which they are processed"~\cite[Art.~5(1)(c)]{gdpr2016}.
- **怎么查**：逐条检查每一处直接引语。

### P55 参考文献格式错误

- **规则**：参考文献标题里的缩写和专有名词要用花括号保护，期刊名首字母大写，页码、编者、预印本编号的格式统一。
- **例子**（BibTeX 会把标题转成句首大写，PAIGE 印成了 Paige）：
  > 改前：title={PAIGE: ...
  > 改后：title={{PAIGE}: ...
- **怎么查**：不只改别人指出的几条，把每一条被引用的条目都查一遍。

### P56 为排版改字

- **规则**：用词按读者的需要定，不按排版定。章末只剩一两行，或者图表打断了句子，等措辞全部定下来以后检查一次，用图表的位置解决，不改字。多出一页没关系。
- **怎么查**：措辞定稿后，在完整的编译结果上查一次：各章起始页、每章最后一页的行数、有没有图表落在句子中间。

---

## 第七组　语气和文风：读起来像机器写的

这一组的每一种写法，单看一处都不算错，叠在一起就会让读者觉得是机器写的。

### P57 冒号代替了「因为」或句号

- **规则**：冒号用来引出列表、引文、问题或定义时保留；代替 `because`、`that is`、`by` 或句号时改掉。一位母语是英语的朋友读完第一、二章说冒号太多，"sounds AI-ish"。
- **例子**：
  > 改前：the channel was not a minor supplement: it provided
  > 改后：the channel was not a minor supplement. It provided
- **怎么查**：脚本（P57）列出每一个带冒号的句子，逐句读。我的第一章 18 个带冒号的句子改了 7 个，第二章 68 个改了 29 个。

### P58 「不是 A，而是 B」的对比句式

- **规则**：直接说是什么，不用「不是 A，而是 B」铺垫（It is not [A], but rather [B]）。但承载内容的否定要保留：研究的局限、不显著的结果、文献的空白、范围的边界。只在三种情况下改：被否定的一半是没人说过的稻草人；它重复了本句或前一句；它重复了附近已经做过的对比。
- **例子**：
  > 改前：an interest is not one quantity but three
  > 改后：an interest has three components

  > 改前：Third, asking and the data sources complement each other rather than substitute for each other.
  > 改后：Third, asking and the data sources complement each other.
- **怎么查**：脚本（P58）列出 `not ... but`、`rather than`、`instead of`、`not only`，分两遍读：先读含两个以上对比的段落，再逐句读剩下的。我的 `rather than` 从 146 处降到 100 处，剩下的都是承载内容的否定。

### P59 破折号

- **规则**：正文不用破折号连接分句（Do not use em dashes as a crutch for clause connection.）。也不要把每个停顿都换成冒号或分号。短横线只用在数字范围里，如 0–4。
- **怎么查**：脚本（P59）。

### P60 句长差不多，或连续三句同一个句式

- **规则**：任意连续五句的词数不要都相差在五个词以内；不要连续三个短语、从句、句子或段落用同一个句式。有意义的排比（并列的名词、步骤的顺序）保留。
- **例子**：
  > 改前：A reply is shaped by the tutor's question and by the exchange in which it is given. A post is shaped by what the student chooses to share with an audience. A browsing history is shaped by the activity the browser records.
  > 改后：A reply is shaped by the tutor's question and by the exchange in which it is given, and a post by what the student chooses to share with an audience. A browsing history, by contrast, is shaped by the activity the browser records.
- **怎么查**：脚本（P60a、P60b）。拆长句之后要再跑一遍，因为拆句会制造新的整齐，比如连着三句都以 `The` 开头。

### P61 空洞的过渡词和段尾总结

- **规则**：删掉 `Overall`、`In summary`、`It is worth noting that`、`Crucially`、`Importantly`、`Ultimately`、`In conclusion` 这类过渡词。段尾那句泛泛的总结，要么删，要么换成具体内容（Either delete generic concluding sentences or replace them with substantive, concrete content.）。
- **例子**：
  > 改前：Together, the studies suggest three implications
  > 改后：The studies suggest three implications

  > 改前（一章的最后一句）：They raise questions for further research.
  > 改后：删去。

  > 改前：In this chapter they serve as the predictors in the outcome analyses of RQ1.2.
  > 改后：In the outcome analyses of RQ1.2, the unit count is the primary predictor and the number of categories covered an exploratory one.
- **怎么查**：脚本（P61a 列出过渡词和常见的「机器词」，P61b 列出段尾句），逐处判断。

### P62 附近重复的发现，镜像式的句子

- **规则**：同一个发现不在相邻的段落里说几遍；不写 `the first ...; the second ...` 那种两半互相对照、像等式一样的句子。平行地报告几个结果不算。
- **例子**：
  > 改前：The second benefit is therefore the one a data source can serve; the first is the one asking already serves.
  > 改后：A data source can add to the content benefit, while for the relational one asking may already be enough.
- **教训**：另一个例子，正是三天前为了解决一个词的撞车（P12）新写的句子。修好一个问题的新句子，后来成了另一类问题的例子。
- **怎么查**：脚本比较相隔十几句以内的每一对句子，标出实词大部分相同的；再找 `is the one`、`; the first`、`the second`、`former/latter`。

### P63 格言、比喻、动名词主语、戏剧化的短句

- **规则**：不写格言式的句子，不给抽象概念用比喻（`interest acts as a bridge`），不让动名词做主语，不用戏剧化的短句。直接说谁做了什么、测量了什么。我读到结论里的一段时，觉得它 "unnatural and troubling"。
- **例子**：
  > 改前：That distance can be measured, and measuring it is what this work offers. Closing it is a design problem.
  > 改后：The grounding audit measures how much of a description consists of such claims. Future systems can be designed to make fewer of them.

  > 改前：The usual explanation is that interest acts as a bridge, making unfamiliar content reachable from familiar territory
  > 改后：The usual explanation is that interest connects unfamiliar content to what the student already knows
- **怎么查**：只能读。

### P64 编辑的文字盖住了作者的声音

- **规则**：保留作者自己的推理和具体的行动者。说清楚是谁、做了什么（Name the person and action.），不要让抽象的措辞、反复的限定和打磨得太光滑的句子，把说法变得比原意更肯定。我请一个模型拿论文对照我原来的想法，它的诊断是："abstract wording, repeated qualifications, and claims that sound more conclusive after being made into polished sentences."
- **例子**：
  > 改前：This dissertation takes identification as its object.
  > 改后：This dissertation examines how a tutor comes to know a student's interests.
- **怎么查**：找一份作者早期的文字（草稿、录音转写、开题报告），和现在的文字对照着读，找出作者原来的说法更自然的地方。

---

## 第八组　成套的方法

### P65 一段要紧的文字反复改的办法（JRfix）

摘要在大约六小时里改了 26 版之后，我把步骤整理成了一个方法，后来用它查全文：

1. **先写下主线**：一两句话写清全文讲什么，再决定这一段为主线的哪一部分服务。不服务任何一部分的句子，删掉或挪走。
2. **像陌生人一样朗读**：逐句读，在每一个停下的地方问：谁的？谁做的？怎么做的？为什么在这里？这个词在这里是什么意思？
3. **八项检查**：
   1. 交代清楚：给结果之前，先说谁对谁做了什么、怎么做的；没有框架的数字，要么补上框架，要么删掉。
   2. 主次：核心构念放在段首，定义之后按名称使用；主线依赖的关键结果要写出来。
   3. 一个说法只有一个范围：不把均值和中位数、一次回答和整场会话、别人的发现和自己的发现、挑出来的两个结果和全部结果混在一句里。
   4. 用测量的名字：量表测的是什么就叫什么（P23）；用能覆盖所有对象的词；含糊的名词换成具体的。
   5. 经济：不服务主线的内容（限定、细节、过程、内部用语）移到它该在的章节，不是删掉。
   6. 动词和语法：动词准确，没有别扭的主语，没有缺动词的句子，并列成分形式一致。
   7. 读者会质疑的逻辑：找出一个敏锐的读者会挑战的句子，拿数据核对；不说过头；保留结论依赖的条件；没检验过的写成可能性。
   8. 首尾呼应：前面引出的词，后面要拆开、要用结果回答、要在结尾呼应。
4. **核对后才保留**：每个数字从数据重算，或在报告它的那一章找到；每个说法在正文里找到支持它的句子。
5. **每种信息放在读者需要它的地方**：摘要和结论放主线，方法放过程，结果放带范围的数字，讨论放解释，局限放没有证明的东西，附录放全部细节，修改史只放在日志里。
6. **改完重读这一段和前一段**："Each fix can create the next problem."

### P66 把过去通过把关的文档整理成规则

如果你有一份已经通过导师把关的文档（开题报告、已发表的论文），它的修改历史里藏着导师的标准。把这些修改整理成规则，再用来查新的文档："The task is to find places where the current text breaks the rules that made those two documents pass, and to propose minimal fixes."

我从开题报告整理出 16 条，其中包括：先定义再使用；只建立在前文之上；逻辑链；说到证据为止；出处和归属；方法先于数字；图注要短；每段每个来源最多一处引文；粗体和斜体只在定义处用一次；表示顺序的词只用于确实有先后的步骤；段落长度；不用模板式结尾；说过的数字和承诺要兑现；不用强化词（`very`、`highly`）；对比要公平。

- **例子**（强化词）：
  > 改前：trained on a very large body of text
  > 改后：trained on a large body of text
