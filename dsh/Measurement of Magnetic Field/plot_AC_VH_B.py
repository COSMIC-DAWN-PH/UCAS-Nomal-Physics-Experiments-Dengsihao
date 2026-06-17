import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Data
B = np.array([37.3, 55.5, 74.1, 92.9, 111.2, 130.6, 148.4])
VH_AC = np.array([6.371, 12.488, 18.909, 25.435, 31.755, 38.547, 44.637])

# Linear Regression
slope, intercept, r_value, p_value, std_err = stats.linregress(B, VH_AC)
line = slope * B + intercept

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(B, VH_AC, color='blue', label='Experimental Data')
plt.plot(B, line, color='red', label=f'Linear Fit: $V_{{H-AC}}={slope:.4f}B + {intercept:.4f}$\n$R^2={r_value**2:.4f}$')

plt.xlabel(r'$B$ (mT)')
plt.ylabel(r'$V_{H-AC}$ (mV)')
plt.title(r'Relationship between $V_{H-AC}$ and $B$ (AC Mode)')
plt.legend()
plt.grid(True)

# Save plot
output_dir = r'c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field'
output_path = os.path.join(output_dir, 'plot_AC_VH_B.png')
plt.savefig(output_path)
print(f"Plot saved to {output_path}")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
