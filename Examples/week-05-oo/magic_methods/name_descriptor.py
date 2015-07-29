class Name(object):
    """
    A data descriptor that sets and returns values
    """

    def __init__(self,val):
        self.value = val

    def __get__(self, obj, objtype):
        print 'GET:'
        return self.value

    def __set__(self, obj, val):
        print 'UPDATE:'
        self.value = val

    def __delete__(self,obj):
        print 'DELETE:'
        self.value = None

class User(object):

    def __init__(self,name_str):
        name = Name(name_str)

if __name__ == '__main__':
    u = User('bob')
    print u.name
    u.name = 'sarah'
    print u.name
    del u.name
    
