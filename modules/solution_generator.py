"""
技术方案生成模块
基于标书解析结果，自动生成技术实现方案
"""
import json
import re
from typing import Dict, List
from datetime import datetime, timedelta

class SolutionGenerator:
    """技术方案生成器"""
    
    def __init__(self):
        """初始化方案生成器"""
        self.solution_templates = self._load_solution_templates()
        self.tech_library = self._load_tech_library()
    
    def generate(self, bid_analysis: Dict) -> Dict:
        """
        生成技术实现方案
        
        参数:
            bid_analysis: 标书解析结果
        
        返回:
            Dict: 包含完整技术方案的字典
        """
        # 提取关键需求
        key_requirements = self._extract_key_requirements(bid_analysis)
        
        # 匹配技术方案
        matched_solutions = self._match_solutions(key_requirements)
        
        # 生成系统架构
        system_architecture = self._generate_architecture(key_requirements)
        
        # 生成实施计划
        implementation_plan = self._generate_implementation_plan(key_requirements)
        
        # 生成技术偏离表
        deviation_table = self._generate_deviation_table(bid_analysis)
        
        # 生成风险评估
        risk_assessment = self._generate_risk_assessment(key_requirements)
        
        return {
            'success': True,
            'solution_overview': {
                'project_name': self._extract_project_name(bid_analysis),
                'solution_type': self._determine_solution_type(key_requirements),
                'total_budget_estimate': self._estimate_budget(key_requirements),
                'implementation_duration': self._estimate_duration(key_requirements)
            },
            'key_requirements': key_requirements,
            'technical_solutions': matched_solutions,
            'system_architecture': system_architecture,
            'implementation_plan': implementation_plan,
            'deviation_table': deviation_table,
            'risk_assessment': risk_assessment,
            'generated_at': datetime.now().isoformat()
        }
    
    def _load_solution_templates(self) -> Dict:
        """加载方案模板库"""
        return {
            '云计算方案': {
                'keywords': ['云平台', '虚拟化', 'IaaS', 'PaaS', 'SaaS'],
                'template': {
                    'architecture': ['云服务器', '负载均衡', '云数据库', '云存储'],
                    'advantages': ['弹性扩展', '按需付费', '高可用性', '运维简单'],
                    'implementation': ['环境规划', '迁移方案', '安全配置', '监控部署']
                }
            },
            '大数据方案': {
                'keywords': ['大数据', '数据分析', 'Hadoop', 'Spark', '数据仓库'],
                'template': {
                    'architecture': ['数据采集', '数据存储', '数据处理', '数据展示'],
                    'advantages': ['海量数据处理', '实时分析', '智能决策', '数据挖掘'],
                    'implementation': ['平台搭建', '数据建模', 'ETL开发', '报表开发']
                }
            },
            'AI智能方案': {
                'keywords': ['人工智能', '机器学习', '深度学习', 'AI', '算法'],
                'template': {
                    'architecture': ['数据预处理', '模型训练', '模型部署', '智能应用'],
                    'advantages': ['智能识别', '自动决策', '预测分析', '效率提升'],
                    'implementation': ['数据准备', '算法选择', '模型训练', '系统集成']
                }
            },
            '物联网方案': {
                'keywords': ['物联网', 'IoT', '传感器', '智能设备', '边缘计算'],
                'template': {
                    'architecture': ['感知层', '网络层', '平台层', '应用层'],
                    'advantages': ['实时监控', '远程控制', '数据采集', '智能管理'],
                    'implementation': ['设备部署', '网络配置', '平台开发', '应用集成']
                }
            }
        }
    
    def _load_tech_library(self) -> Dict:
        """加载技术库"""
        return {
            '服务器': {
                'Intel': ['Xeon Silver', 'Xeon Gold', 'Xeon Platinum'],
                'AMD': ['EPYC 7002', 'EPYC 7003', 'EPYC 9000'],
                'specs': ['双路CPU', '128GB内存', '2TB SSD']
            },
            '网络设备': {
                'Cisco': ['Catalyst 9000', 'ASR 1000', 'ISR 4000'],
                'Huawei': ['CloudEngine', 'NetEngine', 'USG6000'],
                'H3C': ['S12500', 'MSR3600', 'SecPath F1000']
            },
            '数据库': {
                'Oracle': ['Oracle 19c', 'Oracle 21c'],
                'MySQL': ['MySQL 8.0', 'MySQL 8.4'],
                'PostgreSQL': ['PostgreSQL 14', 'PostgreSQL 15']
            },
            '操作系统': {
                'Linux': ['CentOS 8', 'Ubuntu 20.04', 'Red Hat 8'],
                'Windows': ['Windows Server 2019', 'Windows Server 2022']
            }
        }
    
    def _extract_key_requirements(self, bid_analysis: Dict) -> List[Dict]:
        """提取关键需求"""
        requirements = []
        
        # 从技术规格中提取
        tech_specs = bid_analysis.get('tech_specifications', [])
        for spec in tech_specs:
            requirement = {
                'type': 'technical',
                'description': spec['content'],
                'priority': 'high',
                'source': f"第{spec['line_number']}行"
            }
            requirements.append(requirement)
        
        # 从AI分析中提取关键技术要点
        ai_analysis = bid_analysis.get('ai_summary', {})
        tech_points = ai_analysis.get('关键技术要点', [])
        for point in tech_points:
            requirement = {
                'type': 'functional',
                'description': point,
                'priority': 'medium',
                'source': 'AI分析'
            }
            requirements.append(requirement)
        
        return requirements[:20]  # 限制数量
    
    def _match_solutions(self, requirements: List[Dict]) -> List[Dict]:
        """匹配技术方案"""
        matched = []
        
        # 分析需求文本，匹配对应方案
        requirement_text = ' '.join([req['description'] for req in requirements])
        
        for solution_name, solution_data in self.solution_templates.items():
            score = 0
            matched_keywords = []
            
            # 计算匹配度
            for keyword in solution_data['keywords']:
                if keyword in requirement_text:
                    score += 1
                    matched_keywords.append(keyword)
            
            if score > 0:
                matched.append({
                    'solution_name': solution_name,
                    'match_score': score,
                    'matched_keywords': matched_keywords,
                    'architecture': solution_data['template']['architecture'],
                    'advantages': solution_data['template']['advantages'],
                    'implementation_steps': solution_data['template']['implementation']
                })
        
        # 按匹配度排序
        matched.sort(key=lambda x: x['match_score'], reverse=True)
        return matched[:3]  # 返回前3个最匹配的方案
    
    def _generate_architecture(self, requirements: List[Dict]) -> Dict:
        """生成系统架构"""
        architecture = {
            'layers': [
                {
                    'name': '展示层',
                    'components': ['Web界面', '移动端应用', '管理后台'],
                    'technologies': ['Vue.js', 'Element UI', 'Responsive Design']
                },
                {
                    'name': '业务层',
                    'components': ['业务逻辑', 'API服务', '数据处理'],
                    'technologies': ['Spring Boot', 'RESTful API', 'Microservices']
                },
                {
                    'name': '数据层',
                    'components': ['关系数据库', '缓存系统', '文件存储'],
                    'technologies': ['MySQL', 'Redis', 'MinIO']
                },
                {
                    'name': '基础设施层',
                    'components': ['服务器', '网络设备', '安全设备'],
                    'technologies': ['Linux Server', 'Docker', 'Nginx']
                }
            ],
            'deployment_model': '分布式部署',
            'scalability': '支持水平扩展',
            'availability': '99.9%可用性保证'
        }
        
        return architecture
    
    def _generate_implementation_plan(self, requirements: List[Dict]) -> Dict:
        """生成实施计划"""
        start_date = datetime.now()
        
        phases = [
            {
                'phase': '需求确认与设计',
                'duration_weeks': 2,
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': (start_date + timedelta(weeks=2)).strftime('%Y-%m-%d'),
                'deliverables': ['需求规格书', '系统设计文档', '项目计划书'],
                'milestones': ['需求确认完成', '架构设计评审通过']
            },
            {
                'phase': '环境准备与开发',
                'duration_weeks': 8,
                'start_date': (start_date + timedelta(weeks=2)).strftime('%Y-%m-%d'),
                'end_date': (start_date + timedelta(weeks=10)).strftime('%Y-%m-%d'),
                'deliverables': ['开发环境', '核心功能模块', '接口文档'],
                'milestones': ['开发环境就绪', '核心功能开发完成']
            },
            {
                'phase': '系统集成与测试',
                'duration_weeks': 4,
                'start_date': (start_date + timedelta(weeks=10)).strftime('%Y-%m-%d'),
                'end_date': (start_date + timedelta(weeks=14)).strftime('%Y-%m-%d'),
                'deliverables': ['集成系统', '测试报告', '用户手册'],
                'milestones': ['系统集成完成', '用户验收测试通过']
            },
            {
                'phase': '部署上线与培训',
                'duration_weeks': 2,
                'start_date': (start_date + timedelta(weeks=14)).strftime('%Y-%m-%d'),
                'end_date': (start_date + timedelta(weeks=16)).strftime('%Y-%m-%d'),
                'deliverables': ['生产环境', '培训材料', '运维文档'],
                'milestones': ['系统正式上线', '用户培训完成']
            }
        ]
        
        return {
            'total_duration_weeks': 16,
            'total_duration_months': 4,
            'phases': phases,
            'critical_path': ['需求确认', '核心开发', '系统测试', '上线部署'],
            'resource_requirements': {
                '项目经理': 1,
                '系统架构师': 1,
                '开发工程师': 4,
                '测试工程师': 2,
                '运维工程师': 1
            }
        }
    
    def _generate_deviation_table(self, bid_analysis: Dict) -> List[Dict]:
        """生成技术偏离表"""
        deviations = []
        
        tech_checklist = bid_analysis.get('tech_checklist', [])
        
        for item in tech_checklist[:15]:  # 限制数量
            # 简单的偏离判断逻辑
            deviation_status = self._determine_deviation_status(item['item'])
            
            deviation = {
                'requirement': item['item'],
                'our_solution': self._generate_solution_description(item['item']),
                'deviation_status': deviation_status,
                'deviation_reason': self._get_deviation_reason(deviation_status),
                'impact_assessment': self._assess_impact(deviation_status),
                'page_reference': item.get('page', 'N/A')
            }
            deviations.append(deviation)
        
        return deviations
    
    def _determine_deviation_status(self, requirement: str) -> str:
        """判断偏离状态"""
        # 简化的偏离判断逻辑
        if any(word in requirement.lower() for word in ['必须', '强制', '不得', '禁止']):
            return '无偏离'
        elif any(word in requirement.lower() for word in ['建议', '优先', '推荐']):
            return '正偏离'
        else:
            return '无偏离'
    
    def _generate_solution_description(self, requirement: str) -> str:
        """生成解决方案描述"""
        # 根据需求生成对应的解决方案描述
        if 'CPU' in requirement or '处理器' in requirement:
            return '采用Intel Xeon Gold系列处理器，性能优于要求'
        elif '内存' in requirement:
            return '配置128GB DDR4内存，满足性能要求'
        elif '存储' in requirement or '硬盘' in requirement:
            return '采用SSD固态硬盘，读写速度优于传统硬盘'
        else:
            return '按照招标要求配置，完全满足技术指标'
    
    def _get_deviation_reason(self, status: str) -> str:
        """获取偏离原因"""
        reasons = {
            '无偏离': '完全符合招标要求',
            '正偏离': '采用更高规格配置，提升系统性能',
            '负偏离': '因技术限制存在差异'
        }
        return reasons.get(status, '需进一步确认')
    
    def _assess_impact(self, status: str) -> str:
        """评估影响"""
        impacts = {
            '无偏离': '无影响',
            '正偏离': '提升系统性能和稳定性',
            '负偏离': '可能影响部分功能，需与用户确认'
        }
        return impacts.get(status, '影响待评估')
    
    def _generate_risk_assessment(self, requirements: List[Dict]) -> Dict:
        """生成风险评估"""
        return {
            'high_risk_items': [
                {
                    'risk': '技术方案复杂度较高',
                    'probability': '中等',
                    'impact': '可能延期',
                    'mitigation': '增加技术预研，制定详细计划'
                },
                {
                    'risk': '第三方系统集成风险',
                    'probability': '中等',
                    'impact': '接口对接困难',
                    'mitigation': '提前与第三方厂商沟通确认接口'
                }
            ],
            'medium_risk_items': [
                {
                    'risk': '用户需求变更',
                    'probability': '较高',
                    'impact': '增加工作量',
                    'mitigation': '建立需求变更管理流程'
                }
            ],
            'risk_summary': '整体风险可控，建议加强项目管理和技术预研'
        }
    
    def _extract_project_name(self, bid_analysis: Dict) -> str:
        """提取项目名称"""
        # 从文档信息中提取项目名称
        doc_info = bid_analysis.get('document_info', {})
        filename = doc_info.get('file_name', '')
        
        if filename:
            # 去除文件扩展名
            name = filename.rsplit('.', 1)[0]
            return name
        
        return '未命名项目'
    
    def _determine_solution_type(self, requirements: List[Dict]) -> str:
        """确定方案类型"""
        requirement_text = ' '.join([req['description'] for req in requirements])
        
        if any(word in requirement_text for word in ['云', '虚拟化', 'SaaS']):
            return '云计算解决方案'
        elif any(word in requirement_text for word in ['大数据', '数据分析', '数据仓库']):
            return '大数据解决方案'
        elif any(word in requirement_text for word in ['AI', '人工智能', '机器学习']):
            return 'AI智能解决方案'
        elif any(word in requirement_text for word in ['物联网', 'IoT', '传感器']):
            return '物联网解决方案'
        else:
            return '信息化系统解决方案'
    
    def _estimate_budget(self, requirements: List[Dict]) -> str:
        """估算预算"""
        # 简化的预算估算逻辑
        req_count = len(requirements)
        if req_count > 15:
            return '500-800万元'
        elif req_count > 10:
            return '300-500万元'
        elif req_count > 5:
            return '100-300万元'
        else:
            return '50-100万元'
    
    def _estimate_duration(self, requirements: List[Dict]) -> str:
        """估算工期"""
        # 简化的工期估算逻辑
        req_count = len(requirements)
        if req_count > 15:
            return '6-8个月'
        elif req_count > 10:
            return '4-6个月'
        elif req_count > 5:
            return '3-4个月'
        else:
            return '2-3个月'


def generate_solution(bid_analysis: Dict) -> Dict:
    """
    技术方案生成入口函数
    
    参数:
        bid_analysis: 标书解析结果
    
    返回:
        Dict: 技术方案
    """
    generator = SolutionGenerator()
    return generator.generate(bid_analysis)