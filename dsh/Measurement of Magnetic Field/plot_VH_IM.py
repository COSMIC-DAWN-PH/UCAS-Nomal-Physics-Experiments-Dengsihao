import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Data from the table
I_M = np.array([0, 50, 100, 150, 200, 250, 300]) # mA
V_H = np.array([0.0000, 0.0128, 0.0258, 0.0388, 0.0518, 0.0650, 0.0781]) # mV

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(I_M, V_H)

# Create plot
plt.figure(figsize=(8, 6))
plt.scatter(I_M, V_H, color='blue', label='Experimental Data')
plt.plot(I_M, slope * I_M + intercept, color='red', label=f'Linear Fit: $V_H = {slope:.4f} I_M + {intercept:.4f}$\n$R^2 = {r_value**2:.4f}$')

plt.xlabel('$I_M$ (mA)')
plt.ylabel('$V_H$ (mV)')
plt.title('Relationship between Hall Voltage $V_H$ and Excitation Current $I_M$')
plt.legend()
plt.grid(True)

# Save plot
output_dir = r"c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field"
output_path = os.path.join(output_dir, 'VH_vs_IM_plot.png')
plt.savefig(output_path)

print(f"Plot saved to: {output_path}")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
