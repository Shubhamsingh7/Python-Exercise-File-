

class Car:
    wheel=4
    seat=4

    @classmethod
    def type(cls):
        print("This is Sedan Car making company")


class Suzuki(Car):

    brand="Suzuki"

    def __init__(self,name,colour,milege,price):
        self.name=name
        self.colour=colour
        self.milage=milege
        self.price=price


    def specifications(self):
        print("Specifications Are:")
        print(f"Brand={Suzuki.brand}")
        print(f"Name={self.name}")
        print(f"Price={self.price}")
        print(f"Milage={self.milage}")
        print(f"Colour={self.colour}")
        print(f"Wheel={Car.wheel}")
        print(f"Seat={Car.seat}")

    @staticmethod
    def BrandInfo():
        print("Suzuki Is Japanese Motar Car Company")





car1=Suzuki("Ciaz","Silver",15,950000)
Car.type()


car1.specifications()
car1.BrandInfo()
print()
car2=Suzuki("Accent","White",12,"650000")

car2.specifications()