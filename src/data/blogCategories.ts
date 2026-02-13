export interface MainBlogCategory {
  key: string;
  label: string;
}

export const MAIN_BLOG_CATEGORIES: MainBlogCategory[] = [
  { key: "data-bi", label: "数据分析与 BI" },
  { key: "ai-agent", label: "AI 系统与智能体" },
  { key: "automation-workflow", label: "自动化与工作流" },
  { key: "frontend-ui", label: "前端与交互实现" },
  { key: "backend-data", label: "后端与数据工程" },
  { key: "project-review", label: "项目复盘" },
];
