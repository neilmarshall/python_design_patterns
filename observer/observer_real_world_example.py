from abc import ABC, abstractmethod

class NewsPublisher(object):
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    @property
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return "Got news: " + self.__latest_news


class Subscriber(ABC):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, '-->', self.publisher.get_news())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, '-->', self.publisher.get_news())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    subscribers = [SMSSubscriber(news_publisher), EmailSubscriber(news_publisher)]
    print("Subscribers:", news_publisher.subscribers)
    news_publisher.add_news("Ground-breaking news!!!")
    news_publisher.notify_subscribers()
    print("Detached:", type(news_publisher.detach()).__name__)
    print("Subscribers:", news_publisher.subscribers)
    news_publisher.add_news("More news!!!")
    news_publisher.notify_subscribers()