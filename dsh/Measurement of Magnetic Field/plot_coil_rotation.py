import matplotlib.pyplot as plt
import numpy as np
import os

# Data
theta = np.array([
    0, 10, 20, 30, 40, 50, 60, 70, 80, 90,
    100, 110, 120, 130, 140, 150, 160, 170, 180, 190,
    200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
    300, 310, 320, 330, 340, 350, 360
])

U_exp = np.array([
    8.64, 8.52, 8.09, 7.48, 6.67, 5.50, 4.28, 2.81, 1.38, 0.00,
    1.57, 3.05, 4.38, 5.56, 6.67, 7.55, 8.12, 8.52, 8.67, 8.48,
    8.19, 7.62, 6.73, 5.61, 4.27, 2.98, 1.60, 0.10, 1.35, 2.91,
    4.24, 5.47, 6.47, 7.41, 8.07, 8.49, 8.64
])

# Theoretical Curve
U_max = 8.64 # U at 0 degrees
theta_smooth = np.linspace(0, 360, 360)
U_theo = U_max * np.abs(np.cos(np.radians(theta_smooth)))

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(theta, U_exp, color='blue', label='Experimental Data', zorder=5)
plt.plot(theta_smooth, U_theo, color='red', linestyle='--', label=r'Theoretical: $U = U_{max}|\cos\theta|$')

plt.xlabel(r'Rotation Angle $\theta$ ($^\circ$)')
plt.ylabel(r'Induced Voltage $U$ (mV)')
plt.title(r'Relationship between Induced Voltage and Coil Angle')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, 361, 30))

# Save plot
output_dir = r'c:\Personal Profie\Profile\UCAS\t-Sophomore\S1 new\Nomal Physics Experiments\dsh\todo1 Measurement of Magnetic Field'
output_path = os.path.join(output_dir, 'plot_coil_rotation.png')
plt.savefig(output_path)

print(f"Plot saved to {output_path}")

# Calculate Mean Absolute Error
U_theo_points = U_max * np.abs(np.cos(np.radians(theta)))
mae = np.mean(np.abs(U_exp - U_theo_points))
print(f"Mean Absolute Error: {mae:.4f} mV")
