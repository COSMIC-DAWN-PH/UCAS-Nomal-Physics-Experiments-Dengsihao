import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import os

# Data
X = np.array([42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16])
B = np.array([35.2, 62.2, 121.8, 148.1, 148.8, 148.7, 148.9, 148.8, 148.6, 148.8, 148.6, 148.6, 148.9, 149.0])

# Sort data by X
sorted_indices = np.argsort(X)
X_sorted = X[sorted_indices]
B_sorted = B[sorted_indices]

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(X_sorted, B_sorted, color='blue', label='Experimental Data')

# Smooth curve using spline
X_smooth = np.linspace(X_sorted.min(), X_sorted.max(), 300)
spl = make_interp_spline(X_sorted, B_sorted, k=3)  # Cubic spline
B_smooth = spl(X_smooth)

plt.plot(X_smooth, B_smooth, color='red', linestyle='-', label='Smooth Curve')

plt.xlabel(r'$X$ (mm)')
plt.ylabel(r'$B$ (mT)')
plt.title(r'Magnetic Field Distribution along Horizontal Direction')
plt.legend()
plt.grid(True)

# Save plot
output_dir = r'c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field'
output_path = os.path.join(output_dir, 'plot_B_X.png')
plt.savefig(output_path)
print(f"Plot saved to {output_path}")
