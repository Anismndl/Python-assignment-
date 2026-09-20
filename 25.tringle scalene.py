import math

# Parent Class
class Triangle:
    def __init__(self, side1, side2, side3, angle1=60, angle2=60, angle3=60):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

# Child Class 1: Equilateral Triangle
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        # All 3 sides are equal and all angles are 60 degrees
        super().__init__(side, side, side, 60, 60, 60)

    def calarea(self):
        # Area = (sqrt(3)/4) * side^2
        area = (math.sqrt(3) / 4) * (self.side1 ** 2)
        return area

    def sindarea(self):
        # Find tangent of all angles
        rad1 = math.radians(self.angle1)
        rad2 = math.radians(self.angle2)
        rad3 = math.radians(self.angle3)
        return math.tan(rad1), math.tan(rad2), math.tan(rad3)

# Child Class 2: Scalene Triangle (Child of Triangle)
class Scalene(Triangle):
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        super().__init__(side1, side2, side3, angle1, angle2, angle3)

    def calperimeter(self):
        # Perimeter = side1 + side2 + side3
        return self.side1 + self.side2 + self.side3

    def calarea(self):
        # Heron's Formula for Scalene Triangle Area
        s = self.calperimeter() / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area


# Driver Code
if __name__ == "__main__":
    print("--- Equilateral Triangle ---")
    eq = EquilateralTriangle(6)
    print(f"Area: {eq.calarea():.4f}")
    t1, t2, t3 = eq.sindarea()
    print(f"Tangents of angles: Tan({eq.angle1}°)= {t1:.4f}, Tan({eq.angle2}°)= {t2:.4f}, Tan({eq.angle3}°)= {t3:.4f}")

    print("\n--- Scalene Triangle ---")
    sc = Scalene(5, 6, 7, 44.42, 57.12, 78.46)
    print(f"Perimeter: {sc.calperimeter()}")
    print(f"Area: {sc.calarea():.4f}")
