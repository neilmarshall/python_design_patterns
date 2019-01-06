from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def notify(self):
        pass


class Subject(object):
    def __init__(self):
        self.__observers = []

    def __repr__(self):
        return type(self).__name__ + '(' + str(id(self)) + ')'

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Subscriber1(Subscriber):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'from', subject)


class Subscriber2(Subscriber):
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'from', subject)


if __name__ == '__main__':
    subject = Subject()
    subscriber1 = Subscriber1(subject)
    subscriber2 = Subscriber2(subject)
    subject.notify_all('notification')