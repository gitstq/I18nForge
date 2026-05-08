# I18nForge

🎉 **README Multi-language Intelligent Generator** | Markdown-aware translation tool with format preservation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/gitstq/I18nForge)](https://github.com/gitstq/I18nForge/stargazers)

[🇨🇳 简体中文](README_zh-CN.md) | [🇹🇼 繁體中文](README_zh-TW.md) | **🇺🇸 English** | [🇯🇵 日本語](README_ja.md) | [🇰🇷 한국어](README_ko.md) | [🇪🇸 Español](README_es.md)

---

## 🎉 Project Introduction

**I18nForge** is a **multi-language intelligent generator** specifically designed for GitHub README files. It intelligently recognizes Markdown formatting, preserves special elements like emojis, code blocks, and links, while translating content into multiple languages.

### ✨ Problems We Solve

- 📝 Manual README translation is time-consuming
- 🎨 Formatting gets messed up, emojis are lost
- 🔗 Links and code blocks get mistranslated
- 🌐 Need multi-language versions but no good tools

### 🚀 Key Differentiators

1. **Markdown-Aware Parsing** - Intelligently identifies headings, lists, code blocks, tables
2. **100% Format Preservation** - Emojis, Markdown syntax, code blocks fully preserved
3. **Zero-Dependency Design** - Pure Python standard library, no external dependencies
4. **Multiple Translation Engines** - Supports Mock, Google, DeepL, OpenAI and more
5. **Auto Language Switcher** - Generates language switcher for easy switching

## ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🎨 **Markdown-Aware** | Smart parsing of Markdown structure, distinguishing translatable content |
| 😊 **Emoji Preservation** | 100% emoji preservation, no visual elements lost |
| 💻 **Code Block Protection** | Code blocks won't be translated, original code preserved |
| 🔗 **Smart Link Handling** | Links and images won't be mistranslated |
| 📊 **Table Support** | Full Markdown table translation support |
| 🌐 **Multi-language Switcher** | Auto-generates language switcher, one-click switching |
| ⚡ **Zero Dependencies** | Pure Python standard library, no extra packages needed |
| 🔧 **Multiple Engines** | Supports Mock, Google, DeepL, OpenAI and more |
| 💾 **Smart Caching** | Local caching of translation results, avoids repetition |
| 🎯 **Incremental Translation** | Only translates new or modified content, saves time |

## 🚀 Quick Start

### 📋 Environment Requirements

- Python 3.8+
- No additional dependencies (zero-dependency design)

### 💾 Installation

**Method 1: pip install**

```bash
pip install i18nforge
```

**Method 2: From source**

```bash
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge
pip install -e .
```

### 📖 Basic Usage

**CLI Usage**

```bash
# Translate to English
i18nforge translate README.md -t en

# Translate to multiple languages
i18nforge translate README.md -t en,ja,ko

# Use specific translation engine
i18nforge translate README.md -t en --engine google
```

**Generate README Template**

```bash
i18nforge generate -n MyProject -d "This is an awesome project" -f "Lightweight" -f "Easy to use"
```

### ⚙️ CLI Options

```
Usage: i18nforge [command] [options]

Commands:
  translate     Translate README file
  generate      Generate README template
  languages     List supported languages

Options:
  -t, --target        Target languages (comma-separated)
  -s, --source        Source language (default: zh-CN)
  -o, --output        Output directory (default: current)
  -e, --engine        Translation engine (mock/google/deepl/openai)
  -k, --api-key       API key
  --no-switcher       Don't generate language switcher
```

## 💡 Design Philosophy & Roadmap

### Design Principles

1. **Zero-Dependency First** - Prioritize Python standard library, lower usage barrier
2. **Format is King** - Don't break original Markdown format during translation
3. **Progressive Enhancement** - Basic features zero-dependency, advanced features optional
4. **User-Friendly** - Clean CLI interface, easy to use

### Architecture

```
┌─────────────────────────────────────────┐
│           I18nForge                      │
├─────────────────────────────────────────┤
│  ┌─────────┐  ┌──────────┐  ┌────────┐ │
│  │  CLI    │  │ Generator │  │ Config │ │
│  └────┬────┘  └────┬─────┘  └────────┘ │
│       │            │                    │
│  ┌────┴────┐  ┌────┴─────┐             │
│  │ Parser  │  │Translator│             │
│  └─────────┘  └──────────┘             │
└─────────────────────────────────────────┘
```

### Future Roadmap

- [ ] v1.1 - Support more Markdown syntax (footnotes, task lists)
- [ ] v1.2 - Add web interface
- [ ] v1.3 - Support OCR translation for image text
- [ ] v2.0 - AI-driven context-aware translation
- [ ] v2.1 - GitHub Actions auto-translate integration
- [ ] v2.2 - Community translation template marketplace

## 🤝 Contributing Guide

We welcome contributions! Please follow these steps:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

### Development Setup

```bash
# Clone the repo
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Format code
black i18nforge/
flake8 i18nforge/
```

## 📄 License

This project is licensed under the **MIT License**. You are free to:

✅ Use, modify, and distribute this software
✅ Commercial use
✅ Private projects

See [LICENSE](LICENSE) for details.

---

<p align="center">
  <strong>Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a></strong>
  <br>
  <sub>If you find this project helpful, please give it a ⭐</sub>
</p>
