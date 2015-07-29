
class Container1( object ):

    def __init__(self):
        self.name = 'parent'


class Container2( object ):

    def __init__(self):
        self._name = 'parent'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    #
    # the above decorator form
    # is equivalent to the following form too
    #
    """
    def get_name(self): return self._name
    def set_name(self,value): self._name = value
    def del_name(self,value): del self._name
    name = property( get_name, set_name, del_name )
    """

class Container3( object ):

    def __init__(self,name=None):
        self._name = 'bangbang!!'
        if name is not None:
            self._name = name

    def name(self):
        print "my name is {}".format(self._name) 


def simulate_getattribute(instance, klass, attrname):
    '''
    assuming Class is a class 
    and instance is an instance of that class,
    then show the resolution workflow of 
    instance.attrname lookups for understanding
    
    NOTE: this is not the same type of workflow 
    for Class.attrname lookups. 
    That workflow involves the Metaclass
    '''

    if attrname in klass.__dict__.keys():
        print "yep, Class.__dict__"
        if hasattr( klass.__dict__[attrname], '__get__' ) and hasattr( klass.__dict__[attrname], '__set__' ):
            print "yep, DATA descriptor found"
            return klass.__dict__[attrname].__get__( instance, klass )
        else:
            print "nope, not a DATA descriptor"

    if attrname in instance.__dict__.keys():
        print "yep, instance.__dict__"
        return instance.__dict__[attrname]

    if attrname in klass.__dict__.keys():
        print "yep, Class.__dict__"
        if hasattr( klass.__dict__[attrname], '__get__' ):
            print "yep, NON-DATA descriptor found"
            return klass.__dict__[attrname].__get__( instance, klass )
        else:
            print "nope, still not found...return from klass.__dict__[ attrname ]"
            # this might trigger AttributeError up the chain
            return klass.__dict__[attrname]

    # this might trigger AttributeError up the chain
    print "nope, still not found...call klass.__getattr__"
    return klass.__getattr__( attrname )

if __name__ == '__main__':
    # 

    p = Container3()
    #print simulate_getattribute(p,type(p),'name')
    


