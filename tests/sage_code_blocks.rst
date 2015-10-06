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
