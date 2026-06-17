import matplotlib.pyplot as plt
import numpy as np
import os

# Constants
mu0 = 4 * np.pi * 1e-7
N = 400
I = 0.060 # A
R = 0.105 # m

# Experimental Data
X_exp = np.array([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25]) # mm
B_exp = np.array([0.210, 0.211, 0.211, 0.211, 0.211, 0.211, 0.211, 0.210, 0.210, 0.210, 0.210]) # mT

# Theoretical Calculation
def B_theoretical(z_mm):
    z = z_mm / 1000.0 # convert to m
    term1 = (R**2 + (R/2 + z)**2)**(-1.5)
    term2 = (R**2 + (R/2 - z)**2)**(-1.5)
    B = 0.5 * mu0 * N * I * (R**2) * (term1 + term2)
    return B * 1000 # convert to mT

# Generate theoretical curve
z_smooth = np.linspace(-30, 30, 300)
B_smooth = B_theoretical(z_smooth)

# Calculate theoretical B at center
B_center_theo = B_theoretical(0)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(X_exp, B_exp, color='blue', label='Experimental Data', zorder=5)
plt.plot(z_smooth, B_smooth, color='red', linestyle='--', label='Theoretical Curve')

plt.xlabel(r'Position $X$ (mm)')
plt.ylabel(r'Magnetic Field $B$ (mT)')
plt.title(r'Magnetic Field Distribution on the Axis of Helmholtz Coils')
plt.legend()
plt.grid(True)

# Save plot
output_dir = r'c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field'
output_path = os.path.join(output_dir, 'plot_helmholtz.png')
plt.savefig(output_path)

print(f"Plot saved to {output_path}")
print(f"Theoretical B at center: {B_center_theo:.4f} mT")
print(f"Experimental B at center (X=0): {B_exp[5]:.4f} mT")
print(f"Average Experimental B (-10 to 10 mm): {np.mean(B_exp[3:8]):.4f} mT")
