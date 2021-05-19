============
 Évènements
============

Des évènements pygame sont postés quand une animation débute ou finis.

Ce paquet rajoute donc deux types d'évènements:

.. attribute:: pygame_animations.ANIMATIONSTARTED
    
    Posté quand une animation débute.

    :Attributs de l'évènement:
        - **animation** : l'animation qui a été lancée.

.. attribute:: pygame_animations.ANIMATIONENDED
    
    Posté quand une animation prends fin.

    :Attributs de l'évènement:
        - **animation** : l'animation qui a pris fin.