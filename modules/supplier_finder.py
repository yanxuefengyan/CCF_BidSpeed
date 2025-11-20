"""
供应商寻源模块
通过网络搜索找到合格的供应商信息
"""
import re
import json
import requests
from typing import Dict, List
from bs4 import BeautifulSoup
import time

class SupplierFinder:
    """供应商查找器"""
    
    def __init__(self):
        """初始化查找器"""
        self.search_engines = {
            'baidu': 'https://www.baidu.com/s?wd=',
            'bing': 'https://www.bing.com/search?q='
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def find(self, requirements: Dict) -> Dict:
        """
        查找供应商
        
        参数:
            requirements: 供应商需求，包含产品类型、技术要求等
        
        返回:
            Dict: 包含前3家供应商信息的字典
        """
        # 提取搜索关键词
        keywords = self._extract_keywords(requirements)
        
        # 搜索供应商
        suppliers = self._search_suppliers(keywords)
        
        # 获取详细信息
        detailed_suppliers = self._enrich_supplier_info(suppliers)
        
        # 评分排序
        ranked_suppliers = self._rank_suppliers(detailed_suppliers, requirements)
        
        # 返回前3家
        top3 = ranked_suppliers[:3]
        
        return {
            'success': True,
            'total_found': len(suppliers),
            'search_keywords': keywords,
            'top_suppliers': top3,
            'search_timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def _extract_keywords(self, requirements: Dict) -> List[str]:
        """提取搜索关键词"""
        keywords = []
        
        # 从需求中提取产品名称
        product_names = requirements.get('product_names', [])
        keywords.extend(product_names)
        
        # 从技术要求中提取品牌
        tech_requirements = requirements.get('tech_requirements', [])
        for req in tech_requirements:
            # 提取品牌名称
            brands = self._extract_brands(req)
            keywords.extend(brands)
        
        # 添加行业关键词
        industry = requirements.get('industry', 'IT设备')
        keywords.append(industry)
        keywords.append('供应商')
        keywords.append('厂商')
        
        # 去重
        keywords = list(set(keywords))
        return keywords[:5]  # 限制关键词数量
    
    def _extract_brands(self, text: str) -> List[str]:
        """从文本中提取品牌名称"""
        # 常见IT品牌列表
        known_brands = [
            'Dell', 'HP', 'Lenovo', 'Huawei', 'H3C', 'Cisco', 
            'IBM', 'Oracle', 'Microsoft', 'Intel', 'AMD',
            '华为', '联想', '浪潮', '曙光', '新华三', '中兴'
        ]
        
        brands = []
        for brand in known_brands:
            if brand.lower() in text.lower() or brand in text:
                brands.append(brand)
        
        return brands
    
    def _search_suppliers(self, keywords: List[str]) -> List[Dict]:
        """搜索供应商（模拟搜索结果）"""
        # 实际应用中这里应该调用真实的搜索API或爬虫
        # 这里使用模拟数据演示
        
        mock_suppliers = [
            {
                'name': '北京中科软科技股份有限公司',
                'website': 'https://www.chinasofti.com',
                'description': '专业IT解决方案提供商，提供软硬件集成服务',
                'matched_keywords': keywords[:2]
            },
            {
                'name': '神州数码集团股份有限公司',
                'website': 'https://www.dcits.com',
                'description': '领先的云计算和IT服务提供商',
                'matched_keywords': keywords[:2]
            },
            {
                'name': '东软集团股份有限公司',
                'website': 'https://www.neusoft.com',
                'description': '大型IT解决方案与服务供应商',
                'matched_keywords': keywords[:2]
            },
            {
                'name': '浪潮电子信息产业股份有限公司',
                'website': 'https://www.inspur.com',
                'description': '中国领先的服务器和存储设备制造商',
                'matched_keywords': keywords[:2]
            },
            {
                'name': '联想集团有限公司',
                'website': 'https://www.lenovo.com.cn',
                'description': '全球领先的PC和服务器供应商',
                'matched_keywords': keywords[:2]
            }
        ]
        
        return mock_suppliers
    
    def _enrich_supplier_info(self, suppliers: List[Dict]) -> List[Dict]:
        """补充供应商详细信息"""
        enriched = []
        
        for supplier in suppliers:
            # 实际应用中这里应该查询企业信用信息系统
            # 这里使用模拟数据
            detailed_info = {
                **supplier,
                'contact_info': self._get_contact_info(supplier['name']),
                'credit_rating': self._get_credit_rating(supplier['name']),
                'business_scope': self._get_business_scope(supplier['name']),
                'past_projects': self._get_past_projects(supplier['name']),
                'certifications': self._get_certifications(supplier['name'])
            }
            enriched.append(detailed_info)
        
        return enriched
    
    def _get_contact_info(self, company_name: str) -> Dict:
        """获取联系信息（模拟）"""
        # 实际应用中应该从公开渠道获取真实信息
        mock_contacts = {
            '北京中科软科技股份有限公司': {
                'contact_person': '张经理',
                'phone': '010-62631234',
                'email': 'sales@chinasofti.com',
                'address': '北京市海淀区中关村软件园'
            },
            '神州数码集团股份有限公司': {
                'contact_person': '李经理',
                'phone': '010-82705678',
                'email': 'info@dcits.com',
                'address': '北京市朝阳区霄云路'
            },
            '东软集团股份有限公司': {
                'contact_person': '王经理',
                'phone': '024-83662345',
                'email': 'contact@neusoft.com',
                'address': '辽宁省沈阳市浑南区'
            },
            '浪潮电子信息产业股份有限公司': {
                'contact_person': '赵经理',
                'phone': '0531-85013111',
                'email': 'service@inspur.com',
                'address': '山东省济南市高新区'
            },
            '联想集团有限公司': {
                'contact_person': '刘经理',
                'phone': '010-58868888',
                'email': 'sales@lenovo.com',
                'address': '北京市海淀区西北旺东路'
            }
        }
        
        return mock_contacts.get(company_name, {
            'contact_person': '销售经理',
            'phone': '待查询',
            'email': '待查询',
            'address': '待查询'
        })
    
    def _get_credit_rating(self, company_name: str) -> str:
        """获取信用等级"""
        # 模拟信用等级
        ratings = ['AAA', 'AA+', 'AA', 'A+']
        import random
        return random.choice(ratings)
    
    def _get_business_scope(self, company_name: str) -> List[str]:
        """获取经营范围"""
        return [
            '计算机软硬件开发与销售',
            '系统集成服务',
            '技术咨询服务',
            '云计算服务',
            '数据中心建设与运维'
        ]
    
    def _get_past_projects(self, company_name: str) -> List[Dict]:
        """获取历史项目（模拟）"""
        return [
            {
                'project_name': '某政府部门信息化建设项目',
                'year': '2024',
                'contract_amount': '500万元',
                'performance': '优秀'
            },
            {
                'project_name': '某银行数据中心建设项目',
                'year': '2023',
                'contract_amount': '800万元',
                'performance': '良好'
            },
            {
                'project_name': '某高校智慧校园项目',
                'year': '2023',
                'contract_amount': '300万元',
                'performance': '优秀'
            }
        ]
    
    def _get_certifications(self, company_name: str) -> List[str]:
        """获取资质证书"""
        return [
            'ISO9001质量管理体系认证',
            'ISO27001信息安全管理体系认证',
            'CMMI5级认证',
            '信息系统集成及服务资质（一级）',
            '高新技术企业证书'
        ]
    
    def _rank_suppliers(self, suppliers: List[Dict], requirements: Dict) -> List[Dict]:
        """对供应商进行评分排序"""
        scored_suppliers = []
        
        for supplier in suppliers:
            score = 0
            scoring_detail = {}
            
            # 信用等级评分（30分）
            credit_scores = {'AAA': 30, 'AA+': 25, 'AA': 20, 'A+': 15}
            credit_score = credit_scores.get(supplier['credit_rating'], 10)
            score += credit_score
            scoring_detail['credit_score'] = credit_score
            
            # 历史业绩评分（30分）
            past_projects = supplier.get('past_projects', [])
            project_score = min(len(past_projects) * 10, 30)
            score += project_score
            scoring_detail['project_score'] = project_score
            
            # 资质证书评分（20分）
            certifications = supplier.get('certifications', [])
            cert_score = min(len(certifications) * 4, 20)
            score += cert_score
            scoring_detail['cert_score'] = cert_score
            
            # 关键词匹配度评分（20分）
            matched_keywords = supplier.get('matched_keywords', [])
            keyword_score = min(len(matched_keywords) * 10, 20)
            score += keyword_score
            scoring_detail['keyword_score'] = keyword_score
            
            supplier['total_score'] = score
            supplier['scoring_detail'] = scoring_detail
            scored_suppliers.append(supplier)
        
        # 按总分排序
        scored_suppliers.sort(key=lambda x: x['total_score'], reverse=True)
        
        return scored_suppliers


def find_suppliers(requirements: Dict) -> Dict:
    """
    供应商查找入口函数
    
    参数:
        requirements: 供应商需求
        {
            'product_names': ['服务器', '交换机'],
            'tech_requirements': ['Intel Xeon处理器', '128GB内存'],
            'industry': 'IT设备',
            'budget_range': '500万元'
        }
    
    返回:
        Dict: 供应商查找结果
    """
    finder = SupplierFinder()
    return finder.find(requirements)