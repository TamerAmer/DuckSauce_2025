import pygame.sprite
import settings
from fighters.alienClasses import crabMan

class HandCard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/button.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft=(x, y))

    def selectFighter(self, x, y, spritesheet):
        selected_fighter = crabMan.CrabMan(True, spritesheet)
        return selected_fighter
