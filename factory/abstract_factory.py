from abc import ABC, abstractmethod

class PizzaFactory(ABC):
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxeVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VegPizza(ABC):
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(ABC):
    @abstractmethod
    def serve(self):
        pass


class DeluxeVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self):
        print(type(self).__name__, "is served with Chicken on", DeluxeVeggiePizza.__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self):
        print(type(self).__name__, "is served with Ham on", MexicanVegPizza.__name__)


class PizzaStore():
    @staticmethod
    def make_pizza():
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            veg_pizza = factory.create_veg_pizza()
            veg_pizza.prepare()
            non_veg_pizza = factory.create_non_veg_pizza()
            non_veg_pizza.serve()


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.make_pizza()