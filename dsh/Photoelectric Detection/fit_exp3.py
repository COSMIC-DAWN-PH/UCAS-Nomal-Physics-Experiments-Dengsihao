import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib

# Set backend to avoid display issues
matplotlib.use('Agg')

# Data
U0 = np.array([
    1.22, 1.34, 1.43, 1.56, 1.66, 1.76, 1.86, 1.96, 2.06, 2.15,
    2.26, 2.36, 2.46, 2.55, 2.64, 2.75, 2.86, 2.96, 3.07, 3.15,
    3.26, 3.37, 3.47, 3.60, 3.68, 3.79, 3.89, 3.98, 4.08, 4.18,
    4.28, 4.40, 4.48, 4.59, 4.69, 4.79, 4.89, 4.99, 5.07, 5.17,
    5.31, 5.37, 5.46, 5.58, 5.69, 5.79, 5.89, 5.99, 6.07, 6.19,
    6.25, 6.42, 6.53
])

P = np.array([
    0.1, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.1, 1.4, 1.7,
    2.2, 2.8, 3.3, 3.8, 4.6, 5.5, 6.4, 7.5, 8.8, 9.6,
    11.1, 12.8, 14.4, 16.5, 17.7, 20.1, 22.4, 24.2, 26.3, 28.2,
    31.2, 34.2, 36.2, 39.1, 41.8, 44.6, 47.3, 49.8, 52.0, 54.5,
    58.3, 59.3, 62.0, 64.6, 67.5, 69.9, 73.2, 74.7, 76.4, 79.2,
    80.6, 84.7, 87.5
])

# Define the power law function P = B * U0^(m+1) -> y = a * x^b
def power_law(x, a, b):
    return a * np.power(x, b)

# Fit the data
popt, pcov = curve_fit(power_law, U0, P)
a_fit, b_fit = popt

# Generate fitted line points
x_fit = np.linspace(min(U0), max(U0), 100)
y_fit = power_law(x_fit, a_fit, b_fit)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(U0, P, color='blue', label='Experimental Data', s=15)
plt.plot(x_fit, y_fit, 'r-', label=f'Fit: $P = {a_fit:.4f} \\cdot U_0^{{{b_fit:.4f}}}$')
plt.xlabel('$U_0$ (V)')
plt.ylabel('$P_{opt}$ (mW)')
plt.title('Light Source Calibration: $P_{opt}$ vs $U_0$')
plt.legend()
plt.grid(True)

# Save the figure
output_path = 'fig_experiment3.png'
plt.savefig(output_path, dpi=300)
print(f"Figure saved to {output_path}")

# Output results for LaTeX
print("FIT_RESULTS_BEGIN")
print(f"B = {a_fit:.4f}")
print(f"n = m + 1 = {b_fit:.4f}")
print(f"Equation: P_{{opt}} = {a_fit:.4f} \\cdot U_0^{{{b_fit:.4f}}}")
print("FIT_RESULTS_END")
