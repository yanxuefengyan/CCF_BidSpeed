# 快速启动指南

## 第一步：安装依赖

```bash
pip install -r requirements.txt
```

如果遇到网络问题，可以使用国内镜像：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 第二步：启动应用

### 方式1：使用启动脚本（推荐）

```bash
python run.py
```

这个脚本会自动：
- ✓ 检查依赖是否完整
- ✓ 创建必要的目录
- ✓ 初始化测试数据
- ✓ 启动应用并打开浏览器

### 方式2：直接启动

```bash
python app.py
```

然后在浏览器中访问：http://localhost:5000

## 第三步：测试功能

### 功能测试清单

1. **上传标书** ✓
   - 支持PDF、Word格式
   - 拖拽或点击上传
   - 最大16MB限制

2. **解读分析** ✓
   - AI智能总结
   - 技术条款清单
   - 评分标准提取

3. **生成方案** ✓
   - 自动匹配技术方案
   - 系统架构设计
   - 实施计划制定
   - 技术偏离表

4. **查找供应商** ✓
   - 智能搜索供应商
   - 企业信用评级
   - 联系方式获取
   - TOP3推荐排序

## 测试数据

项目自带测试标书文件：`test_data/sample_bid.txt`

这是一个完整的标书样例，包含：
- 项目概况
- 技术要求
- 功能需求
- 商务条款
- 评分标准
- 重要日期

## 常见问题

### Q1: 启动失败提示缺少模块？
**A:** 运行 `pip install -r requirements.txt` 安装所有依赖

### Q2: 上传文件后无响应？
**A:** 检查 `uploads/` 目录是否存在，如果不存在运行 `mkdir uploads`

### Q3: AI分析结果不准确？
**A:** 目前使用的是模拟数据。如需使用真实AI服务，请在 `config.json` 中配置文心一言API密钥

### Q4: 如何导出分析结果？
**A:** 导出功能正在开发中，当前版本可以通过浏览器打印功能保存为PDF

### Q5: 供应商信息是真实的吗？
**A:** 当前版本使用的是模拟数据。实际应用中会连接企业信用查询系统和招投标平台获取真实数据

## 进阶配置

### 配置文件说明

`config.json` 主要配置项：

```json
{
  "api_key": "",           // 文心一言API密钥（可选）
  "upload": {
    "max_file_size": "16MB",
    "allowed_extensions": ["pdf", "docx", "doc"]
  }
}
```

### API密钥获取

1. 访问百度智能云：https://cloud.baidu.com
2. 注册并创建应用
3. 获取API Key和Secret Key
4. 填入 `config.json` 的 `api_key` 字段

## 下一步

- 查看 `README.md` 了解项目详细信息
- 运行 `python test_system.py` 进行系统测试
- 访问 `/api/` 查看API文档（开发中）

## 技术支持

如遇到问题，请查看：
1. 错误日志（控制台输出）
2. 浏览器开发者工具（F12）
3. 项目文档：README.md

祝您使用愉快！🎉