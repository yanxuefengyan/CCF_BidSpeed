"""
启动脚本 - 标书速读(BidSpeed)应用
"""
import os
import sys
import json
import time
import webbrowser
from threading import Timer

def check_dependencies():
    """检查依赖是否已安装"""
    print("检查依赖...")
    
    try:
        import flask
        import flask_cors
        import PyPDF2
        print("✓ 依赖检查通过")
        return True
    except ImportError as e:
        print(f"✗ 缺少依赖: {e}")
        print("请先运行: pip install -r requirements.txt")
        return False

def check_config():
    """检查配置文件"""
    print("检查配置...")
    
    if not os.path.exists('config.json'):
        print("✗ 未找到配置文件")
        return False
    
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 检查必要的配置项
        if not config.get('upload', {}).get('storage_path'):
            print("✗ 配置文件缺少上传路径设置")
            return False
        
        print("✓ 配置检查通过")
        return True
    except Exception as e:
        print(f"✗ 配置文件读取失败: {e}")
        return False

def create_directories():
    """创建必要的目录"""
    print("创建必要的目录...")
    
    # 创建上传目录
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        print("✓ 创建上传目录: uploads/")
    
    # 创建数据目录
    if not os.path.exists('data'):
        os.makedirs('data')
        print("✓ 创建数据目录: data/")
    
    return True

def open_browser():
    """在默认浏览器中打开应用"""
    webbrowser.open('http://localhost:5000')

def run_app():
    """运行Flask应用"""
    print("正在启动应用...")
    
    # 延迟1秒后自动打开浏览器
    Timer(1, open_browser).start()
    
    # 导入主应用模块
    from app import app
    
    # 启动Flask应用
    app.run(debug=True, host='0.0.0.0', port=5000)

def create_test_data():
    """准备测试数据"""
    print("准备测试数据...")
    
    # 创建上传目录中的测试文件
    test_upload_path = os.path.join('uploads', 'sample_bid.pdf')
    
    if not os.path.exists(test_upload_path) and os.path.exists('test_data/sample_bid.txt'):
        # 复制测试数据到上传目录
        with open('test_data/sample_bid.txt', 'r', encoding='utf-8') as source:
            content = source.read()
            
        # 创建一个模拟的处理结果
        with open(test_upload_path.replace('.pdf', '.txt'), 'w', encoding='utf-8') as target:
            target.write(content)
            
        print(f"✓ 测试数据已准备: {test_upload_path.replace('.pdf', '.txt')}")
    
    return True

def setup_modules():
    """初始化模块目录"""
    print("初始化模块...")
    
    if not os.path.exists('modules/__init__.py'):
        os.makedirs('modules', exist_ok=True)
        # 创建__init__.py文件
        with open('modules/__init__.py', 'w', encoding='utf-8') as f:
            f.write('# 模块初始化文件\n')
        print("✓ 初始化模块目录")
    
    return True

def main():
    """主函数"""
    print("\n=== 标书速读(BidSpeed)启动助手 ===\n")
    
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    # 检查配置
    if not check_config():
        print("\n请检查配置文件后重试")
        sys.exit(1)
    
    # 创建目录
    create_directories()
    
    # 初始化模块
    setup_modules()
    
    # 准备测试数据
    create_test_data()
    
    print("\n=== 启动应用 ===\n")
    print("应用将在浏览器中自动打开: http://localhost:5000")
    print("按 Ctrl+C 可以停止服务\n")
    
    # 运行应用
    run_app()

if __name__ == "__main__":
    main()