
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data from the LaTeX table
V2 = np.array([600, 650, 700, 750, 800, 850, 900, 950, 1000])
V1 = np.array([133, 137, 142, 153, 164, 170, 180, 191, 198])

# Calculate ratios
ratios = V2 / V1

# Linear regression V1 vs V2
slope, intercept, r_value, p_value, std_err = stats.linregress(V2, V1)
r_squared = r_value**2

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(V2, V1, color='blue', label='Experimental Data')
plt.plot(V2, slope * V2 + intercept, color='red', linestyle='--', label=f'Linear Fit: $V_1 = {slope:.4f} V_2 {intercept:+.2f}$\n$R^2 = {r_squared:.4f}$')

plt.xlabel(r'Anode Voltage $V_2$ (V)')
plt.ylabel(r'Focusing Voltage $V_1$ (V)')
plt.title(r'Relationship between Focusing Voltage $V_1$ and Anode Voltage $V_2$')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot
plt.savefig('focusing_plot.png', dpi=300)

# Output for LaTeX
print("Ratios:", ", ".join([f"{r:.2f}" for r in ratios]))
print(f"Average Ratio: {np.mean(ratios):.2f}")
print(f"Std Dev of Ratio: {np.std(ratios):.4f}")
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_squared:.4f}")
print(f"Standard Error: {std_err:.4f}")
print(f"Pearson Correlation: {r_value:.4f}")

# Generate LaTeX table row for ratios
ratio_row = " & ".join([f"{r:.2f}" for r in ratios])
print(f"LaTeX Ratio Row: {ratio_row}")
