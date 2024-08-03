# Example file showing a basic pygame "game loop"
import pygame
from button import Button

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

record_button = Button("Record", None, None, pygame.K_q)

# initialize the test bit outside of the loop
o = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                o = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                o = False  
    
    
    record_button.loop(events, o)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()