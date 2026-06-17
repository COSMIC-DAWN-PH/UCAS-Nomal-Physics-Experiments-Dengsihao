import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import os

# Data
IM = np.array([50, 75, 100, 125, 150, 175, 200])
VH_AC = np.array([6.371, 12.488, 18.909, 25.435, 31.755, 38.547, 44.637])

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(IM, VH_AC, color='blue', label='Experimental Data')

# Smooth curve using spline
IM_smooth = np.linspace(IM.min(), IM.max(), 300)
spl = make_interp_spline(IM, VH_AC, k=3)  # Cubic spline
VH_AC_smooth = spl(IM_smooth)

plt.plot(IM_smooth, VH_AC_smooth, color='red', linestyle='-', label='Smooth Curve')

plt.xlabel(r'$I_M$ (mA)')
plt.ylabel(r'$V_{H-AC}$ (mV)')
plt.title(r'Relationship between $V_{H-AC}$ and $I_M$')
plt.legend()
plt.grid(True)

# Save plot
output_dir = r'c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field'
output_path = os.path.join(output_dir, 'plot_VH_AC_IM.png')
plt.savefig(output_path)
print(f"Plot saved to {output_path}")
