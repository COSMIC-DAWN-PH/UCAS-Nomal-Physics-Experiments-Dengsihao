import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data from the table
I_S = np.array([0, 0.50, 1.00, 1.50, 2.00, 2.50, 3.00]) # mA
V_H = np.array([0, 0.0261, 0.0515, 0.0770, 0.1028, 0.1282, 0.1542]) # mV

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(I_S, V_H)

# Create plot
plt.figure(figsize=(8, 6))
plt.scatter(I_S, V_H, color='blue', label='Experimental Data')
plt.plot(I_S, slope * I_S + intercept, color='red', label=f'Linear Fit: $V_H = {slope:.4f} I_S + {intercept:.4f}$\n$R^2 = {r_value**2:.4f}$')

plt.xlabel('$I_S$ (mA)')
plt.ylabel('$V_H$ (mV)')
plt.title('Relationship between Hall Voltage $V_H$ and Working Current $I_S$')
plt.legend()
plt.grid(True)

# Save plot
import os
output_dir = r"c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field"
output_path = os.path.join(output_dir, 'VH_vs_IS_plot.png')
plt.savefig(output_path)

print(f"Plot saved to: {output_path}")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
