
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Data encoding
# Including the room temperature point: t = 26.0, Rt = 2.45 kOhm
t_c = np.array([26.0, 30.0, 35.0, 40.0, 45.0, 50.0])  # Temperature in Celsius
R_t = np.array([2.45, 2.15, 1.84, 1.58, 1.34, 1.12])  # Resistance in kOhms

# Convert to Kelvin
T_k = t_c + 273.15
inv_T = 1 / T_k
ln_R = np.log(R_t * 1000) # Convert to Ohms for ln calculation to be standard, though B is unitless wrt R units.

# Linear regression for B value
# ln(R) = ln(A) + B * (1/T)
slope, intercept, r_value, p_value, std_err = stats.linregress(inv_T, ln_R)
B = slope
A = np.exp(intercept)

# --- Plot 1: Rt vs t ---
plt.figure(figsize=(8, 6))
plt.scatter(t_c, R_t, color='red', label='Experiment Data')
# Generate smooth curve for fit
t_smooth = np.linspace(min(t_c), max(t_c), 100)
T_smooth = t_smooth + 273.15
R_smooth = (A * np.exp(B / T_smooth)) / 1000 # Convert back to kOhms
plt.plot(t_smooth, R_smooth, color='blue', label=f'Fit: $R_t = {A/1000:.4f} e^{{{B:.1f}/T}}$ k$\Omega$')

plt.xlabel('Temperature $t$ ($^\circ$C)')
plt.ylabel('Resistance $R_t$ (k$\Omega$)')
plt.title('Thermistor Resistance vs Temperature')
plt.legend()
plt.grid(True)
output_path1 = os.path.join(script_dir, 'thermistor_resistance_plot.png')
plt.savefig(output_path1)

# --- Plot 2: ln(Rt) vs 1/T ---
plt.figure(figsize=(8, 6))
plt.scatter(inv_T, ln_R, color='red', label='Experiment Data')
plt.plot(inv_T, slope * inv_T + intercept, color='blue', label=f'Linear Fit: $\ln R_t = {slope:.1f}(1/T) {intercept:+.2f}$')

plt.xlabel('Inverse Temperature $1/T$ ($K^{-1}$)')
plt.ylabel('$\ln R_t$ ($\ln \Omega$)')
plt.title('Linear fit of $\ln R_t$ vs $1/T$')
plt.legend()
plt.grid(True)
output_path2 = os.path.join(script_dir, 'thermistor_ln_plot.png')
plt.savefig(output_path2)

# Results
print(f"B value (slope): {B:.5f} K")
print(f"A value: {A:.5e} Ohm")
print(f"R-squared: {r_value**2:.5f}")
print(f"Plot 1 saved to: {output_path1}")
print(f"Plot 2 saved to: {output_path2}")
