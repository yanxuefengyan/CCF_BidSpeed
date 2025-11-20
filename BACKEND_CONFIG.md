# 后端API配置指南

## 1. 环境准备

### 1.1 安装依赖
```bash
pip install -r requirements.txt
```

### 1.2 创建必要的目录
系统会自动创建以下目录（如果不存在）：
- `uploads/` - 存储上传的文件
- `data/` - 存储数据库文件

## 2. API密钥配置

### 2.1 获取文心一言API密钥
1. 访问百度智能云平台：https://console.bce.baidu.com/
2. 创建应用并获取 API Key 和 Secret Key
3. 在项目根目录创建 `.env` 文件

### 2.2 配置 .env 文件
复制 `.env.example` 为 `.env`，然后填入您的密钥：

```
WENXIN_API_KEY=your_actual_api_key
WENXIN_SECRET_KEY=your_actual_secret_key
```

### 2.3 修改代码以读取环境变量
在 `app.py` 开头添加：

```python
from dotenv import load_dotenv
load_dotenv()

# 读取环境变量
WENXIN_API_KEY = os.getenv('WENXIN_API_KEY')
WENXIN_SECRET_KEY = os.getenv('WENXIN_SECRET_KEY')
```

## 3. 配置文件说明 (config.json)

### 3.1 基础配置
```json
{
  "app_name": "标书速读 - BidSpeed",
  "version": "1.0.0",
  "debug": true
}
```

### 3.2 AI服务配置
```json
{
  "ai_service": {
    "provider": "wenxin",
    "api_endpoint": "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro",
    "timeout": 30
  }
}
```

### 3.3 上传配置
```json
{
  "upload": {
    "max_file_size": "16MB",
    "allowed_extensions": ["pdf", "docx", "doc", "txt"],
    "storage_path": "uploads/"
  }
}
```

## 4. API端点详解

### 4.1 文件上传 API
**端点：** `POST /api/upload`

**请求格式：**
- Content-Type: multipart/form-data
- 字段：file (文件)

**响应示例：**
```json
{
  "message": "文件上传成功",
  "filename": "标书.pdf",
  "file_path": "uploads/标书.pdf",
  "processing_result": {...}
}
```

### 4.2 标书解析 API
**端点：** `POST /api/analyze`

**请求格式：**
```json
{
  "file_path": "uploads/标书.pdf"
}
```

**响应示例：**
```json
{
  "success": true,
  "metadata": {
    "total_words": 1580,
    "key_points_count": 15
  },
  "ai_summary": {...},
  "tech_checklist": [...],
  "tech_specifications": [...],
  "scoring_rules": [...]
}
```

### 4.3 生成技术方案 API
**端点：** `POST /api/generate-solution`

**请求格式：**
```json
{
  "bid_analysis": {
    "metadata": {...},
    "ai_summary": {...}
  }
}
```

### 4.4 查找供应商 API
**端点：** `POST /api/find-suppliers`

**请求格式：**
```json
{
  "requirements": {
    "product_names": ["服务器", "交换机"],
    "tech_requirements": ["Intel Xeon", "128GB"],
    "industry": "IT设备",
    "budget_range": "500万元"
  }
}
```

## 5. 启动应用

### 5.1 开发环境
```bash
python app.py
```
应用将在 http://localhost:5000 启动

### 5.2 生产环境
使用 gunicorn：
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 6. 模块功能说明

### 6.1 document_processor.py
负责处理上传的文档，提取文本内容

### 6.2 bid_analyzer.py
使用AI分析标书内容，提取关键信息

### 6.3 solution_generator.py
基于标书分析生成技术方案

### 6.4 supplier_finder.py
搜索并推荐符合要求的供应商

## 7. 常见问题

### 7.1 文件上传失败
- 检查文件大小是否超过16MB
- 确认文件格式是否支持（PDF、DOCX、DOC、TXT）
- 确保 `uploads/` 目录有写入权限

### 7.2 API调用超时
- 检查网络连接
- 调整 `config.json` 中的 `timeout` 配置
- 验证API密钥是否正确

### 7.3 AI服务调用失败
- 确认已正确配置 `.env` 文件
- 检查API密钥是否有效
- 确认账户余额是否充足

## 8. 安全建议

1. **不要将 `.env` 文件提交到版本控制系统**
2. **生产环境关闭 debug 模式**
3. **使用 HTTPS 协议**
4. **添加请求频率限制**
5. **验证上传文件的安全性**

## 9. 性能优化

1. **使用缓存**：缓存频繁访问的数据
2. **异步处理**：对于耗时操作使用异步任务队列
3. **文件清理**：定期清理过期的上传文件
4. **日志记录**：记录所有API调用和错误信息

## 10. 技术支持

如有问题，请联系：
- 技术负责人：严工
- 联系电话：18971087214