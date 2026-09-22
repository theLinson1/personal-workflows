# 提炼来源与边界

本包没有扫描完整聊天历史，也没有推断人格或声称掌握完整个人思维模型。

## v0.1 的历史提炼记录（2026-09-21）

下面保留 Windows 初版对其来源的描述；这些旧工作区未在本次 Mac 整合中重新读取。v0.2 的新增依据在后文单独列出。

| 来源 | 实际发现 | 本包如何处理 |
|---|---|---|
| 本次用户对话 | iOS 为主、兼顾 KMP；迁移个人方法；context 入职后取得 | 记录为明确背景与意图 |
| 工作区 `anker-ai-pilot` | 问题定义、取舍、验证、归纳，也包含测评人工关卡 | 提炼方法；不继承测评专用暂停、倒计时、固定轮次 |
| 工作区 `business-decision-analysis` | 从决策出发，比较方案，检查反证 | 形成 `frame-problem` 与 `compare-options` 草案 |
| 工作区 `evidence-validator` | 定义口径、检查证据与限制 | 提炼 `verify-delivery`；没有移植数据分析专属检查全集 |
| 工作区 `executive-synthesis` | 主张、证据、行动和限制保持一致 | 纳入交付结论与验证输出 |
| 个人 `write-chinese-fiction` | 领域明确；区分来源原则与操作化扩展 | 保留来源区分方法，不将文学写作规则扩大为工程偏好 |
| 本轮设计建议 | 入职后采集 context，任务后增量沉淀 | 新增 `bootstrap-project-context` 与 `capture-workflow`，待实践验证 |

旧材料存在于工作区，只能证明曾有这些工作流文件；不能证明用户逐条认可或已经在工作中验证。来源名称用于追溯，本包不要求新电脑存在这些原始文件。

## 变更判断

当一个真实任务产生经验，先判断落点：

- 当前任务的参数：留在该任务记录。
- 当前项目的事实或约定：写入项目 context。
- 已明确的稳定个人偏好：更新个人档案，按需要人工合并到个人 `AGENTS.md`。
- 可重复的方法和判断边界：更新对应 skill。
- 未经验证的设想：记录为候选，不宣称已经沉淀。

“掌握某个概念”不必立刻创建 skill。只有它改变了下一次任务的判断、执行或验证方式，才值得写进技能。

## v0.2 的实际对照与整合（2026-09-22）

用户要求先比较 GitHub handoff 与本地 skills，再基于本地方法补全可供下一台电脑复用的包。对照基线是仓库提交 `ba858dbee988c96c6bbbc41746fa740ca1590301`；逐项结果见 [本地对照表](local-comparison.md)。

实际读取 15 个本地手动安装 skill 的入口：个人目录 10 个、Office CLI 1 个、精简 superpowers 4 个；通用方法与学习设计按需追读支持资源。系统与托管插件不作为个人方法复制。

| 来源 | 迁入位置 | 保留与改写 |
|---|---|---|
| requirements-closure | frame-problem 的分级参考 | 保留 P0/P1/P2、阻塞阶段、假设验证；不保留固定全表和重复阶段审批 |
| brainstorming（lean）与 grill-me | compare-options 与访谈参考 | 保留先找已有答案、真实取舍、依赖顺序；深挖只在对应请求下使用 |
| using-git-worktrees（lean） | compare-options 的隔离参考 | 保留按收益隔离、用户修改、基线、避免重复创建，不设默认隔离仪式 |
| systematic-debugging（lean） | debug-with-evidence | 保留可证伪假设、最小诊断、两次失败返回证据及诊断/修复授权边界 |
| verification-before-completion（lean） | verify-delivery | 补入最后相关修改之后重新检查、读取退出状态与证据范围 |
| project-memory | bootstrap-project-context 与记忆参考 | 保留分类、历史决定和问题复用；避免重复档案、自动指令改写与含混凭据记录 |
| layered-learning-design | 同名独立 skill，全部 12 个内容文件 | 保留学习流程、模板和参考；规范描述行、收窄工程任务误触发；两份外部课程例子添加未打包/未复验说明 |
| 本次整合判断 | capture-workflow、客户端观察点、安装分组 | 新增规则替代关系和正反例；语音/云链路是可选调查点；core/all 是打包选择，不宣称是用户长期偏好 |

源文件指纹见 [local-source-snapshot.json](local-source-snapshot.json)。它记录源入口和完整学习资源的 SHA-256，使用可移植目录别名，没有源机用户名路径。指纹用于日后发现来源变化，不是验证方法效果或用户认可的证据。

完整学习包的原始来源为用户的 [layered-learning-design 仓库](https://github.com/theLinson1/layered-learning-design)，本次以本机实际文件为整合输入，未假定它与远端最新提交完全相同。源目录的 `.git` 不随 skill 带走。外部课程目录和旧报告仅作为历史例子，没有搬入或冒充当前工程资源。

资讯、写作、图像、宠物、Office 工具等不同用途保留在来源环境，不纳入默认工程包。详细依赖和去向在对照表逐项说明；没有删除或修改任何源 skill。

本次新增安装测试与场景推演只支持各自覆盖的结论。目标公司内部工程、账号、设备与平台行为仍待入职后通过项目证据确认，不从岗位名称或面试描述推导实现事实。
