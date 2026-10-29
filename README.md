# academic-revision-checklist

给英文学术写作用的修改清单：66 条规则，16 条快速清单，一套「一个案例，一条规则，查全文」的做法，和一个列候选的脚本。

这些规则来自我的英文博士论文（人机交互方向，2026 年 10 月通过答辩）五周、60 多轮的修改记录。每一条都是先在一个具体的句子上卡住，修好，再抽象成一条能拿去检查的规则，然后带着它把全文查一遍。

可以直接当清单读，也可以装成 Claude 的 skill，让 Claude 按这套做法逐句帮你查。

[English summary](#english)

## 「AI 痕迹」指什么

这里说的「AI 痕迹」，跟检测器查不查得出来没多大关系。它指的是读者第一次读就卡住、要回头再读一遍的地方。导师、委员会、审稿人读到这种地方，就会觉得是机器写的。

学校或期刊要求说明 AI 用在了哪里，就照规定写清楚。

## 十六条快速清单

改完一段，逐条问一遍。

1. 第一次读的人会在这一句停下吗？要读两遍的，写下原因。
2. 一句话只报一个结果。
3. 写了 more、higher，就写出和谁比。
4. significant 只用在差异、关联或检验上，不用在比例或平均数上。
5. this、these、the former、the name 这类词，指的东西在前一句之内吗？
6. 一个名字只指一样东西，普通词别撞上自己定义的术语。
7. 冒号只用来引出列表、引文、问题或定义。
8. 少用先否定再肯定的铺垫，带内容的否定留下。
9. 正文不用破折号连接分句。
10. 连着几句长度差不多、开头一样的，改掉一处。
11. 空的过渡词和段尾总结，能删就删，删不掉就换成具体内容。
12. 用自己和这个领域会用的词，能用常用词就不用生僻词。
13. 论文只写研究本身，不写论文是怎么改出来的。
14. 研究问题、引文、数字、自己的反思，不交给 AI 改。
15. 改完重读这一段和前一段，字数上限、段落长度这些硬指标再跑一遍。
16. 别人和 AI 的意见，先拿原文和数据对过，成立的才改。

66 条的完整版在 [`references/checklist.md`](references/checklist.md)，每条一句话；规则、改前改后的原句和查法在 [`references/patterns.md`](references/patterns.md)，编号一致。

## 文件

```text
academic-revision-checklist/
├── README.md                    就是这个文件
├── SKILL.md                     给 Claude 的说明（英文）
├── LICENSE
├── references/
│   ├── checklist.md             16 条快速清单和 66 条一句话规则，从这里开始
│   ├── patterns.md              66 条的完整版：规则、论文里真改过的句子、怎么查
│   ├── workflow.md              一轮修改怎么走，外部意见怎么核对，给其他模型的提示词
│   ├── reading-protocols.md     像第一次读的人那样读，标题怎么读，出声读
│   └── lessons.md               九条原则和八条教训
└── scripts/
    └── flag_candidates.py       列出脚本找得到的候选：破折号、冒号、对比句式等
```

规则和说明是中文写的，例子都是英文原句。

## 怎么用

### 1. 当清单读

从 `references/checklist.md` 开始。想知道某一条为什么要改、怎么改，就看 `patterns.md` 里同一个编号。

### 2. 装成 Claude Code 的 skill

```bash
git clone https://github.com/JimmyRaoUF/academic-revision-checklist.git ~/.claude/skills/academic-revision-checklist
```

然后在 Claude Code 里说「用 academic-revision-checklist 检查 chapter3.tex」，或者输入 `/academic-revision-checklist`。只想在一个项目里用，就放到那个项目的 `.claude/skills/` 下面。

### 3. 在 Claude 网页版或桌面版里用

把整个文件夹打包成 zip，作为自定义 skill 上传，步骤见 Claude 帮助中心的 [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)。文件夹名要和 skill 名一致。从 GitHub 点 Download ZIP 得到的文件夹叫 `academic-revision-checklist-main`，要先改回 `academic-revision-checklist` 再打包。也可以只把 `checklist.md` 和需要的 `patterns.md` 章节贴进对话。

### 4. 在 ChatGPT、Gemini 等其他模型里用

把 `references/checklist.md` 贴进去，再用 `references/workflow.md` 里的提示词模板。要它逐句读、标出读者会停下的句子，不要让它整段重写。它给的每一条意见，都先拿原文和数据核对。

### 5. 跑脚本

只需要 Python 3，不用装别的包。

```bash
python3 scripts/flag_candidates.py chapter3.tex --summary
python3 scripts/flag_candidates.py chapter3.tex chapter4.tex --md flags.md
python3 scripts/flag_candidates.py paper.md --max-para 150
```

能读 `.tex`、`.md` 和 `.txt`，会跳过表格、图、公式和注释。脚本负责把可疑的地方列全，判断还得靠读。我改论文时，缩写检查标出 13 处，真有问题的只有 3 处。

## 几样东西从不交给 AI 改

研究问题的措辞、引文原文、没有数据支撑的数字、自己写的反思段落。每一轮都把它们单列出来，只报告，不改。

## 作者

Nanjie (Jimmy) Rao，佛罗里达大学（University of Florida）Human-Centered Computing 博士，2026 年 10 月通过答辩。

- 个人网站：[nanjierao.github.io](https://nanjierao.github.io)
- Google Scholar：[Nanjie Rao (Jimmy)](https://scholar.google.com/citations?user=EBetHqQAAAAJ)
- 知乎：[刀口饶](https://www.zhihu.com/people/daozhu)，这份清单最早发在知乎的一个回答里
- YouTube：[@drluckydadredl](https://www.youtube.com/@drluckydadredl)

<!-- 截图：两张图放进 assets/ 以后，删掉这一行和这段的最后一行，留下中间两行图片
![Title slide of Nanjie (Jimmy) Rao's PhD dissertation defense, University of Florida, October 2026](assets/defense_title_slide.png)
![Google Scholar profile of Nanjie (Jimmy) Rao](assets/google_scholar.png)
-->

觉得有用就点个 star，也可以在知乎告诉我它帮你改了哪一句。发现规则之间打架，或者有新的例子，欢迎开 issue。

## 许可

文字部分（README、SKILL.md 和 `references/`）用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，可以转载、改写、商用，注明出处就行。脚本（`scripts/`）用 MIT。详见 [LICENSE](LICENSE)。

## 引用

```text
Rao, N. (2026). academic-revision-checklist: 66 rules for revising academic writing for a first-time reader [Computer software]. GitHub. https://github.com/JimmyRaoUF/academic-revision-checklist
```

---

## English

A reader-first revision checklist for academic English: 66 rules, a 16-item quick list, a method, and a script.

It comes from five weeks and more than 60 revision rounds of my English-language HCI dissertation, defended in October 2026. Each rule began as one sentence where a reader stopped: me reading aloud, my advisor, a friend who is a native speaker, or a reviewing model. The fix was written as a rule that can be checked and then applied to the whole document.

"Reads like AI" here means the places where a first-time reader stops or reads twice. This is not a tool for getting past AI detectors.

**The 16-item quick list**

1. Would a first-time reader stop at this sentence? If they would read it twice, write down why.
2. Report one result per sentence.
3. If you write "more" or "higher", say than what.
4. Use "significant" only for a difference, an association or a test, never for a share or a mean.
5. Does "this", "these", "the former" or "the name" point to something within the previous sentence?
6. Use one name for one thing, and keep ordinary words from colliding with your defined terms.
7. Use a colon only to introduce a list, a quotation, a question or a definition.
8. Use few "not A but B" set-ups, and keep the negations that carry content.
9. Use no em dashes to join clauses in the body text.
10. When several sentences in a row have nearly the same length or the same opening, change one.
11. Delete hollow transitions and paragraph endings that only summarize. If one cannot go, replace it with something specific.
12. Use the words you and your field would use, and prefer the common word.
13. Write about the research, not about how the text was revised.
14. Keep research questions, quotations, numbers and your own reflections away from AI editing.
15. After a change, reread that paragraph and the one before it, and rerun hard limits such as word caps and paragraph length.
16. Check comments from people and from AI against the text and the data, and apply only what holds.

**How to use it**

- As a checklist: start with `references/checklist.md`. The full patterns, with English before and after examples, are in `references/patterns.md` (written in Chinese).
- As a Claude Code skill: `git clone https://github.com/JimmyRaoUF/academic-revision-checklist.git ~/.claude/skills/academic-revision-checklist`, then ask Claude to check a chapter with it. `SKILL.md` is in English.
- The script needs Python 3 and nothing else: `python3 scripts/flag_candidates.py chapter.tex --summary`. It lists candidates, and you decide by reading.

Author: Nanjie (Jimmy) Rao, Human-Centered Computing PhD, University of Florida (defended October 2026). Website: [nanjierao.github.io](https://nanjierao.github.io). Google Scholar: [Nanjie Rao (Jimmy)](https://scholar.google.com/citations?user=EBetHqQAAAAJ). Zhihu: [刀口饶](https://www.zhihu.com/people/daozhu). YouTube: [@drluckydadredl](https://www.youtube.com/@drluckydadredl). Text under CC BY 4.0, scripts under MIT.
