#!/usr/bin/env python3
"""
I18nForge - README Multi-language Intelligent Generator
README多语言智能生成器 - 专为开源项目打造

A zero-dependency, Markdown-aware translation tool designed specifically for
GitHub README files. Preserves formatting, emojis, code blocks, and links
while intelligently translating content.

Author: gitstq
License: MIT
"""

__version__ = "1.0.0"
__author__ = "gitstq"

from .parser import MarkdownParser
from .translator import Translator
from .generator import ReadmeGenerator
from .config import SUPPORTED_LANGUAGES, DEFAULT_CONFIG

__all__ = [
    "MarkdownParser",
    "Translator",
    "ReadmeGenerator",
    "SUPPORTED_LANGUAGES",
    "DEFAULT_CONFIG",
]
