"""
文档处理模块
支持PDF、Word等格式的文档解析
"""
import os
import PyPDF2
from docx import Document

def process_document(file_path):
    """
    处理上传的文档，提取文本内容
    
    参数:
        file_path: 文件路径
    
    返回:
        dict: 包含文件信息和提取内容的字典
    """
    file_extension = os.path.splitext(file_path)[1].lower()
    
    try:
        if file_extension == '.pdf':
            text_content = extract_pdf_text(file_path)
        elif file_extension in ['.docx', '.doc']:
            text_content = extract_word_text(file_path)
        elif file_extension == '.txt':
            text_content = extract_txt_text(file_path)
        else:
            return {
                'success': False,
                'error': '不支持的文件格式'
            }
        
        return {
            'success': True,
            'file_name': os.path.basename(file_path),
            'file_type': file_extension,
            'text_content': text_content,
            'text_length': len(text_content)
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': f'文档处理失败: {str(e)}'
        }

def extract_pdf_text(pdf_path):
    """从PDF文件提取文本"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
    except Exception as e:
        raise Exception(f"PDF解析错误: {str(e)}")
    
    return text

def extract_word_text(word_path):
    """从Word文件提取文本"""
    text = ""
    try:
        doc = Document(word_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        raise Exception(f"Word解析错误: {str(e)}")
    
    return text

def extract_txt_text(txt_path):
    """从TXT文件提取文本"""
    text = ""
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except UnicodeDecodeError:
        # 尝试其他编码
        try:
            with open(txt_path, 'r', encoding='gbk') as file:
                text = file.read()
        except Exception as e:
            raise Exception(f"TXT解析错误: {str(e)}")
    except Exception as e:
        raise Exception(f"TXT解析错误: {str(e)}")
    
    return text

def clean_text(text):
    """清理提取的文本"""
    # 移除多余的空白
    text = '\n'.join(line.strip() for line in text.split('\n') if line.strip())
    return text