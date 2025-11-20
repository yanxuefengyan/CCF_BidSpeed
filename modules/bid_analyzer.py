"""
标书解析模块
使用AI进行标书内容的智能解读和总结
"""
import re
import json
import requests
from typing import Dict, List

class BidAnalyzer:
    """标书解析器"""
    
    def __init__(self, api_key=None):
        """
        初始化解析器
        
        参数:
            api_key: 文心一言API密钥（从环境变量或配置文件读取）
        """
        self.api_key = api_key or self._load_api_key()
        self.api_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"
    
    def _load_api_key(self):
        """从配置文件加载API密钥"""
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get('api_key', '')
        except:
            return ''
    
    def analyze(self, text_content: str) -> Dict:
        """
        分析标书内容
        
        参数:
            text_content: 标书文本内容
        
        返回:
            Dict: 包含解析结果的字典
        """
        # 提取关键信息
        key_sections = self._extract_key_sections(text_content)
        
        # 使用AI进行深度解读
        ai_analysis = self._ai_deep_analysis(text_content, key_sections)
        
        # 提取技术规范
        tech_specs = self._extract_tech_specifications(text_content)
        
        # 提取评分细则
        scoring_rules = self._extract_scoring_rules(text_content)
        
        # 生成结构化清单
        tech_checklist = self._generate_tech_checklist(tech_specs, scoring_rules)
        
        return {
            'success': True,
            'key_sections': key_sections,
            'ai_summary': ai_analysis,
            'tech_specifications': tech_specs,
            'scoring_rules': scoring_rules,
            'tech_checklist': tech_checklist,
            'metadata': {
                'total_words': len(text_content),
                'key_points_count': len(tech_checklist)
            }
        }
    
    def _extract_key_sections(self, text: str) -> Dict:
        """提取关键章节"""
        sections = {
            '项目概况': [],
            '技术要求': [],
            '商务条款': [],
            '评分标准': [],
            '合同条款': []
        }
        
        # 使用关键词匹配提取章节
        keywords_map = {
            '项目概况': ['项目概况', '项目背景', '采购需求'],
            '技术要求': ['技术要求', '技术规格', '技术参数', '功能需求'],
            '商务条款': ['商务要求', '付款方式', '交货期'],
            '评分标准': ['评分', '打分', '评审', '权重'],
            '合同条款': ['合同', '违约', '质保']
        }
        
        lines = text.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 检测章节标题
            for section, keywords in keywords_map.items():
                if any(keyword in line for keyword in keywords):
                    current_section = section
                    break
            
            # 添加内容到对应章节
            if current_section and len(line) > 10:
                sections[current_section].append(line)
        
        # 限制每个章节的内容长度
        for section in sections:
            sections[section] = sections[section][:20]  # 保留前20行
        
        return sections
    
    def _ai_deep_analysis(self, text: str, key_sections: Dict) -> Dict:
        """使用AI进行深度分析"""
        # 构建提示词
        prompt = f"""请对以下标书内容进行专业分析，包括：
1. 核心需求总结（200字以内）
2. 关键技术要点（列举5-10个）
3. 重要时间节点
4. 潜在风险点
5. 建议关注事项

标书关键章节：
{json.dumps(key_sections, ensure_ascii=False, indent=2)[:2000]}

请以JSON格式返回分析结果。"""
        
        # 调用AI API（这里使用模拟数据，实际需要配置真实API）
        if not self.api_key:
            return self._mock_ai_analysis()
        
        try:
            # TODO: 实际集成文心一言API
            # response = requests.post(self.api_url, json={
            #     'messages': [{'role': 'user', 'content': prompt}]
            # }, headers={'Authorization': f'Bearer {self.api_key}'})
            # return response.json()
            
            return self._mock_ai_analysis()
        except Exception as e:
            return {
                'error': f'AI分析失败: {str(e)}',
                'fallback': self._mock_ai_analysis()
            }
    
    def _mock_ai_analysis(self) -> Dict:
        """模拟AI分析结果（用于演示）"""
        return {
            '核心需求总结': '本项目为某单位信息化系统建设项目，主要包括硬件采购、软件开发及系统集成服务，预算约500万元，工期6个月。',
            '关键技术要点': [
                '服务器配置：双路CPU、128GB内存、2TB存储',
                '网络设备：核心交换机、防火墙、负载均衡',
                '软件系统：支持微服务架构，前后端分离',
                '数据库：支持主从备份、容灾方案',
                '安全要求：等保三级认证'
            ],
            '重要时间节点': {
                '投标截止': '2025-12-01',
                '项目启动': '2025-12-15',
                '验收时间': '2026-06-15'
            },
            '潜在风险点': [
                '技术规格要求严格，需确保产品兼容性',
                '评分标准中业绩权重较高',
                '质保期要求3年，需考虑长期服务能力'
            ],
            '建议关注事项': [
                '重点关注第3章技术参数偏离表',
                '需提供类似项目业绩证明材料',
                '注意商务报价中的服务费用占比'
            ]
        }
    
    def _extract_tech_specifications(self, text: str) -> List[Dict]:
        """提取技术规范"""
        specs = []
        
        # 使用正则提取技术参数
        param_patterns = [
            r'(\d+)\s*(核|路|GB|TB|Mbps|台|套)',
            r'(CPU|内存|硬盘|带宽|处理器)[:：]\s*([^\n]+)',
        ]
        
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if any(keyword in line for keyword in ['配置', '参数', '规格', '要求']):
                specs.append({
                    'line_number': i + 1,
                    'content': line.strip(),
                    'category': '技术规格'
                })
        
        return specs[:50]  # 限制返回数量
    
    def _extract_scoring_rules(self, text: str) -> List[Dict]:
        """提取评分细则"""
        rules = []
        
        lines = text.split('\n')
        for i, line in enumerate(lines):
            # 查找包含分值的行
            if re.search(r'\d+\s*分', line):
                rules.append({
                    'line_number': i + 1,
                    'content': line.strip(),
                    'score': self._extract_score(line)
                })
        
        return rules
    
    def _extract_score(self, text: str) -> int:
        """从文本中提取分值"""
        match = re.search(r'(\d+)\s*分', text)
        return int(match.group(1)) if match else 0
    
    def _generate_tech_checklist(self, specs: List[Dict], rules: List[Dict]) -> List[Dict]:
        """生成技术条款清单"""
        checklist = []
        
        # 合并技术规格和评分规则
        for spec in specs[:20]:
            item = {
                'item': spec['content'],
                'page': spec['line_number'],
                'score': 0,
                'priority': 'medium'
            }
            
            # 匹配对应的评分
            for rule in rules:
                if any(word in rule['content'] for word in spec['content'].split()[:3]):
                    item['score'] = rule['score']
                    break
            
            # 根据分值设置优先级
            if item['score'] >= 10:
                item['priority'] = 'high'
            elif item['score'] >= 5:
                item['priority'] = 'medium'
            else:
                item['priority'] = 'low'
            
            checklist.append(item)
        
        # 按优先级和分值排序
        checklist.sort(key=lambda x: (
            {'high': 0, 'medium': 1, 'low': 2}[x['priority']],
            -x['score']
        ))
        
        return checklist


def analyze_bid(file_path: str) -> Dict:
    """
    标书分析入口函数
    
    参数:
        file_path: 标书文件路径
    
    返回:
        Dict: 分析结果
    """
    from .document_processor import process_document
    
    # 先处理文档提取文本
    doc_result = process_document(file_path)
    
    if not doc_result.get('success'):
        return doc_result
    
    # 使用分析器进行解析
    analyzer = BidAnalyzer()
    analysis_result = analyzer.analyze(doc_result['text_content'])
    
    # 合并文档信息
    analysis_result['document_info'] = {
        'file_name': doc_result['file_name'],
        'file_type': doc_result['file_type'],
        'text_length': doc_result['text_length']
    }
    
    return analysis_result