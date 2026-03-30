
import matplotlib.pyplot as plt
import numpy as np
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Data from experiment
t_set = np.array([40.0, 42.5, 44.5, 46.7, 50.0])
U_o_meas = np.array([-0.4, -0.427, -0.449, -0.480, -0.518]) * 1000 # Convert V to mV ? No, table says mV. 
# Table says: 测试电压 U_o (mV) : -0.4, -0.427... 
# Wait, -0.4 mV is very small. lambda is -0.4 V = -400 mV.
# The table in the snippet says:
# 测试电压 U_o (mV) & -0.4 & -0.427 & ...
# But lambda is -0.4 V.
# Let's look at the theoretical equation: Uo(V) = -0.4 - 0.01*(t-40).
# at t=40, Uo = -0.4 V = -400 mV.
# The table data seems to be in V, but labeled mV? Or maybe labeled V?
# Snippet: "表头参数选择：\lambda = -0.4\mathrm{V}， m = -0.01\mathrm{V}/^\circ\mathrm{C}"
# Snippet table row: "测试电压 $U_o$ ($\mathrm{mV}$)" -> Values: -0.4, -0.427.
# If values are -0.4, that looks like Volts. -0.4 mV would be -0.0004 V.
# If values are Volts, then -0.4 V.
# Let's assume the table unit is wrong in the latex snippet and it should be V, or the values are actually -400, -427 etc in mV.
# Given the values are written as -0.4, they are almost certainly Volts.
# I will treat them as Volts in the plot (or convert to mV for nicer numbers).
# Let's convert to mV for plotting standard.

U_o_volts = np.array([-0.4, -0.427, -0.449, -0.480, -0.518])
U_o_mv = U_o_volts * 1000

# Theoretical Design Line
# U_0 = lambda + m(t - t1)
# lambda = -400 mV, m = -10 mV/C, t1 = 40 C
t_theory = np.linspace(30, 55, 100)
U_o_theory = -400 - 10 * (t_theory - 40)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot theoretical line
plt.plot(t_theory, U_o_theory, 'b--', label='Design Target ($U_o = -400 - 10(t-40)$ mV)')

# Plot experimental points
plt.scatter(t_set, U_o_mv, color='red', marker='o', s=50, zorder=5, label='Measured Data')

# Labels
plt.xlabel('Temperature $t$ ($^\circ$C)')
plt.ylabel('Output Voltage $U_o$ (mV)')
plt.title('Non-equilibrium Bridge Output vs Temperature')
plt.legend()
plt.grid(True)

# Annotate points
for i, txt in enumerate(U_o_mv):
    plt.annotate(f"({t_set[i]}, {txt:.0f})", (t_set[i], U_o_mv[i]), xytext=(0, 10), textcoords='offset points', ha='center')

# Save
output_path = os.path.join(script_dir, 'thermometer_design_plot.png')
plt.savefig(output_path)

print(f"Plot saved to: {output_path}")
