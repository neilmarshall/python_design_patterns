from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def doThis(self):
        pass


class StartState(State):
    def doThis(self):
        print("TV Switching ON...")


class StopState(State):
    def doThis(self):
        print("TV Switching OFF...")


class TVContext(State):

    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def doThis(self):
        self.state.doThis()


if __name__ == '__main__':
    context = TVContext()
    start = StartState()
    stop  = StopState()
    context.set_state(start)
    context.doThis()
    context.set_state(stop)
    context.doThis()
