
import numpy as np
import matplotlib.pyplot as plt

# Data
U1 = np.arange(0.0, 7.0, 0.5) # 0.0 to 6.5 step 0.5

# U2 arrays in mV
U2_2V = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.2, 0.2])
U2_3V = np.array([0.6, 0.7, 0.7, 0.8, 0.8, 0.9, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.4])
U2_4V = np.array([2.0, 2.0, 2.1, 2.2, 2.3, 2.4, 2.6, 2.8, 2.9, 2.9, 3.0, 3.2, 3.5, 3.8])

# Verify lengths
assert len(U1) == len(U2_2V) == len(U2_3V) == len(U2_4V)

def process_data(u1_arr, u2_mv_arr):
    # I = U2 / 10 (mA)
    # U_cell = U1 - U2/1000 (V)
    I_mA = u2_mv_arr / 10.0
    U_cell = u1_arr - (u2_mv_arr / 1000.0)
    return U_cell, I_mA

U_cell_2V, I_2V = process_data(U1, U2_2V)
U_cell_3V, I_3V = process_data(U1, U2_3V)
U_cell_4V, I_4V = process_data(U1, U2_4V)

# Print Table Data
print("Table Data (Latex format):")
print(r"U1 (V) & U_cell (V) & I (mA) & U_cell (V) & I (mA) & U_cell (V) & I (mA) \\")
for i in range(len(U1)):
    print(f"{U1[i]:.1f} & {U_cell_2V[i]:.4f} & {I_2V[i]:.2f} & {U_cell_3V[i]:.4f} & {I_3V[i]:.2f} & {U_cell_4V[i]:.4f} & {I_4V[i]:.2f} \\\\")

# Plotting
plt.figure(figsize=(8, 6))

plt.plot(U_cell_2V, I_2V, 'o-', label='$U_0=2$V (Weak Light)')
plt.plot(U_cell_3V, I_3V, 's-', label='$U_0=3$V (Medium Light)')
plt.plot(U_cell_4V, I_4V, '^-', label='$U_0=4$V (Strong Light)')

plt.xlabel('Reverse Bias Voltage $U$ (V)')
plt.ylabel('Photocurrent $I$ (mA)')
plt.title('I-V Characteristics of Silicon Photocell under Reverse Bias')
plt.legend()
plt.grid(True)
plt.savefig('fig_experiment6_reverse.png')
