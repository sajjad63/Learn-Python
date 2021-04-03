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


y = Human(name="sajjad")
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
        return "{} is {}".format(self.name, self.gender)


m = Man(name="maza", age=32)
print(m)


class Woman(Man):
    def __init__(self, *args, **kwargs):
        # super(Woman, self).__init__(*args, **kwargs)
        # Human.__init__(*args, **kwargs)
        self.double_bmi = None
        print(kwargs)
        self.hair_color = kwargs.pop("hair_color")
        print(kwargs)
        super().__init__(*args, **kwargs)
        self.gender = "female"
        # self.hair_color = kwargs["hair_color"]
        print(kwargs)


    def calc_double_bmi(self):
        self.double_bmi = 2 * self.weight / math.pow(self.height, 2)
        return self.double_bmi

    def __str__(self):
        return "{}Double BMI is: {}".format(self.name, self.double_bmi)


f = Woman(name="safur", age=32, weight=45, height=1.630, hair_color="blonde")
print(f.calc_double_bmi())
