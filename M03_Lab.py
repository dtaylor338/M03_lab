class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType= vehicleType

vt=Vehicle(input("What type of vehicle is it? "))

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, sunroof):
        self.year=year
        self.make=make
        self.model=model
        self.doors=doors
        self.sunroof=sunroof

v1=Automobile(input("What year is it? "), input("Make? "), input("Model? "), input("Number of doors? "), input("Sunroof or Solidroof? "))


print("Vehicle Type:", vt.vehicleType)
print("Model Year:", v1.year)
print("Vehicle Make:", v1.make)
print("Vehicle Model:", v1.model)
print("Number of Doors:",v1.doors)
print("Sunroof or Solid:", v1.sunroof)