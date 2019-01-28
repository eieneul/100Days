"""
<面向对象进阶>

装饰器，静态方法和类方法，继承和多态

"""


# @property 装饰器
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 getter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s are playing chess.' % self._name)
        else:
            print('%s are gambling.' % self._name)


def main1():
    person = Person('Jerry', 14)
    person.play()
    person.age = 22
    person.play()
    """注意下面修改名字会出现AttributeError: can't set attribute
       原因是上面代码中我们只写了age的setter而没有写name的修改器"""
    # person.name = 'Tim'


"""
__slots__   
如果我们需要限定自定义类型的对象只能绑定某些属性，
可以通过在类中定义__slots__变量来进行限定。
需要注意的是__slots__的限定只对当前类的对象生效，
对子类并不起任何作用。

"""


class Person2(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 getter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s are playing chess.' % self._name)
        else:
            print('%s are gambling.' % self._name)


def main2():
    person = Person2('Harry', 12)
    person.age = 17
    person._gender = 'male'
    person.play()


"""
之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，
通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长
未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三
角形，这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来
（因为都不知道三条边能不能构成三角形），所以这个方法是属于三角形类而并不属于三
角形对象的。我们可以使用静态方法来解决这类问题，代码如下所示。

"""
from math import sqrt
class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a+b>c and b+c>a and a+c>b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def main3():
    a,b,c = 3,4,5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形')


# 定义类的方法
from time import sleep, localtime, time


class Clock:
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def __str__(self):
        """显示"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main_clock():
    clock = Clock.now()
    while True:
        print(clock)
        sleep(1)
        clock.run()


"""
继承和多态

刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发中，
我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。

"""


# 创建一个父类
class Person3:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在玩耍' % self._name)

    def watch_av(self):
        if self._age < 18:
            print('%s只能观看《熊出没》' % self._name)
        else:
            print('%s正在观看岛国爱情动作片' % self._name)


class Student(Person3):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Teacher(Person3):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在教%s' % (self._name, self._title, course))


def main_school():
    stu = Student('小明', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    tea = Teacher('白玉荣', 39, '班主任')
    tea.teach('数学')
    tea.watch_av()

"""
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，
不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。

"""
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪' % self._nickname)


class Cat(Pet):

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main_pet():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


"""
在上面的代码中，我们将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，
这种类的存在就是专门为了让其他类去继承它。Python从语法层面并没有像Java或C#那样提供对抽象类的支持，
但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，
如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。上面的代码中，
Dog和Cat两个子类分别对Pet类中的make_voice抽象方法进行了重写并给出了不同的实现版本，
当我们在main函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。

"""

if __name__ == '__main__':
    # main1()
    # main2()
    # main3()
    # main_clock()
    # main_school()
    main_pet()
