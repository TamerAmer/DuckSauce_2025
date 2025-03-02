import pygame
import sys
from main import Program

# 1. Initialize pygame
pygame.init()

# 2. Define screen dimensions and create the display surface
WIDTH, HEIGHT = 800, 442
#screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 3. Load and scale the background image
background_image = pygame.image.load("assets/IMG_rift.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

temp_screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 4. Create a 'button' rectangle (we'll use this to detect clicks)
button_width, button_height = 100, 100
button_rect = pygame.Rect(0, 0, button_width, button_height)
button_rect.center = (WIDTH // 2, HEIGHT // 2)

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

# 7. Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            pygame.quit()  # Quit the start screen Pygame instance
            p = Program()  # Create the main program
            p.load()
            p.program_loop()
            sys.exit()  # Ensure the script exits after the main loop

        # 8. Draw
        temp_screen.blit(background_image, (0, 0))
        pygame.draw.rect(temp_screen, (200, 200, 200), button_rect)

        if button_rect.collidepoint(pygame.mouse.get_pos()):
            temp_screen.blit(button_icon_hover, button_icon_hover_rect)
        else:
            temp_screen.blit(button_icon, button_icon_rect)

        pygame.display.flip()

# 13. Quit pygame
pygame.quit()
sys.exit()
