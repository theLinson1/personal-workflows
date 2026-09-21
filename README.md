# Personal Workflows

把个人工作方法带到下一台电脑，在真实任务中继续改进。面向 Codex，也可直接让其他能读取 Markdown 的工具按需阅读。

这是 **v0.1 初始方法包**：已确认的个人意图、从既有材料提炼的候选方法，以及入职后接入项目 context 的入口。它不是对个人长期习惯的完整描述，也没有随身记的内部架构、协议或构建信息。

## 当前已知

- 你即将从事客户端工作，以 iOS 为主、兼顾 KMP，可能涉及硬件交互、软件维护和渐进改造。
- 你希望迁移的是自己的 skills 与思考、协作方法，能通过 GitHub 持续维护。
- 项目 context 需要入职后取得，现在不预填事实。

细节和来源见 [个人方法档案](profile/personal-method.md) 与 [提炼依据](docs/provenance.md)。岗位方向只用于提示以后查什么，不自动决定技术方案。

## 带走什么

| 层次 | 文件或目录 | 用途 |
|---|---|---|
| 个人意图与候选偏好 | `profile/personal-method.md` | 记录哪些是本人明确表达，哪些仍需通过实践验证 |
| 按需调用的方法 | `skills/` | 定义问题、比较方案、验证结果、沉淀经验、接入 context |
| 项目事实 | context 模板生成的项目内文件 | 入职后从代码、命令、团队约定中补齐，留在对应项目 |

项目 context 放在工作项目中；个人方法仓库只保留可跨项目使用的抽象。复制项目代码、协议、日志、凭据或整个聊天记录，不是这个包的安装步骤。

## 五个 skills

| Skill | 何时用 | 主要产物 |
|---|---|---|
| `frame-problem` | 任务模糊、方案先行、需要确定优先问题时 | 目标、约束、完成标准、最有价值的下一步 |
| `compare-options` | 技术选型、架构取舍、迁移路径有真实分歧时 | 依据、代价、反证、可逆性和建议 |
| `verify-delivery` | 检查修复或交付是否足以支撑“完成”时 | 已验证与未验证的证据、缺口和最小补救 |
| `capture-workflow` | 任务结束或你纠正 AI 后，希望保留经验时 | 归属判断、规则补丁、适用边界与验证记录 |
| `bootstrap-project-context` | 刚接手项目或项目事实已经变化时 | 有来源、有状态、可更新的项目 context |

前 3 个是从旧工作流提炼的方法草案。后 2 个是为“入职后接入并持续沉淀”新增的机制建议。它们都不是未经实践就宣称成熟的专家技能。不要每次把五个全跑一遍；简单任务直接完成。

## 在公司 Mac 上安装

需要 Python 3.10+，以及能访问该私有 GitHub 仓库的账号。先克隆这个仓库，或下载 ZIP 解压；进入含本文件的目录，再运行：

```bash
git clone https://github.com/theLinson1/personal-workflows.git
cd personal-workflows

# 预览将安装的 5 个 skills，不写文件
python3 scripts/install.py --dry-run

# 推荐：技能目录链接到这个仓库，之后 git pull 即可更新内容
python3 scripts/install.py --mode link
```

默认目标是 `~/.agents/skills`。源码仓库为 [theLinson1/personal-workflows](https://github.com/theLinson1/personal-workflows)，按用户选择设为私有。

Windows 或不希望创建链接的环境：

```powershell
python scripts/install.py --mode copy
```

按需安装，或者限制在一个项目中：

```bash
python3 scripts/install.py --only capture-workflow bootstrap-project-context
python3 scripts/install.py --dest /path/to/work-project/.agents/skills --mode link
```

安装器只安装所选 skill 文件夹，不修改全局配置、账号、权限或现有 `AGENTS.md`。相同内容会跳过；同名但不同内容会停止，供你先比较。默认自动发现，不需要改成“只可显式调用”。链接模式需要保留克隆目录；复制模式更新前需自行备份并移开旧目录，安装器不会覆盖它。

打开 Codex 的新任务，在技能选择器确认名称；若没有出现，重启 Codex。可先调用一个：

```text
$capture-workflow 从这次任务里提炼值得保留的方法。
区分我明确说过的偏好、你建议的方法、当前项目事实。
只做最小的 skill 改动，不把项目内容带入个人仓库。
```

也可以在目标电脑让 Codex 的 `$skill-installer` 从此 GitHub 仓库的 `skills/<名称>` 安装指定技能。选择一种安装方式，避免同一技能重复发现。[官方技能说明](https://learn.chatgpt.com/docs/build-skills)

## 第一次使用

安装 skills 不会自动加载 `profile/`。第一次需要个性化协作时，可以直接说：

```text
请读取这个仓库的 profile/personal-method.md。
已确认内容是我的背景和意图；候选方法可试用，不要当成我已确认的长期偏好。
这次先使用最相关的方法，任务结束后再记录哪些适合我。
```

若以后希望跨任务长期生效，可把**你已确认**的少量协作偏好合并到自己的 `AGENTS.md`。本包不自动合并；技能方法、稳定偏好和项目事实各自维护，避免把全部文档塞进每个任务。

## 入职后接入 context

在公司项目目录打开 Codex 后：

```text
$bootstrap-project-context 帮我建立当前项目的最小 context。
我以 iOS 为主、兼顾 KMP。先阅读现有 AGENTS.md、README、构建配置和相关代码。
只记录有来源的事实；没有看到的架构、硬件协议和迁移计划标为未知。
生成到当前项目已有的文档位置；没有约定时使用 docs/ai-context/。
```

只补当前任务需要的部分，不要求入职第一天画完全部架构。工具不可用时保留静态发现和下一条验证命令，不把“尚未运行”写成成功。

项目事实在项目侧更新。个人方法从真实任务中回流：

```text
$capture-workflow 这次我纠正了你：看到 KMP 需求后，不应立刻假定要迁移 UI。
请判断这是当前项目约束，还是可推广的方法；给出依据和最小修改。
```

这只是一个使用示例，不是关于公司迁移方案的已知事实。

## 维护与打包

```bash
# 在 clone 目录更新后，link 模式无需再次安装
git pull --ff-only

# 检查包内技能元数据与引用
python3 scripts/validate.py
```

原始经验先写在任务所在项目，只有不依赖内部事实的做法才整理回这个仓库。一次纠错可以形成局部规则，不必变成全局禁止项。每条新方法保留来源、适用范围、可能失效的条件和实际验证状态。

根目录 `plugin.json` 提供可分发的 Agent Plugin 标识，`.codex-plugin/plugin.json` 保留 Codex 兼容元数据。`skills/` 是两种安装方式共同使用的源；不含 MCP、hooks 或专用运行时。官方支持用插件打包多个技能。[插件打包说明](https://developers.openai.com/plugins/build/plugins)

本版通过私有 GitHub 仓库分发源码，未注册 marketplace，也未发布到公共插件目录。文件结构校验和临时目录安装验证不等于实际工作效果验证；Mac、iOS 工程及公司环境仍待实际使用检验。

## 当前本机已有 skills 如何处理

| 类型 | 处理建议 |
|---|---|
| 已有个人 `write-chinese-fiction` | 保留为文学写作专用，不能直接认定其中所有表达习惯适用于工程协作 |
| 试炼包的决策、证据、归纳流程 | 提炼为本包方法草案，移除测评关卡、倒计时与固定提交格式 |
| `skill-creator`、`skill-installer` | 使用目标 Codex 随附的版本来继续创作和安装 |
| 飞书、文档、浏览器、设计等插件 | 需要时在目标环境重新安装和授权；本包不复制插件缓存或登录状态 |

最值得继续投入的是 `capture-workflow`：让下一次真实任务比这一次更贴合你，而不是一次写很多看起来完整的技能。
