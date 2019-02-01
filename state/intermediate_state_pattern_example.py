class ComputerState(object):
    name = "state"
    allowed_states = []

    def switch_state(self, new_state):
        if new_state.name in self.allowed_states:
            print(f"Current: {self} => switched to new state {new_state.name}")
            self.__class__ = new_state
        else:
            print(f"Current: {self} => switching to {new_state.name} not possible")

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed_states = ['on']


class On(ComputerState):
    name = "on"
    allowed_states = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = "suspend"
    allowed_states = ['on']


class Hibernate(ComputerState):
    name = "hibernate"
    allowed_states = ['on']


class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch_state(state)


if __name__ == '__main__':
    computer = Computer()

    # switch on
    computer.change(On)

    # switch off
    computer.change(Off)

    # switch on again
    computer.change(On)

    # suspend
    computer.change(Suspend)

    # attempt to hibernate -- this will fail
    computer.change(Hibernate)

    # switch back on
    computer.change(On)

    # finally off
    computer.change(Off)