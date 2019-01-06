from abc import ABC, abstractmethod

class Trip(ABC):

    @abstractmethod
    def set_transport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def return_home(self):
        pass

    def itinerary(self):
        self.set_transport()
        self.day1()
        self.day2()
        self.day3()
        self.return_home()


class VeniceTrip(Trip):

    def set_transport(self):
        print("Take a boat and find your way in the Grand Canal")

    def day1(self):
        print("Visit St Mark's Basilica in St Mark's square")

    def day2(self):
        print("Appreciate Doge's Palace")

    def day3(self):
        print("Enjoy the food near the Rialto Bridge")

    def return_home(self):
        print("Get souvenirs for friends and get back")


class MaldivesTrip(Trip):

    def set_transport(self):
        print("On foot, on any island, Wow!")

    def day1(self):
        print("Enjoy the marine life of Banana Reed")

    def day2(self):
        print("Go for the water sports and snorkelling")

    def day3(self):
        print("Relax on the beach and enjoy the sun")

    def return_home(self):
        print("Don't feel like leaving the beach :(")


class TravelAgency(object):

    @staticmethod
    def arrange_trip():
        choice = input("What kind of place would you like to go - historical or beach?\n\t>>> ")
        if choice.lower()[0] == 'h':
            trip = VeniceTrip()
        elif choice.lower()[0] == 'b':
            trip = MaldivesTrip()
        else:
            raise ValueError("Must specify one of 'historical' or 'beach'")
        trip.itinerary()


if __name__ == '__main__':
    try:
        TravelAgency.arrange_trip()
    except ValueError:
        import sys; sys.exit()