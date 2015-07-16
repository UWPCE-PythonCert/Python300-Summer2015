class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        print "__iter__ called"
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


y = yrange(3)
print y
print list( y )
print list( y )
