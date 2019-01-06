"""Example taken from Wikipedia (https://en.wikipedia.org/wiki/Proxy_pattern)"""

from abc import ABC, abstractmethod

class AbstractCar(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(AbstractCar):
    def drive(self):
        print("Car has been driven!")


class Driver(object):
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver):
        self.driver = driver
        self.car = Car()

    def drive(self):
        if self.driver.age >= 17:
            self.car.drive()
        else:
            print("Too young to drive!")


if __name__ == '__main__':
    driver1 = Driver(16)
    car1 = ProxyCar(driver1)
    car1.drive()

    driver2 = Driver(25)
    car2 = ProxyCar(driver2)
    car2.drive()