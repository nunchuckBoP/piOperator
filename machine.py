from statemachine import StateMachine, State

# Finite State Machine

# machine states
SETUP = 0
IDLE = 1
PLAYING = 2
PLAYING_RECORD = 3

class gListener(object):
    
    def __init__(self, name):
        self.name = name
    
    def before_transition(self, event, source, target):
        print("STATE: Leaving state %s" % source.id)
    
    def after_transition(self, event, source, target):
        #print("Machine transitioned from: %s \tto %s \t after event %s" % (source.id, target.id, event))
        pass
    
    def on_enter_state(self, target, event):
        print("STATE: Entered state %s" % target.id)
    
# end gListener

class GameEngine(StateMachine):
    "An awesome beat-box machine"
    
    # Sets of the possible states of the system
    stopped = State(initial=True)
    setup = State()
    playing = State()
    playing_record = State() # playing and recording button presses
    playing_sampling = State() # playing and sampling mic
    sampling = State() # stopped and sampling sound with mic
    
    # sets of the events of the state
    play_pb = (
        stopped.to(playing)
    )
    record_pb = (
        setup.to(stopped) | 
        playing.to(playing_record) | 
        stopped.to(playing_record)
    )
    record_release = (
        playing_record.to(playing)
    )
    stop_pb = (
        playing.to(stopped) |
        playing_record.to(stopped)
    )
    setup_pb = (
        stopped.to(setup)
    )
    sample_pb = (
        stopped.to(sampling)
    )
    sample_pb = (
        playing.to(playing_sampling)
    )
    
    def isPlaying(self):
        if self.current_state == playing | self.current_state == playing_record | \
            self.current_state == playing_sampling:
                return True
        else:
            return False
    
# end of system class
    