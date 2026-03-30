import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Data
IM = np.array([50, 75, 100, 125, 150, 175, 200])
B = np.array([37.3, 55.5, 74.1, 92.9, 111.2, 130.6, 148.4])

# Linear Regression
slope, intercept, r_value, p_value, std_err = stats.linregress(IM, B)
line = slope * IM + intercept

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(IM, B, color='blue', label='Experimental Data')
plt.plot(IM, line, color='red', label=f'Linear Fit: $B={slope:.4f}I_M + {intercept:.4f}$\n$R^2={r_value**2:.4f}$')

plt.xlabel(r'$I_M$ (mA)')
plt.ylabel(r'$B$ (mT)')
plt.title(r'Relationship between $B$ and $I_M$ (AC Mode)')
plt.legend()
plt.grid(True)

# Save plot
output_dir = r'c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field'
output_path = os.path.join(output_dir, 'plot_AC_B_IM.png')
plt.savefig(output_path)
print(f"Plot saved to {output_path}")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
