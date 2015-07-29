class A(object):
    def __init__(self, arg):
        print "A"
        arg = "A" + arg
        # swallow
        super(A, self).__init__(arg)

    def duckduck(self):
        super(A, self).duckduck()

class B(object):
    def __init__(self, arg):
        print "B"
        arg = "B" + arg
        # swallow
        #super(B, self).__init__(arg)

class C(A):
    def __init__(self, arg):
        print "C","arg=",arg
        arg = 'C' + arg
        super(C, self).__init__(arg)

    def duckduck(self):
        super(C, self).duckduck()

class D(B):
    def __init__(self, arg):
        print "D", "arg=",arg
        arg = 'D' + arg
        super(D, self).__init__(arg)

class E(C,D):
    def __init__(self, arg):
        print "E", "arg=",arg
        arg = 'E' + arg
        super(E, self).__init__(arg)

    def duckduck(self):
        super(E, self).duckduck()

if __name__ == '__main__':

    print "[ MRO ]: {}".format([i.__name__ for i in E.mro()])
    e = E('blah')
    #e.duckduck()
    
