# I18nForge

🎉 **README多語言智慧生成器** | Markdown-aware README translation tool with format preservation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/gitstq/I18nForge)](https://github.com/gitstq/I18nForge/stargazers)

[🇨🇳 简体中文](README.md) | **🇹🇼 繁體中文** | [🇺🇸 English](README_en.md) | [🇯🇵 日本語](README_ja.md) | [🇰🇷 한국어](README_ko.md) | [🇪🇸 Español](README_es.md)

---

## 🎉 專案介紹

**I18nForge** 是一款專為GitHub README設計的**多語言智慧生成器**。它能夠智慧識別Markdown格式，保留表情符號、程式碼區塊、連結等特殊元素，同時將內容翻譯成多種語言。

### ✨ 解決的問題

- 📝 手動翻譯README費時費力
- 🎨 翻譯後格式混亂，表情符號遺失
- 🔗 連結、程式碼區塊被誤翻譯
- 🌐 需要多語言版本但沒有好工具

### 🚀 自研差異化亮點

1. **Markdown感知解析** - 智慧識別標題、列表、程式碼區塊、表格
2. **格式100%保留** - 表情符號、Markdown語法、程式碼區塊完整保留
3. **零依賴設計** - 純Python標準庫，無外部依賴
4. **多翻譯引擎** - 支援Mock、Google、DeepL、OpenAI等多種翻譯服務
5. **語言自動切換** - 生成語言切換器，方便用戶切換語言

## ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 🎨 **Markdown感知** | 智慧解析Markdown結構，區分可翻譯內容和格式元素 |
| 😊 **表情保留** | 100%保留表情符號，不遺失任何視覺元素 |
| 💻 **程式碼區塊保護** | 程式碼區塊內容不會被翻譯，保持原始程式碼 |
| 🔗 **連結智慧** | 連結和圖片不會被誤翻譯 |
| 📊 **表格支援** | 完整支援Markdown表格翻譯 |
| 🌐 **多語言切換** | 自動生成語言切換器，多語言版本一鍵切換 |
| ⚡ **零依賴** | 純Python標準庫實現，無需安裝額外套件 |
| 🔧 **多引擎** | 支援Mock、Google、DeepL、OpenAI等多種翻譯引擎 |
| 💾 **智慧快取** | 翻譯結果本地快取，避免重複翻譯 |
| 🎯 **增量翻譯** | 只翻譯新增或修改的內容，節省時間和成本 |

## 🚀 快速開始

### 📋 環境要求

- Python 3.8+
- 無需其他依賴（零依賴設計）

### 💾 安裝步驟

**方式一：pip安裝**

```bash
pip install i18nforge
```

**方式二：從原始碼安裝**

```bash
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge
pip install -e .
```

### 📖 基本使用

**命令列使用**

```bash
# 翻譯為英文
i18nforge translate README.md -t en

# 翻譯為多種語言
i18nforge translate README.md -t en,ja,ko

# 使用指定翻譯引擎
i18nforge translate README.md -t en --engine google
```

**生成README模板**

```bash
i18nforge generate -n MyProject -d "這是一個很棒的專案" -f "輕量級" -f "易於使用"
```

### ⚙️ 命令列選項

```
用法: i18nforge [命令] [選項]

命令:
  translate     翻譯README檔案
  generate      生成README模板
  languages     顯示支援的語言列表

選項:
  -t, --target        目標語言（逗號分隔）
  -s, --source        來源語言（預設: zh-CN）
  -o, --output        輸出目錄（預設: 目前目錄）
  -e, --engine        翻譯引擎（mock/google/deepl/openai）
  -k, --api-key       API金鑰
  --no-switcher       不生成語言切換器
```

## 💡 設計思路與迭代規劃

### 設計理念

1. **零依賴優先** - 優先使用Python標準庫，降低使用門檻
2. **格式至上** - 翻譯過程中不破壞原有Markdown格式
3. **漸進增強** - 基礎功能零依賴，高級功能可選擴展
4. **用戶友好** - 簡潔的CLI介面，易於使用

### 架構設計

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

### 未來迭代計畫

- [ ] v1.1 - 支援更多Markdown語法（腳註、工作列表）
- [ ] v1.2 - 添加Web介面
- [ ] v1.3 - 支援圖片內文字OCR翻譯
- [ ] v2.0 - AI驅動的上下文感知翻譯
- [ ] v2.1 - GitHub Actions自動翻譯整合
- [ ] v2.2 - 社群貢獻的翻譯模板市場

## 🤝 貢獻指南

歡迎貢獻程式碼！請遵循以下步驟：

1. Fork本倉庫
2. 建立特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 建立Pull Request

### 開發環境設置

```bash
# 克隆倉庫
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge

# 安裝開發依賴
pip install -e ".[dev]"

# 執行測試
pytest tests/

# 程式碼格式化
black i18nforge/
flake8 i18nforge/
```

## 📄 開源協議說明

本專案基於 **MIT License** 開源，您可以：

✅ 自由使用、修改、分發本軟體
✅ 商業用途
✅ 私有專案使用

詳見 [LICENSE](LICENSE) 檔案。

---

<p align="center">
  <strong>Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a></strong>
  <br>
  <sub>如果這個專案對您有幫助，請給它一個 ⭐</sub>
</p>
