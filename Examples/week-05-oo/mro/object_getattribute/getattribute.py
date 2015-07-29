
def object_getattribute(instance, klass, attrname, klass_mro=[]):
    '''
    NOTE: the resolution workflow
    for Class.attrname lookups is different
    '''
    print "[ INSPECTING ]: %s" % klass

    if attrname in klass.__dict__.keys():
        print "yep, in Class.__dict__"
        if ( hasattr( klass.__dict__[attrname], '__get__' )
             and hasattr( klass.__dict__[attrname], '__set__' ) ):
            print "yep, DATA descriptor found"
            return klass.__dict__[attrname].__get__( instance, klass )
        else:
            print "nope, not a DATA descriptor"
    else:
        print "nope, not in Class.__dict__"

    if attrname in instance.__dict__.keys():
        print "yep, instance.__dict__"
        return instance.__dict__[attrname]
    else:
        print "nope, not in instance.__dict__"

    if attrname in klass.__dict__.keys():
        print "yep, in Class.__dict__"
        if hasattr( klass.__dict__[attrname], '__get__' ):
            print "yep, NON-DATA descriptor found"
            return klass.__dict__[attrname].__get__( instance, klass )
        else:
            print "return from Class.__dict__[ attrname ]"
            return klass.__dict__[attrname]
    else:
        print "nope, not in Class.__dict__"

    if hasattr( klass, '__getattr__' ):
        print "return from Class.__getattr__( attrname )"
        return klass.__getattr__( attrname )
    else:
        print "nope, no __getattr__ override"

    return object_getattribute( instance,
    klass_mro.pop(0), attrname, klass_mro=klass_mro )