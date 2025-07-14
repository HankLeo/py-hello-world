from math import sqrt


# 要测试的类
class Calculator:
    """简单的计算器类"""

    def add(self, a, b):
        """加法"""
        return a + b

    def subtract(self, a, b):
        """减法"""
        return a - b

    def multiply(self, a, b):
        """乘法"""
        return a * b

    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

    def square_root(self, x):
        """平方根"""
        if x < 0:
            raise ValueError("不能计算负数的平方根")
        return sqrt(x)

    def get_random_number(self):
        """获取随机数（模拟需要mock的方法）"""
        import random
        return random.randint(1, 100)
