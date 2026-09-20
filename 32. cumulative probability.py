import numpy as np
import scipy.stats as stats

def calculate_cumulative_probability():
    print("=== Cumulative Probability Analysis (CDF) ===\n")
    
    # ---------------------------------------------------------
    # 1. Continuous Distribution: Normal Distribution
    # Scenario: Mean = 100, Standard Deviation = 15
    # Find P(X <= 115) - Probability of score being <= 115
    # ---------------------------------------------------------
    mean = 100
    std_dev = 15
    x_val = 115
    
    # Calculate CDF for Normal Distribution
    prob_normal = stats.norm.cdf(x_val, loc=mean, scale=std_dev)
    print("--- 1. Continuous (Normal Distribution) ---")
    print(f"Mean = {mean}, Std Dev = {std_dev}")
    print(f"P(X <= {x_val}) : {prob_normal:.4f} ({prob_normal * 100:.2f}%)")
    
    # Probability in an Interval: P(85 <= X <= 115) = CDF(115) - CDF(85)
    prob_interval = stats.norm.cdf(115, loc=mean, scale=std_dev) - stats.norm.cdf(85, loc=mean, scale=std_dev)
    print(f"P(85 <= X <= 115) : {prob_interval:.4f} ({prob_interval * 100:.2f}%)\n")

    # ---------------------------------------------------------
    # 2. Discrete Distribution: Binomial Distribution
    # Scenario: Tossing a fair coin 10 times (n=10, p=0.5)
    # Find P(X <= 4) - Getting 4 or fewer heads
    # ---------------------------------------------------------
    n_trials = 10
    prob_success = 0.5
    k_successes = 4
    
    # Calculate CDF for Binomial Distribution
    prob_binom = stats.binom.cdf(k_successes, n=n_trials, p=prob_success)
    print("--- 2. Discrete (Binomial Distribution) ---")
    print(f"Trials = {n_trials}, Probability of success = {prob_success}")
    print(f"P(X <= {k_successes}) : {prob_binom:.4f} ({prob_binom * 100:.2f}%)")

if __name__ == "__main__":
    calculate_cumulative_probability()
