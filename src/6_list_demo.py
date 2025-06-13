########## 1. 基础操作 ##########

# 创建列表
fruits = ['apple', 'banana', 'orange', 'grape']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]

# 访问元素
print(f"第一个元素：{fruits[0]}")  # 输出: apple (第一个元素)
print(fruits[-1])  # 输出: grape (最后一个元素)
print(len(fruits))  # 输出: 4 (列表长度)

# 切片操作
print(numbers[1:3])  # 输出: [2, 3] (索引1到2)
print(numbers[:3])  # 输出: [1, 2, 3] (前三个元素)
print(numbers[2:])  # 输出: [3, 4, 5] (从索引2开始)
print(numbers[::-1])  # 输出: [5, 4, 3, 2, 1] (反转列表)

# 修改元素
fruits[1] = 'pear'
print(fruits)  # 输出: ['apple', 'pear', 'orange', 'grape']

########## 2. 添加和删除元素 ##########

# 添加元素
fruits.append('kiwi')  # 在末尾添加
print(fruits)  # ['apple', 'pear', 'orange', 'grape', 'kiwi']

fruits.insert(1, 'mango')  # 在索引1处插入
print(fruits)  # ['apple', 'mango', 'pear', 'orange', 'grape', 'kiwi']

# 合并列表
more_fruits = ['pineapple', 'watermelon']
fruits.extend(more_fruits)  # 扩展列表
print(fruits)

# 删除元素
removed = fruits.pop()  # 删除并返回最后一个元素
print(f"Removed: {removed}, List: {fruits}")

removed = fruits.pop(2)  # 删除并返回索引2的元素
print(f"Removed: {removed}, List: {fruits}")

fruits.remove('orange')  # 删除第一个匹配的元素
print(fruits)

del fruits[0]  # 删除索引0的元素
print(fruits)

fruits.clear()  # 清空列表
print(fruits)  # 输出: []

########## 3. 列表操作和方法 ##########

numbers = [5, 2, 8, 1, 9, 3]

# 排序
numbers.sort()  # 原地排序
print(numbers)  # 输出: [1, 2, 3, 5, 8, 9]

numbers.sort(reverse=True)  # 降序排序
print(numbers)  # 输出: [9, 8, 5, 3, 2, 1]

# 不修改原列表的排序
sorted_numbers = sorted(numbers)  # 返回新列表
print(sorted_numbers)  # 输出: [1, 2, 3, 5, 8, 9]

# 反转
numbers.reverse()  # 原地反转
print(numbers)  # 输出: [1, 2, 3, 5, 8, 9]

# 查找元素
print(numbers.index(5))  # 输出: 3 (返回第一个匹配的索引)
print(8 in numbers)  # 输出: True
print(10 in numbers)  # 输出: False

# 计数
numbers.append(5)
print(numbers.count(5))  # 输出: 2 (统计元素出现次数)

########## 4. 列表推导式和高级操作 ##########

# 列表推导式
squares = [x ** 2 for x in range(10)]
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # 输出: [0, 4, 16, 36, 64]

# 嵌套列表推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 使用enumerate同时获取索引和值
for index, value in enumerate(['a', 'b', 'c']):
    print(f"Index: {index}, Value: {value}")

# 使用zip合并多个列表
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

########## 5. 复制列表 ##########
original = [1, 2, 3]

# 浅拷贝
copy1 = original.copy()  # 方法1
copy2 = list(original)  # 方法2
copy3 = original[:]  # 方法3

# 修改拷贝不会影响原列表
copy1.append(4)
print(original)  # 输出: [1, 2, 3]
print(copy1)  # 输出: [1, 2, 3, 4]

# 注意嵌套列表的浅拷贝问题
nested = [[1, 2], [3, 4]]
nested_copy = nested.copy()
nested_copy[0][0] = 99
print(nested)  # 输出: [[99, 2], [3, 4]] (也被修改了)

# 深拷贝
import copy

deep_copy = copy.deepcopy(nested)
deep_copy[0][0] = 100
print(nested)  # 输出: [[99, 2], [3, 4]] (未被修改)
print(deep_copy)  # 输出: [[100, 2], [3, 4]]

########## 6. 列表作为栈和队列 ##########
# 列表作为栈使用 (LIFO)
stack = []
stack.append(1)  # 入栈
stack.append(2)
stack.append(3)
print(stack.pop())  # 出栈 (3)
print(stack.pop())  # 出栈 (2)

# 列表作为队列使用 (FIFO) - 不推荐，效率低
queue = []
queue.append(1)  # 入队
queue.append(2)
queue.append(3)
print(queue.pop(0))  # 出队 (1) - O(n)操作
print(queue.pop(0))  # 出队 (2)

# 更好的队列实现
from collections import deque

queue = deque()
queue.append(1)  # 入队
queue.append(2)
print(queue.popleft())  # 出队 (1) - O(1)操作
