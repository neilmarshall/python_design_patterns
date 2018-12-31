from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


# forest factory definition
class ForestFactory(object):
    @staticmethod
    def make_sound(object_type):
        return eval(object_type)().do_say()


# client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make sound - Dog or Cat?")
    ff.make_sound(animal)