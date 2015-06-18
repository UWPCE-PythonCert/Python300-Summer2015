.. _testing_addendum:

*********************************************
Test Addendum 
*********************************************

The things we forgot to talk about

================================
Automate As Much As Possible
================================


.. rst-class:: left


The tooling and analysis that helps you write good code can be cumbersome to manage.  Earlier examples showed us tools such as: 

``coverage`` ( detail where you need more tests )

``pep8`` ( for style errors )

``pyflakes`` ( for functional errors )

Isn't there an easier way to see the interaction of these things with my code?

IDE(s) of Course
--------------------

Text editors can handle some static analyis, lookups. Most, like ``Sublime``, come with plugins

A full-blown IDE usually comes with that plus more: 

    * jumping around the codebase faster ( ex. source code )
    
    * debugging 
    
    * syntax, style, functional errors

    * testing is integrated

    * sometimes coverage is too

IDE Examples
------------------------

Common Python IDE(s): 

    * Aptana Studio

    * PyDev

    * PyCharm


PyCharm Example ( Coverage and PEP8 )
-------------------------------------------

Remember this wonderful program?

.. code-block:: ipython

    from sys import *

    a = 0; b = 1

    def foo( x ):
        if x:
            print "in branch"
            if x + 1:
                print "+ 1"
        print "out of branch"


Decorator definition
-----------------------

Python functions can accept functions as arguments and return them:

.. code-block:: ipython

    def x( function_z ):
        def y():
            # execute the passed fn
            function_z()
        return y

We also know that Python functions are just objects:

.. code-block:: ipython

    In [1]: def foo():pass

    In [2]: isinstance( foo, object )
    Out[2]: True

.. nextslide:: 

What if we wanted to add additional functionality to an object at runtime but without changing the object?

If we do this type of thing a lot, then we are just following a pattern ( as in Gang-of-Four )


Decorator example and demo
-----------------------------

.. code-block:: ipython

    def loggly(func):
        def logger(*args, **kwargs):
            if not kwargs.get( 'muffle', False ):
                print "executing '{}'".format( func.__name__ )
                print "\twith args: {}".format( args )
                print "\twith kwargs: {}".format( kwargs )
            return func(*args, **kwargs)
        return logger

Decorator Excercise
-----------------------------

1. Write a decorator that times the execution of a function


