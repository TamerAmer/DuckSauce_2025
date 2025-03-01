import pygame
import settings

class Alien(pygame.sprite.Sprite):
    def __init__(self, selected, spritesheet, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.selected = selected
        self.spritesheet = spritesheet
        self.image = pygame.Surface((10, 10))
        self.image.fill(settings.TOMATO)  # placeholder surface and rect before the sprite is added

        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.original_image = self.image
        self.rect.topleft = (x, y)

        self.x = x
        self.y = y


