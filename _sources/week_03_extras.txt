.. _week_03_extras:

*********************************************
Week 3 Extras
*********************************************

A Note About Generators


=============================================
Django Generator Examples
=============================================

.. rst-class:: left
    
    We saw examples of generators being used in the Django project:

    1. Looping over GDAL/OGR `features <https://github.com/django/django/blob/db77915c9fd35a203edd8206f702ee4082f04d4a/django/contrib/gis/gdal/feature.py#L50-L53>`_

    2. Database query `functions <https://github.com/django/django/blob/355c5edd9390caad5725375abca03460805f663b/django/db/models/query.py>`_


    Questions:

        * Did you notice that almost all `__iter__` function end with a `yield`?

        * What's the benefit of having `yield` here?


Generator Review
--------------------------

Last time we saw that the print statement after the `yield` statement executes at an unexpected time

.. code-block:: ipython

    def count_to_10():
        print "executing..."
        for i in range(10):
            j = yield i
            print "continue..." 


.. nextslide::

.. code-block:: ipython

    In [2]: citer = count_to_10()

    In [3]: citer.next()
    executing...
    Out[3]: 0

    In [4]: citer.next()
    continue...
    Out[4]: 1

We didn't look at the stack frames in ``pdb`` for this example.

Can we expect anything different happening on the stack due to the ``yield`` statement ?

.. nextslide::

Interested in how generators work? 

Look at the teaser in ``week-03-debugging/generators/generator_as_functions.py``



