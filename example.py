#!/usr/bin/env python3
"""
GitHub MCP 示例 Python 脚本

这个脚本展示了如何使用 Python 进行一些基本操作。
"""

def greet(name: str) -> str:
    """
    返回一个问候语
    
    Args:
        name: 要问候的名字
        
    Returns:
        包含问候语的字符串
    """
    return f"你好, {name}! 欢迎使用 GitHub MCP!"

def main():
    """主函数"""
    name = "GitHub 用户"
    message = greet(name)
    print(message)
    
    # 演示一些基本操作
    numbers = [1, 2, 3, 4, 5]
    doubled = [x * 2 for x in numbers]
    print(f"原始数字: {numbers}")
    print(f"翻倍后: {doubled}")

if __name__ == "__main__":
    main()