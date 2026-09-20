import math

def perform_mathematical_computations():
    # 1. Basic Mathematical Constants
    print("--- Constants ---")
    print(f"Value of Pi (π): {math.pi}")
    print(f"Value of Euler's number (e): {math.e}")
    
    # 2. Trigonometric Calculations
    angle_degrees = 45
    angle_radians = math.radians(angle_degrees)
    print("\n--- Trigonometry ---")
    print(f"Sin({angle_degrees}°): {math.sin(angle_radians):.4f}")
    print(f"Cos({angle_degrees}°): {math.cos(angle_radians):.4f}")
    print(f"Tan({angle_degrees}°): {math.tan(angle_radians):.4f}")
    
    # 3. Logarithmic and Exponential Functions
    num = 100
    print("\n--- Logarithms & Power ---")
    print(f"Square root of {num}: {math.sqrt(num)}")
    print(f"Natural Log (ln) of {num}: {math.log(num):.4f}")
    print(f"Base-10 Log of {num}: {math.log10(num)}")
    print(f"2 to the power 5: {math.pow(2, 5)}")
    
    # 4. Factorial and GCD
    print("\n--- Factorial & GCD ---")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"GCD of 24 and 36: {math.gcd(24, 36)}")

# Function Call
if __name__ == "__main__":
    perform_mathematical_computations()
