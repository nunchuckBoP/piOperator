from machine import GameEngine, gListener
import pygame
from button import Button
from metranome import BeatCounter


def button_press(*args, **kwargs):
    print("Button pressed\trow:%s\tcolumn:%s" % (kwargs['row'], kwargs['column']))
# end button press
    
def button_release(*args, **kwargs):
    print("Button released\trow:%s\tcolumn:%s" % (kwargs['row'], kwargs['column']))
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
    fps = 60
    counter = BeatCounter(fps, bpm=120, total=4)

    buttons = [
        
        [
            Button("0x0", 0, 0, button_press, button_release, pygame.K_1),
            Button("0x1", 0, 1, button_press, button_release, pygame.K_2),
            Button("0x2", 0, 2, button_press, button_release, pygame.K_3),
            Button("0x3", 0, 3, button_press, button_release, pygame.K_4),
            Button("0x4", 0, 4, button_press, button_release, pygame.K_5),
            Button("0x5", 0, 5, button_press, button_release, pygame.K_6)
        ],
        
        [
            Button("1x0", 1, 0, button_press, button_release, pygame.K_q),
            Button("1x1", 1, 1, button_press, button_release, pygame.K_w),
            Button("1x2", 1, 2, button_press, button_release, pygame.K_e),
            Button("1x3", 1, 3, button_press, button_release, pygame.K_r),
            Button("1x4", 1, 4, button_press, button_release, pygame.K_t),
            Button("1x5", 1, 5, button_press, button_release, pygame.K_y)
        ],
        
        [
            Button("2x0", 2, 0, button_press, button_release, pygame.K_a),
            Button("2x1", 2, 1, button_press, button_release, pygame.K_s),
            Button("2x2", 2, 2, button_press, button_release, pygame.K_d),
            Button("2x3", 2, 3, button_press, button_release, pygame.K_f),
            Button("2x4", 2, 4, button_press, button_release, pygame.K_g),
            Button("2x5", 2, 5, button_press, button_release, pygame.K_h)
        ],
        
        [
            Button("3x0", 3, 0, button_press, button_release, pygame.K_z),
            Button("3x1", 3, 1, button_press, button_release, pygame.K_x),
            Button("3x2", 3, 2, button_press, button_release, pygame.K_c),
            Button("3x3", 3, 3, button_press, button_release, pygame.K_v),
            Button("3x4", 3, 4, button_press, button_release, pygame.K_b),
            Button("3x5", 3, 5, button_press, button_release, pygame.K_n)
        ]
    ]
    
    # beats per minute
    bpm = 60

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            # end if
        # end for
        
        # picks up the button presses
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

        # counter loop
        counter.loop(True)

        clock.tick(fps)  # limits FPS to 60

    pygame.quit()