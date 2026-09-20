import numpy as np
from scipy.stats import chi2_contingency

def perform_chi_square_test():
    print("=== Chi-Square (χ²) Test of Independence ===\n")
    
    # 2x2 Contingency Table (Observed Frequencies)
    # Example: Gender vs Preferred Mode of Education (Online vs Offline)
    observed_data = np.array([
        [30, 10],  # Male:   30 Online, 10 Offline
        [15, 25]   # Female: 15 Online, 25 Offline
    ])
    
    print("Observed Contingency Table:")
    print("         Online  Offline")
    print(f"Male   :  {observed_data[0][0]}       {observed_data[0][1]}")
    print(f"Female :  {observed_data[1][0]}       {observed_data[1][1]}")
    print("-" * 50)
    
    # Perform Chi-Square Test of Independence
    chi2_stat, p_val, dof, expected_data = chi2_contingency(observed_data)
    
    # Display Statistical Results
    print(f"1. Chi-Square Statistic (χ²) : {chi2_stat:.4f}")
    print(f"2. p-value                   : {p_val:.4f}")
    print(f"3. Degrees of Freedom (dof)  : {dof}")
    print("\n4. Expected Frequencies Table:")
    print(np.round(expected_data, 2))
    
    # Hypothesis Decision (Alpha = 0.05)
    alpha = 0.05
    print("\n--- Hypothesis Test Result ---")
    if p_val < alpha:
        print(f"Since p-value ({p_val:.4f}) < {alpha}, we REJECT the Null Hypothesis.")
        print("Conclusion: There IS a significant association between Gender and Preference.")
    else:
        print(f"Since p-value ({p_val:.4f}) >= {alpha}, we FAIL to reject the Null Hypothesis.")
        print("Conclusion: Gender and Preference are INDEPENDENT of each other.")

if __name__ == "__main__":
    perform_chi_square_test()
