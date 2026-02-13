# astroblog

一个基于 Astro + Frosti 定制的个人静态博客项目。  
仓库地址：`https://github.com/slightyy/astroblog`

## 项目简介

本项目用于个人博客与项目展示，当前已包含：

- 文章系统（Markdown / MDX）
- 分类、标签、归档、搜索
- 项目页面（项目经历、进行中项目等）
- 响应式布局与明暗主题
- GitHub 静态托管 + Vercel 部署

## 技术栈

- `Astro`
- `Tailwind CSS`
- `daisyUI`
- `Pagefind`（站内搜索）
- `MDX`

## 本地开发

### 1. 安装依赖

```bash
npm install
```

### 2. 生成搜索索引（首次或文章更新后建议执行）

```bash
npm run search:index
```

### 3. 启动开发环境

```bash
npm run dev
```

默认访问：`http://localhost:4321`

## 常用命令

```bash
# 开发
npm run dev

# 构建
npm run build

# 预览构建结果
npm run preview

# 清理搜索相关产物
npm run search:clean

# 重新生成搜索索引
npm run search:index
```

## 目录说明

```text
src/
  content/
    blog/                 # 博客文章（.md/.mdx）
  pages/
    blog/                 # 文章列表、分类、标签、搜索等页面
    project.astro         # 项目总览页
    project/              # 各项目详情页（可继续新增）
  components/             # 组件
frosti.config.yaml        # 站点配置（菜单、社交链接、主题等）
public/                   # 静态资源
```

## 如何写新文章

请在 `src/content/blog` 下新建 `.md` 或 `.mdx` 文件。

示例 Frontmatter：

```yaml
---
title: 文章标题
description: 文章描述
pubDate: 2026-02-13
updated: 2026-02-13
draft: false
categories:
  - project-review
tags:
  - Astro
  - Blog
---
```

说明：

- `draft: true` 时文章不会在正式环境列表中显示
- `categories` 和 `tags` 用于分类页和标签页聚合
- 使用 MDX 时可在文内直接 `import` 组件

## 搜索功能说明

本项目搜索依赖 Pagefind 索引。若页面提示搜索失败，请执行：

```bash
npm run search:index
```

然后刷新页面即可。

## 部署说明（GitHub + Vercel）

你当前是本地写作后推送仓库的方式，推荐流程：

1. 本地完成内容更新
2. 执行 `npm run build`（可选但建议）
3. `git add . && git commit -m "update blog" && git push`
4. Vercel 自动拉取并部署

如果你改动了大量文章，部署前可先执行一次 `npm run search:index` 做本地验证。

## 个性化配置

站点主要配置文件为 `frosti.config.yaml`，可修改：

- 站点标题、描述、语言、主题
- 顶部/侧边菜单
- 个人信息与社交链接
- 首页与页脚展示内容

## 许可证

项目沿用仓库中的 `LICENSE`。

