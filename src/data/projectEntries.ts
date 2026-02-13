export type ProjectCategory = "participated" | "ongoing";

export interface ProjectEntry {
  slug: string;
  title: string;
  summary: string;
  category: ProjectCategory;
}

export const projectEntries: ProjectEntry[] = [
  {
    slug: "truck-bi-dashboard",
    title: "某卡车企业的 BI 面板搭建",
    summary: "业务指标看板设计与可视化落地，支持管理层日常决策查看。",
    category: "participated",
  },
  {
    slug: "education-panel-and-database",
    title: "某教育机构的前端面板和后端数据库搭建",
    summary: "完成前端展示面板与后端数据模型搭建，支持运营数据统一管理。",
    category: "participated",
  },
  {
    slug: "data-collection-automation",
    title: "数据采集自动化流程搭建",
    summary: "将重复采集流程自动化，提升数据入库效率并降低人工操作成本。",
    category: "participated",
  },
  {
    slug: "modao-ui-end-to-end",
    title: "墨刀设计 UI 搭建全流程",
    summary: "从原型到交互到页面规范输出，形成可交付的 UI 设计流程。",
    category: "participated",
  },
  {
    slug: "literature-review-ai-system",
    title: "文献综述 AI 构建系统",
    summary: "构建文献收集、摘要提取、主题归纳的一体化智能辅助流程。",
    category: "ongoing",
  },
  {
    slug: "mcp-skills-bi-automation",
    title: "基于 MCP 和 Skills 的自动化 BI 分析系统",
    summary: "将工具链与分析流程模块化，探索可复用的自动化 BI 方案。",
    category: "ongoing",
  },
  {
    slug: "desktop-open-agent-hardware",
    title: "桌面开源智能体硬件",
    summary: "探索软硬件协同的本地智能体形态与持续运行能力。",
    category: "ongoing",
  },
  {
    slug: "skills-data-cleaning-system",
    title: "Skills 的数据清洗系统构建",
    summary: "围绕数据标准化、缺失处理和质量校验搭建清洗能力。",
    category: "ongoing",
  },
];

export const participatedProjects = projectEntries.filter(
  (project) => project.category === "participated",
);

export const ongoingProjects = projectEntries.filter(
  (project) => project.category === "ongoing",
);
