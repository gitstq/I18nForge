#!/usr/bin/env python3
"""
Test Module - 测试模块
测试Markdown解析和翻译功能
"""

import unittest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from i18nforge.parser import MarkdownParser, BlockType
from i18nforge.translator import Translator, MockTranslator, TranslationEngine
from i18nforge.generator import ReadmeGenerator
from i18nforge.config import SUPPORTED_LANGUAGES


class TestMarkdownParser(unittest.TestCase):
    """测试Markdown解析器"""
    
    def setUp(self):
        self.parser = MarkdownParser()
    
    def test_parse_heading(self):
        """测试标题解析"""
        content = "# Hello World"
        blocks = self.parser.parse(content)
        
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0].block_type, BlockType.HEADING)
        self.assertEqual(blocks[0].content, "Hello World")
        self.assertEqual(blocks[0].level, 1)
    
    def test_parse_multiple_headings(self):
        """测试多个标题"""
        content = """# Title 1
## Title 2
### Title 3"""
        blocks = self.parser.parse(content)
        
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0].level, 1)
        self.assertEqual(blocks[1].level, 2)
        self.assertEqual(blocks[2].level, 3)
    
    def test_parse_code_block(self):
        """测试代码块解析"""
        content = """```python
def hello():
    print("Hello")
```"""
        blocks = self.parser.parse(content)
        
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0].block_type, BlockType.CODE_BLOCK)
        self.assertEqual(blocks[0].attributes['language'], 'python')
    
    def test_parse_table(self):
        """测试表格解析"""
        content = """| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |"""
        blocks = self.parser.parse(content)
        
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0].block_type, BlockType.TABLE)
    
    def test_parse_paragraph(self):
        """测试段落解析"""
        content = "This is a paragraph.\nWith multiple lines."
        blocks = self.parser.parse(content)
        
        self.assertTrue(len(blocks) >= 1)
    
    def test_extract_translatable(self):
        """测试提取可翻译内容"""
        content = """# Heading
Some paragraph text.

```python
print("code")
```

More text."""
        blocks = self.parser.parse(content)
        translatable = self.parser.extract_translatable()
        
        # 应该提取标题和段落，不提取代码块
        code_blocks = [t for t in translatable if t[1] == BlockType.CODE_BLOCK]
        self.assertEqual(len(code_blocks), 1)


class TestTranslator(unittest.TestCase):
    """测试翻译器"""
    
    def setUp(self):
        self.translator = Translator(engine=TranslationEngine.MOCK)
    
    def test_mock_translate(self):
        """测试模拟翻译"""
        result = self.translator.translate(
            "项目介绍",
            source_lang='zh',
            target_lang='en'
        )
        
        self.assertEqual(result.translated, "Project Introduction")
    
    def test_batch_translate(self):
        """测试批量翻译"""
        texts = ["项目介绍", "核心特性", None]
        results = self.translator.batch_translate(texts, 'zh', 'en')
        
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0].translated, "Project Introduction")
        self.assertEqual(results[1].translated, "Core Features")
        self.assertEqual(results[2].translated, "")
    
    def test_empty_text(self):
        """测试空文本"""
        result = self.translator.translate("", 'zh', 'en')
        self.assertEqual(result.translated, "")
        self.assertEqual(result.confidence, 1.0)


class TestReadmeGenerator(unittest.TestCase):
    """测试README生成器"""
    
    def setUp(self):
        self.translator = Translator(engine=TranslationEngine.MOCK)
        self.generator = ReadmeGenerator(
            project_name="TestProject",
            translator=self.translator,
            source_lang='zh-CN',
            target_langs=['en']
        )
    
    def test_language_switcher(self):
        """测试语言切换器"""
        switcher = self.generator.generate_language_switcher(['zh-CN', 'en'])
        
        self.assertIn('🇨🇳', switcher)
        self.assertIn('🇺🇸', switcher)
        self.assertIn('README.md', switcher)
    
    def test_generate_simple(self):
        """测试简单README生成"""
        content = """# Test Project

这是一个测试项目。

## 功能

- 功能1
- 功能2

## 安装

```bash
pip install test
```

## 许可证

MIT
"""
        results = self.generator.generate(
            source_content=content,
            output_dir='/tmp/i18nforge_test',
            generate_switcher=False
        )
        
        self.assertIn('zh-CN', results)
        self.assertIn('en', results)


class TestConfig(unittest.TestCase):
    """测试配置"""
    
    def test_supported_languages(self):
        """测试支持的语言"""
        self.assertIn('zh-CN', SUPPORTED_LANGUAGES)
        self.assertIn('en', SUPPORTED_LANGUAGES)
        self.assertIn('ja', SUPPORTED_LANGUAGES)
    
    def test_language_flags(self):
        """测试语言旗帜"""
        for lang_code, info in SUPPORTED_LANGUAGES.items():
            self.assertIn('flag', info)


if __name__ == '__main__':
    unittest.main(verbosity=2)
