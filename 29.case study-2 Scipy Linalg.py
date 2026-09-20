import numpy as np
from scipy import linalg

def scipy_linalg_case_study():
    print("=== Case Study 2: SciPy Linear Algebra (scipy.linalg) ===\n")
    
    # -------------------------------------------------------------
    # Question 1: Solve System of Linear Equations
    # 2x + 3y = 8
    # 4x + 8y = 14
    # -------------------------------------------------------------
    print("--- 1. Linear Equations Solver ---")
    A_eq = np.array([[2, 3], [4, 8]])
    B_eq = np.array([8, 14])
    
    # Using scipy.linalg.solve
    solution = linalg.solve(A_eq, B_eq)
    print(f"Equations: 2x + 3y = 8, 4x + 8y = 14")
    print(f"Solution: x = {solution[0]:.4f}, y = {solution[1]:.4f}\n")

    # -------------------------------------------------------------
    # Question 2: Two-Car Velocity Problem
    # Same direction: (v1 - v2) * 6 = Distance
    # Opposite direction: (v1 + v2) * 1 = Distance
    # Let Distance between P and Q = 120 km (assumed)
    # -------------------------------------------------------------
    print("--- 2. Two-Car Velocity Solver ---")
    D = 120  # Distance in km
    # Eq 1: 6*v1 - 6*v2 = D  => 6*v1 - 6*v2 = 120
    # Eq 2: 1*v1 + 1*v2 = D  => 1*v1 + 1*v2 = 120
    A_cars = np.array([[6, -6], [1, 1]])
    B_cars = np.array([D, D])
    
    velocities = linalg.solve(A_cars, B_cars)
    print(f"Assumed Distance between P and Q = {D} km")
    print(f"Velocity of Car 1 (v1): {velocities[0]:.2f} km/h")
    print(f"Velocity of Car 2 (v2): {velocities[1]:.2f} km/h\n")

    # -------------------------------------------------------------
    # Question 3: 4x4 Matrix Operations & LU Decomposition
    # -------------------------------------------------------------
    print("--- 3. 4x4 Matrix Operations & LU Decomposition ---")
    M = np.array([
        [4, 1, 2, 3],
        [3, 6, 1, 2],
        [2, 2, 8, 1],
        [1, 5, 2, 9]
    ], dtype=float)
    
    print("Original 4x4 Matrix M:")
    print(M)
    
    # Transpose
    print("\ni) Transpose of Matrix:")
    print(M.T)
    
    # Matrix Rank using NumPy/SciPy
    rank = np.linalg.matrix_rank(M)
    print(f"\nii) Rank of Matrix: {rank}")
    
    # Eigenvalues and Eigenvectors
    eigenvalues, eigenvectors = linalg.eig(M)
    print("\niii) Eigenvalues:")
    print(np.round(eigenvalues.real, 4))
    print("\nEigenvectors:")
    print(np.round(eigenvectors.real, 4))
    
    # PLU Decomposition
    P, L, U = linalg.lu(M)
    print("\niv) PLU Decomposition:")
    print("Permutation Matrix P:")
    print(P)
    print("\nLower Triangular Matrix L:")
    print(np.round(L, 4))
    print("\nUpper Triangular Matrix U:")
    print(np.round(U, 4))

if __name__ == "__main__":
    scipy_linalg_case_study()
