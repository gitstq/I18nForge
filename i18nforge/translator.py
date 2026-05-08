"""
Translator Module - 翻译引擎
支持多种翻译服务：Google Translate、DeepL、OpenAI、本地模拟
"""

import re
import json
import hashlib
from typing import Dict, List, Optional, Callable
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class TranslationEngine(Enum):
    """翻译引擎"""
    GOOGLE = "google"
    DEEPL = "deepl"
    OPENAI = "openai"
    MOCK = "mock"  # 用于测试/离线


@dataclass
class TranslationResult:
    """翻译结果"""
    source: str
    target: str
    translated: str
    engine: str
    confidence: float = 1.0
    error: Optional[str] = None


class BaseTranslator(ABC):
    """翻译器基类"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
    
    @abstractmethod
    def translate(self, text: str, source_lang: str, target_lang: str) -> TranslationResult:
        """翻译文本"""
        pass
    
    def batch_translate(self, texts: List[str], source_lang: str, target_lang: str) -> List[TranslationResult]:
        """批量翻译"""
        results = []
        for text in texts:
            if text is None:
                results.append(TranslationResult(
                    source="",
                    target=target_lang,
                    translated="",
                    engine=self.__class__.__name__,
                    confidence=1.0
                ))
            else:
                results.append(self.translate(text, source_lang, target_lang))
        return results


class MockTranslator(BaseTranslator):
    """模拟翻译器 - 用于测试/离线模式"""
    
    # 模拟翻译映射表
    MOCK_TRANSLATIONS = {
        ('zh', 'en'): {
            '项目介绍': 'Project Introduction',
            '核心特性': 'Core Features',
            '快速开始': 'Quick Start',
            '详细使用指南': 'Detailed Usage Guide',
            '设计思路与迭代规划': 'Design Philosophy and Roadmap',
            '打包与部署指南': 'Packaging and Deployment Guide',
            '贡献指南': 'Contributing Guide',
            '开源协议说明': 'License',
            '环境要求': 'Environment Requirements',
            '安装步骤': 'Installation Steps',
            '安装': 'Installation',
            '使用': 'Usage',
            '配置': 'Configuration',
            '示例': 'Examples',
            '特点': 'Features',
            '功能': 'Features',
            '优势': 'Advantages',
            '轻量级': 'Lightweight',
            '零依赖': 'Zero dependencies',
            '开源': 'Open Source',
            '免费': 'Free',
            '易于使用': 'Easy to use',
            '高性能': 'High Performance',
            '跨平台': 'Cross-platform',
            '支持': 'Support',
            '中文': 'Chinese',
            '简体中文': 'Simplified Chinese',
            '繁体中文': 'Traditional Chinese',
            '英语': 'English',
            '日语': 'Japanese',
            '韩语': 'Korean',
            '西班牙语': 'Spanish',
            '欢迎': 'Welcome',
            '感谢': 'Thanks',
            '联系': 'Contact',
            '反馈': 'Feedback',
            '问题': 'Issues',
            '建议': 'Suggestions',
            '贡献': 'Contribute',
            '社区': 'Community',
            '文档': 'Documentation',
            '教程': 'Tutorial',
            '指南': 'Guide',
            '用户': 'User',
            '开发者': 'Developer',
            '许可证': 'License',
            'MIT': 'MIT',
        },
        ('zh-CN', 'en'): {
            '项目介绍': 'Project Introduction',
            '核心特性': 'Core Features',
            '快速开始': 'Quick Start',
            '详细使用指南': 'Detailed Usage Guide',
            '设计思路与迭代规划': 'Design Philosophy and Roadmap',
            '打包与部署指南': 'Packaging and Deployment Guide',
            '贡献指南': 'Contributing Guide',
            '开源协议说明': 'License',
            '环境要求': 'Environment Requirements',
            '安装步骤': 'Installation Steps',
            '安装': 'Installation',
            '使用': 'Usage',
            '配置': 'Configuration',
            '示例': 'Examples',
            '特点': 'Features',
            '功能': 'Features',
            '优势': 'Advantages',
            '轻量级': 'Lightweight',
            '零依赖': 'Zero dependencies',
            '开源': 'Open Source',
            '免费': 'Free',
            '易于使用': 'Easy to use',
            '高性能': 'High Performance',
            '跨平台': 'Cross-platform',
            '支持': 'Support',
            '欢迎': 'Welcome',
            '感谢': 'Thanks',
            '许可证': 'License',
        },
        ('en', 'zh'): {
            'Project Introduction': '项目介绍',
            'Core Features': '核心特性',
            'Quick Start': '快速开始',
            'Features': '功能',
            'Installation': '安装',
            'Usage': '使用',
            'Configuration': '配置',
            'License': '开源协议说明',
            'Welcome': '欢迎',
            'Thanks': '感谢',
            'Lightweight': '轻量级',
            'Zero dependencies': '零依赖',
            'Open Source': '开源',
            'Free': '免费',
        }
    }
    
    def translate(self, text: str, source_lang: str, target_lang: str) -> TranslationResult:
        """模拟翻译"""
        original_text = text
        key = (source_lang, target_lang)
        
        if key in self.MOCK_TRANSLATIONS:
            mapping = self.MOCK_TRANSLATIONS[key]
            for src, tgt in mapping.items():
                if src in text:
                    text = text.replace(src, tgt)
        
        # 简单处理未映射的文本
        if text == original_text:  # 如果没有找到映射
            if source_lang in ('zh', 'zh-CN') and target_lang == 'en':
                # 简单的中文到英文的伪翻译
                text = f"[EN] {text}"
            elif source_lang == 'en' and target_lang in ('zh', 'zh-CN'):
                text = f"[中文] {text}"
        
        return TranslationResult(
            source=original_text,
            target=target_lang,
            translated=text,
            engine="Mock",
            confidence=0.9
        )


class GoogleTranslator(BaseTranslator):
    """Google Translate 翻译器"""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        self._cache: Dict[str, str] = {}
    
    def translate(self, text: str, source_lang: str, target_lang: str) -> TranslationResult:
        """使用Google Translate API翻译"""
        cache_key = f"{source_lang}:{target_lang}:{text}"
        
        if cache_key in self._cache:
            return TranslationResult(
                source=text,
                target=target_lang,
                translated=self._cache[cache_key],
                engine="Google",
                confidence=0.95
            )
        
        # 如果没有API密钥，使用requests模拟基础翻译
        try:
            import urllib.parse
            import urllib.request
            
            url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={urllib.parse.quote(text)}"
            
            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode())
                translated = ''.join(item[0] for item in data[0] if item[0])
                
                self._cache[cache_key] = translated
                
                return TranslationResult(
                    source=text,
                    target=target_lang,
                    translated=translated,
                    engine="Google",
                    confidence=0.95
                )
        except Exception as e:
            return TranslationResult(
                source=text,
                target=target_lang,
                translated=text,
                engine="Google",
                confidence=0.0,
                error=str(e)
            )


class Translator:
    """统一翻译接口"""
    
    ENGINES = {
        TranslationEngine.GOOGLE: GoogleTranslator,
        TranslationEngine.DEEPL: None,  # 需要deepl库
        TranslationEngine.OPENAI: None,  # 需要openai库
        TranslationEngine.MOCK: MockTranslator,
    }
    
    def __init__(self, engine: TranslationEngine = TranslationEngine.MOCK, api_key: Optional[str] = None):
        self.engine = engine
        
        if engine == TranslationEngine.DEEPL:
            try:
                import deepl
                self._translator = deepl.Translator(api_key) if api_key else None
            except ImportError:
                print("Warning: deepl library not installed. Falling back to mock translator.")
                self._translator = MockTranslator()
        elif engine == TranslationEngine.OPENAI:
            try:
                import openai
                self._translator = openai
                self._translator.api_key = api_key or "sk-mock"
            except ImportError:
                print("Warning: openai library not installed. Falling back to mock translator.")
                self._translator = MockTranslator()
        else:
            translator_class = self.ENGINES.get(engine, MockTranslator)
            self._translator = translator_class(api_key) if translator_class else MockTranslator()
    
    def translate(
        self,
        text: str,
        source_lang: str = 'auto',
        target_lang: str = 'en'
    ) -> TranslationResult:
        """翻译单个文本"""
        if not text or not text.strip():
            return TranslationResult(
                source=text,
                target=target_lang,
                translated=text,
                engine=self.engine.value,
                confidence=1.0
            )
        
        return self._translator.translate(text, source_lang, target_lang)
    
    def batch_translate(
        self,
        texts: List[str],
        source_lang: str = 'auto',
        target_lang: str = 'en'
    ) -> List[TranslationResult]:
        """批量翻译"""
        return self._translator.batch_translate(texts, source_lang, target_lang)
    
    def translate_with_context(
        self,
        texts: List[str],
        context: str = "",
        source_lang: str = 'auto',
        target_lang: str = 'en'
    ) -> List[str]:
        """带上下文的翻译（用于保持标题和内容的一致性）"""
        results = []
        
        # 添加上下文到每次翻译
        for text in texts:
            if text is None:
                results.append(None)
            else:
                full_text = f"{context}\n\n{text}" if context else text
                result = self.translate(full_text, source_lang, target_lang)
                
                # 移除上下文部分
                if context and result.translated:
                    # 简单处理：移除上下文前缀
                    translated = result.translated
                    if context in translated:
                        translated = translated.replace(context, '').strip()
                        # 清理可能残留的分隔符
                        translated = re.sub(r'^[\n\r]+', '', translated)
                    results.append(translated)
                else:
                    results.append(result.translated)
        
        return results


def create_translator(
    engine: str = "mock",
    api_key: Optional[str] = None
) -> Translator:
    """工厂函数：创建翻译器"""
    try:
        engine_enum = TranslationEngine(engine.lower())
    except ValueError:
        print(f"Warning: Unknown engine '{engine}'. Falling back to mock.")
        engine_enum = TranslationEngine.MOCK
    
    return Translator(engine=engine_enum, api_key=api_key)
