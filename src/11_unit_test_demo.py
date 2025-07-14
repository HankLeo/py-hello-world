"""
Python unittest 单元测试框架用法示例

"""

import unittest
from unittest import mock

from src.unit_test_class import Calculator


# 测试类，继承自unittest.TestCase
class TestCalculator(unittest.TestCase):
    """Calculator类的测试用例"""

    def setUp(self):
        """在每个测试方法前运行"""
        self.calc = Calculator()
        print("\n准备测试环境...")

    def tearDown(self):
        """在每个测试方法后运行"""
        print("清理测试环境...")

    def test_add(self):
        """测试加法"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """测试减法"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiply(self):
        """测试乘法"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """测试除法"""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=6)

        # 测试异常
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_square_root(self):
        """测试平方根"""
        self.assertAlmostEqual(self.calc.square_root(4), 2)
        self.assertAlmostEqual(self.calc.square_root(2), 1.414214, places=6)

        # 测试异常
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    @unittest.skip("暂时跳过这个测试")
    def test_skip_example(self):
        """跳过测试的示例"""
        self.fail("这个测试不应该运行")


# 测试套件示例
def suite():
    """自定义测试套件"""
    test_suite = unittest.TestSuite()
    # 添加特定测试
    test_suite.addTest(TestCalculator('test_add'))
    test_suite.addTest(TestCalculator('test_multiply'))
    return test_suite


# 模拟对象测试示例
class TestMockExample(unittest.TestCase):
    """模拟对象测试示例"""

    def test_mock_method(self):
        """模拟方法测试"""
        # 创建Calculator实例
        calc = Calculator()

        # 使用patch模拟get_random_number方法
        with mock.patch.object(calc, 'get_random_number', return_value=42) as mocked_method:
            result = calc.get_random_number()

            # 验证
            self.assertEqual(result, 42)
            mocked_method.assert_called_once()

    def test_mock_whole_class(self):
        """模拟整个类"""
        # 模拟Calculator类
        with mock.patch('src.unit_test_class.Calculator') as MockCalculator:
            # 设置模拟类的行为
            mock_instance = MockCalculator.return_value
            mock_instance.add.return_value = 10

            # 使用模拟类
            # calc = Calculator() 不可以直接实例化Calculator类，因为它被mock了
            calc = MockCalculator()
            result = calc.add(3, 7)

            # 验证
            self.assertEqual(result, 10)
            mock_instance.add.assert_called_once_with(3, 7)


if __name__ == "__main__":
    # 运行所有测试
    print("=== 运行所有测试 ===")
    unittest.main(verbosity=2)

    # 或者运行自定义测试套件
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite())
