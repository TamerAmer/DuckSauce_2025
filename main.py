import pygame
import grid
import settings
import sprites as spr
from fighters.alienClasses import crabMan
from fighters.alienClasses import rayMan
from fighters.alienClasses import cyclopsMan
import card_selection
import copy


class Program:
    def __init__(self):
        # Initialise
        pygame.init()
        pygame.mixer.init()
        info = pygame.display.Info()
        self.screen_size = (info.current_w, info.current_h)
        self.screen = pygame.display.set_mode((self.screen_size[0]*0.7, self.screen_size[1]*0.7))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        #self.landscape = pygame.Rect(-200, 200, 2000, 2000)
        self.all_sprites = pygame.sprite.Group()
        self.all_drawings = []
        self.simulating = False
        self.layer_sprites = pygame.sprite.Group()
        self.selected_fighter = None
        self.card_list = []
        self.grid = []
        self.grid_aliens = []
        self.battle_button = None

    def load(self):
        # Load resources
        self.spritesheet = spr.Spritesheet(settings.SPRITESHEET, settings.SPRITESHEET_XML)

        # Load grid
        self.grid = grid.Grid(4, 8, settings.GRID_SPACE_SIZE, settings.GREEN, 150, 50)
        self.grid.GenerateCoordinates()

        # Load backdrop
        backdrop_background = pygame.image.load("assets/backdrop.png").convert_alpha()
        backdrop_alien_domain = pygame.image.load("assets/alien_domain.png").convert_alpha()
        backdrop_earth_domain = pygame.image.load("assets/earth_domain.png").convert_alpha()
        backdrop_grid_field = pygame.image.load("assets/grid_field.png").convert_alpha()

        # Scale the backdrop if necessary
        backdrop_background = pygame.transform.scale(backdrop_background, self.screen.get_size())
        backdrop_alien_domain = pygame.transform.scale(backdrop_alien_domain, (self.screen.get_size()[0] * 0.5, self.screen.get_size()[1] * 0.5))
        backdrop_alien_domain = pygame.transform.rotate(backdrop_alien_domain, 90)  # Rotate 90 degrees
        backdrop_earth_domain = pygame.transform.scale(backdrop_earth_domain, (self.screen.get_size()[0] * 0.5, self.screen.get_size()[1] * 0.5))
        backdrop_earth_domain = pygame.transform.rotate(backdrop_earth_domain, 270)  # Rotate 90 degrees
        backdrop_grid_field = pygame.transform.scale(backdrop_grid_field, (settings.GRID_SPACE_SIZE * (self.grid.columns), settings.GRID_SPACE_SIZE * (self.grid.rows )))

        # **Calculate Dynamic Positions**
        earth_x = self.grid.gridOffsetX - backdrop_earth_domain.get_width() + 50
        alien_x = self.grid.gridOffsetX + (self.grid.columns * self.grid.gridSpaceSize) - 50

        # Store images in all_drawings as (image, position) tuples
        self.all_drawings.append((backdrop_background, (0, 0)))
        self.all_drawings.append((backdrop_alien_domain, (alien_x, -40)))
        self.all_drawings.append((backdrop_earth_domain, (earth_x, -10)))
        self.all_drawings.append((backdrop_grid_field, (self.grid.gridOffsetX, self.grid.gridOffsetZ)))

        # Tile (buttons) definitions
        rayManTile = card_selection.HandCard(100, 470, self.spritesheet, "rayman", rayMan.RayMan(True, self.spritesheet))
        crabManTile = card_selection.HandCard(250, 470, self.spritesheet, "crabman", crabMan.CrabMan(True, self.spritesheet))
        cyclopsManTile = card_selection.HandCard(400, 470, self.spritesheet, "cyclopsman", cyclopsMan.CyclopsMan(True, self.spritesheet))
        self.card_list.append(crabManTile)
        self.card_list.append(rayManTile)
        self.card_list.append(cyclopsManTile)
        self.all_sprites.add(crabManTile)
        self.all_sprites.add(rayManTile)
        self.all_sprites.add(cyclopsManTile)

        self.battle_button = self.battleButton()

    def battleButton(self):
        button_width, button_height = 100, 100
        button_rect = pygame.Rect(0, 0, button_width, button_height)
        button_rect.center = (800, 520)
        button_icon = pygame.image.load("assets/button1.png").convert_alpha()
        icon_width, icon_height = button_width, button_width
        button_icon = pygame.transform.scale(button_icon, (icon_width, icon_height))
        button_icon_hover = pygame.image.load("assets/button2.png").convert_alpha()
        button_icon_hover = pygame.transform.scale(button_icon_hover, (icon_width, icon_height))
        button_icon_rect = button_icon.get_rect()
        button_icon_rect.center = button_rect.center
        button_icon_hover_rect = button_icon_hover.get_rect()
        button_icon_hover_rect.center = button_rect.center

        return (button_rect, button_icon_rect, button_icon_hover, button_icon_hover_rect, button_icon)

    def program_loop(self):
        # Performs a program loop
        while self.running:
            self.clock.tick(settings.FPS)
            self.events()
            self.draw()
            self.update()


    def update(self):
        self.grid.getMouseGridCoords()
        self.all_sprites.update(self)

    def events(self):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                self.running = False
            keys = pygame.key.get_pressed()
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()

                # Check button collision
                for i in self.card_list:
                    if i.rect.collidepoint(event.pos[0], event.pos[1]) and (self.selected_fighter is None):
                        self.selected_fighter = type(i.fighter)(True, self.spritesheet)  # Clone the fighter
                        self.all_sprites.add(self.selected_fighter)

            # Drag and drop creater
            if self.selected_fighter is not None:
                mouse_pos = pygame.mouse.get_pos()
                self.selected_fighter.x = mouse_pos[0]
                self.selected_fighter.rect.x = mouse_pos[0]
                self.selected_fighter.y = mouse_pos[1]
                self.selected_fighter.rect.y = mouse_pos[1]
                if not pygame.mouse.get_pressed()[0]:  # This means that the selected fighter is deselected

                    # Here we place aliens
                    selected_alien = copy.deepcopy(self.selected_fighter)
                    isPlacementValid = self.grid.checkAlienPlacement(selected_alien, self.grid.getMouseGridCoords())
                    if isPlacementValid:
                        self.grid.addAlien(selected_alien, self.grid.getMouseGridCoords())
                        selected_alien.rect.x = self.grid.gridOffsetX + self.grid.getMouseGridCoords()[0] * self.grid.gridSpaceSize
                        selected_alien.rect.y = self.grid.gridOffsetZ + self.grid.getMouseGridCoords()[1] * self.grid.gridSpaceSize
                        self.all_sprites.add(selected_alien)

                    self.all_sprites.remove(self.selected_fighter)
                    self.selected_fighter = None

            if self.selected_fighter is not None:
                mouse_pos = pygame.mouse.get_pos()
                # if pygame.mouse.get_pressed()[0]:
                    # self.selected_fighter = None
                self.selected_fighter.x = mouse_pos[0]
                self.selected_fighter.y = mouse_pos[1]

            # Battle button event
            if event.type == pygame.MOUSEBUTTONDOWN and self.battle_button[0].collidepoint(event.pos):
                print("horray")



    def draw(self):
        for image, position in self.all_drawings:
            self.screen.blit(image, position)
        self.grid.drawGrid(self.screen)
        self.all_sprites.draw(self.screen)
        if self.battle_button[0].collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.battle_button[2], self.battle_button[3])
        else:
            self.screen.blit(self.battle_button[4], self.battle_button[1])
        pygame.display.flip()

    def show_title_screen(self):
        # Draw the title screen
        pass



#self.all_sprites.add(crabManTile)

