from mixin_bases import *
from getattribute import object_getattribute

class Foo(Uno,Dos): pass
func = object_getattribute( Foo(), Foo, 'log', klass_mro=Foo.mro()[1:] )
func()
print "\n"

class Foo(Boom,Uno,Dos): pass
func = object_getattribute( Foo(), Foo, 'log', klass_mro=Foo.mro()[1:] )
func()
print "\n"

class Foo(Uno,Boom,Dos): pass
func = object_getattribute( Foo(), Foo, 'log', klass_mro=Foo.mro()[1:] )
func()
print "\n"

class Foo(Uno,Dos,Boom): pass
func = object_getattribute( Foo(), Foo, 'log', klass_mro=Foo.mro()[1:] )
func()
print "\n"
