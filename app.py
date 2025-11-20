from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import json
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 导入自定义模块
from modules.document_processor import process_document
from modules.bid_analyzer import analyze_bid
from modules.solution_generator import generate_solution
from modules.supplier_finder import find_suppliers

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

# 从环境变量和配置文件加载配置
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 环境变量配置
WENXIN_API_KEY = os.getenv('WENXIN_API_KEY')
WENXIN_SECRET_KEY = os.getenv('WENXIN_SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
PORT = int(os.getenv('PORT', 5000))
HOST = os.getenv('HOST', '0.0.0.0')

# 配置上传文件存储
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB 最大上传限制

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """文档上传接口"""
    if 'file' not in request.files:
        return jsonify({'error': '没有文件'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    
    if file and allowed_file(file.filename):
        # 保存原始文件名用于显示
        original_filename = file.filename
        
        # 使用时间戳生成安全的存储文件名，同时保留扩展名
        import time
        timestamp = str(int(time.time() * 1000))
        file_ext = os.path.splitext(original_filename)[1]
        safe_filename = f"{timestamp}{file_ext}"
        
        # 保存文件到两个位置：
        # 1. 使用时间戳文件名保存（用于后端处理）
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
        file.save(file_path)
        
        # 2. 同时保存原始文件名的副本（用于保留原始文件）
        original_file_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
        import shutil
        shutil.copy2(file_path, original_file_path)
        
        # 处理上传的文档
        result = process_document(file_path)
        
        return jsonify({
            'message': '文件上传成功',
            'filename': original_filename,  # 返回原始文件名用于显示
            'file_path': file_path,
            'original_file_path': original_file_path,  # 返回原始文件路径
            'processing_result': result
        })
    
    return jsonify({'error': '不支持的文件类型'}), 400

@app.route('/api/analyze', methods=['POST'])
def analyze_document():
    """标书解析接口"""
    data = request.json
    file_path = data.get('file_path')
    
    if not file_path or not os.path.exists(file_path):
        return jsonify({'error': '文件不存在'}), 400
    
    analysis_result = analyze_bid(file_path)
    return jsonify(analysis_result)

@app.route('/api/generate-solution', methods=['POST'])
def create_solution():
    """生成技术方案接口"""
    data = request.json
    bid_analysis = data.get('bid_analysis')
    
    if not bid_analysis:
        return jsonify({'error': '缺少标书解析数据'}), 400
    
    solution = generate_solution(bid_analysis)
    return jsonify(solution)

@app.route('/api/find-suppliers', methods=['POST'])
def search_suppliers():
    """寻找供应商接口"""
    data = request.json
    requirements = data.get('requirements')
    
    if not requirements:
        return jsonify({'error': '缺少供应商需求数据'}), 400
    
    suppliers = find_suppliers(requirements)
    return jsonify(suppliers)

# 服务前端静态文件
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    # 检查必要的配置
    if not WENXIN_API_KEY:
        print("⚠️  警告: 未找到 WENXIN_API_KEY 环境变量")
        print("   请创建 .env 文件并添加您的API密钥")
    
    print(f"🚀 启动 {config.get('app_name', 'BidSpeed')} v{config.get('version', '1.0.0')}")
    print(f"📡 服务地址: http://{HOST}:{PORT}")
    print(f"📁 上传目录: {UPLOAD_FOLDER}")
    print(f"🤖 AI服务: {config['ai_service']['provider']}")
    
    app.run(debug=DEBUG, host=HOST, port=PORT)