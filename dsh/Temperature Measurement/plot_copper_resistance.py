
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Data encoding
# Including the room temperature point: t = 26.0, Rx = 56.0
t = np.array([26.0, 30.0, 35.0, 40.0, 45.0, 50.0])  # Temperature in Celsius
R_x = np.array([56.0, 57.5, 58.7, 59.8, 61.0, 62.0])  # Resistance in Ohms

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(t, R_x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter(t, R_x, color='red', label='Experiment Data')
plt.plot(t, slope * t + intercept, color='blue', label=f'Linear Fit: $R_x = {slope:.4f}t {intercept:+.4f}$')

# Labels and title
plt.xlabel('Temperature $t$ ($^\circ$C)')
plt.ylabel('Resistance $R_x$ ($\Omega$)')
plt.title('Copper Resistance vs Temperature')
plt.legend()
plt.grid(True)

# Save the plot to the same directory as the script
output_path = os.path.join(script_dir, 'bi_copper_resistance_plot.png')
plt.savefig(output_path)

# Calculate alpha
# R_x = R_0 (1 + alpha * t) = R_0 + R_0 * alpha * t
# Fit: y = mx + c  => m = R_0 * alpha, c = R_0
# alpha = m / c
alpha = slope / intercept

print(f"Slope: {slope:.5f} Ohm/C")
print(f"Intercept (R0): {intercept:.5f} Ohm")
print(f"Alpha (slope/intercept): {alpha:.5e} /C")
print(f"R-squared: {r_value**2:.5f}")
print(f"Plot saved to: {output_path}")
