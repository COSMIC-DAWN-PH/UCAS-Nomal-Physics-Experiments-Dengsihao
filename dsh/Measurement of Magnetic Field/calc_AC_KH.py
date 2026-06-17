import numpy as np
from scipy import stats

# Data
B = np.array([37.3, 55.5, 74.1, 92.9, 111.2, 130.6, 148.4])
VH_AC = np.array([6.371, 12.488, 18.909, 25.435, 31.755, 38.547, 44.637])
IS_AC = 1.0 # mA

# Linear Regression for VH vs B
slope, intercept, r_value, p_value, std_err = stats.linregress(B, VH_AC)

# Calculate KH
# Slope k = KH * IS
# KH = k / IS
# Units: k is mV/mT, IS is mA
# KH = (mV/mT) / mA = mV/(mA*mT)
# Convert to mV/(mA*T) by multiplying by 1000
KH_measured = (slope / IS_AC) * 1000

KH_theoretical = 316 # mV/(mA*T)

# Error Analysis
error = abs(KH_measured - KH_theoretical) / KH_theoretical * 100

print(f"Slope (k): {slope:.6f} mV/mT")
print(f"Intercept: {intercept:.6f} mV")
print(f"R-squared: {r_value**2:.6f}")
print(f"KH_measured: {KH_measured:.2f} mV/(mA*T)")
print(f"KH_theoretical: {KH_theoretical} mV/(mA*T)")
print(f"Relative Error: {error:.2f}%")
