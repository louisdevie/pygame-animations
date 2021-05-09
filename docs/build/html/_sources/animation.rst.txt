=======================
 Les classes Animation
=======================

------------------
 Classe Animation
------------------

.. class:: pygame_animations.Animation(target, duration[, effect] [, flag=None], **attrs)

    Une animation.
    
    :Paramètres:
        - **target** *(object)*: l'objet à animer.
        - **duration** *(int, float)*: durée de l'animation, en secondes.
        - **effect** *(callable)*: effet à appliquer à l'animation. Il peut être un :ref:`effet natif <nativeeffects>` ou un :ref:`effet personnalisé <customeffects>`.
        - **flag** : sert à repérer l'animation. N'importe quoi peut être utilisé, et un même flag peut être utilisé sur différentes animations.
        - **attrs** : propriétés à animer. pour désigner une sous-propriété ``a.b.c``, utilisez ``a__b__c``
    
    .. attribute:: target
        
        (Lecture seule) L'objet ciblé par l'animation.
    
    .. attribute:: duration
        
        (Lecture seule) La durée de l'animation, convertie et arrondie en millisecondes.
    
    .. function:: start()
        
        Lance l'animation. Elle ne peut être appelée qu'une seule fois.
        
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


--------------------------
 Classe AnimationSequence
--------------------------

.. class:: pygame_animations.AnimationSequence(a, b, [*others] [, flag=None])
    
    Inhérite de ``pygame_animations.Animation``

    Plusieurs animations lancées les une après les autres.
    Une séquence peut être créée en additionnant plusieurs animations : ``anim1 + anim2 + anim3`` vaut ``AnimationSequence(anim1, anim2, anim3)``
    
    :Paramètres:
        - **a**, **b** et **others** *(Animation)*: les animations de la séquence
        - **flag** : sert à repérer l'animation. N'importe quoi peut être utilisé, et un même flag peut être utilisé sur différentes animations.
    
    .. attribute:: animations
        
        (Lecture seule) Les animations qui composent la séquence.
    
    .. attribute:: duration
        
        (Lecture seule) La durée de l'animation, égale à la somme des durées des animations.
    
    .. function:: start()
        
        Lance l'animation. Elle ne peut être appelée qu'une seule fois.
        
        :Paramètres: Aucuns
        
        :Renvoie: ``None``

    .. _stopsequence:

    .. function:: stop([noerror=False])

        Arrête la séquence et appelle :ref:`stop() <stopmethod>` sur toutes les animations.
        
        :Paramètres:
            - **noerror** *(bool)*: quand la méthode est appelée sur une animation qui n'est pas en cours, ignore si ``True`` ou lève une ``RuntimeError`` si ``False``.
        
        :Renvoie: ``None``

    .. _cancelsequence:

    .. function:: cancel([noerror=False])

        Pareil que :ref:`stop() <stopsequence>`, mais appelle :ref:`cancel() <cancelmethod>` sur toutes les animations.

        :Paramètre:
            - **noerror** *(bool)*: voir :ref:`stop() <stopmethod>`
        
        :Renvoie: ``None``

    .. _fastforwardsequence:

    .. function:: fastforward([noerror=False])

        Pareil que :ref:`stop() <stopsequence>`, mais appelle :ref:`fastforward() <fastforwardmethod>` sur toutes les animations.

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


-----------------------
 Classe AnimationGroup
-----------------------

.. class:: pygame_animations.AnimationGroup(a, b, [*others] [, flag=None])
    
    Inhérite de ``pygame_animations.Animation``

    Plusieurs animations lancées en même temps.
    Un groupe peut être créé en utilisant l'opérateur ``&`` entre plusieurs animations : ``anim1 & anim2 & anim3`` vaut ``AnimationGroup(anim1, anim2, anim3)``
    
    :Paramètres:
        - **a**, **b** et **others** *(Animation)*: les animations du groupe
        - **flag** : sert à repérer l'animation. N'importe quoi peut être utilisé, et un même flag peut être utilisé sur différentes animations.
    
    .. attribute:: animations
        
        (Lecture seule) Les animations qui composent le groupe.
    
    .. attribute:: duration
        
        (Lecture seule) La durée de l'animation, égale à la durée la plus longue de toutes les animations.
    
    .. function:: start()
        
        Lance l'animation. Elle ne peut être appelée qu'une seule fois.
        
        :Paramètres: Aucuns
        
        :Renvoie: ``None``

    .. _stopgroup:

    .. function:: stop([noerror=False])

        Arrête la séquence et appelle :ref:`stop() <stopmethod>` sur toutes les animations.
        
        :Paramètres:
            - **noerror** *(bool)*: quand la méthode est appelée sur une animation qui n'est pas en cours, ignore si ``True`` ou lève une ``RuntimeError`` si ``False``.
        
        :Renvoie: ``None``

    .. _cancelgroup:

    .. function:: cancel([noerror=False])

        Pareil que :ref:`stop() <stopgroup>`, mais appelle :ref:`cancel() <cancelmethod>` sur toutes les animations.

        :Paramètre:
            - **noerror** *(bool)*: voir :ref:`stop() <stopmethod>`
        
        :Renvoie: ``None``

    .. _fastforwardgroup:

    .. function:: fastforward([noerror=False])

        Pareil que :ref:`stop() <stopgroup>`, mais appelle :ref:`fastforward() <fastforwardmethod>` sur toutes les animations.

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