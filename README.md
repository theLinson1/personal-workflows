# Personal Workflows

把已有的思考与协作方法带到下一台电脑，在真实工作中继续改进。

**v0.2：已将 Windows 初始包与本地 15 个手动安装的 skills 对比整合。** 保留原来的五个入口，补入需求分级、方案访谈、隔离基线、项目记忆与新鲜验证；新增排障入口，完整带入可选学习设计。它们是可复用的方法，不代表已经在目标公司的工程里验证过。

明天直接从 [HANDOFF.md](HANDOFF.md) 开始。完整对照见 [本地 skills 对比](docs/local-comparison.md)，来源和适配边界见 [provenance](docs/provenance.md)，实际检查见 [validation](docs/validation.md)。

## 包含哪些能力

| 安装组 | Skill | 何时使用 |
|---|---|---|
| core | `bootstrap-project-context` | 接手项目或更新事实；读取已有文档、历史决策和已知问题 |
| core | `frame-problem` | 需求含糊；分清目标、约束，以及未知阻塞哪个决定 |
| core | `compare-options` | 有实际取舍的技术选型、迁移路线；可选深度访谈和隔离实验 |
| core | `debug-with-evidence` | 非预期行为；用可证伪假设和最小诊断定位原因 |
| core | `verify-delivery` | 交付核验；用最后相关修改后的直接证据支持完成声明 |
| core | `capture-workflow` | 从任务或纠正中提炼方法，收窄或替换旧规则 |
| all 额外包含 | `layered-learning-design` | 设计/审计课程与练习，以实践、反馈和迁移证据判断掌握 |

按当前任务选最相关入口，不要求每次按顺序跑一遍。学习设计有独立触发范围；请求直接修复代码时不会因此变成教学问答。

## 安装

需要 Python 3.9+（本次在 3.9.6 验证）。克隆私有仓库需要有访问权限；也可以使用完整 ZIP 解压目录。进入含本文件的目录：

```bash
git clone https://github.com/theLinson1/personal-workflows.git
cd personal-workflows
python3 scripts/validate.py

# 默认 core：六个工程 skills；预览不写文件
python3 scripts/install.py --dry-run

# Mac/Linux：链接到当前仓库，后续 git pull 更新
python3 scripts/install.py --profile core --mode link
```

Windows 或不使用链接的环境：

```powershell
python scripts/validate.py
python scripts/install.py --profile core --mode copy
```

要包含学习设计，或只选择部分能力：

```bash
python3 scripts/install.py --profile all --mode link
python3 scripts/install.py --only layered-learning-design --mode link
python3 scripts/install.py --only capture-workflow bootstrap-project-context --mode link
```

`--profile` 与 `--only` 二选一。默认目录为 `~/.agents/skills`；项目内安装可用 `--dest /path/to/work-project/.agents/skills`。插件安装会发现全部七个 skills，`core/all` 仅是本安装器的分组。

安装器不改账号、权限、全局配置或 `AGENTS.md`。同内容跳过，同名不同内容会在开始安装前拒绝覆盖。链接安装需要保留源码目录；复制安装更新时先比较并备份旧目录，移开后再安装。这里不自动修改当前电脑已经安装的任何 skill。

重新打开 Codex 任务，确认技能选择器可见。已有同名或同用途的本地 skills 时，先参考 [对照表](docs/local-comparison.md) 选择一套，避免 `requirements-closure`、`brainstorming`、`verification-before-completion` 与本包重复引导。同名冲突会被安装器发现，**不同名称但功能重叠不会被自动检测**。

## 工作方法和项目事实

| 内容 | 维护位置 |
|---|---|
| 本人明确表达的背景与意图、候选方法 | [个人方法档案](profile/personal-method.md) |
| 可重复使用的判断与步骤 | 本仓库 `skills/` |
| 代码、构建、协议、架构、历史决策、问题记录 | 工作项目已有文档；没有约定时再建立最小 context |

安装不会自动加载 `profile/`。希望 Codex 了解方法来源时，可让它读取档案；只把已确认内容视为本人偏好，不能从已安装某个 skill 推断我认同其中所有规则。

本仓库只保存能脱离项目独立成立的方法。公司代码、录音、转写、日志、内部接口和凭据留在批准的工作环境；整个聊天历史、插件缓存和登录状态不是迁移内容。

## 接手项目与持续复用

```text
$bootstrap-project-context 帮我建立当前项目的最小 context。
先阅读现有 AGENTS.md、README、构建配置及与当前任务相关的历史决定。
我以 iOS 为主、兼顾 KMP；只记录有来源的事实，未知保持未知。
优先补现有文档，没有约定再使用 docs/ai-context/。
```

项目资料未到手时，输出待查入口即可，不推断具体架构。缺少 Xcode、真机或公司服务时，保留静态发现与下一条验证动作。

```text
$capture-workflow 这次我纠正了你：不要把 KMP 业务逻辑共享自动扩展为 UI 迁移。
请判断这是项目约束还是可推广的方法，更新对应位置，说明替代了哪条旧规则。
```

上面是使用示例，不是关于目标公司路线的事实。更完整的第一天使用方式见 [HANDOFF.md](HANDOFF.md)。

## 维护和校验

```bash
git pull --ff-only
python3 scripts/validate.py
python3 -m unittest discover -s scripts -v
```

校验和安装测试只需 Python 标准库。安装测试全部在临时目录运行，不会修改本机已安装的 skills。结构、隔离安装和场景推演的结论各自记录，不能代替真实工程效果。

`plugin.json` 和 `.codex-plugin/plugin.json` 保留现有分发元数据，版本同步为 0.2.0。本包没有注册 marketplace，不复制 Codex 自带技能或第三方插件运行时；需要浏览器、文档、图像等能力时，在新环境正常安装对应工具。
