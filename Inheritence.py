


class Honda:
    def bike(self):
        print("We will make bike")

    def racebikes(self):
        print("We will maake racing bikes")


class Car():
    def car(self):
        print("We will Cars")



class MediumCars(Car,Honda):

    def city(self):
        print("We will make Honda city")



a=MediumCars()

a.bike()


b=Honda()

b.racebikes()