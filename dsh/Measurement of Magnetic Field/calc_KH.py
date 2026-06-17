
# Values from previous fits and data
# Assuming the voltage data in tables is in Volts (V) despite the header saying mV,
# because otherwise the KH value would be 1000x off from the theoretical 345 mV/mA/T.

# 1. From VH - IS curve
slope_VH_IS = 0.0513 # V/mA (corrected unit assumption)
I_M_1 = 200 # mA
# B at I_M = 200 mA from Table 3 (or fit)
B_at_200 = 148.58 # mT
B_at_200_T = B_at_200 / 1000.0 # T

KH_1 = slope_VH_IS / B_at_200_T # V / (mA * T)
KH_1_mV = KH_1 * 1000 # mV / (mA * T)

# 2. From VH - IM curve and B - IM curve
slope_VH_IM = 0.00026 # V/mA (corrected unit assumption)
slope_B_IM = 0.7468 # mT/mA
slope_B_IM_T = slope_B_IM / 1000.0 # T/mA
I_S_2 = 1.00 # mA

# VH = KH * IS * B = KH * IS * (slope_B_IM * IM + intercept)
# Slope of VH vs IM is KH * IS * slope_B_IM
KH_2 = slope_VH_IM / (I_S_2 * slope_B_IM_T) # V / (mA * T)
KH_2_mV = KH_2 * 1000 # mV / (mA * T)

# Average
KH_avg = (KH_1_mV + KH_2_mV) / 2

# Theoretical
KH_theoretical = 345 # mV / (mA * T)

# Error
relative_error = abs(KH_avg - KH_theoretical) / KH_theoretical * 100

print(f"KH_1: {KH_1_mV:.2f}")
print(f"KH_2: {KH_2_mV:.2f}")
print(f"KH_avg: {KH_avg:.2f}")
print(f"Error: {relative_error:.2f}%")
