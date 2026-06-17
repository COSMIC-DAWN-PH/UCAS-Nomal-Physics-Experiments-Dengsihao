
import numpy as np
from scipy.stats import linregress
import pandas as pd

# Define the datasets
datasets = [
    {
        "name": "Dataset 1 (AP 50cm)",
        "widths_cm": [1, 3, 5, 10],
        "measurements_ms": [
            [34.10, 34.67, 34.31, 34.35, 34.21],  # 1cm
            [102.20, 102.04, 102.40, 102.41, 102.42], # 3cm
            [168.20, 168.75, 169.18, 167.82, 167.08], # 5cm
            [323.60, 325.85, 324.41, 325.41, 324.82]  # 10cm
        ]
    },
    {
        "name": "Dataset 2 (AP 50cm, steeper)",
        "widths_cm": [1, 3, 5, 10],
        "measurements_ms": [
            [20.75, 20.71, 20.78, 20.85, 20.67],
            [61.96, 61.87, 61.69, 61.79, 61.76],
            [101.95, 101.98, 102.12, 102.15, 102.05],
            [199.32, 199.35, 199.42, 199.77, 199.44]
        ]
    },
    {
        "name": "Dataset 3 (AP 60cm)",
        "widths_cm": [1, 3, 5, 10],
        "measurements_ms": [
            [19.04, 18.99, 19.04, 18.94, 19.04],
            [56.66, 56.59, 56.76, 56.74, 56.87],
            [94.12, 93.99, 94.02, 94.11, 94.14],
            [183.44, 184.39, 184.08, 183.94, 183.74]
        ]
    }
]

print("Processing Datasets...\n")

for ds in datasets:
    print(f"--- {ds['name']} ---")
    
    widths_m = np.array(ds["widths_cm"]) / 100.0
    avg_times_ms = []
    avg_times_s = []
    velocities_ms = []
    
    print(f"{'Width (cm)':<12} {'Avg Time (ms)':<15} {'Velocity (m/s)':<15}")
    
    for i, measurements in enumerate(ds["measurements_ms"]):
        # 1. Calculate average time
        t_mean_ms = np.mean(measurements)
        t_mean_s = t_mean_ms / 1000.0
        
        avg_times_ms.append(t_mean_ms)
        avg_times_s.append(t_mean_s)
        
        # 2. Calculate average velocity v = delta_s / delta_t
        width_m = widths_m[i]
        v = width_m / t_mean_s
        velocities_ms.append(v)
        
        print(f"{ds['widths_cm'][i]:<12} {t_mean_ms:<15.3f} {v:<15.4f}")
    
    # 3. Linear Regression v = v0 + (a/2) * delta_t
    # y = v
    # x = delta_t (in seconds)
    # slope = a/2
    # intercept = v0
    
    slope, intercept, r_value, p_value, std_err = linregress(avg_times_s, velocities_ms)
    
    v0 = intercept
    a = slope * 2
    r_squared = r_value**2
    
    print("\nRegression Results:")
    print(f"Intercept (v0): {v0:.4f} m/s")
    print(f"Slope (a/2):    {slope:.4f}")
    print(f"Acceleration (a): {a:.4f} m/s^2")
    print(f"R-squared:      {r_squared:.6f}")
    print("\n" + "="*40 + "\n")
