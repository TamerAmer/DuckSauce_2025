from os import path

TITLE = "Rift Invaders"
FPS = 30
FALLOW = (193, 154, 107)
GREEN = (0, 255, 0)
TOMATO = (255, 99, 71)
GRID_SPACE_SIZE = 80

# Images
images_dir = path.join(path.dirname(__file__), 'assets', 'sprites')
SPRITESHEET = path.join(images_dir, 'spritesheet.png')
SPRITESHEET_XML = path.join(images_dir, 'spritesheet atlas.xml')