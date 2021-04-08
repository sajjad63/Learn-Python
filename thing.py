class Thing(object):
    def __init__(self, weight=None, dimension=None):
        self.weight = weight
        self.dimension = dimension
        self.density = self.weight / self.dimension

    # def __str__(self):
    #     return "weight is {},density is {} and dimension is {} and " \
    #            "it's type is {} and parent is{}".format(
    #         self.weight,
    #         self.density,
    #         self.dimension,
    #         self.__class__.__name__,
    #         [i.__name__ for i in self.__class__.__bases__]

    def __str__(self):
        return f"weight is {self.weight}, density is {self.density} and dimension is {self.dimension}" \
               f" and it's type is {[i.__name__ for i in self.__class__.__bases__]}."


class WarmMixin:
    def warm(self):
        if isinstance(self, Liquid):
            item = {"weight": self.weight / 10, "dimension": self.dimension * 10}
            return Gas(**item)
        elif isinstance(self,Solid):
            item = {"weight": self.weight, "dimension": self.dimension}
            return Liquid(**item)

        else:
            raise NotImplementedError


class CoolMixin:
    def cool(self):
        if isinstance(self, Gas):
            item = {"weight": self.weight * 10, "dimension": self.dimension / 10}
            return Liquid(**item)
        elif isinstance(self, Liquid):
            item = {"weight": self.weight, "dimension": self.dimension}
            return Solid(**item)
        else:
            raise NotImplementedError


class Solid(WarmMixin, Thing):
    pass


class Liquid(CoolMixin, WarmMixin, Thing):
    pass


class Gas(CoolMixin, WarmMixin, Thing):
    pass


class Water(Liquid):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # def warm(self):
    #     item = {"weight": self.weight / 10, "dimension": self.dimension / 5}
    #     g = Gas(**item)
    #     # g.weight = self.weight / 10
    #     # g.dimension = self.dimension * 5
    #     return g
    #
    # def cool(self):
    #     item = {"weight": self.weight, "dimension": self.dimension * 1.1}
    #     i = Solid(**item)
    #     # i.weight = self.weight
    #     # i.dimension = self.dimension * 1.1
    #     return i


class Sugar(Solid):
    pass
    # def warm(self):
    #     item = {"weight": self.weight, "dimension": self.dimension}
    #     return Liquid(**item)


class CubedSugar(Solid):
    pass
    # def warm(self):
    #     item = {"weight": self.weight, "dimension": self.dimension}
    #     return Liquid(**item)


class Syrup(Water, CubedSugar):
    def __init__(self, water, sugar):
        super(Water, self).__init__(water.weight, water.dimension)
        super(CubedSugar, self).__init__(sugar.weight, sugar.dimension)
        self.weight = water.weight + sugar.weight
        self.dimension = water.dimension + sugar.dimension


w = Water(weight=1, dimension=1)
print(w)
print(w.warm())
print(w.cool())
z = w.warm()
# z.warm()

s = Sugar(weight=1, dimension=1)
print(s.warm())

sy = Syrup(w, s)
print(sy)
print(sy.warm())
print(sy.cool())
