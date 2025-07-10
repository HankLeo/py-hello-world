"""
Python 继承与多态示例

继承：子类继承父类的属性和方法
多态：不同子类对同一方法有不同的实现方式
"""


# 父类/基类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """动物叫的方法"""
        raise NotImplementedError("子类必须实现此方法")


# 子类/派生类 - 继承自Animal
class Dog(Animal):
    def speak(self):
        """狗叫的实现"""
        return f"{self.name} 说: 汪汪!"

    def fetch(self):
        """狗特有的方法"""
        return f"{self.name} 正在捡球"


# 子类/派生类 - 继承自Animal
class Cat(Animal):
    def speak(self):
        """猫叫的实现"""
        return f"{self.name} 说: 喵喵!"

    def climb(self):
        """猫特有的方法"""
        return f"{self.name} 正在爬树"


# 子类/派生类 - 继承自Animal
class Duck(Animal):
    def speak(self):
        """鸭子叫的实现"""
        return f"{self.name} 说: 嘎嘎!"

    def swim(self):
        """鸭子特有的方法"""
        return f"{self.name} 正在游泳"


# 多态演示函数
def animal_speak(animal_obj):
    """接受任何Animal子类对象，调用其speak方法"""
    print(animal_obj.speak())


# 多重继承示例
class FlyingCreature:
    def fly(self):
        return f"{self.name} 正在飞翔"


class Bat(Animal, FlyingCreature):
    def speak(self):
        return f"{self.name} 发出超声波"


# 方法重写示例
class LoudDog(Dog):
    def speak(self):
        """重写父类方法，实现不同的行为"""
        original_sound = super().speak()  # 调用父类方法
        return original_sound.upper() + " 很大声!"


if __name__ == "__main__":
    # 创建不同子类的实例
    dog = Dog("旺财")
    cat = Cat("咪咪")
    duck = Duck("唐老鸭")
    bat = Bat("蝙蝠侠")
    loud_dog = LoudDog("吵闹的狗")

    # 继承演示
    print("\n=== 继承演示 ===")
    print(dog.fetch())  # 调用Dog特有的方法
    print(cat.climb())  # 调用Cat特有的方法
    print(duck.swim())  # 调用Duck特有的方法
    print(bat.fly())  # 多重继承的方法

    # 多态演示
    print("\n=== 多态演示 ===")
    animal_speak(dog)  # 调用Dog的speak方法
    animal_speak(cat)  # 调用Cat的speak方法
    animal_speak(duck)  # 调用Duck的speak方法
    animal_speak(bat)  # 调用Bat的speak方法
    animal_speak(loud_dog)  # 调用重写后的方法

    # isinstance和issubclass检查
    print("\n=== 类型检查 ===")
    print(f"dog是Animal的实例吗? {isinstance(dog, Animal)}")  # True
    print(f"dog是Cat的实例吗? {isinstance(dog, Cat)}")  # False
    print(f"Dog是Animal的子类吗? {issubclass(Dog, Animal)}")  # True
    print(f"Bat是FlyingCreature的子类吗? {issubclass(Bat, FlyingCreature)}")  # True

    # 方法重写演示
    print("\n=== 方法重写演示 ===")
    print(loud_dog.speak())
    print(f"父类方法仍然存在: {super(LoudDog, loud_dog).speak()}")
