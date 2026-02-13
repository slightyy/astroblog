const CATEGORY_LABELS: Record<string, string> = {
  Documentation: "文档教程",
  Examples: "示例演示",
  "data-bi": "数据分析与 BI",
  "ai-agent": "AI 系统与智能体",
  "automation-workflow": "自动化与工作流",
  "frontend-ui": "前端与交互实现",
  "backend-data": "后端与数据工程",
  "project-review": "项目复盘",
};

const TAG_LABELS: Record<string, string> = {
  Makrdown: "Markdown",
  Markdown: "Markdown",
  Mathematics: "数学",
  Comments: "评论",
  Blog: "博客",
  Project: "项目",
  Frosti: "Frosti",
  Waline: "Waline",
  Astro: "Astro",
  LaTeX: "LaTeX",
};

export function getCategoryLabel(category: string): string {
  return CATEGORY_LABELS[category] || category;
}

export function getTagLabel(tag: string): string {
  return TAG_LABELS[tag] || tag;
}
