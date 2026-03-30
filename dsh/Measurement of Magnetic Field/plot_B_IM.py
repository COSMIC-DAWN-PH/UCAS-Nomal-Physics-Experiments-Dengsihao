import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Data from the table
I_M = np.array([0, 50, 100, 150, 200, 250, 300]) # mA
B = np.array([0, 36.98, 74.25, 111.70, 148.58, 186.53, 224.03]) # mT

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(I_M, B)

# Create plot
plt.figure(figsize=(8, 6))
plt.scatter(I_M, B, color='blue', label='Experimental Data')
plt.plot(I_M, slope * I_M + intercept, color='red', label=f'Linear Fit: $B = {slope:.4f} I_M + {intercept:.4f}$\n$R^2 = {r_value**2:.4f}$')

plt.xlabel('$I_M$ (mA)')
plt.ylabel('$B$ (mT)')
plt.title('Relationship between Magnetic Induction $B$ and Excitation Current $I_M$')
plt.legend()
plt.grid(True)

# Save plot
output_dir = r"c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field"
output_path = os.path.join(output_dir, 'B_vs_IM_plot.png')
plt.savefig(output_path)

print(f"Plot saved to: {output_path}")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
