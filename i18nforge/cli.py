#!/usr/bin/env python3
"""
I18nForge CLI - 命令行接口
README多语言智能生成器CLI工具
"""

import argparse
import sys
import os
from pathlib import Path
from typing import List, Optional

from i18nforge import __version__
from i18nforge.parser import MarkdownParser
from i18nforge.translator import Translator, TranslationEngine, create_translator
from i18nforge.generator import ReadmeGenerator
from i18nforge.config import (
    SUPPORTED_LANGUAGES,
    get_enabled_languages,
    get_language_display_name,
    DEFAULT_CONFIG
)


def create_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器"""
    parser = argparse.ArgumentParser(
        prog='i18nforge',
        description='🎉 I18nForge - README多语言智能生成器 | Markdown-aware README translation tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 翻译README到英文
  i18nforge translate README.md -t en

  # 翻译README到多种语言
  i18nforge translate README.md -t en,ja,ko

  # 使用Google翻译
  i18nforge translate README.md -t en --engine google

  # 生成项目README模板
  i18nforge generate -n MyProject -d "A great project" -f "Feature 1" -f "Feature 2"

  # 查看支持的语言
  i18nforge languages

Quick Start:
  1. Create or prepare your README.md in Chinese (zh-CN)
  2. Run: i18nforge translate README.md -t en,ja,ko
  3. All language versions will be generated automatically!

For more information, visit: https://github.com/gitstq/I18nForge
        """
    )
    
    # 版本信息
    parser.add_argument(
        '--version', '-v',
        action='version',
        version=f'I18nForge {__version__}'
    )
    
    # 子命令
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # translate 子命令
    translate_parser = subparsers.add_parser(
        'translate',
        help='Translate README to target languages',
        description='Translate README.md to specified languages'
    )
    translate_parser.add_argument(
        'input',
        nargs='?',
        default='README.md',
        help='Input README file (default: README.md)'
    )
    translate_parser.add_argument(
        '-t', '--target',
        required=True,
        help='Target languages (comma-separated, e.g., en,ja,ko)'
    )
    translate_parser.add_argument(
        '-s', '--source',
        default='zh-CN',
        help='Source language (default: zh-CN)'
    )
    translate_parser.add_argument(
        '-o', '--output',
        default='.',
        help='Output directory (default: current directory)'
    )
    translate_parser.add_argument(
        '-e', '--engine',
        default='mock',
        choices=['google', 'deepl', 'openai', 'mock'],
        help='Translation engine (default: mock)'
    )
    translate_parser.add_argument(
        '-k', '--api-key',
        help='API key for the translation engine'
    )
    translate_parser.add_argument(
        '--no-switcher',
        action='store_true',
        help='Do not generate language switcher'
    )
    
    # generate 子命令
    generate_parser = subparsers.add_parser(
        'generate',
        help='Generate README template',
        description='Generate a new multi-language README template'
    )
    generate_parser.add_argument(
        '-n', '--name',
        required=True,
        help='Project name'
    )
    generate_parser.add_argument(
        '-d', '--description',
        required=True,
        help='Project description'
    )
    generate_parser.add_argument(
        '-f', '--feature',
        action='append',
        dest='features',
        help='Project features (can be specified multiple times)'
    )
    generate_parser.add_argument(
        '-t', '--target',
        default='en,ja,ko,es',
        help='Target languages (comma-separated, default: en,ja,ko,es)'
    )
    generate_parser.add_argument(
        '-s', '--source',
        default='zh-CN',
        help='Source language (default: zh-CN)'
    )
    generate_parser.add_argument(
        '-o', '--output',
        default='.',
        help='Output directory (default: current directory)'
    )
    
    # languages 子命令
    languages_parser = subparsers.add_parser(
        'languages',
        help='List supported languages',
        description='Show all supported languages'
    )
    languages_parser.add_argument(
        '--enabled-only',
        action='store_true',
        help='Show only enabled languages'
    )
    
    return parser


def cmd_translate(args) -> int:
    """翻译命令"""
    print(f"\n🚀 I18nForge - README多语言翻译器")
    print(f"   版本: {__version__}")
    print(f"   源文件: {args.input}")
    print(f"   源语言: {args.source}")
    print(f"   目标语言: {args.target}")
    print(f"   翻译引擎: {args.engine}")
    print("-" * 50)
    
    # 解析目标语言
    target_langs = [lang.strip() for lang in args.target.split(',')]
    
    # 检查输入文件
    if not os.path.exists(args.input):
        print(f"❌ Error: File not found: {args.input}")
        return 1
    
    # 读取输入文件
    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 创建翻译器
    translator = create_translator(args.engine, args.api_key)
    
    # 创建生成器
    generator = ReadmeGenerator(
        project_name=Path(args.input).stem,
        translator=translator,
        source_lang=args.source,
        target_langs=target_langs
    )
    
    # 生成多语言README
    try:
        results = generator.generate(
            source_content=content,
            output_dir=args.output,
            generate_switcher=not args.no_switcher
        )
        
        print("\n" + "=" * 50)
        print("✅ 翻译完成! Generated files:")
        for lang, content_preview in results.items():
            filename = f"README_{lang}.md" if lang != 'en' and lang != args.source else "README.md"
            if lang == args.source:
                filename = "README.md"
            elif lang == 'en':
                filename = "README.md"
            else:
                filename = f"README_{lang}.md"
            print(f"   📄 {filename}")
        
        print("\n🎉 所有语言版本已生成!")
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1


def cmd_generate(args) -> int:
    """生成命令"""
    print(f"\n🎨 I18nForge - README模板生成器")
    print(f"   版本: {__version__}")
    print(f"   项目名称: {args.name}")
    print(f"   项目描述: {args.description}")
    print(f"   目标语言: {args.target}")
    print("-" * 50)
    
    # 解析目标语言
    target_langs = [lang.strip() for lang in args.target.split(',')]
    features = args.features or ["轻量级设计", "易于使用", "开源免费"]
    
    # 创建翻译器
    translator = create_translator("mock")
    
    # 创建生成器
    generator = ReadmeGenerator(
        project_name=args.name,
        translator=translator,
        source_lang=args.source,
        target_langs=target_langs
    )
    
    # 生成模板
    try:
        results = generator.generate_template(
            project_name=args.name,
            description=args.description,
            features=features,
            output_dir=args.output
        )
        
        print("\n" + "=" * 50)
        print("✅ 模板生成完成! Generated files:")
        for lang in results.keys():
            filename = f"README_{lang}.md" if lang != 'en' and lang != args.source else "README.md"
            if lang == args.source:
                filename = "README.md"
            elif lang == 'en':
                filename = "README.md"
            else:
                filename = f"README_{lang}.md"
            print(f"   📄 {filename}")
        
        print("\n🎉 请编辑源语言README.md，添加项目详细内容!")
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1


def cmd_languages(args) -> int:
    """语言列表命令"""
    print(f"\n🌐 I18nForge - 支持的语言")
    print(f"   版本: {__version__}")
    print("-" * 50)
    
    enabled_count = 0
    total_count = 0
    
    for code, info in SUPPORTED_LANGUAGES.items():
        total_count += 1
        if args.enabled_only and not info.get('enabled', True):
            continue
        
        enabled_count += 1
        flag = info.get('flag', '🏳️')
        native = info.get('native_name', code)
        name = info.get('name', '')
        status = "✅" if info.get('enabled', True) else "❌"
        
        print(f"   {flag} {code:<8} {native:<15} {name} {status}")
    
    print("-" * 50)
    print(f"总计: {enabled_count} 种语言")
    return 0


def main():
    """主函数"""
    parser = create_parser()
    args = parser.parse_args()
    
    # 如果没有子命令，显示帮助
    if not args.command:
        # 尝试翻译默认README
        if os.path.exists('README.md'):
            args.command = 'translate'
            args.input = 'README.md'
            args.target = 'en'
            args.source = 'zh-CN'
            args.output = '.'
            args.engine = 'mock'
            args.api_key = None
            args.no_switcher = False
            print("\n📝 检测到 README.md 文件，是否翻译为英文?")
            print("   (使用 --help 查看所有选项)")
            print()
            return cmd_translate(args)
        else:
            parser.print_help()
            return 0
    
    # 根据子命令执行
    if args.command == 'translate':
        return cmd_translate(args)
    elif args.command == 'generate':
        return cmd_generate(args)
    elif args.command == 'languages':
        return cmd_languages(args)
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
