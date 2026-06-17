import matplotlib.pyplot as plt
import numpy as np
import os

# Data
r = np.array([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25]) # mm
B = np.array([0.210, 0.210, 0.211, 0.211, 0.211, 0.211, 0.211, 0.210, 0.210, 0.210, 0.210]) # mT

# Theoretical Central Value (calculated previously)
B_center_theo = 0.2055 # mT

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(r, B, color='blue', label='Experimental Data', zorder=5)
plt.axhline(y=B_center_theo, color='green', linestyle='--', label=f'Theoretical Center Value ({B_center_theo:.4f} mT)')

# Connect points with a smooth line or just a line
plt.plot(r, B, color='blue', linestyle='-', alpha=0.5)

plt.xlabel(r'Radial Position $r$ (mm)')
plt.ylabel(r'Magnetic Field $B$ (mT)')
plt.title(r'Magnetic Field Distribution along Radial Direction of Helmholtz Coils')
plt.legend()
plt.grid(True)
plt.ylim(0.20, 0.22) # Set y-axis limits to show detail

# Save plot
output_dir = r'c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field'
output_path = os.path.join(output_dir, 'plot_helmholtz_radial.png')
plt.savefig(output_path)

print(f"Plot saved to {output_path}")
print(f"Average Experimental B: {np.mean(B):.4f} mT")
