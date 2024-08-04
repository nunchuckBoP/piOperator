import time
class BeatCounter(object):
    
    def __init__(self, fps, bpm=120, total=8):
        self.bpm = bpm
        self.fps = fps
        self.total = total
        self.count = 0
        self.sub_count = 0
        self.__loop_count__ = 0
        self.__fps__ = fps # frames per second or loops per second
        self.__lasttime__ = 0
        self.subbeat = 0
        
    def get_bpm(self):
        return self.bpm
    
    def set_bpm(self, value):
        if self.bpm != value:
            self.bpm = value
        # end if

    def on_subbeat_changed(self):
        print("SUB BEAT: %s" % self.subbeat)

    def loop(self, playing=False):
        
        # calculate the sub-beats per minute
        # beats per minute times sub beats per beat
        # 1-e-and-a
        # 120 * 4 = 480
        sbpm = self.bpm * 4

        # calculate the loops per sub beat
        # 1 min           60 sec      60 loops
        # ------       x  -----   x  ----------
        # 480 sbeats      1 min        1 sec
        lpsb = (1/sbpm) * 60 * self.fps

        # total is
        _t = self.total * 4 

        if playing:
            
            if self.sub_count >= _t:
                self.sub_count = 0
            if self.__loop_count__ >= lpsb:
                self.sub_count += 1
                
                # perform all operations on the beat
                self.subbeat = self.sub_count
                self.on_subbeat_changed()

                self.__loop_count__ = 0
            # end if

            self.__loop_count__ += 1
        # end if
    # end loop