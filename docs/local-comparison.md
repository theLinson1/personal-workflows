# Windows handoff 与本地 skills 对照

对照日期：2026-09-22。目的：把已有思考与协作方法带到新电脑，接入真实项目后继续改进。

Windows 初版已经覆盖“定义问题、比较方案、核验交付、沉淀经验、接入项目 context”。本地最有价值的补充是：需求未知项的分级与阻塞范围、可证伪的故障诊断、最终修改后的验证、历史决策的使用方式，以及独立的学习设计能力。

本次采用 **core 6 / all 7**：保留并增强原有五个入口，新增 `debug-with-evidence`；完整保留 `layered-learning-design` 作为可选的第七个入口。相近能力合并，避免多个 skill 同时重复澄清、审批或核验。

## 阅读范围与证据边界

实际扫描到的个人或手动安装 skills 共 **15 个**：

- `~/.codex/skills/` 顶层 10 个。
- `~/.agents/skills/officecli` 1 个。
- `~/.codex/superpowers-lean/skills/` 4 个。

这些路径只说明本次对照的来源，不是安装后的运行依赖。新电脑不需要保留源电脑的目录布局。

已阅读 Windows 包的 5 个 `SKILL.md`、README、profile、provenance、validation、context 与经验卡模板、客户端观察点。对本地通用方法读取正文及相关模板；对资讯、写作、图像、Office 等专业技能读取 `SKILL.md` 中的用途、触发与依赖说明；对 `layered-learning-design` 检查了全部 12 个内容文件和内部引用。

下表的“源文件实际能力”来自所读文件；“本包处理”是本次整合选择。安装了某个 skill，不等于用户逐条确认了其中的规则，也不能据此把它写成稳定个人偏好。本次没有运行资讯推送、图像生成、Office 安装或外部课程练习。

## 全部 15 个 skills 的处理

| 本地 skill | 源文件实际能力 | 与 Windows 初版的关系 | 本包处理与依赖边界 |
|---|---|---|---|
| `requirements-closure` | 区分问题可探索、规格可规划、实施可开始；P0/P1/P2 未知分级；假设依据、风险与验证；客户端行为、回退、实验等检查 | 与 `frame-problem` 重合，细化了未知项的后续处置 | 融入 `frame-problem`。保留“阻塞哪个步骤”与高影响未知不擅自定案；不照搬固定全表、重复审批和对外部 `writing-plans` 的依赖 |
| `grill-me` | 沿决策依赖逐层深挖；一次一个问题；给出推荐答案；代码可回答的问题先查代码 | 与 `compare-options` 互补，是更深入的交互模式 | 融入 `compare-options` 的可选深挖模式。用户需要压力测试或深入访谈时使用；能力保留，不再增加同义入口，也不让每次任务都无限追问 |
| `project-memory` | 项目事实、ADR、已知故障和工作记录；修改前查历史决定；修订决定时说明原因与日期 | 与 `bootstrap-project-context` 和 `capture-workflow` 部分重合；补充持续维护 | 采纳“先读再改”和分流规则，优先使用项目已有文档。不强制创建四个空文件，不自动改写 `CLAUDE.md` / `AGENTS.md`；只记录非敏感配置和凭据的安全存储位置 |
| `layered-learning-design` | 能力变化、入口状态、阻塞差距、最小增量、练习、反馈、迁移；课程设计与审计；可选交互学习合约 | 独有能力，五个通用入口不能替代 | 完整保留为 all 的第七个 skill，包含模板、领域适配和例子。交互教学等待只作用于已选择的学习模式，不阻塞普通工程交付 |
| `aihot` | 从公开 API 查询 AI 资讯、精选与日报，区分时间窗与分类 | 与工程方法包用途不同 | 暂不迁入。使用时依赖网络与公开服务；原文示例使用 `curl`、`jq`，API 调用有 User-Agent 要求。需要时从其来源单独安装 |
| `follow-builders` | 获取 AI builders 公开聚合内容，生成摘要；支持可选定时与外部发送 | 与工程方法包用途不同 | 暂不迁入。依赖公开 feed、随包脚本与配置；定时能力取决于目标平台，Telegram / 邮件发送另有凭据。原文的初始化与定时规则不构成本次创建自动化或发送消息的授权 |
| `gpt-image-2-style-library` | 用风格库与案例编写图像提示词 | 与工程方法包用途不同 | 暂不迁入。需要其 `references/style-library.md`；素材与生成维护脚本属于源库。它提供提示词方法，不自带图像生成运行时 |
| `hatch-pet` | 制作、修复、验证并打包 Codex v2 动画宠物，含完整视觉 QA | 与工程方法包用途不同 | 暂不迁入。依赖 `$imagegen`、Codex 工具、带 Pillow 的工作区 Python、随包脚本和资源；不能只拷一个 `SKILL.md` 就视为可用 |
| `khazix-writer` | 公众号长文的选题、协作、风格与质检方法 | 与工程方法包用途不同 | 暂不迁入。需要其写作参考资料；专用文风和完整质检输出不扩展为日常工程沟通偏好 |
| `qu-ai-wei` | 简体中文改写；保留原文事实与语体；识别 AI 腔；附打磨报告 | 与工程方法包用途不同 | 暂不迁入。依赖其白名单等参考资源；文本编辑规则和报告要求只适用于相应写作任务，不添加到工程交付默认输出 |
| `officecli` | 通过 CLI 创建、读取、修改与校验 Word、Excel、PowerPoint；按格式加载专用规则 | 与工程方法包用途不同 | 暂不迁入。目标电脑需要 `officecli` 二进制，专业场景规则由 `officecli load_skill` 提供；拷贝本文件不等于已安装工具。本次未执行其安装命令 |
| `brainstorming`（lean） | 先查 context，识别会影响实施的未知；推荐方案优先；真实备选最多两个；按风险描述设计 | 与 `frame-problem` / `compare-options` 高度重合 | 融入现有入口，保留按任务大小工作、复用已确认决定；不另增发现阶段，也不在已有授权后重开固定审批 |
| `systematic-debugging`（lean） | 精确症状与环境；单个可证伪根因假设；最小诊断；两次修复失败后回到证据 | 现包只有验证，没有完整诊断流程 | 转化为新增 `debug-with-evidence`。诊断负责找原因，`verify-delivery` 负责修复后的完成证据；不强制所有小修复先写自动化测试 |
| `using-git-worktrees`（lean） | 判断隔离收益；检查仓库与用户修改；沿用目录约定；建立相关基线；避免重复 worktree | 独有的执行隔离规则，可服务于方案实施 | 放入 `compare-options` 的 isolation reference，按隔离需求读取。保留实质规则而不重复入口；小修改不自动创建，提交、合并和清理仍以任务授权为准 |
| `verification-before-completion`（lean） | 最终修改后执行相关检查；读取退出状态、输出与警告；不把旧结果或代理报告当作更强主张的证据 | 与 `verify-delivery` 高度重合 | 融入 `verify-delivery`，突出验证的新鲜度与证据范围，不再安装第二个重复入口 |

“暂不迁入”表示当前入职方法包不包含该专业用途，并非删除或否定原有 skill；它们仍可按任务单独安装和使用。

## 五个原入口保留什么、补什么

| 原入口 | 保留的已有设计 | 从本地补入的关键规则 |
|---|---|---|
| `frame-problem` | 目标、约束、完成证据；按规模输出；不制造“唯一关键矛盾” | 未知项按影响和阻塞步骤分级；能探索不等于能实施；可暂定项需要依据和验证，可延期项需要解决时点 |
| `compare-options` | 真正不同的路径、代价、可逆性、改变结论的证据；不凑方案数 | 可选深挖沿决策依赖展开；先从代码取答案；实施需要隔离时再读取 worktree 规则 |
| `verify-delivery` | 每个完成主张匹配直接证据；真机、模拟器与静态阅读的边界；不过度验证 | 最终修改后更新证据；完整读取相关检查结果；早前成功或他人结论不能证明当前产物 |
| `bootstrap-project-context` | 记录来源、版本、状态和失效条件；项目事实留在项目里 | 先查历史 ADR 和已知问题；发现冲突时说明依据；事实、决定、故障和工作记录按项目约定保存 |
| `capture-workflow` | 区分用户确认、实践支持的候选、AI 建议；一次纠正不变全局禁令；最小补丁 | 保持规则间关系清楚，记录适用与不适用场景；本地文件存在只作为来源证据，不升级为用户偏好 |

`capture-workflow` 在本地通用方法中没有完整的直接替代品。它负责把经历转成可复用规则，值得继续保留。把“旧方法什么时候失效”写清，是本次整合建议；不能反过来说用户过去已经这样做。

## core 6 与 all 7 的使用边界

| 安装范围 | 入口 | 用途 |
|---|---|---|
| core | `frame-problem`、`compare-options`、`debug-with-evidence`、`verify-delivery`、`capture-workflow`、`bootstrap-project-context` | 接手项目、澄清任务、做决定、排查故障、验证和沉淀 |
| all | core 加 `layered-learning-design` | 另有课程、学习练习、教学材料审计或交互学习的需要 |

不是每个任务顺序运行六个技能。清楚的小改动可以直接做；故障先诊断；架构取舍才比较；学习目标才使用学习适配。深挖访谈和 worktree 隔离是按需能力，不是第八、第九个重复入口。

## 避免继承的触发冲突

- **重复澄清与审批：** requirements-closure 原文有两次阶段确认和固定完整报告，lean brainstorming 也有实施前批准。保留实质未知与决策边界，已有授权和已确认设计继续有效。
- **多个项目真相源：** bootstrap 不再旁建一套与现有 ADR、context、runbook 冲突的文档；项目记忆按已有位置增量维护。
- **凭据措辞冲突：** project-memory 主文有 “credentials” 的含混例句，但其 key-facts 模板明确禁止密码、API key 和敏感凭据。迁移采用后者边界，只记录非敏感事实与安全存储位置。
- **学习门槛扩散：** layered-learning 的 `wait / advance / repair`、明确卡住才给提示和 artifact gate，只属于对应交互学习合约，不成为代码修复或交付任务的默认暂停规则。
- **源文档被当作当前指令：** 本次读取的安装、推送、定时、生成等命令均为待分析材料。打包不等于执行这些操作，也不携带来源电脑的账号或授权。

## 学习 skill 的可移植性检查

检查范围是 `layered-learning-design` 的 12 个内容文件：`SKILL.md`、`agents/openai.yaml`、3 个 assets、7 个 references。内部显式引用的 assets / references 均存在；未发现源电脑用户名绝对路径、公司内部案例或外部 `skill://` 资源依赖。源目录还包含 `.git`，它属于安装来源的仓库元数据，不能作为 skill 内容复制。

两份例子引用了未随 skill 提供的外部课程文件，需要明确标为来源示例：

| 文件 | 未打包的外部示例 | 使用边界 |
|---|---|---|
| `references/engineering-incremental-course-example.md` | `learn-claude-code` 中的 `s06_subagent/code.py`、`s07_skill_loading/code.py` | 可读取已抽象的教学结构；要实际执行示例，需另行取得并确认相应课程版本 |
| `references/rag-lesson-08-query-transformation-example.md` | `projects/agent-lab/` 的脚本、fixture、报告，以及 `lessons/08-query-transformation/` | 目录和排名结果是历史教学示例；不能声称当前项目存在这些文件或本次复现了其结果 |

完整带入表示保留全部学习规则、模板和参考文档，不表示附带两套课程源码。例子需要来源边界说明，不能为了让路径“存在”而生成未经验证的替代代码。教学方法自身不依赖这些外部课程才能使用；具体练习需要的工具与工程环境由学习任务决定。

## 系统和插件作为运行环境处理

系统技能如 `skill-creator`、`skill-installer`、`plugin-creator`、`openai-docs`、`imagegen`，以及浏览器、Chrome、Data、文档、PDF、演示文稿、表格、Product Design、Sites、可视化等插件，属于目标工具环境。它们不计入上面的 15 个个人或手动安装 skills，也不复制缓存目录。

方法包的 Markdown 可单独读取；某个实际任务需要浏览器、办公文档、图像生成或外部应用时，再检查目标环境的工具与授权。复制 skill 不会迁移登录状态、插件可用性、模型权限或企业项目访问权限。

## 本次结论的验证范围

本对照证明已检查源文件及方法差异，不证明新电脑上的工程、硬件和教学任务已经运行成功。包结构与安装验证见 [验证记录](validation.md)，来源与整合记录见 [提炼来源](provenance.md)。后续应从真实任务记录哪些规则有效、哪些触发过宽，再做最小修订。
