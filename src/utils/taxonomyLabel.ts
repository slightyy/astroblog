const CATEGORY_LABELS: Record<string, string> = {
  Documentation: "文档教程",
  Examples: "示例演示",
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

