.. _week_05_properties:

*********************************************
Week 5 Properties 
*********************************************

The three forms

=============================================
Properties: What and Why?
=============================================

.. rst-class:: left

    **1.** Wrapper functions that controll access (get,set,delete) to an attribute.

    **2.** Provides encapsulation


Properties First Form
=======================

Using decorators

.. rst-class:: left

    .. code-block:: ipython

        class Form1( object ):
            def __init__(self, name):
                self._name = name

            @property
            def name(self):
                return self._name

            @name.setter
            def name(self,value):
                self._name = value

            @name.deleter
            def name(self):
                del self._name


Properties Second Form
=======================

Using __builtins__.property

.. rst-class:: left

    .. code-block:: ipython

        class Form2( object ):

            def __init__(self,name):
                self._name = name

            def get_name(self): 
                return self._name

            def set_name(self,value):
                self._name = value

            def del_name(self): 
                del self._name

            # NOTE where this is bound
            name = property( get_name, set_name, del_name )


Properties Third Form
=======================

Using magic methods __get__, __set__, and __delete__ ( `use case <https://github.com/mitsuhiko/flask/search?utf8=%E2%9C%93&q=ConfigAttribute>`_ )

.. rst-class:: left

    .. code-block:: ipython

        class Name(object):
            def __init__(self,val):
                self.value = val

            def __get__(self, obj, objtype):
                return self.value

            def __set__(self, obj, val):
                self.value = val

            def __delete__(self,obj):
                del self.value







    
