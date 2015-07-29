class A(object):
    def __init__(self):
        print "A",
        super(A, self).__init__()

class B(object):
    def __init__(self):
        print "B",
        super(B, self).__init__()

class Plastic(object):
    def __init__(self):
        print "Plastic"


class App(A,B,Plastic):
    def __init__(self):
        print "App"
        super( App, self ).__init__()

if __name__ == '__main__':
    print "[ MRO ]:", [x.__name__ for x in App.__mro__]
    App()
    

