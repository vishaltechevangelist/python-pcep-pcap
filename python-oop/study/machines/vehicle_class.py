class Vehicle:

    # class variable should not be changed outside the class
    color = 'Red'
    vehicle_counter = 0

    def __init__(self, body_type, make):
        # instance variable associated with instance
        self.vehicle_body = body_type
        self.vehicle_make = make
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):
        return Vehicle.vehicle_counter

    def display_make(self):
        return self.vehicle_make

    def drive(self):
        print("Vehicle driving...")

# Truck class inheriting from Vehicle class
class Truck(Vehicle):
    # Overriding the method defined in parent/base
    def drive(self):
        print("{} driving".format(self.vehicle_make))

# Motorcycle is the child class of parent vehicle class
class MotorCycle(Vehicle):
    # Overriding the method defined in parent/base
    def drive(self):
        print("{} driving very fast".format(self.vehicle_make))