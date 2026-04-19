from abc import ABC, abstractmethod

# Transport vositalari uchun umumiy klass
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

# Obyekt yaratish uchun factory klassi
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Bunday transport vositasi yo'q")

# Avtomobil klassi
class Car(Vehicle):
    def drive(self):
        return "Avtomobil harakat qilmoqda"

# Velosiped klassi
class Bike(Vehicle):
    def drive(self):
        return "Velosiped harakat qilmoqda"

# Kamyon klassi
class Truck(Vehicle):
    def drive(self):
        return "Kamyon harakat qilmoqda"

# Factory klassidan obyekt yaratish
factory = VehicleFactory()

# Obyekt yaratish
car = factory.create_vehicle("car")
bike = factory.create_vehicle("bike")
truck = factory.create_vehicle("truck")

# Obyekt ishlatish
print(car.drive())  # Avtomobil harakat qilmoqda
print(bike.drive())  # Velosiped harakat qilmoqda
print(truck.drive())  # Kamyon harakat qilmoqda
