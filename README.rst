==============
``switchcase``
==============

``switchcase`` implements a simple Switch-Case construct in Pure Python.

Under the hood, the ``switch`` function works by simply returning a length-1
list containing a matching function.  The entire implementation is 3 lines long:

.. code:: python

    from operator import eq
    def switch(value, comp=eq):
        return [lambda match: comp(match, value)]


Basic Usage
-----------

.. code-block:: python

    >>> from switchcase import switch
    >>> def func(x):
    ...     for case in switch(x):
    ...         if case(0):
    ...             print("x was 0")
    ...             break
    ...         if case(1):
    ...             print("x was 1")
    ...             break
    ...     else:
    ...         print("x was unmatched")
    >>> func(0)
    "x was 0"
    >>> func(1)
    "x was 1"
    >>> func(2)
    "x was unmatched"


Custom Comparisons
------------------

By default, ``switch`` uses ``operator.eq`` to compare the value passed to
``switch`` and the values subsequently passed to ``case``.  You can override
this behavior by passing a comparator function to ``switch`` as a second
argument.


.. code-block:: python

   >>> import re
   >>> from switchcase import switch
   >>> def f(x):
   ...     out = []
   ...     for case in switch(x, comp=re.match):
   ...         if case("foo_bar"):
   ...             out.append(0)
   ...             break
   ...         if case("foo_.*"):
   ...             out.append(1)
   ...         if case(".*_bar"):
   ...             out.append(2)
   ...         return out
   >>> f("foo_bar")
   [0]
   >>> f("foo_notbar")
   [1]
   >>> f("notfoo_bar")
   [2]
   >>> f("foo____bar")
   [1, 2]
