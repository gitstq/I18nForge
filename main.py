#!/usr/bin/env python3
"""
I18nForge - README多语言智能生成器

A zero-dependency, Markdown-aware translation tool designed specifically for
GitHub README files. Preserves formatting, emojis, code blocks, and links
while intelligently translating content.

Usage:
    # Translate README
    python -m i18nforge translate README.md -t en,ja,ko

    # Generate template
    python -m i18nforge generate -n MyProject -d "Description"

Author: gitstq
License: MIT
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from i18nforge.cli import main

if __name__ == '__main__':
    main()
