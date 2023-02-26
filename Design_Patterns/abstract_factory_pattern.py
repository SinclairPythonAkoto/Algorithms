"""Abstract Factory Pattern 

You are a company that does bodywork on cars before sendign them off to
their respected dealerships. This company has a number of different clients, 
all with different needs.

The Abstract Factory pattern can help the company manage & organise the different operations, 
to match the needs for all their clients.
"""
# import abc library to create abstract class
from abc import ABC, abstractmethod

class ModifyVehicle(ABC):
    @abstractmethod
    def modify_car(self):
        pass

    @abstractmethod
    def modify_van(self):
        pass


class LondonDealership(ModifyVehicle):
    def modify_car(self):
        return JaguarXE()
    
    def modify_van(self):
        return Townstart()
    
class ManchesterDealership(ModifyVehicle):
    def modify_car(self):
        return Polo()
    
    def modify_van(self):
        return Transit()
    

class WheelModifications(ABC):
    @abstractmethod
    def modify_wheels(self):
        pass


class JaguarXE(WheelModifications):
    def modify_wheels(self):
        return "Jaguar XE - chrome alloys"
    

class Townstart(WheelModifications):
    def modify_wheels(self):
        return "Nissan Townstart - bolt pattern 5x114.3"


class BodyworkModifications(ABC):
    @abstractmethod
    def modify_body(self):
        pass


class Polo(BodyworkModifications):
    def modify_body(self):
        return "Volkswagen - Polo metalic blue"


class Transit(BodyworkModifications):
    def modify_body(self):
        return "Ford Transit - lime green"


london_shop: LondonDealership = LondonDealership()
modify_jaguar = london_shop.modify_car()
modify_nissan = london_shop.modify_van()
print("London Dealership Changes")
print(modify_jaguar.modify_wheels())
print(modify_nissan.modify_wheels()+"\n")

manchester_shop: ManchesterDealership = ManchesterDealership()
modify_vw = manchester_shop.modify_car()
modify_ford = manchester_shop.modify_van()
print("Manchester Dealership Changes")
print(modify_vw.modify_body())
print(modify_ford.modify_body())


# Output
# London Dealership Changes
# Jaguar XE - chrome alloys
# Nissan Townstart - bolt pattern 5x114.3

# Manchester Dealership Changes
# Volkswagen - Polo metalic blue
# Ford Transit - lime green

# Notice the Dealership class is being called where
# the car class functions are being used.
# We create an object from the Dealership class, which gives
# us to access all the car class functions.