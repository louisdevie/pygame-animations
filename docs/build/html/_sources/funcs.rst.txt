===========
 Fonctions
===========

.. function:: pygame_animations.update_animations()
    
    Actualise toutes les animations en cours. Il faut l'appeler avant de dessiner chaque frame.
    
    :Paramètres: Aucuns
    
    :Renvoie: ``None``

.. function:: pygame_animations.stop_all([flags=None])
    
    Arrête toutes les animations en cours. Voir :ref:`Animation.stop <stopmethod>` pour plus d'informations.

    Si ``flags`` est passé, arrête uniquement les animations correspondantes. Voir :ref:`Animation.match <matchmethod>` pour plus d'informations.
    
    :Paramètres: Aucuns
    
    :Renvoie: ``None``

.. function:: pygame_animations.cancel_all([flags=None])
    
    Annule toutes les animations en cours. Voir :ref:`Animation.cancel <cancelmethod>` pour plus d'informations.

    Si ``flags`` est passé, annule uniquement les animations correspondantes. Voir :ref:`Animation.match <matchmethod>` pour plus d'informations.
    
    :Paramètres: Aucuns
    
    :Renvoie: ``None``

.. function:: pygame_animations.fastforward_all([flags=None])
    
    Termine toutes les animations en cours. Voir :ref:`Animation.fastforward <fastforwardmethod>` pour plus d'informations.

    Si ``flags`` est passé, termine uniquement les animations correspondantes. Voir :ref:`Animation.match <matchmethod>` pour plus d'informations.
    
    :Paramètres: Aucuns
    
    :Renvoie: ``None``