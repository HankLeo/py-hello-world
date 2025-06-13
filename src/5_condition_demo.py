# 示例1: 基本的if-else语句
age = 18
if age >= 18:
    print("你已经成年了！")
else:
    print("你还未成年。")

# 示例2: 使用elif处理多个条件
score = 85
if score >= 90:
    print("优秀！")
elif score >= 80:
    print("良好！")
elif score >= 60:
    print("及格。")
else:
    print("不及格，需要努力！")

# 示例3: 使用and、or、not的逻辑运算
temperature = 25
weather = "晴天"

if temperature > 30 or (weather == "晴天" and temperature > 25):
    print("今天很热，注意防晒！")
elif not (weather == "雨天" or weather == "雪天"):
    print("今天天气不错，适合外出。")
else:
    print("今天天气不太好。")

# 示例4: 嵌套if语句
has_ticket = True
knife_length = 12  # 刀的长度(cm)

if has_ticket:
    print("有票，可以进入安检。")
    if knife_length > 10:
        print("携带的刀具过长，不允许进入！")
    else:
        print("安检通过，祝您旅途愉快！")
else:
    print("请先购票。")

# 示例5: Python特有的链式比较写法
x = 17

# 传统写法（其他语言常见）
if x > 15 and x < 20:
    print("x在15和20之间（传统写法）")

# Python特有的优雅链式比较
if 15 < x < 20:
    print("x在15和20之间（Python链式写法）")

# 更复杂的链式比较示例
y = 25
if 10 < x < 20 <= y <= 30:
    print(f"x在10-20之间({x})，且y在20-30之间({y})")

# 注意：这种写法不仅限于数字，也适用于其他可比较类型
name = "Bob"
if "A" < name < "C":
    print("名字在A和C之间（按字母顺序）")

# 示例6：三元运算
# value_if_true if condition else value_if_false
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)  # 输出: 成年

score = 85
result = "及格" if score >= 60 else "不及格"
print(f"考试成绩: {result}")  # 输出: 考试成绩: 及格

# 4. 嵌套三元运算（不推荐，可读性差）
x = 10
message = "大于10" if x > 10 else ("等于10" if x == 10 else "小于10")
print(message)  # 输出: 等于10
