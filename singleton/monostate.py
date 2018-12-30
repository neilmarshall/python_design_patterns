class Borg():
    __shared_state = {"1": "2"}
    def __init__(self):
        self.x  =1
        self.__dict__ = self.__shared_state
        pass


b = Borg()
b1 = Borg()
b.x = 4

print("Borg object 'b': ", b)  # b and b1 are distinct objects
print("Borg object 'b1': ", b1)
print("Object state 'b': ", b.__dict__)
print("Object state 'b1': ", b1.__dict__)