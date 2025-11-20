"""
标书速读核心模块包
包含文档处理、标书分析、方案生成、供应商查找等功能
"""

__version__ = '1.0.0'
__author__ = 'BidSpeed Team'

# 导出主要模块
from .document_processor import process_document
from .bid_analyzer import analyze_bid
from .solution_generator import generate_solution
from .supplier_finder import find_suppliers

__all__ = [
    'process_document',
    'analyze_bid', 
    'generate_solution',
    'find_suppliers'
]