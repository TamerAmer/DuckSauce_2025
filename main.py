import pygame
import pygame.gfxdraw
from os import path

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (79, 79, 69)
YELLOW = (255, 255, 0)
BLUE = (51, 153, 255)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
DODGER_BLUE = (30, 144, 255)
LIGHT_BLUE = (135, 206, 250)
TOMATO = (255, 99, 71)

# Game Properties
FPS = 20
GRID_SIZE = 70

def app_setup():
    #time.sleep(2)
    screen, screen_size = get_display()

def get_display():
    screen_size = pygame.display.get_surface().get_size()
    screen = pygame.display.get_surface()
    return screen, screen_size

def adjust_grid_for_screen(tile_size):
    """Push grid in place by some offset."""
    screen, screen_size = get_display()
    grid_window = tile_size*10
    x_offset = screen_size[0] // 2 - grid_window // 2
    y_offset = screen_size[1] // 2 - grid_window // 2
    #[x_offset, y_offset] = coords_point_to_from_pygame([x_offset, y_offset])
    return screen, grid_window, x_offset, y_offset


def draw_grid(tile_size):
    screen, _, x_offset, y_offset = adjust_grid_for_screen(tile_size)

    for r in range(10):
        for c in range(10):
            pygame.draw.rect(screen, BLACK, [x_offset + c*tile_size, y_offset + r*tile_size, tile_size, tile_size], 1)


# Initialise
pygame.init()
update_clock = pygame.time.Clock()

app_setup()