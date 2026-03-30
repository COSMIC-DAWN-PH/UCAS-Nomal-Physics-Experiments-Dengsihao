import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Data
f = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
U_max = np.array([1.44, 2.13, 2.87, 3.63, 4.29, 4.98, 5.71, 6.43, 7.13, 7.84, 8.63])
B = np.array([0.211, 0.208, 0.210, 0.212, 0.209, 0.208, 0.209, 0.209, 0.209, 0.209, 0.210])

# Linear Regression for U_max vs f
slope, intercept, r_value, p_value, std_err = stats.linregress(f, U_max)
line_U = slope * f + intercept

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: U_max vs f
ax1.scatter(f, U_max, color='blue', label='Experimental Data')
ax1.plot(f, line_U, color='red', label=f'Linear Fit: $U={slope:.4f}f + {intercept:.4f}$\n$R^2={r_value**2:.4f}$')
ax1.set_xlabel(r'Frequency $f$ (Hz)')
ax1.set_ylabel(r'Induced Voltage $U_{max}$ (mV)')
ax1.set_title(r'Relationship between $U_{max}$ and Frequency $f$')
ax1.legend()
ax1.grid(True)

# Plot 2: B vs f
mean_B = np.mean(B)
ax2.scatter(f, B, color='green', label='Calculated B')
ax2.axhline(y=mean_B, color='orange', linestyle='--', label=f'Mean B = {mean_B:.4f} mT')
ax2.set_xlabel(r'Frequency $f$ (Hz)')
ax2.set_ylabel(r'Magnetic Field $B$ (mT)')
ax2.set_title(r'Relationship between Calculated $B$ and Frequency $f$')
ax2.legend()
ax2.grid(True)
ax2.set_ylim(0.20, 0.22)

plt.tight_layout()

# Save plot
output_dir = r'c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field'
output_path = os.path.join(output_dir, 'plot_frequency_effect.png')
plt.savefig(output_path)

print(f"Plot saved to {output_path}")
print(f"Slope (U vs f): {slope}")
print(f"Intercept (U vs f): {intercept}")
print(f"R-squared: {r_value**2}")
print(f"Mean B: {mean_B}")
print(f"Std B: {np.std(B)}")
