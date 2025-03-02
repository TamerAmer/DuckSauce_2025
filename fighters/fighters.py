import settings
import pygame

class Fighters(pygame.sprite.Sprite):
    def __init__(self, selected, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.selected = selected
        self.spritesheet = spritesheet
        self.image = pygame.Surface((10, 10))
        self.image.fill(settings.TOMATO)  # placeholder surface and rect before the sprite is added
        self.rect = self.image.get_rect()
        self.original_image = self.image