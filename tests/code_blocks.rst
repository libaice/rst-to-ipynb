Code blocks
-----------

.. code:: python

    this = 'is a code block'
    x = 1
    no = 'really!'
    p = argwhere(x == 2)

.. code:: python

    from pylab import linspace
    t = linspace(0, 1)
    x = t**2

::

    from pylab import *
    x = logspace(0, 1)
    y = x**2
    figure()
    plot(x, y)
    show()

Support for Python doctest code blocks::

    >>> 1+1
    2
    >>> for x in range(3):
    ...      print x
    0
    1
    2
    >>> x = 1
    >>> x = 2
