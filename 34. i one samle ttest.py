import numpy as np
from scipy import stats

def perform_one_sample_ttest():
    print("=== One-Sample t-Test ===\n")
    
    # Sample Dataset: Marks of 10 students in a test
    sample_marks = np.array([75, 82, 68, 90, 85, 78, 88, 70, 92, 80])
    
    # Hypothesized Population Mean (e.g., Target passing benchmark = 75)
    pop_mean = 75
    
    print(f"Sample Marks: {sample_marks}")
    print(f"Sample Mean : {np.mean(sample_marks):.2f}")
    print(f"Target Population Mean (μ): {pop_mean}")
    print("-" * 50)
    
    # Perform One-Sample t-Test
    t_stat, p_val = stats.ttest_1samp(sample_marks, pop_mean)
    
    # Display Results
    print(f"1. t-statistic : {t_stat:.4f}")
    print(f"2. p-value     : {p_val:.4f}")
    
    # Hypothesis Decision (Alpha = 0.05)
    alpha = 0.05
    print("\n--- Hypothesis Test Result ---")
    if p_val < alpha:
        print(f"Since p-value ({p_val:.4f}) < {alpha}, we REJECT the Null Hypothesis.")
        print("Conclusion: The sample mean is significantly DIFFERENT from the population mean.")
    else:
        print(f"Since p-value ({p_val:.4f}) >= {alpha}, we FAIL to reject the Null Hypothesis.")
        print("Conclusion: There is NO significant difference between the sample mean and the population mean.")

if __name__ == "__main__":
    perform_one_sample_ttest()
