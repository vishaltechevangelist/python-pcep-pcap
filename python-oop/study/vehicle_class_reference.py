from machines.vehicle_class import Vehicle, Truck, MotorCycle

car = Vehicle('HatchBack', 'Maruti')
print(car.vehicle_make)

truck1 = Truck("Big Rig", "Mercedes")
truck2 = Truck("Small Rig", "Chevy")
truck3 = Truck("Big Rig", "Toyota")

print(truck3.get_vehicle_count())
truck3.drive()

moto = MotorCycle("Racing", "KTM Duke")

for v in [car, truck1, moto]:
    v.drive()


