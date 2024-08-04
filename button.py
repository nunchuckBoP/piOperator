
STATE_PRESSED = 1
STATE_RELEASED = 0

MODE_SOUND = 0
MODE_FX = 1

import pygame

class Button(object):
    """
    Button Class
    Description: A device class for buttons that include an override value. That way a button can be pressed
    from a keyboard, or a GPIO input, or button matrix, or whatever.
    """
    def __init__(self, name, row, column, on_press_callback, on_release_callback, keyboard_key=None):
        self.name = name
        self.on_press = on_press_callback
        self.on_release = on_release_callback
        self.state = STATE_RELEASED
        self.key = keyboard_key
        self.__keystate__ = False # latching keystate for keyboard button
        self.sound = None
        self.fx = None
        self.row = row
        self.column = column
        self.mode = MODE_SOUND

    def __on_press__(self):
        #print("%s key pressed" % self.name)
        if self.on_press is not None:
            self.on_press(name=self.name, row=self.row, column=self.column)
        
    def __on_release__(self):
        #print("%s key released" % self.name)
        if self.on_release is not None:
            self.on_release(name=self.name, row=self.row, column=self.column)
    
    def setMdoe(self, value):
        if self.mode != value:
            self.mode = value
        # end if
    # end setMode

    def getMode(self):
        return self.mode
    # end getMode

    def setState(self, value):
        if self.state != value:
            self.state = value
            if self.state == STATE_PRESSED:
                self.__on_press__()
            else:
                self.__on_release__()
            # end if
        # end if
    # end setstate
    
    def loop(self, events, override_value):
        for event in events:                
            if event.type == pygame.KEYDOWN:
                if event.key == self.key:
                    self.__keystate__ = True
                # end if
            elif event.type == pygame.KEYUP:
                if event.key == self.key:
                    self.__keystate__ = False
                # end if    
            # end if        
        # end if
        
        if self.__keystate__ == True or override_value == True:
            self.setState(STATE_PRESSED)
        elif self.__keystate__ == False and override_value == False:
            self.setState(STATE_RELEASED)
        # end if
    # end blip 
    
    def get_sound(self):
        return self.sound
    # end get_sound
    
    def get_fx(self):
        return self.fx
    # end get_fx
    
    def set_sound(self, file_path):
        # this method assigns a sound to the button
        self.sound = file_path
    # end set_sound
        
    def set_fx(self, fx_name):
        # this assigns 
        self.fx_name = fx_name
    # set_fx
        
# end class