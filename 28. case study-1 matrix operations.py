import numpy as np

def matrix_operations_case_study():
    print("=== Case Study 1: Matrix Operations using NumPy ===\n")
    
    # Define two 3x3 matrices A and B
    A = np.array([
        [2, 1, 3],
        [0, 5, 6],
        [1, 8, 9]
    ], dtype=float)

    B = np.array([
        [4, 2, 1],
        [1, 3, 0],
        [5, 1, 2]
    ], dtype=float)

    print("Matrix A (3x3):")
    print(A)
    print("\nMatrix B (3x3):")
    print(B)
    print("=" * 45)

    # 1. Find Inverse of Matrix A
    try:
        inv_A = np.linalg.inv(A)
        print("\n1. Inverse of Matrix A (A^-1):")
        print(np.round(inv_A, 4))
    except np.linalg.LinAlgError:
        print("\n1. Matrix A is singular and has no inverse.")

    # 2. Find Determinant of Matrix B
    det_B = np.linalg.det(B)
    print(f"\n2. Determinant of Matrix B (|B|): {det_B:.4f}")

    # 3. Print Result of (A . A) - Matrix Multiplication
    A_dot_A = np.dot(A, A)  # Alternative: A @ A
    print("\n3. Result of Matrix Multiplication (A . A):")
    print(A_dot_A)

if __name__ == "__main__":
    matrix_operations_case_study()
