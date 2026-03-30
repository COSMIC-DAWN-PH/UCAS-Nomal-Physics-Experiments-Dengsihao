
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Data encoding
t = np.array([26.0, 30.0, 35.0, 40.0, 45.0, 50.0])  # Temperature in Celsius
E_x = np.array([0.91, 1.07, 1.27, 1.49, 1.70, 1.91])  # EMF in mV

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(t, E_x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter(t, E_x, color='red', label='Experiment Data')
plt.plot(t, slope * t + intercept, color='blue', label=f'Linear Fit: $E_x = {slope:.4f}t {intercept:+.4f}$')

# Labels and title
plt.xlabel('Temperature $t$ ($^\circ$C)')
plt.ylabel('EMF $E_x$ (mV)')
plt.title('Thermocouple EMF vs Temperature')
plt.legend()
plt.grid(True)

# Save the plot to the same directory as the script
output_path = os.path.join(script_dir, 'thermocouple_plot.png')
plt.savefig(output_path)

# Print the alpha (slope)
print(f"Alpha (slope): {slope:.5f} mV/C")
print(f"Intercept: {intercept:.5f} mV")
print(f"R-squared: {r_value**2:.5f}")
print(f"Plot saved to: {output_path}")
