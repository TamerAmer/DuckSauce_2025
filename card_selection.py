import pygame.sprite
<<<<<<< HEAD
import settings
from aliens import crabMan
=======
from fighters.alienClasses import crabMan
>>>>>>> 9c5ac98e5fb21fae6c19122895f50ffc2008a1bc

class HandCard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/button.png")
<<<<<<< HEAD
        #self.image = pygame.Surface((30, 45))
        #self.image.fill(settings.TOMATO)  # placeholder surface and rect before the sprite is added
        #self.image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def selectFighter(self, x, y, spritesheet):
        selected_fighter = crabMan.CrabMan(True, spritesheet, x, y)
=======
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft=(x, y))

    def selectFighter(self, x, y, spritesheet):
        selected_fighter = crabMan.CrabMan(True, spritesheet)
>>>>>>> 9c5ac98e5fb21fae6c19122895f50ffc2008a1bc
        return selected_fighter
