# Parent Class
class Vehicle:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    # Parent method
    def transport_type(self):
        return "It is a general vehicle."

# Child Class 1: Bus
class Bus(Vehicle):
    # Method Overriding (Polymorphism)
    def transport_type(self):
        return f"{self.brand} {self.name} is a road transport."

# Child Class 2: Boat
class Boat(Vehicle):
    # Method Overriding (Polymorphism)
    def transport_type(self):
        return f"{self.brand} {self.name} is a water transport."


# Objects create kora holo
bus1 = Bus("Passenger Bus", "Tata")
boat1 = Boat("Speedboat", "Yamaha")

# Polymorphism in action: Same loop/function call but different output
for vehicle in (bus1, boat1):
    print(vehicle.transport_type())
