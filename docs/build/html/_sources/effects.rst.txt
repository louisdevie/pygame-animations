====================
 Effets d'animation
====================

.. _nativeeffects:

---------------
 Effets natifs
---------------

Les effets natif sont regroupés dans l'énumération ``pygame_animations.Effects``:

+--------------------------+--------------------------------------------------+
|``Effects.linear``        | vitesse constante                                |
+--------------------------+--------------------------------------------------+
|``Effects.sin_in``        | accélération, de la plus douce à la plus brutale |
|                          |                                                  |
|``Effects.square_in``     |                                                  |
|                          |                                                  |
|``Effects.cubic_in``      |                                                  |
|                          |                                                  |
|``Effects.quad_in``       |                                                  |
+--------------------------+--------------------------------------------------+
|``Effects.sin_out``       | décélération, de la plus douce à la plus brutale |
|                          |                                                  |
|``Effects.square_out``    |                                                  |
|                          |                                                  |
|``Effects.cubic_out``     |                                                  |
|                          |                                                  |
|``Effects.quad_out``      |                                                  |
+--------------------------+--------------------------------------------------+
|``Effects.sin_in_out``    | accélération au début et décélération à la fin,  |
|                          | de la plus douce à la plus brutale               |
|``Effects.square_in_out`` |                                                  |
|                          |                                                  |
|``Effects.cubic_in_out``  |                                                  |
|                          |                                                  |
|``Effects.quad_in_out``   |                                                  |
+--------------------------+--------------------------------------------------+
|``Effects.sin_shake``     | avance et recule avec une amplitude décroissante |
+--------------------------+--------------------------------------------------+
|``Effects.bounce_in``     | rebondis au début                                |
+--------------------------+--------------------------------------------------+
|``Effects.bounce_out``    | rebondis à la fin                                |
+--------------------------+--------------------------------------------------+
|``Effects.bounce_in_out`` | rebondis au début et à la fin                    |
+--------------------------+--------------------------------------------------+

.. Tip:: ``Effects`` étant une énumération, vous pouvez l'utiliser dans un boucle ``for in``, et l'effet ``Effects.linear`` peut aussi être désigné par ``Effects["linear"]`` ou ``Effects[0]`` (attention, ils ne sont pas dans l'ordre dans le tableau ci-dessus).

----------------------
 Effets personnalisés
----------------------

.. _customeffects:

Un objet qui valide les conditions suivantes peut être utilisée comme effet:

- appellable (fonction, expression lambda, ...)
- prends un seul paramètre, de type ``float`` entre 0 (inclus) et 1 (inclus)
- renvoie un ``float``

Le paramètre est la progression *dans le temps* de l'animation (de 0 au début à 1 à la fin).

La valeur revoyée est la progression dans l'animation (0 = état initial et 1 = état final). Elle doit être à 0 au début et à 1 à la fin (exception: ``Effects.sin_shake`` qui revient à 0).