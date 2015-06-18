.. _scipy:

======================
Intro to Numpy / Scipy
======================

.. Contents:

.. .. toctree::
..    :maxdepth: 2


Scipy
=====

.. rst-class:: left

  The scipy "Stack" is a collection of core packages used for scientific / numerical computing.

  http://www.scipy.org/stackspec.html

  Many other domain-specific packages area available:

    Core "stack" is what most people will want, regardless of domain.

What's in the scipy stack?
--------------------------

* Python (http://www.python.org)
* NumPy (http://www.numpy.org)
* SciPy library (http://www.scipy.org)
* Matplotlib (http://matplotlib.org/)
* IPython (http://ipython.org/)

* nose (https://nose.readthedocs.org)
* pandas (http://pandas.pydata.org/)
* Sympy (http://sympy.org/)

Learning Resources
------------------

There are a lot of noteworthy tutorials and documentation out there. Here are some for you to investigate.

http://scipy-lectures.github.io/

https://github.com/SciTools/courses/blob/master/README.md

https://github.com/jrjohansson/scientific-python-lectures

https://github.com/WeatherGod/AnatomyOfMatplotlib

http://wiki.scipy.org/Tentative_NumPy_Tutorial

For those familiar with MATLAB:

http://wiki.scipy.org/NumPy_for_Matlab_Users

The ipython "notebook"
-----------------------

iPython has been used here and there in class. It's another interactive console for testing and running
Python code.

It has another useful interface: the "notebook"

The notebook provides a way to intersperse chunks of text, code and images

It runs in a browser, you kick it off with:

.. code-block:: bash

  ipython notebook

It should start your browser and show the notebooks in the directory where you ran the command


numpy
=====

.. rst-class:: left

  `numpy` is the core package that entire scipy stack is built on.

  The other tools rest on understanding what a numpy array is -- that's mostly what we'll talk about here

So what is numpy?
-----------------

It's a Python extension module ( `docs <http://www.numpy.org/>`_ )

1) An N-Dimensional array object

  - Really this ``ndarray`` is the core of it all

2) A whole pile of tools for operations on/with that object.


Why numpy?
----------

Classic answer: Lots of numbers

  * Faster
  * Less memory
  * More data types

Even if you don't have lot of numbers:

  * N-d array slicing
  * Vector operations
  * Flexible data types

.. nextslide::

Wrapper for a block of memory:

  * Interfacing with C libs
  * PyOpenGL
  * GDAL
  * NetCDF4
  * Shapely

Image processing:

  * PIL
  * WxImage
  * ndimage


This Talk
----------

There are a lot of tutorials and documentation out there.

Let's spend some time on the "how to use it" stuff.

Getting started
================

.. rst-class:: left

  Example code is in the class repo:

  ``SystemDevelopment2015/Examples/week-05-numpy``

  Those are a bunch of ipython notebooks.

  Get your command line into that dir, then start up the iPyhton notebook:

  ``$ ipython notebook``

  This should fie up your browser, and give you a list of notebooks to choose from.

Array Constructors:
-------------------

How do you make an array?

From scratch: ``ones(), zeros(), empty(), arange(), linspace(), logspace()``

( Default dtype: ``np.float64`` )

From sequences:  ``array(), asarray()`` ( Build from any sequence )

demo: ``constructors.ipynb``


Indexing and slicing
--------------------

How do you get parts of the array out?

Indexing and slicing much like regular python sequences, but extended to multi-dimensions.

However: a slice is a "view" on the array -- new object, but shares memory:

demo: ``slice.ipynb``


Reshaping:
-----------

numpy arrays have a particular shape.

But they are really wrappers around a block of data

So they can be re-shaped -- same data, arranged differently

demo: ``reshaping.ipynb``


Broadcasting:
-------------

Element-wise operations among two different rank arrays:

This is the key power of numpy!

Simple case: scalar and array:
::

    In [37]: a
    Out[37]: array([1, 2, 3])
    In [38]: a*3
    Out[38]: array([3, 6, 9])


Great for functions of more than one variable on a grid

demo: ``broadcasting.ipynb``

Fancy Indexing
--------------

As we've seen, you can slice and dice nd arrays much like regular python sequences.

This model is extended to multiple dimensions.

But it still only lets you extract rectangular blocks of elements.

For more complex sub-selection: we use "fancy indexing":

demo: ``fancy_indexing.ipynb``


.. What is an nd array under the hood?
    -----------------------------------

     * N-dimensional (up to 32!)

     * Homogeneous array:

       - Every element is the same type

         (but that type can be a pyObject)

       - Int, float, char -- more exotic types

       - "rank" – number of dimensions

     * Strided data:

       - Describes how to index into block of memory

       - PEP 3118 -- Revising the buffer protocol


    demo: ``memory_struct.ipynb``


.. Built-in Data Types
    -------------------

    * Signed and unsigned Integers

      - 8, 16, 32, 64 bits

    * Floating Point

      - 32, 64, 96, 128 bits (not all platforms)

    * Complex

      - 64, 128, 192, 256 bits

    * String and unicode

      - Static length

    * Bool --  8 bit

    * Python Object

      - Really a pointer

    demo: ``object.ipynb``


.. Text File I/O
   --------------

    Loading from text (CSV, etc):

      * ``np.loadtxt``
      * ``np.genfromtxt`` ( a few more features )

    Saving as text (CSV):

      * ``np.savetxt()``

.. Compound dtypes
    ---------------

      * Can define any combination of other types

        - Still Homogeneous:  Array of structs.
      * Can name the fields

      * Can be like a database table

      * Useful for reading binary data


    demo: ``dtypes.ipynb``


.. Numpy Persistence:
   ------------------

      * ``np.tofile() / np.fromfile()``

        - Just the raw bytes, no metadata

      *  ``pickle``

      * ``np.savez()``  -- numpy zip format

        - Compact: binary dump plus metadata

      * netcdf

        - NetCDF4 (https://github.com/Unidata/netcdf4-python)

      * Hdf

        - Pyhdf

        - pytables


Stride Tricks
--------------

numpy arrays are really wrappers about "strided data"

This means that there is a single linear block of memory with the
values in it.

The "strides" describe how that data is arranged to look like an array of more dimensions: 2D, 3D, 4D etc.

Mostly, numpy handles all this under the hood for you, so you can logically work with the data as though it were multi-dimensional.

But you can actually manipulate the description of the data, so that it "acts" like it is arranged differently than it is:

``stride_tricks.ipynb``

.. Using numpy arrays when computation isn't critical
    --------------------------------------------------

    numpy arrays are mostly about performance and memory use.

    But you still may want to use them for other reasons.

    some data naturally is in 2-d or 3-d arrays.

    sometimes you need to work on a sub-view of the data as an independent object.

    For example: A Sudoko game:

     * The board is 9X9
     * Sub-divided into 3X3 squares
     * And you need to examine the rows and columns

    Example: ``sudoku-chb.py``

Exercise
=============

.. rst-class:: left

    Open up `/examples/week-05-numpy/images/images.py`

    **1.** Write a function that rotates the image 180 degrees ( multiple ways to do this )

    **2.** Write a function that crops the image to some dimension of your choice

    **3.** Create a small test RGB image (see below). Choose an RGB value set to replace. How do we target that selection? ( HINT: np.all ):

.. rst-class:: left

    .. code-block:: ipython

        print np.random.choice([0,255],size=(4,4,3)).astype( np.uint8 )
        array([[[255, 255, 255],
                [  0,   0, 255],
                [  0,   0, 255],
                [  0, 255, 255]],
        ...



matplotlib
==========

.. rst-class:: left

  Matplotlib is the most common plotting library for python.

  * Flexible
  * Publication quality
  * Primarily 2d graphics (some 3d)

  See the Gallery here:

  http://matplotlib.org/gallery.html

matplotlib APIs
-------------------

Matplotlib has two different (but related) APIs:

**1.** The "pylab" API:

  * Derived from the MATLAB API, and most suitable for interactive use

**2.** The Object Oriented API:

  * reflects the underlying OO structure of matplolib
  * more "pythonic"
  * much better suited to embedding plotting in applications
  * better suited to re-using code

Tutorial
--------

Here is a small ipython notebook tutorial to run through: 

``SystemDevelopment2015/Examples/week-05-matplotlib``

There are two notebooks in the directory -- the **learner** and **instructor** notebooks. They are identical. Use the **learner** and keep the **instructor** for backup in case something gets messed up.

`Here <https://github.com/WeatherGod/AnatomyOfMatplotlib>`_ is a more thorough tutorial for you to go through when you have more time:


Pandas
=======

.. rst-class:: left

  Python Data Analysis Library

  Pandas provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

  Modeled after R's dataframe concept, it provides some pretty neat tools for doing simple statistical analysis and plotting of larg-ish data sets.

  It's particularly powerful for time series.

  ``http://pandas.pydata.org/``

Learning Pandas
----------------

The official documentation is excellent, including tutorials:

http://pandas.pydata.org/pandas-docs/stable/

http://pandas.pydata.org/pandas-docs/stable/10min.html

http://pandas.pydata.org/pandas-docs/stable/tutorials.html

In addition, there are a large number of tutorials on the web:

This one is oriented to folks familiar with SQL:

http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/

And this is a good one to get started quick:

http://synesthesiam.com/posts/an-introduction-to-pandas.html


Scipy
=====

.. rst-class:: left

  The scipy package itself is a large collection of cool stuff for scientific computing. ( http://docs.scipy.org/doc/scipy/reference/ )

  You'll see there lots of stuff! If it's at all general purpose for computation, you're likely to find it there.

  Some of the most common sub-packages:

   * Special functions (scipy.special)
   * Integration (scipy.integrate)
   * Optimization (scipy.optimize)
   * Interpolation (scipy.interpolate)
   * Fourier Transforms (scipy.fftpack)
   * Signal Processing (scipy.signal)
   * Linear Algebra (scipy.linalg)
   * Spatial data structures and algorithms (scipy.spatial)
   * Statistics (scipy.stats)
   * Multidimensional image processing (scipy.ndimage)






