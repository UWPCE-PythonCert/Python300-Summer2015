class Boom(object):
    def log(self):
        print "[ BOOMTOWN ]: %s" % (self.__repr__())

class Basic(object):
    def log(self):
        print self.__class__

class Uno(Basic):
    pass

class Dos(Basic):
    pass