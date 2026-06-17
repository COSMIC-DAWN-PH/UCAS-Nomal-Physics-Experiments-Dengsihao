import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib

# Set backend
matplotlib.use('Agg')

# Raw Data
# U0, UOC
data = np.array([
    [0, 0.01], [0.76, 0.01], [0.87, 0.02], [0.99, 0.05], [1.10, 0.11],
    [1.20, 0.20], [1.29, 0.32], [1.38, 0.46], [1.49, 0.63], [1.59, 0.83],
    [1.68, 0.98], [1.77, 1.15], [1.86, 1.33], [2.01, 1.58], [2.13, 1.77],
    [2.20, 1.89], [2.30, 2.05], [2.41, 2.19], [2.50, 2.32], [2.59, 2.44],
    [2.69, 2.56], [2.81, 2.71], [2.88, 2.79], [2.98, 2.89], [3.09, 3.00],
    [3.19, 3.10], [3.29, 3.18], [3.37, 3.26], [3.49, 3.36], [3.60, 3.44],
    [3.69, 3.50], [3.80, 3.59], [3.90, 3.66], [4.08, 3.77], [4.20, 3.84],
    [4.39, 3.88], [4.39, 3.95], # Note: 4.38 in original text table col 2 row 18, 
                                # but col 3 row 1 is 4.39. Wait, let me check the image/text carefully.
                                # Col 2 last row: 2.41, 2.19. Col 2 row 17: 2.41, 2.19.
                                # Looking at the provided tex content:
                                # Col 1: ... 2.41 2.19
                                # Col 2: 2.50 ... 4.38 3.88 (This is last row of col 2)
                                # Col 3: 4.39 3.95 (This is 1st row of col 3)
                                # There is a data point 4.38 and 4.39. Let's strictly follow the table.
])

# Re-entering data strictly from table to ensure accuracy
# Col 1
c1 = [
    (0, 0.01), (0.76, 0.01), (0.87, 0.02), (0.99, 0.05), (1.10, 0.11),
    (1.20, 0.20), (1.29, 0.32), (1.38, 0.46), (1.49, 0.63), (1.59, 0.83),
    (1.68, 0.98), (1.77, 1.15), (1.86, 1.33), (2.01, 1.58), (2.13, 1.77),
    (2.20, 1.89), (2.30, 2.05), (2.41, 2.19)
]
# Col 2
c2 = [
    (2.50, 2.32), (2.59, 2.44), (2.69, 2.56), (2.81, 2.71), (2.88, 2.79),
    (2.98, 2.89), (3.09, 3.00), (3.19, 3.10), (3.29, 3.18), (3.37, 3.26),
    (3.49, 3.36), (3.60, 3.44), (3.69, 3.50), (3.80, 3.59), (3.90, 3.66),
    (4.08, 3.77), (4.20, 3.84), (4.38, 3.88)
]
# Col 3
c3 = [
    (4.39, 3.95), (4.50, 4.01), (4.60, 4.06), (4.70, 4.11), (4.80, 4.15),
    (4.94, 4.22), (5.04, 4.26), (5.16, 4.31), (5.27, 4.35), (5.37, 4.38),
    (5.46, 4.41), (5.57, 4.45), (5.70, 4.49), (5.82, 4.52), (5.90, 4.54),
    (6.00, 4.57), (6.10, 4.60), (6.24, 4.63), (6.32, 4.65), (6.47, 4.68)
]

data_points = c1 + c2 + c3
data_np = np.array(data_points)
U0 = data_np[:, 0]
UOC = data_np[:, 1]

# Calibration Parameters
B = 0.5930
m_plus_1 = 2.7030

# Calculate P
# Filter out U0 = 0 to avoid log(0) error
valid_indices = U0 > 0.1 # filter out 0 and possibly very small noise if any, 0.76 is min non-zero
U0_valid = U0[valid_indices]
UOC_valid = UOC[valid_indices]

P_valid = B * np.power(U0_valid, m_plus_1)

# Define P0 as the maximum calculated intensity
P0 = np.max(P_valid)
P_rel = P_valid / P0
ln_P_rel = np.log(P_rel)

# Fit function: Uoc = a + b * ln(P/P0)
def log_fit_func(x, a, b):
    return a + b * x

popt, pcov = curve_fit(log_fit_func, ln_P_rel, UOC_valid)
a_fit, b_fit = popt

# Generate fitted line
x_fit = np.linspace(min(ln_P_rel), max(ln_P_rel), 100)
y_fit = log_fit_func(x_fit, a_fit, b_fit)

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(ln_P_rel, UOC_valid, color='blue', label='Experimental Data', s=15)
plt.plot(x_fit, y_fit, 'r-', label=f'Fit: $U_{{OC}} = {a_fit:.4f} + {b_fit:.4f} \\ln(P/P_0)$')
plt.xlabel('$\\ln(P / P_0)$')
plt.ylabel('$U_{OC}$ (V)')
plt.title('Relationship between $U_{OC}$ and Relative Light Intensity')
plt.legend()
plt.grid(True)

# Save figure
output_path = 'fig_experiment4.png'
plt.savefig(output_path, dpi=300)
print(f"Figure saved to {output_path}")

# Output Table Info
print("TABLE_DATA_BEGIN")
print(f"P0 (max) = {P0:.4f} mW")
for i in range(len(U0_valid)):
    print(f"{U0_valid[i]:.2f}, {P_valid[i]:.4f}, {P_rel[i]:.4f}, {ln_P_rel[i]:.4f}, {UOC_valid[i]:.2f}")
print("TABLE_DATA_END")

print("FIT_RESULTS_BEGIN")
print(f"a = {a_fit:.4f}")
print(f"b = {b_fit:.4f}")
print("FIT_RESULTS_END")
