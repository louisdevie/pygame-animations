============================
 Comment utiliser le paquet
============================

--------------------------------
 Intégrer le paquet avec pygame
--------------------------------

Importer le paquet
==================

*Après* avoir importé ``pygame``, importez le paquet avec

.. code-block:: python
    
    import pygame_animations

Le nom est un peut long, alors il vaut mieux que vous l'importiez en tant que

.. code-block:: python
    
    import pygame_animations as anim


Appeler ``update_animation``
============================

La seule chose nécéssaire pour que le paquet fonctionne, c'est d'appeler

.. code-block:: python
    
    anim.update_animations()

à chaque frame. Le mieux est de l'appeler juste avant de dessiner quoit que ce soit.

----------------------
 Créer des animations
----------------------

Pour créer une animation, créez un objet ``pygame_animations.Animation`` et appelez sa méthode ``start()`` pour l'éxecuter.

Exemple : Déplacer un lutin
===========================

Le code suivant déplace le lutin ``monlutin`` en x=200 en 2 secondes :

.. code-block:: python
    
    anim.Animation(monlutin, 2, rect__x=200).start()


``monlutin`` est l'objet à animer. Pour cet exemple, c'est un ``pygame.sprite.Sprite`` mais vous pouvez cibler n'importe quel objet.


``2`` est la durée de l'animation, en secondes. Vous pouvez aussi passer un flottant, et la durée sera arrondie à la milliseconde.


``rect__x=200`` est la propriété à animer (ici ``monlutin.rect.x``).
Le ``__`` remplace les ``.`` pour viser les sous-propriétés, par exemple ``a.b.c`` devient ``a__b__c``.
Vous pouvez animer autant de propriétes que vous voulez en même temps. 

-----------------------------
 Synthèse : un "Hello World"
-----------------------------

.. code-block:: python
    
    import pygame
    import pygame_animations as anim
    
    pygame.init()
    
    surface = pygame.display.set_mode((640, 480))
    
    font = pygame.font.SysFont('default', 52)
    
    class MySprite (pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = font.render("Hello, World!", 1, (255, 255, 255))
            self.rect = self.image.get_rect()
    label = MySprite()
    group = pygame.sprite.Group(label)
    
    a = anim.Animation(label, 2, anim.Effects.cubic_in_out, rect__x=640-label.rect.w, rect__y=480-label.rect.h)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
        
        t = pygame.time.get_ticks()
        if t>3000 and a.can_run(): # l'animation démarre après 3s
        a.start()
        
        anim.update_animations()
        
        surface.fill((0, 0, 0))
        group.draw(surface)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()