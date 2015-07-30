class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n
        self.xiter = iter(xrange(self.n))

    def __iter__(self):
        return self

    def next(self):
        return self.xiter.next()


if __name__ == '__main__':
    y = yrange(3)
    print y
    for i in y:
        print i
