
import numpy as np
import matplotlib.pyplot as plt

# Data
# U0 (V), U2 (mV)
data = np.array([
    [2.11, 0.1],
    [2.60, 0.3],
    [3.09, 0.7],
    [3.62, 1.3],
    [4.11, 2.0],
    [4.59, 3.0],
    [5.09, 4.2],
    [5.60, 5.6],
    [5.78, 6.3],
    [6.16, 7.4],
    [6.35, 8.2],
    [6.48, 8.6]
])

U0 = data[:, 0]
U2 = data[:, 1]

# 1. Calculate relative intensity Pi/P0
# Formula: P_intensity = 0.5930 * U0 ** 2.7030
# P0 is the max intensity (corresponding to max U0)

Pi = 0.5930 * (U0 ** 2.7030)
P0 = np.max(Pi)
relative_intensity = Pi / P0

# 2. Calculate I_SC
# I_SC = U2 / 10 (mA)
I_SC = U2 / 10.0

# 3. Fit linear function I_SC = a * (Pi/P0) + b
coefficients = np.polyfit(relative_intensity, I_SC, 1)
polynomial = np.poly1d(coefficients)
fitted_line = polynomial(relative_intensity)

# Print results for table
print("Table Data:")
print("U0 (V) | U2 (mV) | Pi (arb) | Pi/P0 | I_SC (mA)")
for i, u0 in enumerate(U0):
    print(f"{u0:.2f} & {U2[i]:.1f} & {Pi[i]:.2f} & {relative_intensity[i]:.3f} & {I_SC[i]:.2f} \\\\")

# Print curve fitting results
print(f"\nLinear Fit Equation: I_SC = {coefficients[0]:.4f} * (Pi/P0) + {coefficients[1]:.4f}")

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(relative_intensity, I_SC, label='Data Points', color='blue', marker='o')
plt.plot(relative_intensity, fitted_line, label=f'Linear Fit: $I_{{SC}} = {coefficients[0]:.2f} (P_i/P_0) {coefficients[1]:+.2f}$', color='red', linestyle='--')
plt.xlabel('Relative Intensity $(P_i/P_0)$')
plt.ylabel('Short-Circuit Current $I_{SC}$ (mA)')
plt.title('Relationship between Short-Circuit Current and Relative Light Intensity')
plt.legend()
plt.grid(True)
plt.savefig('fig_experiment5_SC.png')
