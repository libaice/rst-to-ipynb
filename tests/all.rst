# This file is built automatically; don't edit

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

Sage code blocks
----------------

Complexité de l'algorithme de tri de Python
===========================================

::

    sage: 1+1
    2
    sage: for x in range(3):
    ....:     print x
    0
    1
    2

Two sage commands without intermediate output get joined in a single
input cell; no output is produced if none is specified::

    sage: 1+1
    sage: 2+2

    sage: 3+3

#. Nested code block A

   ::

       sage: 1+1

#.  Nested code block B

    ::

       sage: 1+1

#. Nested code block C (failing: the inner indent should match the itemized text indent)

    ::

        sage: 1+1

.. TOPIC:: A doubly nested sage code block

    #.  Calculer le plus grand élément d'une liste

        ::

            sage: 1+1

        ::

            sage: def plus_grand_element(liste):
            ....:     """
            ....:     Renvoie le plus grand élément de la liste
            ....:     EXAMPLES::
            ....:         sage: plus_grand_element([7,3,1,10,4,10,2,9])
            ....:         10
            ....:         sage: plus_grand_element([7])
            ....:         7
            ....:     """
            ....:     resultat = liste[0]
            ....:     for i in range(1, len(liste)-1):
            ....:         # Invariant: resultat est le plus grand element de liste[:i]
            ....:         assert resultat in liste[:i]
            ....:         assert all(resultat >= x for x in liste[:i])
            ....:         if liste[i] > resultat:
            ....:             resultat = liste[i]
            ....:     return resultat
            sage: plus_grand_element([7,3,1,10,4,10,2,9])
            10

        Foo (Failing).

        Bla::

            sage: 1+1

        Don't forget the mandatory new line after `::` ::
            sage: 1+1

.. NOTE::

   Blah (Failing)::

       sage: 1+1

   Foo (Failing)::

       sage: 1+1



.. TOPIC:: Note

   Blah::

       sage: 1+1

   Foo::

       sage: 1+1


Complexité de l'algorithme de tri de Python
===========================================

.. TOPIC:: Exercice

    #.  Estimer la complexité de la fonction suivante

        ::

	    sage: def fusion(l1, l2):
	    ....:     sort(l1+l2)

Images
------

.. image:: hood.jpg
   :width: 60 %

List
----

Bullets
~~~~~~~

-  b1
-  b2
-  b3

List
~~~~

1. l1
2. l2
3. l3

Math
----

Inline maths with math role: `x^3+\frac{1+\sqrt{2}}{\pi}`

Inline maths with default role: :math:`x^3+\frac{1+\sqrt{2}}{\pi}`

Inline maths using dollar signs (not supported yet): $x^3+\frac{1+\sqrt{2}}{\pi}$

.. MATH::

   x^3+\frac{1+\sqrt{2}}{\pi}

Quote
-----

    This is a quote!

Table
-----

+------+------+
| C1   | C2   |
+======+======+
| a    | b    |
+------+------+
| c    | d    |
+------+------+

Topics
------

.. TOPIC:: Definition

    Hello, this is a block definition

    Some more text

    #.  An enumeration

        .. TOPIC:: Note

            A nested topic within the enumeration within a topic


        Back to the item

    #.  Next item

.. TOPIC:: Exercice

    Donner des algorithmes et leur complexité au pire et en moyenne
    pour les problèmes suivants:

    #.  Effectuer un pivot de Gauss sur une matrice

        .. TOPIC:: Note

            Digression: Complexité arithmétique versus complexité binaire

    #.  Calculer le déterminant d'une matrice

