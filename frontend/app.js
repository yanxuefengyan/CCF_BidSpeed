const { createApp, ref, reactive } = Vue;

const app = createApp({
    setup() {
        const uploadUrl = '/api/upload';
        const uploadedFile = ref(null);
        const analyzing = ref(false);
        const analysisResult = ref(null);
        const activeTab = ref('summary');
        const generatingSolution = ref(false);
        const solutionResult = ref(null);
        const solutionTab = ref('solutions');
        const searchingSuppliers = ref(false);
        const supplierResult = ref(null);
        const showUpload = ref(false);
        const currentPage = ref('home');

        const goToPage = (page) => {
            currentPage.value = page;
            if (page === 'upload') {
                showUpload.value = true;
            } else if (page === 'support') {
                // 显示技术支持联系方式 - 使用可靠的alert替代ElMessageBox
                alert('技术负责人：严工\n联系电话：18971087214');
                // 重置页面状态，保持在当前页面
                currentPage.value = 'home';
                showUpload.value = false;
            } else {
                showUpload.value = false;
            }
        };

        const startUsing = () => {
            showUpload.value = true;
        };

        const watchDemo = () => {
            // 加载演示数据
            loadDemoData();
        };
        
        const loadDemoData = () => {
            // 模拟已上传文件
            uploadedFile.value = {
                filename: 'demo_bid.pdf',
                file_path: 'test_data/sample_bid.txt'
            };
            
            // 加载演示的解析结果
            analysisResult.value = {
                success: true,
                metadata: {
                    total_words: 1580,
                    key_points_count: 15
                },
                ai_summary: {
                    核心需求总结: "本项目为某政府部门信息化系统建设项目，预算500万元，工期6个月。主要建设内容包括硬件设备采购（服务器、网络设备）、软件系统开发（支持微服务架构、前后端分离）以及安全防护体系搭建（等保三级）。",
                    关键技术要点: [
                        "采用微服务架构，前后端分离设计",
                        "数据库选用MySQL 8.0或PostgreSQL 14",
                        "符合等级保护三级安全标准",
                        "支持多因素认证和数据加密",
                        "提供移动端适配和系统集成接口"
                    ],
                    重要时间节点: {
                        "投标截止": "2025-12-15",
                        "开标时间": "2025-12-20",
                        "项目启动": "2026-01-01",
                        "预计验收": "2026-06-30"
                    }
                },
                tech_checklist: [
                    { item: "服务器配置：双路CPU，128GB内存，2TB存储", page: 1, score: 15, priority: "high" },
                    { item: "核心交换机、防火墙、负载均衡器", page: 1, score: 10, priority: "high" },
                    { item: "操作系统：Linux CentOS 8或更高版本", page: 1, score: 5, priority: "medium" },
                    { item: "数据库：MySQL 8.0或PostgreSQL 14", page: 1, score: 8, priority: "high" },
                    { item: "支持微服务架构，前后端分离", page: 1, score: 10, priority: "high" },
                    { item: "符合等级保护三级标准", page: 1, score: 12, priority: "high" },
                    { item: "支持多因素认证", page: 1, score: 8, priority: "medium" },
                    { item: "数据加密传输和存储", page: 2, score: 8, priority: "high" },
                    { item: "用户管理模块", page: 2, score: 6, priority: "medium" },
                    { item: "工作流引擎", page: 2, score: 8, priority: "medium" },
                    { item: "数据分析和可视化", page: 2, score: 7, priority: "medium" },
                    { item: "移动端适配", page: 2, score: 6, priority: "low" },
                    { item: "系统集成接口", page: 2, score: 8, priority: "medium" },
                    { item: "7*24小时售后服务，2小时内响应", page: 3, score: 5, priority: "medium" },
                    { item: "3年质保期", page: 3, score: 3, priority: "low" }
                ],
                tech_specifications: [
                    { category: "硬件要求", content: "服务器：双路CPU，128GB内存，2TB存储" },
                    { category: "硬件要求", content: "网络设备：核心交换机、防火墙、负载均衡器" },
                    { category: "软件要求", content: "操作系统：Linux CentOS 8或更高版本" },
                    { category: "软件要求", content: "数据库：MySQL 8.0或PostgreSQL 14" },
                    { category: "软件要求", content: "应用框架：支持微服务架构，前后端分离" },
                    { category: "安全要求", content: "符合等级保护三级标准" },
                    { category: "安全要求", content: "支持多因素认证" },
                    { category: "安全要求", content: "数据加密传输和存储" }
                ],
                scoring_rules: [
                    { category: "技术方案", item: "系统架构设计", score: 15, weight: "15%" },
                    { category: "技术方案", item: "功能实现方案", score: 15, weight: "15%" },
                    { category: "技术方案", item: "安全保障措施", score: 10, weight: "10%" },
                    { category: "投标人资质", item: "相关项目经验", score: 15, weight: "15%" },
                    { category: "投标人资质", item: "技术团队实力", score: 15, weight: "15%" },
                    { category: "商务报价", item: "价格合理性", score: 20, weight: "20%" },
                    { category: "服务方案", item: "售后服务", score: 10, weight: "10%" }
                ]
            };
            
            // 加载演示的技术方案
            solutionResult.value = {
                success: true,
                solution_overview: {
                    solution_type: "微服务架构云原生解决方案",
                    total_budget_estimate: "480万元",
                    implementation_duration: "6个月"
                },
                technical_solutions: [
                    {
                        solution_name: "微服务架构方案",
                        match_score: "95%",
                        advantages: [
                            "高度模块化，易于维护和扩展",
                            "支持独立部署和弹性伸缩",
                            "技术栈灵活，可针对不同服务选择最优技术"
                        ]
                    },
                    {
                        solution_name: "容器化部署方案",
                        match_score: "90%",
                        advantages: [
                            "环境一致性，减少部署问题",
                            "资源利用率高，降低硬件成本",
                            "支持快速回滚和灰度发布"
                        ]
                    },
                    {
                        solution_name: "DevOps自动化方案",
                        match_score: "88%",
                        advantages: [
                            "持续集成/持续部署，提升交付效率",
                            "自动化测试，保障代码质量",
                            "运维自动化，降低人工成本"
                        ]
                    }
                ],
                system_architecture: {
                    layers: [
                        {
                            name: "前端展示层",
                            components: ["Web前端", "移动端APP", "管理后台"],
                            technologies: ["Vue.js 3", "React Native", "Element Plus"]
                        },
                        {
                            name: "API网关层",
                            components: ["API网关", "负载均衡", "认证授权"],
                            technologies: ["Kong", "Nginx", "OAuth 2.0"]
                        },
                        {
                            name: "微服务层",
                            components: ["用户服务", "工作流服务", "数据分析服务"],
                            technologies: ["Spring Boot", "Node.js", "Python"]
                        },
                        {
                            name: "数据存储层",
                            components: ["关系数据库", "缓存", "对象存储"],
                            technologies: ["PostgreSQL 14", "Redis", "MinIO"]
                        }
                    ]
                },
                implementation_plan: {
                    phases: [
                        {
                            phase: "需求分析与设计",
                            duration_weeks: 4,
                            start_date: "2026-01-01",
                            end_date: "2026-01-28",
                            deliverables: ["需求规格说明书", "系统设计方案", "原型设计"]
                        },
                        {
                            phase: "系统开发",
                            duration_weeks: 12,
                            start_date: "2026-01-29",
                            end_date: "2026-04-22",
                            deliverables: ["核心功能模块", "API接口", "前端界面"]
                        },
                        {
                            phase: "测试与优化",
                            duration_weeks: 4,
                            start_date: "2026-04-23",
                            end_date: "2026-05-20",
                            deliverables: ["测试报告", "性能优化", "安全加固"]
                        },
                        {
                            phase: "部署与验收",
                            duration_weeks: 4,
                            start_date: "2026-05-21",
                            end_date: "2026-06-17",
                            deliverables: ["系统部署", "用户培训", "验收文档"]
                        }
                    ]
                },
                deviation_table: [
                    {
                        requirement: "操作系统：Linux CentOS 8",
                        our_solution: "采用Ubuntu 22.04 LTS",
                        deviation_status: "正偏离",
                        impact_assessment: "Ubuntu更稳定且支持周期更长"
                    },
                    {
                        requirement: "数据库：MySQL 8.0或PostgreSQL 14",
                        our_solution: "采用PostgreSQL 14",
                        deviation_status: "无偏离",
                        impact_assessment: "完全符合要求"
                    },
                    {
                        requirement: "符合等级保护三级标准",
                        our_solution: "符合等保三级标准",
                        deviation_status: "无偏离",
                        impact_assessment: "完全符合要求"
                    }
                ],
                key_requirements: {
                    product_names: ["服务器", "交换机", "防火墙"],
                    tech_requirements: ["Intel Xeon处理器", "128GB内存", "等保三级"],
                    industry: "IT设备及软件",
                    budget_range: "500万元"
                }
            };
            
            // 加载演示的供应商数据
            supplierResult.value = {
                success: true,
                total_found: 15,
                top_suppliers: [
                    {
                        name: "华为技术有限公司",
                        credit_rating: "AAA",
                        total_score: 95,
                        description: "全球领先的ICT基础设施和智能终端提供商，在企业信息化领域拥有丰富经验和完善的产品体系。",
                        website: "https://www.huawei.com",
                        contact_info: {
                            contact_person: "张经理",
                            phone: "400-822-9999",
                            email: "enterprise@huawei.com",
                            address: "广东省深圳市龙岗区坂田华为基地"
                        },
                        past_projects: [
                            { project_name: "某省政务云平台建设", year: 2024, amount: "1200万元" },
                            { project_name: "某市智慧城市项目", year: 2023, amount: "800万元" }
                        ]
                    },
                    {
                        name: "浪潮电子信息产业股份有限公司",
                        credit_rating: "AAA",
                        total_score: 92,
                        description: "中国领先的云计算、大数据服务商，在政府、企业信息化建设领域拥有深厚积累。",
                        website: "https://www.inspur.com",
                        contact_info: {
                            contact_person: "李经理",
                            phone: "400-860-0011",
                            email: "gov@inspur.com",
                            address: "山东省济南市高新区浪潮路1036号"
                        },
                        past_projects: [
                            { project_name: "某部委大数据平台", year: 2024, amount: "900万元" },
                            { project_name: "某省电子政务系统", year: 2023, amount: "650万元" }
                        ]
                    },
                    {
                        name: "东软集团股份有限公司",
                        credit_rating: "AA+",
                        total_score: 90,
                        description: "中国领先的IT解决方案与服务供应商，在医疗、政府、企业等领域拥有丰富的项目经验。",
                        website: "https://www.neusoft.com",
                        contact_info: {
                            contact_person: "王经理",
                            phone: "400-650-0066",
                            email: "gov@neusoft.com",
                            address: "辽宁省沈阳市浑南区世纪路2号"
                        },
                        past_projects: [
                            { project_name: "某市卫生信息平台", year: 2024, amount: "700万元" },
                            { project_name: "某厅办公自动化系统", year: 2023, amount: "550万元" }
                        ]
                    }
                ]
            };
            
            showUpload.value = true;
            ElMessage.success('演示数据已加载，您可以查看完整的工作流程');
        };

        const handleUploadSuccess = (response) => {
            uploadedFile.value = response;
            ElMessage.success(`文件 ${response.filename} 上传成功`);
            // 重置分析结果，确保"开始解读标书"按钮可见
            analysisResult.value = null;
        };

        const handleUploadError = () => {
            ElMessage.error('文件上传失败，请重试');
            // 清除上传文件状态
            uploadedFile.value = null;
        };

        const beforeUpload = (file) => {
            const isAllowedType = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'].includes(file.type);
            const isLt16M = file.size / 1024 / 1024 < 16;

            if (!isAllowedType) {
                ElMessage.error('只能上传PDF、Word或TXT文档');
            }
            if (!isLt16M) {
                ElMessage.error('文件大小不能超过16MB');
            }
            return isAllowedType && isLt16M;
        };

        const analyzeBid = async () => {
            if (!uploadedFile.value) {
                ElMessage.warning('请先上传标书文件');
                return;
            }
            analyzing.value = true;
            console.log('开始解读标书...'); // 添加调试日志
            try {
                const response = await axios.post('/api/analyze', { file_path: uploadedFile.value.file_path });
                console.log('API Response:', response.data); // 调试日志
                
                if (response.data && response.data.success === true) {
                    // 初始化分析结果的必要字段
                    const result = response.data;
                    
                    // 确保结果中包含所需的对象结构
                    if (!result.metadata) {
                        result.metadata = { 
                            total_words: 0, 
                            key_points_count: 0 
                        };
                    }
                    
                    if (!result.ai_summary) {
                        result.ai_summary = {
                            核心需求总结: "暂无数据",
                            关键技术要点: [],
                            重要时间节点: {}
                        };
                    }
                    
                    if (!result.tech_checklist) {
                        result.tech_checklist = [];
                    }
                    
                    if (!result.tech_specifications) {
                        result.tech_specifications = [];
                    }
                    
                    if (!result.scoring_rules) {
                        result.scoring_rules = [];
                    }
                    
                    analysisResult.value = result;
                    ElMessage.success('标书解读完成');
                } else {
                    ElMessage.error(response.data?.error || '解析失败，返回数据格式不正确');
                    console.error('API返回错误:', response.data);
                    // 清除分析结果，允许重新解读
                    analysisResult.value = null;
                }
            } catch (error) {
                ElMessage.error('标书解读失败，请重试');
                console.error(error);
                // 清除分析结果，允许重新解读
                analysisResult.value = null;
            } finally {
                analyzing.value = false;
            }
            console.log('解读标书完成，analysisResult:', analysisResult.value); // 添加调试日志
        };

        const generateSolution = async () => {
            if (!analysisResult.value) {
                ElMessage.warning('请先完成标书解读');
                return;
            }
            generatingSolution.value = true;
            try {
                const response = await axios.post('/api/generate-solution', { bid_analysis: analysisResult.value });
                solutionResult.value = response.data;
                ElMessage.success('技术方案生成完成');
            } catch (error) {
                ElMessage.error('技术方案生成失败，请重试');
                console.error(error);
            } finally {
                generatingSolution.value = false;
            }
        };

        const findSuppliers = async () => {
            if (!solutionResult.value) {
                ElMessage.warning('请先生成技术方案');
                return;
            }
            searchingSuppliers.value = true;
            try {
                const response = await axios.post('/api/find-suppliers', { requirements: solutionResult.value.key_requirements });
                supplierResult.value = response.data;
                ElMessage.success('供应商查找完成');
            } catch (error) {
                ElMessage.error('供应商查找失败，请重试');
                console.error(error);
            } finally {
                searchingSuppliers.value = false;
            }
        };

        return {
            uploadUrl,
            uploadedFile,
            analyzing,
            analysisResult,
            activeTab,
            generatingSolution,
            solutionResult,
            solutionTab,
            searchingSuppliers,
            supplierResult,
            showUpload,
            currentPage,
            startUsing,
            watchDemo,
            handleUploadSuccess,
            handleUploadError,
            beforeUpload,
            analyzeBid,
            generateSolution,
            findSuppliers,
            goToPage
        };
    }
});

app.use(ElementPlus);
app.mount('#app');