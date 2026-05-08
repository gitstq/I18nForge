# I18nForge

🎉 **README多语言智能生成器** | Markdown-aware README translation tool with format preservation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/gitstq/I18nForge)](https://github.com/gitstq/I18nForge/stargazers)

[简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | **English** | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md)

---

## 🎉 项目介绍

**I18nForge** 是一款专为GitHub README设计的**多语言智能生成器**。它能够智能识别Markdown格式，保留表情符号、代码块、链接等特殊元素，同时将内容翻译成多种语言。

### ✨ 解决的问题

- 📝 手动翻译README费时费力
- 🎨 翻译后格式错乱，表情符号丢失
- 🔗 链接、代码块被误翻译
- 🌐 需要多语言版本但没有好工具

### 🚀 自研差异化亮点

1. **Markdown感知解析** - 智能识别标题、列表、代码块、表格
2. **格式100%保留** - 表情符号、Markdown语法、代码块完整保留
3. **零依赖设计** - 纯Python标准库，无外部依赖
4. **多翻译引擎** - 支持Google、DeepL、OpenAI等多种翻译服务
5. **语言自动切换** - 生成语言切换器，方便用户切换语言

## ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🎨 **Markdown感知** | 智能解析Markdown结构，区分可翻译内容和格式元素 |
| 😊 **表情保留** | 100%保留表情符号，不丢失任何视觉元素 |
| 💻 **代码块保护** | 代码块内容不会被翻译，保持原始代码 |
| 🔗 **链接智能** | 链接和图片不会被误翻译 |
| 📊 **表格支持** | 完整支持Markdown表格翻译 |
| 🌐 **多语言切换** | 自动生成语言切换器，多语言版本一键切换 |
| ⚡ **零依赖** | 纯Python标准库实现，无需安装额外包 |
| 🔧 **多引擎** | 支持Mock、Google、DeepL、OpenAI等多种翻译引擎 |
| 💾 **智能缓存** | 翻译结果本地缓存，避免重复翻译 |
| 🎯 **增量翻译** | 只翻译新增或修改的内容，节省时间和成本 |

## 🚀 快速开始

### 📋 环境要求

- Python 3.8+
- 无需其他依赖（零依赖设计）

### 💾 安装步骤

**方式一：pip安装**

```bash
pip install i18nforge
```

**方式二：从源码安装**

```bash
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge
pip install -e .
```

### 📖 基本使用

**翻译现有README**

```bash
# 翻译为英文
i18nforge translate README.md -t en

# 翻译为多种语言
i18nforge translate README.md -t en,ja,ko

# 使用指定翻译引擎
i18nforge translate README.md -t en --engine google
```

**生成README模板**

```bash
i18nforge generate -n MyProject -d "这是一个很棒的项目" -f "轻量级" -f "易于使用"
```

### ⚙️ 命令行选项

```
用法: i18nforge [命令] [选项]

命令:
  translate     翻译README文件
  generate      生成README模板
  languages     显示支持的语言列表

选项:
  -t, --target        目标语言（逗号分隔）
  -s, --source        源语言（默认: zh-CN）
  -o, --output        输出目录（默认: 当前目录）
  -e, --engine        翻译引擎（mock/google/deepl/openai）
  -k, --api-key       API密钥
  --no-switcher       不生成语言切换器
```

## 💡 使用示例

### 示例1：基础翻译

```bash
# 准备一个中文README.md
echo "# 欢迎使用
这是一个示例项目。
" > README.md

# 翻译为英文
i18nforge translate README.md -t en
```

生成的文件：

```
README.md      # 原始中文版本
README_en.md   # 英文版本（如果源语言不是英文）
```

### 示例2：多语言项目

```bash
# 生成包含切换器的多语言README
i18nforge translate README.md -t en,ja,ko,es

# 输出文件
README.md      # 中文
README_ja.md   # 日语
README_ko.md   # 韩语
README_es.md   # 西班牙语
```

### 示例3：使用Python API

```python
from i18nforge import ReadmeGenerator
from i18nforge.translator import create_translator

# 创建翻译器
translator = create_translator("mock")

# 创建生成器
generator = ReadmeGenerator(
    project_name="MyProject",
    translator=translator,
    source_lang='zh-CN',
    target_langs=['en', 'ja', 'ko']
)

# 读取并翻译
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

results = generator.generate(content, output_dir='.')
```

## 🗺️ 设计思路与迭代规划

### 设计理念

1. **零依赖优先** - 优先使用Python标准库，降低使用门槛
2. **格式至上** - 翻译过程中不破坏原有Markdown格式
3. **渐进增强** - 基础功能零依赖，高级功能可选扩展
4. **用户友好** - 简洁的CLI界面，易于使用

### 架构设计

```
┌─────────────────────────────────────────┐
│           I18nForge                      │
├─────────────────────────────────────────┤
│  ┌─────────┐  ┌──────────┐  ┌────────┐ │
│  │  CLI    │  │ Generator │  │ Config │ │
│  └────┬────┘  └────┬─────┘  └────────┘ │
│       │            │                    │
│  ┌────┴────┐  ┌────┴─────┐             │
│  │ Parser  │  │ Translator│             │
│  └─────────┘  └──────────┘             │
└─────────────────────────────────────────┘
```

### 未来迭代计划

- [ ] v1.1 - 支持更多Markdown语法（脚注、任务列表）
- [ ] v1.2 - 添加Web界面
- [ ] v1.3 - 支持图片内文字OCR翻译
- [ ] v2.0 - AI驱动的上下文感知翻译
- [ ] v2.1 - GitHub Actions自动翻译集成
- [ ] v2.2 - 社区贡献的翻译模板市场

## 📦 打包与部署

### 发布到PyPI

```bash
# 构建发布包
python -m build

# 上传到PyPI
twine upload dist/*
```

### Docker部署

```dockerfile
FROM python:3.10-slim
RUN pip install i18nforge
WORKDIR /workspace
COPY README.md .
RUN i18nforge translate README.md -t en,ja,ko
```

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建Pull Request

### 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/

# 代码格式化
black i18nforge/
flake8 i18nforge/
```

## 📄 开源协议说明

本项目基于 **MIT License** 开源，您可以：

✅ 自由使用、修改、分发本软件
✅ 商业用途
✅ 私有项目使用

详见 [LICENSE](LICENSE) 文件。

---

<p align="center">
  <strong>Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a></strong>
  <br>
  <sub>If you find this project helpful, please give it a ⭐</sub>
</p>
