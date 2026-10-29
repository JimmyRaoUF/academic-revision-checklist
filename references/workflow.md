# 一轮修改怎么走

## 「AI 痕迹」指什么

这里说的「AI 痕迹」，跟检测器查不查得出来没多大关系。它指的是读者第一次读就卡住、要回头再读一遍的地方。导师、委员会、审稿人读到这种地方，就会觉得是机器写的。学校或期刊要求说明 AI 用在了哪里，就照规定写清楚。

## 一个案例，一条规则，查全文

每一轮都是四步：

1. **一个具体的案例**：你朗读时卡住，或者导师、朋友、审阅的模型在某一句停下。
2. **修好这一处**。
3. **归成一类**：这一处属于哪一类问题？写成一条能拿去检查的规则。抽象要到能检查的程度，又不能只按字面查。导师指出的是「研究问题的修改史」，只按字面查，就只会去找「研究问题」这几个字；按她的逻辑查，又找出三类句子（见 P42）。我当时的原话是 "check (举一反三, not just literally)"。抽象得太粗也会出错。要是把 route 全部换成 data source，就会把两样东西合成一个名字（P14）。
4. **带着规则查全文**：逐句读，标出可疑的地方，逐处核对，修改，再记录。

最早说出这个循环的，是我朗读摘要时的一句话："I want you to not just take the surface value, but also try to distill my style and learn about it and try to apply it, for even though places where I haven't pointed out and fixed them."

## 全文检查的三种做法

1. **逐句读**：从第一句读到最后一句，每一句都问同一组问题（`reading-protocols.md`）。最慢，但能发现脚本找不到的停顿。
2. **先用脚本找候选，再逐处读**：脚本按词或句式列出所有可能的地方（`scripts/flag_candidates.py`），每一处再读上下文来判断。脚本只能找它认得的写法，判断要靠读。
3. **请一个没有背景的读者**：让没读过这篇论文的人或模型，只说哪里读不懂、哪里要读两遍，再逐条用原文核对，成立的才改。

我自己的要求是："I don't want machine regex check, but your intelligence check by reading through every sentence and think about fixes, not python script automation"。脚本是找候选的，不是做判断的。

## 每一处修改都留下什么

- 一份修改清单：每一处的原文和新文，原文必须在文件里恰好出现一次；
- 修改前的备份；
- 编译和检查：页数、目录页码、引用、段落长度、这次修改相关的脚本计数；
- 一条日志，写明为什么改，最好引用提出问题的那个人的原话。

有了这些，才敢大面积地改，哪一处改坏了也能单独撤回。

## 不交给 AI 改的东西

每一轮都单列出来，只报告，不改：

- 研究问题的措辞；
- 引文原文（文献引文和参与者的话）；
- 没有数据支撑的数字（数字只能按数据改）；
- 作者自己的反思段落；
- 作者已经明确做过决定的地方。

## 外部意见（人或模型）怎么用

- **先核对，再采用。** 每一条意见都拿原文和数据对过：成立的改，部分成立的按原文调整，不成立的写明理由。我的论文里，一次通读给了 44 条，用了 40 条；另一次两份审阅一共 44 条，成立的是 21 条。没成立的里面，有一条说正文的相关系数范围和表格对不上，其实是模型把表里的一列看错了；还有一条建议的拆句，会让一个假设的后半句丢掉 "as an untested hypothesis" 这个限定。
- **不成立的不再翻案。** 下一轮把「已经决定、已经核对过」的清单交给审阅者，请它不要再提，除非有新证据。
- **第二轮给新的任务。** 第一轮让它挑问题；第二轮把这一轮改了什么（改前、改后、页码）列给它，请它只看这些新改动有没有带来新问题，再去读第一轮没细读的章节。

### 给没有背景的读者的提示词（第一轮）

```text
You are reading my manuscript for the first time. Do not rewrite it.
List every sentence where a careful first-time reader would stop or read twice.
For each: the page, the exact sentence, why a reader stops (one clause),
and the smallest fix in my plain style (no new claims, numbers or citations;
no em dashes). Do not comment on research questions, quotations or numbers;
report problems in them without proposing a rewrite.
```

### 第二轮的提示词骨架

```text
Attached: the latest PDF, and a context file with (1) every change since the
version you reviewed (page, before, after, why), and (2) every point from the
earlier reviews and what happened to it.

A. Check each change: is it better, the same or worse for a first-time reader;
   did the meaning change; did it create a new problem (broken grammar, a pointer
   that now refers to the wrong thing, three sentences in a row with the same
   opening, five sentences of nearly the same length, a mismatch with the same
   statement elsewhere)?
B. Read closely the parts no reviewer has read closely: [chapters].
C. Check that the same results are stated the same way in the abstract,
   introduction, results and conclusion.
Do not raise again anything marked decided or frozen, unless you can show
something its reason misses.
```

## 最后两步

1. **一遍不带清单的通读。** 每一种检查都有盲区。`lay in` 这个我读着就别扭的说法，过了大约十二轮检查都没被发现，因为没有哪个检查专门找它。所以脚本和清单之外，最后还要有一遍从头读到尾的通读，最好出声读。
2. **版面检查（P56）。** 措辞全部定稿以后，在完整的编译结果上检查一次：各章起始页、每章最后一页的行数、有没有图表落在句子中间。用图表的位置解决，不改字。多出一页没关系。
