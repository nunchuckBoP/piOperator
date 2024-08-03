from machine import GameEngine, gListener
import pygame
from button import Button


def button_press(*args, **kwargs):
    print("%s button pressed" % kwargs['name'])
# end button press
    
def button_release(*args, **kwargs):
    print("%s button released" % kwargs['name'])
# end button press

# BEATBOX
# Made for a raspberry pi W / or 3/4.
# This is a beat box module, created in pygame
if __name__ == '__main__':

        # Example file showing a basic pygame "game loop"

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    record_button = Button("Record", None, None, pygame.K_q)

    buttons = [
        
        [
            Button("0x0", button_press, button_release, pygame.K_1),
            Button("0x1", button_press, button_release, pygame.K_2),
            Button("0x3", button_press, button_release, pygame.K_3),
            Button("0x4", button_press, button_release, pygame.K_4),
            Button("0x5", button_press, button_release, pygame.K_5)
        ],
        
        [
            Button("1x0", button_press, button_release, pygame.K_q),
            Button("1x1", button_press, button_release, pygame.K_w),
            Button("1x2", button_press, button_release, pygame.K_e),
            Button("1x3", button_press, button_release, pygame.K_r),
            Button("1x4", button_press, button_release, pygame.K_t)
        ],
        
        [
            Button("2x0", button_press, button_release, pygame.K_a),
            Button("2x1", button_press, button_release, pygame.K_s),
            Button("2x2", button_press, button_release, pygame.K_d),
            Button("2x3", button_press, button_release, pygame.K_f),
            Button("2x4", button_press, button_release, pygame.K_g)
        ],
        
        [
            Button("3x0", button_press, button_release, pygame.K_z),
            Button("3x1", button_press, button_release, pygame.K_x),
            Button("3x2", button_press, button_release, pygame.K_c),
            Button("3x3", button_press, button_release, pygame.K_v),
            Button("3x4", button_press, button_release, pygame.K_b)
        ]
    ]

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            # end if
        # end for
        
        for a_row in buttons:
            for aButton in a_row:
                aButton.loop(events, False)
            # end for
        # end for
        
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()