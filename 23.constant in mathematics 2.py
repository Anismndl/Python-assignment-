import scipy.constants as const
import math

def mathematical_constants_part2():
    print("=== Mathematical & Scientific Constants (Part 2) ===\n")
    
    # 1. Golden Ratio (Phi - φ)
    golden_ratio = (1 + math.sqrt(5)) / 2
    print(f"1. Golden Ratio (φ): {golden_ratio:.6f}")
    
    # 2. Euler-Mascheroni Constant (gamma - γ) using SciPy
    # γ is the limiting difference between the harmonic series and natural logarithm
    print(f"2. Euler-Mascheroni Constant (γ): {const.euler:.6f}\n")
    
    # 3. SciPy Physical & Mathematical Constants
    print("--- Constants from scipy.constants ---")
    print(f"Speed of Light in vacuum (c): {const.c} m/s")
    print(f"Planck Constant (h): {const.h} J·s")
    print(f"Gravitational Constant (G): {const.G} m^3 kg^-1 s^-2")
    print(f"Elementary Charge (e): {const.e} C")
    print(f"Avogadro Constant (N_A): {const.N_A} mol^-1\n")
    
    # 4. Angle Conversions
    print("--- Angle Conversions ---")
    deg = 180
    print(f"{deg} degrees in radians: {const.degree * deg:.4f} rad")

if __name__ == "__main__":
    mathematical_constants_part2()
