# 上游来源与精选维护

## 来源

本仓库是公开 `PennixRv/pennix-skills-extra` fork，父仓库为 `mattpocock/skills`。本次审核和首发基线为 `49dd158d1076134a641b33efb035946536778336`；实施时上游 main 仍为该提交。保留完整 Git 历史和 MIT 许可，`upstream` remote 只用于 fetch 和人工审阅。

## 当前修订任务

任务为 `pennix-curation`，源码工作分支 `task/pennix-curation`，目标 `main`。它执行 `codex-workflow-optimization` 根任务 `matt-skills-pennix-lifecycle-plan` 已获用户明确批准的 revision 3 中列明的精选 fork 修改面；根侧记录负责跨仓库协调，本文件是本源码仓库的修订任务与上游维护自然落点，不建立第二任务运行时。

当前阶段为精选内容适配与静态验收。保留十项原位 Skill：`diagnosing-bugs`、`codebase-design`、`prototype`、`improve-codebase-architecture`、`retro`、`teach`、`loop-me`、`writing-fragments`、`writing-shape`、`wait-what`；已物理移除其他 28 个 Skill 目录。保留原名，七项仅显式调用，前三项沿默认发现策略。`writing-beats` 只将已核验分支差集融合进 `writing-shape/BEATS.md`，不保留独立入口。

静态验收已通过十项数量/名称/frontmatter、七项显式策略、逐目录来源及 MIT notice、22 条支持引用、根及桶索引、28 项排除、完整库分发入口清理和现有 Pennix 名称互斥；HITL 模板通过 Bash 语法检查及无敏感数据的输入夹具。复核修正了复现不可用时的残留硬性门槛、原型留存和复盘上下文压力臆断，保留当前项目原生协作合同。安装、双集合和宿主发现/触发验收由完整任务后续阶段执行，当前不声明全任务完成。

## 适配和验收边界

去除强制代理、第二 tracker/任务、自动知识写入、强制术语改名与无授权部署副作用；按现有 Pennix 路由、Grill、中文写作及项目 Trellis 原生入口协作。保留英文上游资产，仅作必要语义适配；新增 Pennix 专有说明使用简体中文。

每个可安装目录包含闭合支持文件、引用、来源和适用 MIT notice。清理完整库 plugin、installer 和发布清单的无效入口；不新增 npm/Plugin 发行，也不设置自动同步。唯一可执行白名单与安装 pin 在 Pennix lifecycle catalog，本文件的名单只是已批准修订记录。

静态结构/引用/元数据/许可审查先完成，再提交推送固定精选 SHA，由 Pennix catalog pin 后实施双集合和宿主发现/触发验收。验收证据不足不得声明完成。扩大接纳名单、owner、来源执行方式、公开行为或验收时回根任务决策，不在本 fork 静默扩大。

## 后续同步

仅在准备精选版本时 fetch 上游，按审核基线比较保留项、被融合方法来源及支持依赖，保留删减并逐处处理 modify/delete 冲突。上游新增或被移除项默认不接纳，不能因合并恢复至发布树。记录审阅基线、适配、验证和精选提交；精选推送、catalog pin 与设备升级是三个独立动作。

审核基线用于源码比较，不能作为精选集合的部署回退点。首发没有旧精选版本时，通过 lifecycle 原生卸载新集合并核验保留的 Pennix 集合；后续版本通过已审核旧精选 SHA 和原生 upgrade/verify 回退，不直接编辑安装副本。
