.. _week_02_leftovers:

*********************************************
Week 2 Leftovers
*********************************************

Name Mangling and Decorators ( Addendum )


=========================================
Name Mangling Protects Expected Behavior
=========================================


.. rst-class:: left

    Name mangling out in the wild:

     - some coders attempt to use it as a "private accessor"

     - protection by obfuscation

     - we saw a method definition ``Foo.__update`` gets mangled as ``Foo._Foo__update``


    The "intended" use case enforced expected behavior during inheritence [#f1]_

.. rubric::

.. [#f1] The Art of Subclassing by Raymond Hettinger, PyCon US 2012


Name Mangling Use Case
------------------------

Take a look at ``/week-03-leftovers/reason_to_mangle.py``

.. code-block:: ipython

    class Parent( object ):
        def __init__(self, iterable):
            self.internal_state = []
            self.update(iterable)

        def update(self, iterable):
            for i in iterable:
                self.internal_state.append(i)

    class Child( Parent ):
        def update(self,iterable):
            self.foobar = list(iterable)

    c = Child([1,2,3,4,5])


Where to Use Decorators?
--------------------------

Gut checking use cases:
    
    - it's a form of refactoring and code reuse; we have some logic that we can generalize

    - we want to modify an existing function's input/output without modifying the function signature

Developers always need to weigh design choices against drawbacks -- some include:

    - Readability

    - Simplicity 

    - Optimization ( Speed/Memory )

Do we really need to use a decorator?

.. nextslide::

.. code-block:: ipython

    # remember this elegant little thing? sure is beautiful
    def memoize(f):
        memo = {}
        def inner(x):
            if x not in memo:
                memo[x] = f(x)
            return memo[x]
        return inner

    @memoize
    def fib(n):
        if n in [0,1]:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    print fib(10)


.. nextslide::


Positives about ``memoize`` decorator:

    - sure is elegant and pythonic ( has a sense of style, if, we can understand it )

    - it's faster than the straight-ahead recursive version ( everyone loves fast things )

Drawbacks about ``memoize`` decorator:

    - it's hard to reason about the execution ( readability might be suffering )


Exercise
--------------------------

Rewrite the recursive ``fib`` function in ``week-03-leftovers/memoize_recursive_decorate.py``

1. keep the recursion

2. rewrite it so you don't use a ``memoize`` decorator. move the ``memoize`` logic into the function

3. which version of of ``fib`` is more readable and appeals to your sense of style?

HINT: The ``inner`` function is a  good indication of how to approach it

.. code-block:: ipython

        ...
        def inner(x):
            if x not in memo:
                memo[x] = f(x)  
            return memo[x]
        ...

Evaluate the Output
--------------------------

1. Run the module ``week-03-leftovers/solutions/memoize_recursive_decorate.py``

2. What does the output tell us about the execution?


