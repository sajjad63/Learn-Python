import math


class Human(object):
    def __init__(self, name=None, age=None, weight=None, height=None):  # parameter
        self.name = name  # property
        self.age = age  # property
        self.weight = weight  # property
        self.height = height  # property
        self.bmi = None  # property

    # method
    def calc_bmi(self):
        self.bmi = self.weight / math.pow(self.height, 2)

    def __str__(self):
        # return self.name + str(self.age)
        return "{name} is {age}".format(name=self.name, age=self.age)


# y = Human(name="sajjad")
# y.age = 37
# print(y)
# print(y.age)
# y.weight, y.height = 90, 1.84
# y.calc_bmi()
# print(y.bmi)

p = Human()
p.name = "parvane"
p.age = 34
print(p)


class Man(Human):
    def __init__(self, *args, **kwargs):
        super(Man, self).__init__(*args, **kwargs)
        self.gender = "male"

    def __str__(self):
        return "{} is {}".format(self.name,self.gender)


m = Man(name="maza", age=32)
print(m)
