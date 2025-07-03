"""
Python 循环语句使用示例

Python中有两种主要的循环结构：
1. for循环 - 遍历可迭代对象中的元素
2. while循环 - 在条件为真时重复执行代码块

此外还包括循环控制语句：
- break - 终止整个循环
- continue - 跳过当前迭代，继续下一次循环
- else - 循环正常结束后执行的代码块
"""

# 1. for循环基础
# ==============================================
print("1. for循环基础:")

# 遍历列表
fruits = ["apple", "banana", "cherry"]
print("\n遍历列表:")
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 遍历字符串
print("\n遍历字符串:")
for char in "Python":
    print(char.upper())

# 遍历字典
print("\n遍历字典:")
person = {"name": "张三", "age": 25, "city": "北京"}
for key in person:
    print(f"{key}: {person[key]}")

# 使用items()同时获取键和值
print("\n使用items()遍历字典:")
for key, value in person.items():
    print(f"{key} => {value}")

# 2. range()函数与for循环
# ==============================================
print("\n\n2. range()函数与for循环:")

# 打印0-4
print("\nrange(5):")
for i in range(5):
    print(i, end=" ")

# 打印5-9
print("\nrange(5, 10):")
for i in range(5, 10):
    print(i, end=" ")

# 打印0-10，步长为2
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")

# 反向打印10-1
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")

# 3. while循环
# ==============================================
print("\n\n\n3. while循环:")

# 基础while循环
print("\n基础while循环:")
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1  # 不要忘记更新条件变量，否则会无限循环

# 用户输入验证
print("\n用户输入验证(模拟):")
# 实际使用时可以取消下面三行的注释
password = ""
while password != "123456":
    password = input("请输入密码(123456): ")
print("密码正确!")

# 使用break退出循环
print("\n使用break退出循环:")
num = 0
while True:
    if num >= 10:
        break
    print(num, end=" ")
    num += 1

# 4. 循环控制语句
# ==============================================
print("\n\n\n4. 循环控制语句:")

# break语句
print("\nbreak语句(遇到3时退出):")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# continue语句
print("\ncontinue语句(跳过偶数):")
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

# else子句
print("\nelse子句(循环正常结束时执行):")
for i in range(3):
    print(i)
else:
    print("循环正常结束")

print("\nelse子句(循环被break中断时不执行):")
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("这行不会打印")

# 5. 嵌套循环
# ==============================================
print("\n\n5. 嵌套循环:")

# 打印乘法表
print("\n九九乘法表:")
for i in range(1, 10):  # 行
    for j in range(1, i + 1):  # 列
        print(f"{j}×{i}={i * j}", end="\t")
    print()  # 换行

# 遍历二维列表
print("\n遍历二维列表:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

# 6. 列表推导式中的循环
# ==============================================
print("\n\n6. 列表推导式中的循环:")

# 创建平方数列表
squares = [x ** 2 for x in range(10)]
print(f"平方数列表: {squares}")

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"偶数平方数列表: {even_squares}")

# 嵌套循环的列表推导式
pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"坐标对: {pairs}")

# 7. 高级循环技巧
# ==============================================
print("\n\n7. 高级循环技巧:")

# 使用enumerate同时获取索引和值
print("\n使用enumerate:")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"索引{index}: {fruit}")

# 使用zip并行遍历多个序列
print("\n使用zip:")
names = ["张三", "李四", "王五"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}的分数是{score}")

# 反向遍历
print("\n反向遍历:")
for fruit in reversed(fruits):
    print(fruit)

# 排序后遍历
print("\n排序后遍历:")
for fruit in sorted(fruits):
    print(fruit)

# 8. 循环中的else子句高级用法
# ==============================================
print("\n\n8. 循环中的else子句高级用法:")

# 在搜索中使用else
print("\n在搜索中使用else:")
numbers = [1, 3, 5, 7, 9]
search_for = 4

for num in numbers:
    if num == search_for:
        print(f"找到数字{search_for}")
        break
else:
    print(f"未找到数字{search_for}")

# 9. 避免无限循环
# ==============================================
print("\n\n9. 避免无限循环:")

# 危险的无限循环(注释掉了，实际不要运行)
# while True:
#     print("这将永远运行!")

# 安全的做法是确保循环条件最终会变为False
print("\n安全的有界循环:")
timeout = 5
while timeout > 0:
    print(f"剩余超时: {timeout}")
    timeout -= 1
else:
    print("循环正常结束")
