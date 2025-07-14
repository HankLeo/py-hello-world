"""
Python 异常处理 (try-except) 用法示例

异常处理是Python中处理运行时错误的重要机制
"""


def divide_numbers():
    """除法运算示例"""
    print("\n=== 除法运算示例 ===")
    while True:
        try:
            # 获取用户输入
            numerator = float(input("请输入分子: "))
            denominator = float(input("请输入分母: "))

            # 尝试除法运算
            result = numerator / denominator

        except ValueError:
            # 处理输入不是数字的情况
            print("错误: 请输入有效的数字!")

        except ZeroDivisionError:
            # 处理除数为0的情况
            print("错误: 分母不能为零!")

        except Exception as e:
            # 处理其他所有异常
            print(f"发生未知错误: {e}")

        else:
            # 如果没有异常发生，执行这里的代码
            print(f"结果是: {result}")
            break

        finally:
            # 无论是否发生异常，都会执行这里的代码
            print("本次运算结束\n")


def file_operations():
    """文件操作示例"""
    print("\n=== 文件操作示例 ===")
    try:
        # 尝试打开并读取文件
        with open("example.txt", "r") as file:
            content = file.read()
            print("文件内容:", content)

    except FileNotFoundError:
        print("错误: 文件不存在!")

    except PermissionError:
        print("错误: 没有文件访问权限!")

    except IOError as e:
        print(f"文件IO错误: {e}")

    else:
        print("文件读取成功!")

    finally:
        print("文件操作完成\n")


def custom_exception():
    """自定义异常示例"""
    print("\n=== 自定义异常示例 ===")

    class NegativeNumberError(Exception):
        """自定义异常类"""

        def __init__(self, value):
            self.value = value
            super().__init__(f"负数错误: {value} 不能是负数")

    try:
        num = int(input("请输入一个正整数: "))
        if num < 0:
            raise NegativeNumberError(num)  # 相当于Java的throw new
        print(f"你输入的正数是: {num}")

    except NegativeNumberError as e:
        print(e)

    except ValueError:
        print("错误: 请输入有效的整数!")

    finally:
        print("自定义异常测试结束\n")


def multiple_exceptions():
    """捕获多种异常"""
    print("\n=== 捕获多种异常 ===")
    try:
        data = {"key": "value"}
        index = int(input("请输入索引(0或1): "))
        print(data[index])

    except (KeyError, IndexError):
        print("错误: 索引或键不存在!")

    except ValueError:
        print("错误: 请输入0或1!")

    finally:
        print("多种异常测试结束\n")


if __name__ == "__main__":
    # 运行各个示例函数
    divide_numbers()
    file_operations()
    custom_exception()
    multiple_exceptions()
