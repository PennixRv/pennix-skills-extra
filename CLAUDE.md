# 精选 fork 维护规则

本仓库沿用 `skills/engineering/`、`skills/productivity/`、`skills/in-progress/` 的上游路径，只保留根 [README.md](README.md) 所列十项。当前修订任务、审核基线和同步方式见 [UPSTREAM.md](UPSTREAM.md)；本文件也通过 `AGENTS.md` 提供给宿主。

- 编辑前读取当前入口及实际引用，保持上游主要方法和格式，只做与已批准 Pennix/Trellis 合同协作所需的适配。
- 新增自定义说明使用简体中文，已有英文内容不追溯翻译。正式名称、源码标识和业务含义保持准确。
- 重要用户选择、任务与实施授权、工具路由、中文写作和知识落点使用现有 Pennix/Trellis 入口；不新增第二套 tracker、强制代理或自动知识写入。
- 每个安装目录自足，包含闭合的支持引用、完整 MIT `LICENSE` 和维护用 `UPSTREAM.md`。来源 SHA、审核过程和许可说明放在维护记录，执行正文保留适用条件与方法。
- 七项显式 Skill 同时保留 `disable-model-invocation: true` 和 `agents/openai.yaml` 的 `policy.allow_implicit_invocation: false`；前三项沿默认策略。根及各桶 README 链接实际保留入口。
- 唯一可执行接纳清单和固定提交由 Pennix lifecycle catalog 管理。不要提供 plugin、全目录链接、npm 或自动同步发行路径。
- 同步只 fetch 上游并人工审阅；保留删除，处理 modify/delete 冲突，检查支持依赖和被融合方法来源。新增项、扩大范围或实质新选择回根协调任务决策。
- `docs/`、`.agents/`、`CHANGELOG.md` 和既有 changeset 为上游历史资产；它们不是当前精选工作流规则，也不参与安装。当前规则从本文件、根维护记录、保留 Skill 和实际宿主合同读取。

提交前核对十项数量、名称及调用策略、支持引用、来源和许可，运行相关验证与 `git diff --check`。推送精选提交之后，才由 Pennix catalog 固定该 SHA 并实施设备部署；未经验证不声明完成。
