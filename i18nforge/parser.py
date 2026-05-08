"""
Markdown Parser Module - Markdown感知解析器
解析并分块Markdown内容，识别各种语法元素
"""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
from enum import Enum


class BlockType(Enum):
    """块类型枚举"""
    HEADING = "heading"           # 标题
    PARAGRAPH = "paragraph"       # 段落
    CODE_BLOCK = "code_block"     # 代码块
    INLINE_CODE = "inline_code"   # 行内代码
    UNORDERED_LIST = "unordered_list"  # 无序列表
    ORDERED_LIST = "ordered_list"      # 有序列表
    LIST_ITEM = "list_item"      # 列表项
    LINK = "link"                 # 链接
    IMAGE = "image"              # 图片
    TABLE = "table"              # 表格
    BLOCKQUOTE = "blockquote"    # 引用块
    HORIZONTAL_RULE = "hr"       # 分隔线
    HTML = "html"                 # HTML标签
    EMOJI = "emoji"              # 表情符号
    PLAIN_TEXT = "plain_text"    # 纯文本


@dataclass
class MarkdownBlock:
    """Markdown块"""
    block_type: BlockType
    content: str
    original: str
    level: int = 0  # 用于标题级别、列表缩进等
    attributes: Dict = field(default_factory=dict)
    children: List['MarkdownBlock'] = field(default_factory=list)
    
    def __repr__(self):
        return f"MarkdownBlock({self.block_type.value}, level={self.level}, content='{self.content[:30]}...')"


class MarkdownParser:
    """Markdown感知解析器"""
    
    # 正则表达式模式
    PATTERNS = {
        'heading': re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE),
        'code_block': re.compile(r'```(\w*)\n(.*?)```', re.DOTALL),
        'inline_code': re.compile(r'`([^`]+)`'),
        'link': re.compile(r'\[([^\]]+)\]\(([^\)]+)\)'),
        'image': re.compile(r'!\[([^\]]*)\]\(([^\)]+)\)'),
        'table_row': re.compile(r'^\|(.+)\|$', re.MULTILINE),
        'table_separator': re.compile(r'^[\s|:-]+$', re.MULTILINE),
        'blockquote': re.compile(r'^>\s+(.+)$', re.MULTILINE),
        'hr': re.compile(r'^[-*_]{3,}$', re.MULTILINE),
        'unordered_list': re.compile(r'^[\s]*[-*+]\s+(.+)$', re.MULTILINE),
        'ordered_list': re.compile(r'^[\s]*\d+\.\s+(.+)$', re.MULTILINE),
        'html_tag': re.compile(r'<[^>]+>'),
        'emoji': re.compile(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002702-\U00002702\U00002600-\U000026FF]'),
    }
    
    def __init__(self):
        self.blocks: List[MarkdownBlock] = []
        self.original_content: str = ""
    
    def parse(self, content: str) -> List[MarkdownBlock]:
        """解析Markdown内容"""
        self.original_content = content
        self.blocks = []
        
        lines = content.split('\n')
        current_block = None
        block_content = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # 代码块
            if line.strip().startswith('```'):
                # 保存之前的块
                if block_content:
                    self._add_block(current_block, '\n'.join(block_content))
                    block_content = []
                
                # 提取代码块
                lang_match = re.match(r'```(\w*)', line)
                lang = lang_match.group(1) if lang_match else ''
                
                code_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code_lines.append(lines[i])
                    i += 1
                
                code_content = '\n'.join(code_lines)
                self.blocks.append(MarkdownBlock(
                    block_type=BlockType.CODE_BLOCK,
                    content=code_content,
                    original=f'```{lang}\n{code_content}\n```',
                    attributes={'language': lang}
                ))
                i += 1
                continue
            
            # 标题
            heading_match = self.PATTERNS['heading'].match(line)
            if heading_match:
                if block_content:
                    self._add_block(current_block, '\n'.join(block_content))
                    block_content = []
                
                hashes, title = heading_match.groups()
                self.blocks.append(MarkdownBlock(
                    block_type=BlockType.HEADING,
                    content=title.strip(),
                    original=line,
                    level=len(hashes),
                    attributes={'raw': line}
                ))
                i += 1
                continue
            
            # 表格
            if line.strip().startswith('|'):
                table_lines = []
                while i < len(lines) and lines[i].strip().startswith('|'):
                    table_lines.append(lines[i])
                    i += 1
                
                # 跳过分隔行
                if i < len(lines) and self.PATTERNS['table_separator'].match(lines[i].strip()):
                    i += 1
                
                self.blocks.append(MarkdownBlock(
                    block_type=BlockType.TABLE,
                    content='\n'.join(table_lines),
                    original='\n'.join(table_lines),
                    attributes={'rows': len(table_lines)}
                ))
                continue
            
            # 引用块
            bq_match = self.PATTERNS['blockquote'].match(line)
            if bq_match:
                if block_content:
                    self._add_block(current_block, '\n'.join(block_content))
                    block_content = []
                
                bq_lines = []
                while i < len(lines) and self.PATTERNS['blockquote'].match(lines[i]):
                    bq_lines.append(self.PATTERNS['blockquote'].match(lines[i]).group(1))
                    i += 1
                
                self.blocks.append(MarkdownBlock(
                    block_type=BlockType.BLOCKQUOTE,
                    content=' '.join(bq_lines),
                    original='\n'.join([f'> {l}' for l in bq_lines]),
                    attributes={'lines': len(bq_lines)}
                ))
                continue
            
            # 分隔线
            if self.PATTERNS['hr'].match(line.strip()):
                if block_content:
                    self._add_block(current_block, '\n'.join(block_content))
                    block_content = []
                
                self.blocks.append(MarkdownBlock(
                    block_type=BlockType.HORIZONTAL_RULE,
                    content='',
                    original=line,
                    attributes={'char': line.strip()[0]}
                ))
                i += 1
                continue
            
            # 列表
            ul_match = self.PATTERNS['unordered_list'].match(line)
            ol_match = self.PATTERNS['ordered_list'].match(line)
            
            if ul_match or ol_match:
                if block_content:
                    self._add_block(current_block, '\n'.join(block_content))
                    block_content = []
                
                list_type = BlockType.UNORDERED_LIST if ul_match else BlockType.ORDERED_LIST
                list_lines = []
                indent_level = len(line) - len(line.lstrip())
                
                while i < len(lines):
                    ul_m = self.PATTERNS['unordered_list'].match(lines[i])
                    ol_m = self.PATTERNS['ordered_list'].match(lines[i])
                    
                    if not (ul_m or ol_m):
                        # 检查缩进是否属于列表
                        if lines[i].strip() and not lines[i].startswith(' '):
                            break
                        if lines[i].strip():
                            list_lines.append(lines[i])
                            i += 1
                            continue
                        break
                    
                    match = ul_m if ul_m else ol_m
                    list_lines.append(match.group(1))
                    i += 1
                
                self.blocks.append(MarkdownBlock(
                    block_type=list_type,
                    content='\n'.join(list_lines),
                    original='\n'.join([line]),
                    level=indent_level,
                    attributes={'items': len(list_lines)}
                ))
                continue
            
            # 普通段落
            if line.strip():
                block_content.append(line)
            elif block_content:
                self._add_block(BlockType.PARAGRAPH, '\n'.join(block_content))
                block_content = []
            
            i += 1
        
        # 处理剩余内容
        if block_content:
            self._add_block(BlockType.PARAGRAPH, '\n'.join(block_content))
        
        return self.blocks
    
    def _add_block(self, block_type: BlockType, content: str):
        """添加块"""
        if not content.strip():
            return
        
        block = MarkdownBlock(
            block_type=block_type,
            content=content,
            original=content,
            attributes=self._analyze_content(content)
        )
        self.blocks.append(block)
    
    def _analyze_content(self, content: str) -> Dict:
        """分析内容特征"""
        attributes = {
            'has_emoji': bool(self.PATTERNS['emoji'].search(content)),
            'has_link': bool(self.PATTERNS['link'].search(content)),
            'has_code': bool(self.PATTERNS['inline_code'].search(content)),
            'has_html': bool(self.PATTERNS['html_tag'].search(content)),
        }
        
        # 提取链接
        links = self.PATTERNS['link'].findall(content)
        if links:
            attributes['links'] = [{'text': l[0], 'url': l[1]} for l in links]
        
        # 提取表情
        emojis = self.PATTERNS['emoji'].findall(content)
        if emojis:
            attributes['emojis'] = emojis
        
        return attributes
    
    def extract_translatable(self) -> List[Tuple[str, BlockType, Dict]]:
        """提取可翻译内容"""
        translatable = []
        
        for block in self.blocks:
            # 这些类型需要翻译
            if block.block_type in [
                BlockType.HEADING,
                BlockType.PARAGRAPH,
                BlockType.UNORDERED_LIST,
                BlockType.ORDERED_LIST,
                BlockType.LIST_ITEM,
                BlockType.BLOCKQUOTE,
            ]:
                translatable.append((block.content, block.block_type, block.attributes))
            # 代码块不翻译内容，但保留结构
            elif block.block_type == BlockType.CODE_BLOCK:
                translatable.append((None, block.block_type, block.attributes))
        
        return translatable
    
    def reconstruct(self, translated_blocks: List[str]) -> str:
        """重构Markdown内容"""
        result = []
        translatable_idx = 0
        
        for block in self.blocks:
            if block.block_type == BlockType.CODE_BLOCK:
                result.append(block.original)
            elif block.block_type == BlockType.TABLE:
                result.append(block.original)
            elif block.block_type == BlockType.HORIZONTAL_RULE:
                result.append(block.original)
            else:
                if translatable_idx < len(translated_blocks):
                    translated = translated_blocks[translatable_idx]
                    result.append(translated)
                    translatable_idx += 1
        
        return '\n\n'.join(filter(None, result))
