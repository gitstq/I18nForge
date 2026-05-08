"""
Configuration Module - 配置模块
定义支持的语言、默认配置等
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field


# 支持的语言
SUPPORTED_LANGUAGES = {
    'zh-CN': {
        'name': '简体中文',
        'native_name': '简体中文',
        'code': 'zh-CN',
        'flag': '🇨🇳',
        'enabled': True,
    },
    'zh-TW': {
        'name': 'Chinese Traditional',
        'native_name': '繁體中文',
        'code': 'zh-TW',
        'flag': '🇹🇼',
        'enabled': True,
    },
    'en': {
        'name': 'English',
        'native_name': 'English',
        'code': 'en',
        'flag': '🇺🇸',
        'enabled': True,
    },
    'ja': {
        'name': 'Japanese',
        'native_name': '日本語',
        'code': 'ja',
        'flag': '🇯🇵',
        'enabled': True,
    },
    'ko': {
        'name': 'Korean',
        'native_name': '한국어',
        'code': 'ko',
        'flag': '🇰🇷',
        'enabled': True,
    },
    'es': {
        'name': 'Spanish',
        'native_name': 'Español',
        'code': 'es',
        'flag': '🇪🇸',
        'enabled': True,
    },
    'fr': {
        'name': 'French',
        'native_name': 'Français',
        'code': 'fr',
        'flag': '🇫🇷',
        'enabled': True,
    },
    'de': {
        'name': 'German',
        'native_name': 'Deutsch',
        'code': 'de',
        'flag': '🇩🇪',
        'enabled': True,
    },
    'ru': {
        'name': 'Russian',
        'native_name': 'Русский',
        'code': 'ru',
        'flag': '🇷🇺',
        'enabled': True,
    },
    'pt': {
        'name': 'Portuguese',
        'native_name': 'Português',
        'code': 'pt',
        'flag': '🇵🇹',
        'enabled': True,
    },
    'it': {
        'name': 'Italian',
        'native_name': 'Italiano',
        'code': 'it',
        'flag': '🇮🇹',
        'enabled': True,
    },
    'ar': {
        'name': 'Arabic',
        'native_name': 'العربية',
        'code': 'ar',
        'flag': '🇸🇦',
        'enabled': True,
    },
    'vi': {
        'name': 'Vietnamese',
        'native_name': 'Tiếng Việt',
        'code': 'vi',
        'flag': '🇻🇳',
        'enabled': True,
    },
    'th': {
        'name': 'Thai',
        'native_name': 'ไทย',
        'code': 'th',
        'flag': '🇹🇭',
        'enabled': True,
    },
    'id': {
        'name': 'Indonesian',
        'native_name': 'Bahasa Indonesia',
        'code': 'id',
        'flag': '🇮🇩',
        'enabled': True,
    },
    'tr': {
        'name': 'Turkish',
        'native_name': 'Türkçe',
        'code': 'tr',
        'flag': '🇹🇷',
        'enabled': True,
    },
    'pl': {
        'name': 'Polish',
        'native_name': 'Polski',
        'code': 'pl',
        'flag': '🇵🇱',
        'enabled': True,
    },
    'nl': {
        'name': 'Dutch',
        'native_name': 'Nederlands',
        'code': 'nl',
        'flag': '🇳🇱',
        'enabled': True,
    },
    'uk': {
        'name': 'Ukrainian',
        'native_name': 'Українська',
        'code': 'uk',
        'flag': '🇺🇦',
        'enabled': True,
    },
}

# 语言名称映射
LANGUAGE_NAMES = {
    'zh': '中文',
    'zh-CN': '简体中文',
    'zh-TW': '繁體中文',
    'en': 'English',
    'ja': '日本語',
    'ko': '한국어',
    'es': 'Español',
    'fr': 'Français',
    'de': 'Deutsch',
    'ru': 'Русский',
    'pt': 'Português',
    'it': 'Italiano',
    'ar': 'العربية',
    'vi': 'Tiếng Việt',
    'th': 'ไทย',
    'id': 'Bahasa Indonesia',
    'tr': 'Türkçe',
    'pl': 'Polski',
    'nl': 'Nederlands',
    'uk': 'Українська',
}


@dataclass
class TranslatorConfig:
    """翻译器配置"""
    engine: str = "mock"  # google, deepl, openai, mock
    api_key: Optional[str] = None
    cache_enabled: bool = True
    cache_dir: str = ".i18nforge_cache"
    retry_count: int = 3
    timeout: int = 30


@dataclass
class GeneratorConfig:
    """生成器配置"""
    source_lang: str = "zh-CN"
    target_langs: List[str] = field(default_factory=lambda: ["en"])
    output_dir: str = "."
    generate_switcher: bool = True
    preserve_formatting: bool = True
    split_long_texts: bool = True
    max_text_length: int = 5000


@dataclass
class DefaultConfig:
    """默认配置"""
    version: str = "1.0.0"
    translator: TranslatorConfig = field(default_factory=TranslatorConfig)
    generator: GeneratorConfig = field(default_factory=GeneratorConfig)
    supported_languages: Dict = field(default_factory=lambda: SUPPORTED_LANGUAGES)


# 全局默认配置
DEFAULT_CONFIG = DefaultConfig()


def get_language_info(lang_code: str) -> Optional[Dict]:
    """获取语言信息"""
    return SUPPORTED_LANGUAGES.get(lang_code)


def get_enabled_languages() -> List[str]:
    """获取所有启用的语言"""
    return [
        code for code, info in SUPPORTED_LANGUAGES.items()
        if info.get('enabled', True)
    ]


def get_language_display_name(lang_code: str) -> str:
    """获取语言显示名称"""
    if lang_code in LANGUAGE_NAMES:
        return LANGUAGE_NAMES[lang_code]
    if lang_code in SUPPORTED_LANGUAGES:
        return SUPPORTED_LANGUAGES[lang_code]['native_name']
    return lang_code
