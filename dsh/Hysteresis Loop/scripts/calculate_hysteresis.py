import math

# Data
H1_mV = [2.80, 4.16, 6.00, 9.52, 13.8, 17.7, 20.2, 38.0, 45.6, 106]
B1_mV = [6.08, 6.80, 6.04, 7.28, 7.28, 6.48, 5.36, 6.64, 6.32, 10.5]

# Parameters
l = 0.130
S = 1.24e-4
N1 = 150
N2 = 150
R1 = 2.0
R2 = 20e3
C = 2.0e-6
mu0 = 4 * 3.14159 * 1e-7

# 3. Permeability constant K
# K = (R2 * C * l * R1) / (N1 * N2 * S * mu0)
K = (R2 * C * l * R1) / (N1 * N2 * S * mu0)
print(f"K calculated: {K}")

# Calibrate U_R_AC
# mu[0] = 1.57e4
# mu[0] = K * (B1_mV[0] / U_R_AC_mV)
# U_R_AC_mV = K * B1_mV[0] / 1.57e4
mu_target_0 = 1.57e4
U_R_AC_mV = K * B1_mV[0] / mu_target_0
print(f"Calibrated U_R_AC_mV: {U_R_AC_mV}")

print("--------------------------------------------------")
print("Table Rows (Current(mA) & H(A/m) & mu & B1 & H1)")

coordinates_mu_H = []

for h1, b1 in zip(H1_mV, B1_mV):
    # 1. Current I (A) = (H1_mV / 1000) / R1
    I_A = (h1 / 1000.0) / R1
    I_mA = I_A * 1000.0
    
    # 2. H (A/m) = N1 * I / l
    H = N1 * I_A / l
    
    # 4. mu = K * (B1_mV / U_R_AC_mV)
    mu = K * (b1 / U_R_AC_mV)
    
    coordinates_mu_H.append((H, mu))

    # Format for LaTeX table
    # Columns: Current (mA), H (A/m), \mu, B1_mV, H1_mV
    
    # mu is around 1e4, so we can convert to 10^3
    mu_10_3 = mu / 1000.0
    
    print(f"{I_mA:.2f} & {H:.2f} & {mu_10_3:.2f} & {b1:.2f} & {h1:.2f} \\\\")

print("--------------------------------------------------")
print("Coordinates for Plot (H, mu)")
coords_str = ""
for h, m in coordinates_mu_H:
    coords_str += f"({h:.2f}, {m:.2f}) "
print(coords_str)
