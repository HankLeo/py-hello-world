"""
Python 高阶函数和匿名函数演示
涵盖内容：lambda, map, filter, reduce, 闭包, 装饰器, 排序等
"""

from functools import reduce
from typing import Callable


# ==================== 1. 匿名函数 lambda ====================
def lambda_demo():
    """lambda 基本用法"""

    # 传统函数定义
    def square(x): return x ** 2

    # lambda 等价形式
    square_lambda = lambda x: x ** 2

    print(f"传统函数: {square(5)}")  # 输出: 25
    print(f"lambda函数: {square_lambda(5)}")  # 输出: 25

    # 立即调用的lambda (IIFE)
    print((lambda x, y: x + y)(3, 4))  # 输出: 7


# ==================== 2. 高阶函数 ====================
def higher_order_demo():
    """map, filter, reduce 演示"""
    numbers = [1, 2, 3, 4, 5]

    # map: 对每个元素应用函数
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"map平方: {squared}")  # 输出: [1, 4, 9, 16, 25]

    # filter: 过滤元素
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter偶数: {evens}")  # 输出: [2, 4]

    # reduce: 累积计算
    product = reduce(lambda x, y: x * y, numbers)
    print(f"reduce乘积: {product}")  # 输出: 120 (1*2*3*4*5)


# ==================== 3. 闭包 ====================
def closure_demo():
    """闭包：函数记住其定义时的环境"""

    def make_multiplier(factor):
        def multiplier(x):
            return x * factor

        return multiplier

    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(f"闭包2倍: {double(5)}")  # 输出: 10
    print(f"闭包3倍: {triple(5)}")  # 输出: 15


# ==================== 4. 装饰器 ====================
def decorator_demo():
    """装饰器：修改或增强函数行为"""

    def simple_decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(f"即将调用函数: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"函数调用完成")
            return result

        return wrapper

    @simple_decorator
    def greet(name):
        print(f"Hello, {name}!")

    greet("Python")  # 输出带装饰器的问候语


# ==================== 5. 高级排序 ====================
def sorting_demo():
    """使用lambda进行复杂排序"""
    students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 72},
        {"name": "Charlie", "grade": 90}
    ]

    # 按成绩降序排序
    sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
    print("按成绩排序:")
    for student in sorted_students:
        print(f"{student['name']}: {student['grade']}")


# ==================== 6. 函数柯里化 ====================
def currying_demo():
    """柯里化：分步传递参数"""

    def add_numbers(a):
        def add_b(b):
            def add_c(c):
                return a + b + c

            return add_c

        return add_b

    # 传统调用
    print(add_numbers(1)(2)(3))  # 输出: 6

    # 分步调用
    add_1 = add_numbers(1)
    add_2 = add_1(2)
    result = add_2(3)
    print(f"柯里化结果: {result}")  # 输出: 6


# ==================== 主程序 ====================
if __name__ == "__main__":
    print("===== lambda演示 =====")
    lambda_demo()

    print("\n===== 高阶函数演示 =====")
    higher_order_demo()

    print("\n===== 闭包演示 =====")
    closure_demo()

    print("\n===== 装饰器演示 =====")
    decorator_demo()

    print("\n===== 高级排序演示 =====")
    sorting_demo()

    print("\n===== 柯里化演示 =====")
    currying_demo()
