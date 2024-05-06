class Vehicle:
    def __init__(self, name, license_plate, color, fuel_type):
        self.name = name
        self.license_plate = license_plate
        self.color = color
        self.fuel_type = fuel_type

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_license_plate(self, license_plate):
        self.license_plate = license_plate

    def get_license_plate(self):
        return self.license_plate

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type

    def get_fuel_type(self):
        return self.fuel_type


class Car(Vehicle):
    def __init__(self, name, license_plate, color, fuel_type, num_doors):
        super().__init__(name, license_plate, color, fuel_type)
        self.num_doors = num_doors

    def set_num_doors(self, num_doors):
        self.num_doors = num_doors

    def get_num_doors(self):
        return self.num_doors


class Motorcycle(Vehicle):
    def __init__(self, name, license_plate, color, fuel_type, num_wheels):
        super().__init__(name, license_plate, color, fuel_type)
        self.num_wheels = num_wheels

    def set_num_wheels(self, num_wheels):
        self.num_wheels = num_wheels

    def get_num_wheels(self):
        return self.num_wheels


# Usage example:
car = Car("Honda Accord", "Emran123", "Blue", "Gasoline", 4)
print("Car Name:", car.get_name())
print("Car License Plate:", car.get_license_plate())
print("Car Color:", car.get_color())
print("Car Fuel Type:", car.get_fuel_type())
print("Number of Doors:", car.get_num_doors())

motorcycle = Motorcycle("Honda", "XYZ456", "Black", "Gasoline", 2)
print("\nMotorcycle Name:", motorcycle.get_name())
print("Motorcycle License Plate:", motorcycle.get_license_plate())
print("Motorcycle Color:", motorcycle.get_color())
print("Motorcycle Fuel Type:", motorcycle.get_fuel_type())
print("Number of Wheels:", motorcycle.get_num_wheels())
