# 标书速读 - BidSpeed

## 项目简介

「标书速读 · BidSpeed」是一个专业的标书处理系统，能够帮助用户快速完成标书解读、技术方案生成和供应商寻源。



功能测试视频：https://live.csdn.net/v/501779



### 核心功能

1. **一键解读与总结** - 支持PDF/Word文档上传，AI自动提取技术规范、评分细则、合同条款
2. **一键制作技术实现方案** - 根据标书要求自动生成技术方案、系统架构和实施计划
3. **全网寻找供应商** - 智能搜索合格供应商，提供前3家的详细信息

### 技术架构

- **后端**: Python + Flask
- **前端**: Vue 3 + Element Plus
- **AI服务**: 文心一言API集成
- **文档处理**: PyPDF2 + python-docx
- **数据存储**: SQLite + 文件存储

## 快速开始

### 环境要求

- Python 3.8+
- pip

### 安装依赖

```bash
# 安装Python依赖
pip install -r requirements.txt
```

### 配置设置

1. 复制配置文件并修改API密钥：
```bash
cp config.json config.local.json
```

2. 在 `config.local.json` 中填入您的文心一言API密钥：
```json
{
  "api_key": "YOUR_API_KEY_HERE"
}
```

### 启动应用

```bash
# 启动后端服务
python app.py
```

应用将在 http://localhost:5000 启动

### 使用说明

1. **上传标书**: 支持PDF、Word格式，最大16MB
2. **解读分析**: 点击"开始解读标书"按钮，AI将自动分析文档内容
3. **生成方案**: 基于解读结果，自动生成技术实现方案
4. **查找供应商**: 根据技术要求，搜索并推荐合适的供应商

## 项目结构

```
├── app.py                 # Flask主应用
├── config.json           # 配置文件
├── requirements.txt      # Python依赖
├── modules/              # 核心功能模块
│   ├── document_processor.py    # 文档处理
│   ├── bid_analyzer.py          # 标书解析
│   ├── solution_generator.py    # 方案生成
│   └── supplier_finder.py       # 供应商查找
├── frontend/             # 前端文件
│   ├── index.html       # 主页面
│   └── app.js           # 前端逻辑
├── uploads/             # 上传文件存储
└── test_data/           # 测试数据
```

## 功能特性

### 智能解读
- 自动识别技术规格和评分标准
- 生成结构化的技术条款清单
- AI总结核心需求和关键要点

### 方案生成
- 匹配最佳技术解决方案
- 自动生成系统架构图
- 制定详细实施计划
- 生成技术偏离表

### 供应商寻源
- 全网智能搜索供应商
- 提供企业信用评级
- 展示历史项目业绩
- 自动排序推荐前3家

## 开发计划

- [x] 基础功能实现
- [x] 前端界面开发
- [ ] AI集成优化
- [ ] 导出功能完善
- [ ] 用户权限管理
- [ ] 数据统计分析

## 贡献指南

欢迎提交Issue和Pull Request来改进项目。

## 许可证

MIT License