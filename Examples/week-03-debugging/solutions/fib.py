class FibIter(object):
    def __init__(self,n):
        self.vals = [0,1]
        self.n = n
        self.i = 0

    def __iter__(self): return self

    def next(self):
        if self.i == self.n:
            raise StopIteration

        self.i += 1
        if self.i in [0,1]:
            return self.i
        else:
            #print "fib({}) = {}".format( self.i, self.vals )
            new_val = sum(self.vals)
            self.vals.pop(0)
            self.vals.append(new_val)
            return new_val

for x in FibIter(20):
    print x
