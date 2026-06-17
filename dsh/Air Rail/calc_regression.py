import numpy as np
from scipy import stats

# Data
m_g = np.array([224.19, 238.95, 251.35, 267.64, 283.98])
T_ms = np.array([1604.62, 1655.78, 1697.53, 1738.54, 1777.74])

# Conversions
m_kg = m_g / 1000.0
T_s = T_ms / 1000.0

# Calculate T^2
T2_s2 = T_s ** 2

# Linear Regression: y = Ax + B
# x = m_kg
# y = T2_s2
slope, intercept, r_value, p_value, std_err = stats.linregress(m_kg, T2_s2)

A = slope
B = intercept
r = r_value

# Calculate k and m0
# Slope A = 4 * PI^2 / k  => k = 4 * PI^2 / A
# Intercept B = A * m0    => m0 = B / A
if A != 0:
    k = (4 * np.pi**2) / A
    m0 = B / A
else:
    k = float('inf')
    m0 = float('nan')

# Output results
print("Processed Data:")
for i in range(len(m_g)):
    print(f"Point {i+1}: m = {m_kg[i]:.5f} kg, T = {T_s[i]:.5f} s, T^2 = {T2_s2[i]:.6f} s^2")

print("\nRegression Results:")
print(f"Slope (A): {A}")
print(f"Intercept (B): {B}")
print(f"Correlation coefficient (r): {r}")
print(f"Equation: T^2 = {A:.4f} * m + {B:.4f}")

print("\nPhysical Constants:")
print(f"k = {k}")
print(f"m0 = {m0}")
