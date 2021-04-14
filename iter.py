class MyNumber(object):
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            i = self.a
            self.a += 1
            return i
        else:
            raise StopIteration


m = MyNumber()
miter = iter(m)
for b in miter:
    print(b)
