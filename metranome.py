import time
class BeatCounter(object):
    
    def __init__(self, fps, bpm=120, ticks=16):
        self.bpm = bpm
        self.beat_active = 1
        self.ticks = ticks
        self.loop_total = 0
        self.__fps__ = fps
        self.__last_time__ = 0
        
    def get_bpm(self):
        return self.bpm
    
    def set_bpm(self, value):
        if self.bpm != value:
            self.bpm = value
    
    def __reset__(self):
        self.beat_active = 1
        self.loop_total = 0
    
    def loop(self, playing=False):
        
        if playing:
            
            self.loop_total += 1
            print(self.loop_total)
        
        else:
            
            pass