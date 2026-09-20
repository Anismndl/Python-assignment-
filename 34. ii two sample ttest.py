import numpy as np
from scipy import stats

def perform_two_sample_ttest():
    print("=== Two-Sample Independent t-Test ===\n")
    
    # Sample Datasets: Marks of two independent groups of students (Section A & Section B)
    group_A = np.array([78, 85, 90, 72, 88, 92, 80, 84])
    group_B = np.array([65, 70, 75, 68, 82, 72, 78, 69])
    
    mean_A = np.mean(group_A)
    mean_B = np.mean(group_B)
    
    print(f"Group A Marks : {group_A}")
    print(f"Group A Mean  : {mean_A:.2f}")
    print(f"Group B Marks : {group_B}")
    print(f"Group B Mean  : {mean_B:.2f}")
    print("-" * 50)
    
    # Perform Two-Sample Independent t-Test
    t_stat, p_val = stats.ttest_ind(group_A, group_B)
    
    # Display Results
    print(f"1. t-statistic : {t_stat:.4f}")
    print(f"2. p-value     : {p_val:.4f}")
    
    # Hypothesis Decision (Alpha = 0.05)
    alpha = 0.05
    print("\n--- Hypothesis Test Result ---")
    if p_val < alpha:
        print(f"Since p-value ({p_val:.4f}) < {alpha}, we REJECT the Null Hypothesis.")
        print("Conclusion: There IS a statistically significant difference between Group A and Group B means.")
    else:
        print(f"Since p-value ({p_val:.4f}) >= {alpha}, we FAIL to reject the Null Hypothesis.")
        print("Conclusion: There is NO significant difference between Group A and Group B means.")

if __name__ == "__main__":
    perform_two_sample_ttest()
