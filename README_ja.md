# I18nForge

🎉 **README多言語インテリジェント生成器** | Markdown-aware README translation tool with format preservation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/gitstq/I18nForge)](https://github.com/gitstq/I18nForge/stargazers)

[🇨🇳 简体中文](README_zh-CN.md) | [🇹🇼 繁體中文](README_zh-TW.md) | [🇺🇸 English](README.md) | **🇯🇵 日本語** | [🇰🇷 한국어](README_ko.md) | [🇪🇸 Español](README_es.md)

---

## 🎉 プロジェクト紹介

**I18nForge**は、GitHubのREADME向けに設計された**多言語インテリジェント生成器**です。Markdownフォーマットをインテリジェントに認識し、絵文字、コードブロック、リンクなどの特殊要素を保持しながら、複数の言語にコンテンツを翻訳します。

### ✨ 解决的问题

- 📝 手動でのREADME翻訳は時間と手間がかかる
- 🎨 翻訳後にフォーマットが崩れる、絵文字が失われる
- 🔗 リンクやコードブロックが誤翻訳される
- 🌐 多言語バージョンが必要だが、適切なツールがない

### 🚀 自研の差別化ポイント

1. **Markdown認識解析** - 見出し、リスト、コードブロック、テーブルをインテリジェントに識別
2. **フォーマット100%保持** - 絵文字、Markdown構文、コードブロックを完全に保持
3. **ゼロ依存設計** - 純粋なPython標準ライブラリ、外部依存なし
4. **複数翻訳エンジン** - Mock、Google、DeepL、OpenAIなど多様な翻訳サービスをサポート
5. **言語自動切り替え** - 言語切り替えボタンを生成、簡単な切り替えを実現

## ✨ コア機能

| 機能 | 説明 |
|------|------|
| 🎨 **Markdown認識** | Markdown構造をインテリジェントに解析し、翻訳可能コンテンツと書式要素を区別 |
| 😊 **絵文字保持** - 100%絵文字保持、視覚要素の欠落なし |
| 💻 **コードブロック保護** | コードブロックのコンテンツは翻訳されない、元のコードを保持 |
| 🔗 **リンクインテリジェント処理** | リンクと画像は誤翻訳されない |
| 📊 **テーブルサポート** | 完全なMarkdownテーブル翻訳サポート |
| 🌐 **多言語切り替え** | 言語切り替えボタンを自動生成、ワンボタンで切り替え可能 |
| ⚡ **ゼロ依存** | 純粋なPython標準ライブラリ實現、追加パッケージ不要 |
| 🔧 **複数エンジン** | Mock、Google、DeepL、OpenAIなど多様な翻訳エンジンをサポート |
| 💾 **インテリジェントキャッシュ** | 翻訳結果をローカルキャッシュ、重複翻訳を回避 |
| 🎯 **增量翻訳** | 新規または変更されたコンテンツのみ翻訳、時間とコストを節約 |

## 🚀 クイックスタート

### 📋 動作環境

- Python 3.8+
- 追加の依存関係なし（ゼロ依存設計）

### 💾 インストール

**方法1：pipインストール**

```bash
pip install i18nforge
```

**方法2：ソースからインストール**

```bash
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge
pip install -e .
```

### 📖 基本的な使用方法

**CLI使用**

```bash
# 英語に翻訳
i18nforge translate README.md -t en

# 複数の言語に翻訳
i18nforge translate README.md -t en,ja,ko

# 指定翻訳エンジンを使用
i18nforge translate README.md -t en --engine google
```

**READMEテンプレート生成**

```bash
i18nforge generate -n MyProject -d "これは素晴らしいプロジェクトです" -f "軽量" -f "使いやすい"
```

### ⚙️ CLIオプション

```
使用方法: i18nforge [コマンド] [オプション]

コマンド:
  translate     READMEファイルを翻訳
  generate      READMEテンプレートを生成
  languages     サポートされている言語一覧を表示

オプション:
  -t, --target        目標言語（カンマ区切り）
  -s, --source        ソース言語（デフォルト: zh-CN）
  -o, --output        出力ディレクトリ（デフォルト: 現在ディレクトリ）
  -e, --engine        翻訳エンジン（mock/google/deepl/openai）
  -k, --api-key       APIキー
  --no-switcher       言語切り替えボタンを生成しない
```

## 💡 設計思想とロードマップ

### 設計原則

1. **ゼロ依存優先** - Python標準ライブラリを優先、使用障壁を低減
2. **フォーマット至上** - 翻訳中に元のMarkdownフォーマットを破壊しない
3. **プログレッシブエンハンスメント** - 基本機能はゼロ依存、高度な機能はオプション
4. **ユーザーフレンドリー** - クリーンなCLIインターフェース使いやすい

### アーキテクチャ

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

### 今後のロードマップ

- [ ] v1.1 - 他のMarkdown構文のサポート（脚注、タスクリスト）
- [ ] v1.2 - Webインターフェースを追加
- [ ] v1.3 - 画像内テキストのOCR翻訳をサポート
- [ ] v2.0 - AI駆動のコンテキスト認識翻訳
- [ ] v2.1 - GitHub Actions自動翻訳統合
- [ ] v2.2 - コミュニティ翻訳テンプレートマーケットプレイス

## 🤝 コントリビュートガイド

コードの貢献を歓迎します！以下の手順に従ってください：

1. このリポジトリをFork
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. Pull Requestを作成

### 開発環境セットアップ

```bash
# リポジトリをクローン
git clone https://github.com/gitstq/I18nForge.git
cd I18nForge

# 開発依存関係をインストール
pip install -e ".[dev]"

# テストを実行
pytest tests/

# コードをフォーマット
black i18nforge/
flake8 i18nforge/
```

## 📄 ライセンス

このプロジェクトは**MIT License**でライセンスされています：

✅ このソフトウェアの自由使用、変更、配布
✅ 商利用
✅ プライベートプロジェクトでの使用

詳細については[LICENSE](LICENSE)をご覧ください。

---

<p align="center">
  <strong>Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a></strong>
  <br>
  <sub>このプロジェクトが役立った方は、⭐をお願いします</sub>
</p>
