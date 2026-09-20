import numpy as np
import scipy.stats as stats

def standard_normal_interval_analysis():
    print("=== Standard Normal Distribution & Confidence Intervals ===\n")
    
    # Standard Normal Distribution parameters: Mean = 0, Std Dev = 1
    mu = 0
    sigma = 1
    
    # 1. empirical Rule Probabilities (68-95-99.7 Rule)
    # P(-1 <= Z <= 1)
    p_1std = stats.norm.cdf(1, mu, sigma) - stats.norm.cdf(-1, mu, sigma)
    # P(-2 <= Z <= 2)
    p_2std = stats.norm.cdf(2, mu, sigma) - stats.norm.cdf(-2, mu, sigma)
    # P(-3 <= Z <= 3)
    p_3std = stats.norm.cdf(3, mu, sigma) - stats.norm.cdf(-3, mu, sigma)
    
    print("--- 1. Empirical Rule (Standard Normal Area) ---")
    print(f"P(-1 <= Z <= 1) [Within 1 Std Dev] : {p_1std:.4f} ({p_1std * 100:.2f}%)")
    print(f"P(-2 <= Z <= 2) [Within 2 Std Dev] : {p_2std:.4f} ({p_2std * 100:.2f}%)")
    print(f"P(-3 <= Z <= 3) [Within 3 Std Dev] : {p_3std:.4f} ({p_3std * 100:.2f}%)\n")
    
    # 2. Confidence Intervals (Z-critical boundaries)
    # 90%, 95%, and 99% Confidence Intervals
    conf_levels = [0.90, 0.95, 0.99]
    
    print("--- 2. Critical Intervals for Standard Normal Distribution ---")
    for conf in conf_levels:
        # Calculate interval boundaries
        lower_z, upper_z = stats.norm.interval(conf, loc=mu, scale=sigma)
        print(f"{int(conf * 100)}% Confidence Interval : Z in [{lower_z:.4f}, {upper_z:.4f}]")

if __name__ == "__main__":
    standard_normal_interval_analysis()
