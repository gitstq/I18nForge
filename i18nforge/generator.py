"""
README Generator Module - README生成器
生成多语言README文件，包含语言切换器
"""

import os
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime

from .parser import MarkdownParser, BlockType
from .translator import Translator, TranslationEngine, create_translator
from .config import SUPPORTED_LANGUAGES, LANGUAGE_NAMES


class ReadmeGenerator:
    """README生成器"""
    
    # README各部分的标题映射（用于生成标准结构）
    SECTION_TITLES = {
        'zh-CN': {
            'project_intro': '🎉 项目介绍',
            'core_features': '✨ 核心特性',
            'quick_start': '🚀 快速开始',
            'environment': '📋 环境要求',
            'installation': '💾 安装步骤',
            'usage': '📖 详细使用指南',
            'configuration': '⚙️ 配置说明',
            'examples': '💡 使用示例',
            'roadmap': '🗺️ 设计思路与迭代规划',
            'deployment': '📦 打包与部署指南',
            'contributing': '🤝 贡献指南',
            'license': '📄 开源协议说明',
        },
        'zh-TW': {
            'project_intro': '🎉 專案介紹',
            'core_features': '✨ 核心特性',
            'quick_start': '🚀 快速開始',
            'environment': '📋 環境要求',
            'installation': '💾 安裝步驟',
            'usage': '📖 詳細使用指南',
            'configuration': '⚙️ 配置說明',
            'examples': '💡 使用範例',
            'roadmap': '🗺️ 設計思路與迭代規劃',
            'deployment': '📦 打包與部署指南',
            'contributing': '🤝 貢獻指南',
            'license': '📄 開源協議說明',
        },
        'en': {
            'project_intro': '🎉 Project Introduction',
            'core_features': '✨ Core Features',
            'quick_start': '🚀 Quick Start',
            'environment': '📋 Environment Requirements',
            'installation': '💾 Installation',
            'usage': '📖 Detailed Usage Guide',
            'configuration': '⚙️ Configuration',
            'examples': '💡 Usage Examples',
            'roadmap': '🗺️ Design Philosophy & Roadmap',
            'deployment': '📦 Packaging & Deployment',
            'contributing': '🤝 Contributing Guide',
            'license': '📄 License',
        },
        'ja': {
            'project_intro': '🎉 プロジェクト紹介',
            'core_features': '✨ コア機能',
            'quick_start': '🚀 クイックスタート',
            'environment': '📋 動作環境',
            'installation': '💾 インストール',
            'usage': '📖 詳細な使い方',
            'configuration': '⚙️ 設定',
            'examples': '💡 使用例',
            'roadmap': '🗺️ 設計思想とロードマップ',
            'deployment': '📦 パッケージとデプロイ',
            'contributing': '🤝 コントリビュート',
            'license': '📄 ライセンス',
        },
        'ko': {
            'project_intro': '🎉 프로젝트 소개',
            'core_features': '✨ 핵심 기능',
            'quick_start': '🚀 빠른 시작',
            'environment': '📋 환경 요구사항',
            'installation': '💾 설치',
            'usage': '📖 상세 사용 가이드',
            'configuration': '⚙️ 설정',
            'examples': '💡 사용 예시',
            'roadmap': '🗺️ 설계 철학 및 로드맵',
            'deployment': '📦 패키징 및 배포',
            'contributing': '🤝 기여 가이드',
            'license': '📄 라이선스',
        },
        'es': {
            'project_intro': '🎉 Introducción del Proyecto',
            'core_features': '✨ Funciones Principales',
            'quick_start': '🚀 Inicio Rápido',
            'environment': '📋 Requisitos del Sistema',
            'installation': '💾 Instalación',
            'usage': '📖 Guía de Uso Detallado',
            'configuration': '⚙️ Configuración',
            'examples': '💡 Ejemplos de Uso',
            'roadmap': '🗺️ Filosofía y Hoja de Ruta',
            'deployment': '📦 Empaquetado y Despliegue',
            'contributing': '🤝 Guía de Contribución',
            'license': '📄 Licencia',
        },
    }
    
    # 语言切换器模板
    LANGUAGE_SWITCHER_TEMPLATE = '''
## 🌐 Language Switcher / 语言切换 / 言語切替

{flags}

[简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md)

---

'''
    
    def __init__(
        self,
        project_name: str,
        translator: Optional[Translator] = None,
        source_lang: str = 'zh-CN',
        target_langs: Optional[List[str]] = None
    ):
        self.project_name = project_name
        self.translator = translator or create_translator("mock")
        self.source_lang = source_lang
        self.target_langs = target_langs or ['en']
        self.parser = MarkdownParser()
        
        # 语言切换器标志
        self._lang_flags = {
            'zh-CN': '🇨🇳',
            'zh-TW': '🇹🇼',
            'en': '🇺🇸',
            'ja': '🇯🇵',
            'ko': '🇰🇷',
            'es': '🇪🇸',
            'fr': '🇫🇷',
            'de': '🇩🇪',
            'ru': '🇷🇺',
            'pt': '🇵🇹',
            'it': '🇮🇹',
            'ar': '🇸🇦',
        }
    
    def generate_language_switcher(self, all_langs: List[str]) -> str:
        """生成语言切换器"""
        flags = ' '.join([
            self._lang_flags.get(lang, '🏳️')
            for lang in all_langs
            if lang in self._lang_flags
        ])
        
        return self.LANGUAGE_SWITCHER_TEMPLATE.format(flags=flags)
    
    def generate(
        self,
        source_content: str,
        output_dir: str = ".",
        generate_switcher: bool = True
    ) -> Dict[str, str]:
        """生成多语言README"""
        results = {}
        
        # 解析源文件
        blocks = self.parser.parse(source_content)
        translatable = self.parser.extract_translatable()
        
        # 生成源语言README（带语言切换器）
        all_langs = [self.source_lang] + self.target_langs
        
        if generate_switcher and len(all_langs) > 1:
            switcher = self.generate_language_switcher(all_langs)
            source_content = source_content + switcher
        
        results[self.source_lang] = source_content
        
        # 翻译到目标语言
        for target_lang in self.target_langs:
            translated_blocks = self._translate_blocks(
                blocks,
                self.source_lang,
                target_lang
            )
            
            # 重构Markdown
            translated_content = self.parser.reconstruct(translated_blocks)
            
            # 添加语言切换器
            if generate_switcher and len(all_langs) > 1:
                switcher = self.generate_language_switcher(all_langs)
                translated_content = translated_content + switcher
            
            results[target_lang] = translated_content
            
            # 保存文件
            self._save_readme(
                translated_content,
                output_dir,
                target_lang
            )
        
        # 保存源语言README
        self._save_readme(
            results[self.source_lang],
            output_dir,
            self.source_lang
        )
        
        return results
    
    def _translate_blocks(
        self,
        blocks: List,
        source_lang: str,
        target_lang: str
    ) -> List[str]:
        """翻译所有块"""
        results = []
        
        for block in blocks:
            if block.block_type == BlockType.CODE_BLOCK:
                # 代码块不翻译
                results.append(None)
            elif block.block_type == BlockType.TABLE:
                # 表格只翻译单元格内容
                translated_table = self._translate_table(
                    block.original,
                    source_lang,
                    target_lang
                )
                results.append(translated_table)
            else:
                # 翻译可翻译内容
                result = self.translator.translate(
                    block.content,
                    source_lang,
                    target_lang
                )
                results.append(result.translated)
        
        return results
    
    def _translate_table(self, table_content: str, source_lang: str, target_lang: str) -> str:
        """翻译表格内容"""
        lines = table_content.strip().split('\n')
        
        if len(lines) < 2:
            return table_content
        
        # 检查是否是表格分隔行
        translated_lines = []
        
        for i, line in enumerate(lines):
            # 跳过分隔行
            if re.match(r'^[\s|:-]+$', line.strip().replace('|', '')):
                translated_lines.append(line)
                continue
            
            # 翻译单元格内容
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            translated_cells = []
            
            for cell in cells:
                if cell and not cell.startswith('`') and not cell.startswith('!'):
                    result = self.translator.translate(cell, source_lang, target_lang)
                    translated_cells.append(result.translated)
                else:
                    translated_cells.append(cell)
            
            translated_lines.append('| ' + ' | '.join(translated_cells) + ' |')
        
        return '\n'.join(translated_lines)
    
    def _save_readme(self, content: str, output_dir: str, lang: str):
        """保存README文件"""
        if lang == self.source_lang or lang == 'en':
            filename = "README.md"
        else:
            filename = f"README_{lang}.md"
        
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Generated: {filepath}")
    
    def generate_template(
        self,
        project_name: str,
        description: str,
        features: List[str],
        output_dir: str = "."
    ) -> Dict[str, str]:
        """生成README模板"""
        templates = {}
        
        for lang in [self.source_lang] + self.target_langs:
            titles = self.SECTION_TITLES.get(lang, self.SECTION_TITLES['en'])
            
            # 构建README内容
            content = f"""# {project_name}

{titles['project_intro']}
{description}

{titles['core_features']}
"""
            for feature in features:
                content += f"- {feature}\n"
            
            content += f"""
{titles['quick_start']}

{titles['environment']}
- Python 3.8+

{titles['installation']}
```bash
pip install {project_name.lower().replace('-', '_')}
```

{titles['usage']}
```python
import {project_name.lower().replace('-', '_')}

# Your code here
```

{titles['contributing']}
Contributions are welcome! Please feel free to submit a Pull Request.

{titles['license']}
This project is licensed under the MIT License.
"""
            
            templates[lang] = content
            self._save_readme(content, output_dir, lang)
        
        return templates
