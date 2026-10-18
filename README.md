# pennix-skills-extra

这是 [mattpocock/skills](https://github.com/mattpocock/skills) 的公开精选 fork，面向现有 Pennix/Trellis 工作流补充方法。保留上游原名和主要结构；`collection.json` 是唯一交付清单，限定十项已审核 Skill 并声明路径和许可。来源、适配与同步规则见 [UPSTREAM.md](UPSTREAM.md)。

## 精选内容

| Skill | 用途 | 调用策略 |
| --- | --- | --- |
| [diagnosing-bugs](skills/engineering/diagnosing-bugs/SKILL.md) | 有界诊断、复现、假设、修复和回归验证 | 默认发现策略 |
| [codebase-design](skills/engineering/codebase-design/SKILL.md) | 深模块、接口、seam 和替代设计比较 | 默认发现策略 |
| [prototype](skills/engineering/prototype/SKILL.md) | 用逻辑或界面原型回答具体设计问题 | 默认发现策略 |
| [improve-codebase-architecture](skills/engineering/improve-codebase-architecture/SKILL.md) | 按已选范围提出有证据的架构改进候选 | 仅显式调用 |
| [retro](skills/engineering/retro/SKILL.md) | 依据实际会话与已有设施提出工作流改进候选 | 仅显式调用 |
| [teach](skills/productivity/teach/SKILL.md) | 在明确学习目录中组织课程、演示和测验 | 仅显式调用 |
| [wait-what](skills/productivity/wait-what/SKILL.md) | 保留事实和条件，重新解释前一回复 | 仅显式调用 |
| [loop-me](skills/in-progress/loop-me/SKILL.md) | 将工作流思路收敛为可执行规格 | 仅显式调用 |
| [writing-fragments](skills/in-progress/writing-fragments/SKILL.md) | 围绕写作目标收集并保真记录素材 | 仅显式调用 |
| [writing-shape](skills/in-progress/writing-shape/SKILL.md) | 将只读素材形成文章，可选择分支模式 | 仅显式调用 |

桶路径沿用上游组织方式；本 fork 的接纳和调用策略以上表及实际元数据为准。`writing-beats` 的差异方法并入 `writing-shape/BEATS.md`，其余已融合或未接纳项均没有独立 Skill 入口。

## 安装与升级

通过已安装的 `pennix-component-lifecycle` 管理集合。工具固定本仓库提交，读取并独立验证 `collection.json`，再将所列内容安装到独立目录，并共同管理集合、receipt 和命令链接。本仓库不维护安装器或生命周期组件动作。

系统安装不会初始化项目。重要选择、规划授权、项目任务与验收、工具路由、中文写作和知识管理继续遵守既有 Pennix/Trellis 原生入口；本集合补充方法。

## 维护与许可

先人工比较上游差异和被融合方法来源，处理删减冲突并验证，再推送精选提交、更新 lifecycle pin 和升级设备。上游新增项须单独决策，不能因同步自动接纳。每个安装目录保留完整 MIT notice 和维护用 `UPSTREAM.md`。

`docs/`、`.agents/`、`CHANGELOG.md` 和既有 changeset 条目保留上游历史说明，当前方法以十项 `SKILL.md` 及其引用为准；本 fork 使用固定提交分发，已移除完整库 plugin、开发链接 installer 和 npm 发行入口。
