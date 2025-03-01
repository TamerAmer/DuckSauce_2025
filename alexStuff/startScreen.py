import pygame
import sys

# 1. Initialize pygame
pygame.init()

# 2. Define screen dimensions and create the display surface
WIDTH, HEIGHT = 800, 442
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button with Image")

# 3. Load and scale the background image
background_image = pygame.image.load("alexStuff/IMG_rift.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# 4. Create a 'button' rectangle (we'll use this to detect clicks)
button_width, button_height = 50, 50
button_rect = pygame.Rect(0, 0, button_width, button_height)
button_rect.center = (WIDTH // 2, HEIGHT // 2)

# 5. Load an image to place inside the button (normal state)
button_icon = pygame.image.load("alexStuff/butt2.png")
icon_width, icon_height = 50, 50
button_icon = pygame.transform.scale(button_icon, (icon_width, icon_height))

# **Load an image for the hover state**
button_icon_hover = pygame.image.load("alexStuff/butt.png")
button_icon_hover = pygame.transform.scale(button_icon_hover, (icon_width, icon_height))

# 6. Get a Rect for the icons, so we can place them in the button center
button_icon_rect = button_icon.get_rect()
button_icon_rect.center = button_rect.center

# **Hover icon rect (same center)**
button_icon_hover_rect = button_icon_hover.get_rect()
button_icon_hover_rect.center = button_rect.center

# 7. Main game loop
running = True
while running:
    # 8. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the button area
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    # 9. Draw the background image
    screen.blit(background_image, (0, 0))

    # 10. Draw the button rectangle (visual representation of a button)
    pygame.draw.rect(screen, (200, 200, 200), button_rect)

    # 11. Draw the appropriate icon (normal or hover)
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        # Mouse is hovering, draw the hover icon
        screen.blit(button_icon_hover, button_icon_hover_rect)
    else:
        # Mouse is not hovering, draw the normal icon
        screen.blit(button_icon, button_icon_rect)

    # 12. Update the display
    pygame.display.flip()

# 13. Quit pygame
pygame.quit()
sys.exit()
