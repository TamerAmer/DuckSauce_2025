import pygame
import pygame.gfxdraw
import numpy
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
    info = pygame.display.Info()
    screen_size = (info.current_w, info.current_h)
    #screen_size = pygame.display.get_desktop_sizes()
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


def check_grid(tile_size):
    """Get grid coordinates of mouse."""
    #mouse_pos = coords_point_to_from_pygame(pygame.mouse.get_pos())
    mouse_pos = pygame.mouse.get_pos()
    _, _, x_offset, y_offset = adjust_grid_for_screen(tile_size)
    #[x_offset, y_offset] = coords_point_to_from_pygame([x_offset, y_offset])

    tile_coords = (-1, -1)
    for r in range(10):
        for c in range(10):
            tile = pygame.Rect(x_offset + c*tile_size, y_offset + r*tile_size, tile_size, tile_size)
            if tile.collidepoint(mouse_pos):
                tile_coords = (c, r)
    return tile_coords


def get_coords_from_grid_matrix(tile_size, coords):
    """Get pixel coordinates from grid coordinates."""
    _, grid_window, x_offset, y_offset = adjust_grid_for_screen(tile_size)
    x = tile_size*coords[0] + x_offset
    y = tile_size*coords[1] + y_offset
    return [x, y]


# Initialise
pygame.init()
update_clock = pygame.time.Clock()
win = pygame.display.set_mode((1200, 900))

#app_setup()


grid_coords = check_grid(GRID_SIZE)

if (grid_coords[0] >= 0 and grid_coords[0] <= 9) and (grid_coords[1] >= 6 and grid_coords[1] <= 9):
    grid_screen_coords = get_coords_from_grid_matrix(GRID_SIZE, grid_coords)

running = True
while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill(WHITE)
    draw_grid(GRID_SIZE)
    pygame.display.update()