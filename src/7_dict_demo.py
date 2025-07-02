"""
Python 字典(dict)使用示例

字典是Python中一种可变容器模型，可存储任意类型对象。
字典的每个键值对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中。
格式如下：
    d = {key1: value1, key2: value2, ...}
"""

# 1. 创建字典
# ==============================================

# 创建空字典
empty_dict = {}
print(f"空字典: {empty_dict}")

# 直接创建字典
person = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "is_student": False,
    "skills": ["Python", "Java", "SQL"]
}
print(f"\n人员信息字典: {person}")

# 使用dict()构造函数创建
fruit_dict = dict(apple=5, banana=8, orange=3)
print(f"\n水果字典: {fruit_dict}")

# 2. 访问字典元素
# ==============================================

# 通过键访问值
print(f"\n姓名: {person['name']}")
print(f"年龄: {person['age']}")
print(f"技能: {person['skills'][0]}")  # 访问嵌套列表

# 使用get()方法访问(更安全，键不存在时返回None或默认值)
print(f"工资: {person.get('salary')}")  # 返回None
print(f"工资: {person.get('salary', 0)}")  # 返回默认值0

# 3. 修改字典
# ==============================================

# 添加/更新键值对
person["salary"] = 15000  # 添加新键
person["age"] = 26  # 更新已有键
print(f"\n更新后的人员信息: {person}")

# 使用update()方法批量更新
person.update({"city": "上海", "is_student": True})
print(f"批量更新后: {person}")

# 4. 删除字典元素
# ==============================================

# 使用del删除指定键
del person["is_student"]
print(f"\n删除'is_student'后: {person}")

# 使用pop()删除并返回值
age = person.pop("age")
print(f"删除的年龄: {age}")
print(f"删除'age'后: {person}")

# 清空字典
fruit_dict.clear()
print(f"\n清空后的水果字典: {fruit_dict}")

# 删除整个字典
del fruit_dict
# print(fruit_dict)  # 这会引发NameError，因为fruit_dict已被删除


# 5. 字典常用操作
# ==============================================

# 获取所有键
keys = person.keys()
print(f"\n所有键: {keys}")  # 返回视图对象

# 获取所有值
values = person.values()
print(f"所有值: {values}")

# 获取所有键值对
items = person.items()
print(f"所有键值对: {items}")

# 检查键是否存在
print(f"'name'在字典中: {'name' in person}")
print(f"'age'在字典中: {'age' in person}")

# 字典长度
print(f"字典长度: {len(person)}")

# 6. 字典遍历
# ==============================================

print("\n遍历字典:")
# 遍历键
print("遍历键:")
for key in person:
    print(key)

# 遍历键值对
print("\n遍历键值对:")
for key, value in person.items():
    print(f"{key}: {value}")

# 7. 字典推导式
# ==============================================

# 创建平方字典
numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers}
print(f"\n数字平方字典: {squares}")

# 条件筛选
even_squares = {num: num ** 2 for num in numbers if num % 2 == 0}
print(f"偶数平方字典: {even_squares}")

# 8. 嵌套字典
# ==============================================

# 创建嵌套字典
company = {
    "name": "ABC科技",
    "departments": {
        "sales": {"employees": 15, "manager": "李四"},
        "development": {"employees": 30, "manager": "王五"},
        "hr": {"employees": 5, "manager": "赵六"}
    }
}

print("\n嵌套字典示例:")
print(f"公司名称: {company['name']}")
print(f"开发部经理: {company['departments']['development']['manager']}")
print(f"销售部员工数: {company['departments']['sales']['employees']}")

# 9. 其他有用方法
# ==============================================

# setdefault(): 如果键不存在则设置默认值
person.setdefault("country", "中国")
print(f"\n设置默认国家后: {person}")

# popitem(): 删除并返回最后一个键值对
last_item = person.popitem()
print(f"删除的最后一项: {last_item}")
print(f"删除后字典: {person}")

# 复制字典
person_copy = person.copy()
print(f"\n字典副本: {person_copy}")
