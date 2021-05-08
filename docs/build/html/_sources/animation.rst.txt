=====================
 La classe Animation
=====================

.. class:: pygame_animations.Animation(target, duration[, effect], **attrs)

    Une animation.
    
    :Paramètres:
        - **target** *(object)*: l'objet à animer.
        - **duration** *(int, float)*: durée de l'animation, en secondes.
        - **effect** *(callable)*: effet à appliquer à l'animation. Il peut être un :ref:`effet natif <nativeeffects>` ou un :ref:`effet personnalisé <customeffects>`.
        - **attrs** : propriétés à animer. pour désigner une sous-propriété ``a.b.c``, utilisez ``a__b__c``
    
    .. attribute:: target
        
        (Lecture seule) L'objet ciblé par l'animation.
    
    .. attribute:: duration
        
        (Lecture seule) La durée de l'animation, convertie et arrondie en millisecondes.
    
    .. function:: start()
        
        Lance l'animation. Elle ne peut être appelée q'une seule fois.
        
        :Paramètres: Aucuns
        
        :Renvoie: ``None``

    .. _stopmethod:

    .. function:: stop([noerror=False])

        Arrête l'animation et laisse l'objet animé tel quel. Une fois arrêtée, elle ne peut pas être relancée.
        
        :Paramètres:
            - **noerror** *(bool)*: quand la méthode est appelée sur une animation qui n'est pas en cours, ignore si ``True`` ou lève une ``RuntimeError`` si ``False``.
        
        :Renvoie: ``None``

    .. _cancelmethod:

    .. function:: cancel([noerror=False])

        Pareil que :ref:`stop() <stopmethod>`, mais remet l'objet animé dans son état initial.

        :Paramètre:
            - **noerror** *(bool)*: voir :ref:`stop() <stopmethod>`
        
        :Renvoie: ``None``

    .. _fastforwardmethod:

    .. function:: fastforward([noerror=False])

        Pareil que :ref:`stop() <stopmethod>`, mais met l'objet animé dans son état final.

        :Paramètre:
            - **noerror** *(bool)*: voir :ref:`stop() <stopmethod>`
        
        :Renvoie: ``None``
        
    .. function:: is_running()

        Renvoie ``True`` si l'animation est en cours.
        
        :Paramètres: Aucuns
        
        :Renvoie: ``bool``
        
    .. function:: can_run()

        Renvoie ``True`` si l'animation n'a pas encore été lancée.
        
        :Paramètres: Aucuns
        
        :Renvoie: ``bool``