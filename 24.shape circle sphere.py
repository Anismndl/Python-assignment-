import math

# Parent Class
class Shape:
    def __init__(self, radius):
        self.radius = radius

# Child Class 1: Circle (Inherits Shape)
class Circle(Shape):
    def cal_area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def display(self):
        print(f"Circle Radius: {self.radius}")
        print(f"Circle Area: {self.cal_area():.4f}")

# Child Class 2: Sphere (Inherits Circle)
class Sphere(Circle):
    def cal_surface_area(self):
        # Surface area of sphere = 4 * pi * r^2
        return 4 * math.pi * (self.radius ** 2)

    def cal_volume(self):
        # Volume of sphere = (4/3) * pi * r^3
        return (4 / 3) * math.pi * (self.radius ** 3)

    def display(self):
        print(f"Sphere Radius: {self.radius}")
        print(f"Sphere Surface Area: {self.cal_surface_area():.4f}")
        print(f"Sphere Volume: {self.cal_volume():.4f}")


# Driver Code
if __name__ == "__main__":
    print("--- Circle Object ---")
    c1 = Circle(5)
    c1.display()

    print("\n--- Sphere Object ---")
    s1 = Sphere(5)
    s1.display()
