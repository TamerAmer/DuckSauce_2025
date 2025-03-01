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

    def load(self):
        # Load resources
        self.spritesheet = spr.Spritesheet(settings.SPRITESHEET, settings.SPRITESHEET_XML)
        print("Load")

    def new(self):
        print("yo")

    def program_loop(self):
        # Performs a program loop
        while self.running:
            self.clock.tick(settings.FPS)
            self.events()
            self.draw()
            self.update()


    def update(self):
        fixedGrid.getMouseGridCoords()
        self.all_sprites.update(self)

    def events(self):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                self.running = False
            keys = pygame.key.get_pressed()
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()

                # Check button collision
                if crabManTile.rect.collidepoint(event.pos[0], event.pos[1]) and (self.selected_fighter == None):
                    self.selected_fighter = crabManTile.selectFighter(event.pos[0], event.pos[1], self.spritesheet)
                    self.all_sprites.add(self.selected_fighter)
                
            # Drag and drop creater
            if self.selected_fighter is not None:
                mouse_pos = pygame.mouse.get_pos()
                self.selected_fighter.x = mouse_pos[0]
                self.selected_fighter.rect.x = mouse_pos[0]
                self.selected_fighter.y = mouse_pos[1]
                self.selected_fighter.rect.y = mouse_pos[1]
                if not pygame.mouse.get_pressed()[0]:  # This means that the selected fighter is deselected
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
                #for i in self.all_sprites:
                #    self.all_sprites.draw(self.screen)

                #    if i.rect.collidepoint(mouse_pos):
                #        outline = hf.get_outline(i.image)
                #        outline_rect = i.rect  # center=self.screen.center)
                        # self.screen.blit(view_layer, (poly_rect.x, poly_rect.y))
                        # pygame.display.update(poly_rect)
                        # pygame.display.flip()

        #hf.camera_handler(self.landscape)

    def draw(self):
        # Draw the screen
        self.screen.fill(settings.FALLOW)

            # pygame.draw.rect(self.screen, FALLOW, self.landscape, 0)
        #for i in range(4):  # Argument of range() must be one higher than the highest entity/immovable.layer value
        #    self.layer_sprites.empty()
        #    self.layer_sprites.add([x for x in self.all_sprites if x.layer == i])
            #self.layer_sprites.draw(self.screen)
        fixedGrid.drawGrid(self.screen)

        self.all_sprites.draw(self.screen)
        self.screen.blit(crabManTile.image, crabManTile.rect.topleft)
        pygame.display.flip()

    def show_title_screen(self):
        # Draw the title screen
        pass


fixedGrid = grid.Grid(5, 6, 80, settings.GREEN, 100, 100)
crabManTile = card_selection.HandCard(0, 0, )
#self.all_sprites.add(crabManTile)

p = Program()

p.load()
p.new()
while p.running:
    p.program_loop()