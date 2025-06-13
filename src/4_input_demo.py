# BMI = weight / (height ** 2)

# 输入
user_weight = float(input("请输入您的体重(kg): "))
user_height = float(input("请输入您的身高(m): "))

# 计算BMI
user_BMI = user_weight / (user_height ** 2)
print("您的BMI是: " + str(user_BMI))
