============
 Évènements
============

Des évènements pygame sont postés quand une animation débute ou finis.

Ce paquet rajoute donc deux types d'évènements:

.. attribute:: pygame_animations.ANIMATIONSTARTED
    
    Posté quand une animation débute.

    :Attributs:
        - **animation** : l'animation qui a été lancée.
        - **flag** : le ``flag`` de l'animation.

.. attribute:: pygame_animations.ANIMATIONENDED
    
    Posté quand une animation prends fin.

    :Attributs:
        - **animation** : l'animation qui a pris fin.
        - **flag** : le ``flag`` de l'animation.