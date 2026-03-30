import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

# Data from the table
T = np.array([7.65, 15.30, 22.95, 30.61, 38.26])
f = np.array([32.5, 42.5, 53.1, 58.8, 65.2])

# Calculate natural logarithms
ln_T = np.log(T)
ln_f = np.log(f)

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(ln_T, ln_f)

# Theory
# f = (1/2L) * sqrt(T/mu)
# ln f = 0.5 * ln T - 0.5 * ln mu - ln(2L)
L = 0.400 # m
mu = 0.00538 # kg/m
theoretical_slope = 0.5
theoretical_intercept = -0.5 * np.log(mu) - np.log(2 * L)

print(f"Experimental Slope: {slope:.4f}")
print(f"Experimental Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")
print(f"Theoretical Slope: {theoretical_slope:.4f}")
print(f"Theoretical Intercept: {theoretical_intercept:.4f}")

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(ln_T, ln_f, color='black', label='Experimental Data', zorder=5)

# Plot fit line
x_fit = np.linspace(min(ln_T)-0.1, max(ln_T)+0.1, 100)
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, 'r-', label=f'Linear Fit: $y = {slope:.2f}x + {intercept:.2f}$\n$R^2 = {r_value**2:.3f}$')

# Plot theoretical line (optional, but good for comparison)
# y_theo = theoretical_slope * x_fit + theoretical_intercept
# plt.plot(x_fit, y_theo, 'b--', label=f'Theoretical: $y = {theoretical_slope:.2f}x + {theoretical_intercept:.2f}$')

plt.xlabel(r'$\ln T$')
plt.ylabel(r'$\ln f$')
plt.title(r'Relationship between $\ln f$ and $\ln T$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Save the plot
output_path = os.path.join(os.getcwd(), 'lnf_lnT_plot.png')
plt.savefig(output_path, dpi=300)
print(f"Plot saved to {output_path}")
