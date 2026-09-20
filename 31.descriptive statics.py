import numpy as np
import pandas as pd
from scipy import stats

def calculate_descriptive_statistics():
    print("=== Descriptive Statistics Analysis ===\n")
    
    # Sample Dataset (e.g., Marks of 15 students)
    data = [65, 78, 85, 90, 85, 92, 70, 85, 88, 76, 95, 60, 85, 70, 82]
    
    print("Dataset:", data)
    print("-" * 50)
    
    # 1. Measures of Central Tendency
    mean_val = np.mean(data)
    median_val = np.median(data)
    mode_val = stats.mode(data, keepdims=True).mode[0]
    
    print("--- Measures of Central Tendency ---")
    print(f"1. Mean (Average)          : {mean_val:.2f}")
    print(f"2. Median (Middle Value)   : {median_val}")
    print(f"3. Mode (Most Frequent)    : {mode_val}\n")
    
    # 2. Measures of Dispersion / Variability
    range_val = np.ptp(data)  # Peak to peak (Max - Min)
    var_val = np.var(data, ddof=1)  # Sample Variance
    std_val = np.std(data, ddof=1)  # Sample Standard Deviation
    iqr_val = stats.iqr(data)       # Interquartile Range
    
    print("--- Measures of Dispersion ---")
    print(f"4. Range (Max - Min)       : {range_val}")
    print(f"5. Variance                : {var_val:.2f}")
    print(f"6. Standard Deviation      : {std_val:.2f}")
    print(f"7. Interquartile Range(IQR): {iqr_val:.2f}\n")
    
    # 3. Measures of Shape
    skewness = stats.skew(data)
    kurtosis = stats.kurtosis(data)
    
    print("--- Shape Measures ---")
    print(f"8. Skewness                : {skewness:.4f}")
    print(f"9. Kurtosis                : {kurtosis:.4f}\n")
    
    # 4. Summary using Pandas Series
    print("--- Pandas Comprehensive Summary ---")
    df = pd.Series(data)
    print(df.describe())

if __name__ == "__main__":
    calculate_descriptive_statistics()
  
