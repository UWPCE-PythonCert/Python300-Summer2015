class A(object):
    def __init__(self):
        print "A",
        super(self.__class__, self).__init__()

class B(A):
    def __init__(self):
        print "B",
        super(self.__class__, self).__init__()

if __name__ == '__main__':
    print "[ MRO ]:", [x.__name__ for x in B.__mro__]
    B()
    

