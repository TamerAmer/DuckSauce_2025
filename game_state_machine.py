import pygame
import grid
import settings
import sprites as spr
from fighters.alienClasses import crabMan
import card_selection


class Program:
    def __init__(self):
        # Initialise
        pygame.init()
        pygame.mixer.init()
        info = pygame.display.Info()
        self.screen_size = (info.current_w, info.current_h)
        self.screen = pygame.display.set_mode((self.screen_size[0] * 0.7, self.screen_size[1] * 0.7))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.all_drawings = []
        self.selected_fighter = None
        self.states = ["title", "selection", "battle"]
        self.current_state = "title"
        self.spritesheet = None
        self.grid = None

    def load(self):
        # Load resources
        self.spritesheet = spr.Spritesheet(settings.SPRITESHEET, settings.SPRITESHEET_XML)
        self.grid = grid.Grid(5, 6, 80, settings.GREEN, 100, 100)
        self.grid.GenerateCoordinates()

    def constant_updater(self):
        self.clock.tick(settings.FPS)
        self.events()
        self.draw()
        self.update()

    def state_machine_controller(self):
        # Controls the states of the game
        if self.current_state == "title":
            self.state_title_screen()
        if self.current_state == "selection":
            print("hes")
            self.state_title_screen()
        if self.current_state == "battle":
            self.state_title_screen()

    def state_title_screen(self):
        background_image = pygame.image.load("assets/IMG_rift.png")
        background_image = pygame.transform.scale(background_image, (self.screen_size[0] * 0.7, self.screen_size[1] * 0.7))

        button_width, button_height = 100, 100
        button_rect = pygame.Rect(0, 0, button_width, button_height)
        button_rect.center = (self.screen_size[0] * 0.7 // 2, self.screen_size[1] * 0.7 // 2)

        # 5. Load an image to place inside the button (normal state)
        button_icon = pygame.image.load("assets/Butts1.png")
        icon_width, icon_height = button_width, button_width
        button_icon = pygame.transform.scale(button_icon, (icon_width, icon_height))

        # **Load an image for the hover state**
        button_icon_hover = pygame.image.load("assets/Butts2.png")
        button_icon_hover = pygame.transform.scale(button_icon_hover, (icon_width, icon_height))

        # 6. Get a Rect for the icons, so we can place them in the button center
        button_icon_rect = button_icon.get_rect()
        button_icon_rect.center = button_rect.center

        # **Hover icon rect (same center)**
        button_icon_hover_rect = button_icon_hover.get_rect()
        button_icon_hover_rect.center = button_rect.center
        while self.current_state == "title":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the user clicked on the button area
                    if button_rect.collidepoint(event.pos):
                        self.current_state = "selector"
                        return

            # 9. Draw the background image
            self.screen.blit(background_image, (0, 0))

            # 10. Draw the button rectangle (visual representation of a button)
            pygame.draw.rect(self.screen, (200, 200, 200), button_rect)

            # 11. Draw the appropriate icon (normal or hover)
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                # Mouse is hovering, draw the hover icon
                self.screen.blit(button_icon_hover, button_icon_hover_rect)
            else:
                # Mouse is not hovering, draw the normal icon
                self.screen.blit(button_icon, button_icon_rect)

            # 12. Update the display
            pygame.display.flip()


    def state_selector_screen(self):
        # TODO backgraound
        # TODO for loop generates HandCards
        # TODO for i in list, position on screen
        while self.current_state is "selector":
            print("selector")
            self.constant_updater()

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
                #if crabManTile.rect.collidepoint(event.pos[0], event.pos[1]) and (self.selected_fighter == None):
                #    self.selected_fighter = crabManTile.selectFighter(event.pos[0], event.pos[1], self.spritesheet)
                #    self.all_sprites.add(self.selected_fighter)

            # Drag and drop creater
            if self.selected_fighter is not None:
                mouse_pos = pygame.mouse.get_pos()
                self.selected_fighter.x = mouse_pos[0]
                self.selected_fighter.rect.x = mouse_pos[0]
                self.selected_fighter.y = mouse_pos[1]
                self.selected_fighter.rect.y = mouse_pos[1]
                if not pygame.mouse.get_pressed()[0]:  # This means that the selected fighter is deselected
                    self.all_sprites.remove(self.selected_fighter)
                    self.selected_fighter = None

                    # Here we place aliens
                    new_crab_man = crabMan.CrabMan(True, self.spritesheet)
                    #isPlacementValid = fixedGrid.checkAlienPlacement(new_crab_man, fixedGrid.getMouseGridCoords())
                    #if isPlacementValid:
                    #    fixedGrid.addAlien(new_crab_man, fixedGrid.getMouseGridCoords())
                    #    new_crab_man.rect.x = fixedGrid.gridOffsetX + fixedGrid.getMouseGridCoords()[
                    #        0] * fixedGrid.gridSpaceSize
                    #    new_crab_man.rect.y = fixedGrid.gridOffsetZ + fixedGrid.getMouseGridCoords()[
                    #        1] * fixedGrid.gridSpaceSize

                    #    self.all_sprites.add(new_crab_man)

                    # self.layer_sprites.empty()
                    # self.layer_sprites.add([x for x in self.all_sprites])
                    # self.layer_sprites.draw(self.screen)
                    if self.selected_fighter in self.all_sprites:
                        self.all_sprites.remove(self.selected_fighter)
                    self.selected_fighter = None

            if self.selected_fighter is not None:
                mouse_pos = pygame.mouse.get_pos()
                # if pygame.mouse.get_pressed()[0]:
                # self.selected_fighter = None
                self.selected_fighter.x = mouse_pos[0]
                self.selected_fighter.y = mouse_pos[1]

            self.layer_sprites.empty()
            self.layer_sprites.add([x for x in self.all_sprites])
            self.layer_sprites.draw(self.screen)
            # for i in self.all_sprites:
            #    self.all_sprites.draw(self.screen)

            #    if i.rect.collidepoint(mouse_pos):
            #        outline = hf.get_outline(i.image)
            #        outline_rect = i.rect  # center=self.screen.center)
            # self.screen.blit(view_layer, (poly_rect.x, poly_rect.y))
            # pygame.display.update(poly_rect)
            # pygame.display.flip()

        # hf.camera_handler(self.landscape)

    def draw(self):
        # Draw the screen
        self.screen.fill(settings.FALLOW)


        #fixedGrid.drawGrid(self.screen)

        self.all_sprites.draw(self.screen)
        #self.screen.blit(crabManTile.image, crabManTile.rect.topleft)
        pygame.display.flip()

    def show_title_screen(self):
        # Draw the title screen
        pass
