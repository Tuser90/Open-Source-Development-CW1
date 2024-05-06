import unittest
from vehicle import Vehicle  # Import the Vehicle class from Vehicle.py


class TestVehicle(unittest.TestCase):

    def setUp(self):
        # Initialize a sample Vehicle instance for testing
        self.vehicle = Vehicle("Car", "ABC123", "Red", "Gasoline")

    def test_set_name(self):
        self.vehicle.set_name("Truck")
        self.assertEqual(self.vehicle.get_name(), "Truck")

    def test_set_license_plate(self):
        self.vehicle.set_license_plate("XYZ456")
        self.assertEqual(self.vehicle.get_license_plate(), "XYZ456")

    def test_set_color(self):
        self.vehicle.set_color("Blue")
        self.assertEqual(self.vehicle.get_color(), "Blue")

    def test_set_fuel_type(self):
        self.vehicle.set_fuel_type("Diesel")
        self.assertEqual(self.vehicle.get_fuel_type(), "Diesel")


if __name__ == '__main__':
    unittest.main()
