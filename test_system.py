"""
系统功能测试脚本
测试各个模块的核心功能
"""
import os
import sys

def test_document_processor():
    """测试文档处理模块"""
    print("\n=== 测试文档处理模块 ===")
    try:
        from modules.document_processor import process_document
        
        # 使用测试数据
        test_file = 'test_data/sample_bid.txt'
        if os.path.exists(test_file):
            result = process_document(test_file)
            if result.get('success'):
                print("✓ 文档处理模块正常")
                print(f"  - 文件名: {result['file_name']}")
                print(f"  - 文本长度: {result['text_length']} 字符")
                return True
            else:
                print(f"✗ 文档处理失败: {result.get('error')}")
                return False
        else:
            print("✗ 测试文件不存在")
            return False
    except Exception as e:
        print(f"✗ 模块导入失败: {e}")
        return False

def test_bid_analyzer():
    """测试标书解析模块"""
    print("\n=== 测试标书解析模块 ===")
    try:
        from modules.bid_analyzer import analyze_bid
        
        test_file = 'test_data/sample_bid.txt'
        if os.path.exists(test_file):
            result = analyze_bid(test_file)
            if result.get('success'):
                print("✓ 标书解析模块正常")
                print(f"  - 关键要点数: {result['metadata']['key_points_count']}")
                print(f"  - 技术规格数: {len(result['tech_specifications'])}")
                print(f"  - 评分规则数: {len(result['scoring_rules'])}")
                return True
            else:
                print(f"✗ 标书解析失败: {result.get('error')}")
                return False
        else:
            print("✗ 测试文件不存在")
            return False
    except Exception as e:
        print(f"✗ 模块测试失败: {e}")
        return False

def test_solution_generator():
    """测试方案生成模块"""
    print("\n=== 测试方案生成模块 ===")
    try:
        from modules.solution_generator import generate_solution
        from modules.bid_analyzer import analyze_bid
        
        test_file = 'test_data/sample_bid.txt'
        if os.path.exists(test_file):
            # 先解析标书
            analysis = analyze_bid(test_file)
            if analysis.get('success'):
                # 生成方案
                result = generate_solution(analysis)
                if result.get('success'):
                    print("✓ 方案生成模块正常")
                    print(f"  - 方案类型: {result['solution_overview']['solution_type']}")
                    print(f"  - 预算估算: {result['solution_overview']['total_budget_estimate']}")
                    print(f"  - 工期估算: {result['solution_overview']['implementation_duration']}")
                    print(f"  - 匹配方案数: {len(result['technical_solutions'])}")
                    return True
                else:
                    print("✗ 方案生成失败")
                    return False
            else:
                print("✗ 标书解析失败，无法测试方案生成")
                return False
        else:
            print("✗ 测试文件不存在")
            return False
    except Exception as e:
        print(f"✗ 模块测试失败: {e}")
        return False

def test_supplier_finder():
    """测试供应商查找模块"""
    print("\n=== 测试供应商查找模块 ===")
    try:
        from modules.supplier_finder import find_suppliers
        
        # 模拟需求
        requirements = {
            'product_names': ['服务器', '交换机'],
            'tech_requirements': ['Intel Xeon处理器', '128GB内存'],
            'industry': 'IT设备',
            'budget_range': '500万元'
        }
        
        result = find_suppliers(requirements)
        if result.get('success'):
            print("✓ 供应商查找模块正常")
            print(f"  - 找到供应商数: {result['total_found']}")
            print(f"  - 推荐前3家:")
            for i, supplier in enumerate(result['top_suppliers'], 1):
                print(f"    {i}. {supplier['name']} (评分: {supplier['total_score']})")
            return True
        else:
            print("✗ 供应商查找失败")
            return False
    except Exception as e:
        print(f"✗ 模块测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("\n" + "="*50)
    print("标书速读(BidSpeed)系统功能测试")
    print("="*50)
    
    results = []
    
    # 测试各个模块
    results.append(("文档处理", test_document_processor()))
    results.append(("标书解析", test_bid_analyzer()))
    results.append(("方案生成", test_solution_generator()))
    results.append(("供应商查找", test_supplier_finder()))
    
    # 输出测试总结
    print("\n" + "="*50)
    print("测试总结")
    print("="*50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{name}: {status}")
    
    print(f"\n总计: {passed}/{total} 测试通过")
    
    if passed == total:
        print("\n🎉 所有测试通过！系统可以正常使用。")
        return 0
    else:
        print("\n⚠️ 部分测试失败，请检查相关模块。")
        return 1

if __name__ == "__main__":
    sys.exit(main())