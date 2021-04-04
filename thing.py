class Thing(object):
    def __init__(self, weight=None, dimension=None, density=None):
        self.weight = weight
        self.dimension = dimension
        self.density = density


class Solid(Thing):
    def __init__(self):
        super().__init__()
        self.weight = True
        self.dimension = True
        self.density = True

    def warm(self):
        pass

    def __str__(self):
        return "{} has {}, {} and {}".format(self, self.weight, self.density, self.dimension)


class Liquid(Thing):
    def __init__(self):
        super().__init__()
        self.weight = True
        self.dimension = False
        self.density = True

    def warm(self):
        pass

    def cool(self):
        pass

    def __str__(self):
        return "{} has {}, {} and {}".format(self, self.weight, self.density, self.dimension)


class Gas(Thing):
    def __init__(self):
        super().__init__()
        self.weight = False
        self.dimension = False
        self.density = False

    def cool(self):
        pass

    def __str__(self):
        return "{} has {}, {} and {}".format(self, self.weight, self.density, self.dimension)


ice = Solid(weight=True, dimension=True, density=True)



