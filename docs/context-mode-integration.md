# Context Mode 集合接入

落实根任务 `codex-workflow-optimization/10-18-context-mode-fastctx-replacement` 的已批准范围：retro 活动引用替代；审核并提交现有 collection manifest、验证器及 CI 草稿，使远端固定提交能独立物化集合。README 与 CLAUDE.md 的既有差异保留，不纳入本次提交。

正式远端制品验收发现根 `AGENTS.md` 符号链接触发 lifecycle 的安全归档拒绝。该入口不在交付 manifest 内，现用 `.gitattributes` 的 `export-ignore` 排除；源码检出仍保留宿主入口，受管 Skill、许可和支持引用均照常交付。消费者继续拒绝链接，不放宽提取规则。须从远端固定提交的真实归档复验。
