import math
import numpy as np

def mathematical_constants_part1():
    print("=== Mathematical Constants (Part 1) ===\n")
    
    # 1. Pi (π) - Ratio of a circle's circumference to its diameter
    print(f"1. Pi (π): {math.pi}")
    print(f"   Value using NumPy: {np.pi}")
    
    # Example: Area of a circle with radius r = 5
    r = 5
    circle_area = math.pi * (r ** 2)
    print(f"   Example: Area of circle (r={r}) = {circle_area:.4f}\n")
    
    # 2. Euler's Number (e) - Base of natural logarithm
    print(f"2. Euler's Constant (e): {math.e}")
    print(f"   Value using NumPy: {np.e}")
    
    # Example: Exponential calculation e^2
    exp_val = math.exp(2)
    print(f"   Example: e^2 = {exp_val:.4f}\n")
    
    # 3. Tau (τ) - Ratio of circle circumference to radius (2 * π)
    print(f"3. Tau (τ = 2π): {math.tau}")
    print(f"   Circumference of circle (r={r}): {math.tau * r:.4f}\n")
    
    # 4. Infinity (∞) and NaN (Not a Number)
    print(f"4. Positive Infinity: {math.inf}")
    print(f"5. NaN Value: {math.nan}")

if __name__ == "__main__":
    mathematical_constants_part1()
