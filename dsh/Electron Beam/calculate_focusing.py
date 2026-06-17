import matplotlib.pyplot as plt
import numpy as np

V2 = np.array([600, 650, 700, 750, 800, 850, 900, 950, 1000])
V1 = np.array([133, 143, 142, 153, 164, 170, 180, 191, 198])

ratios = V2 / V1

print("Ratios V2/V1:")
print(" & ".join([f"{r:.2f}" for r in ratios]))
print(f"Average Ratio: {np.mean(ratios):.2f}")

# Plot
plt.figure(figsize=(8, 6))
# Attempt to use a font that supports Chinese
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'Microsoft YaHei', 'DejaVu Sans'] 
plt.rcParams['axes.unicode_minus'] = False

plt.scatter(V2, V1, label='实验数据', color='blue')

# Fit V1 = a * V2 + b
slope, intercept = np.polyfit(V2, V1, 1)
x_line = np.linspace(min(V2), max(V2), 100)
y_line = slope * x_line + intercept

plt.plot(x_line, y_line, 'r--', label=f'拟合: $V_1 = {slope:.4f} V_2 {intercept:+.2f}$')

plt.title('电聚焦：聚焦电压 $V_1$ 随阳极电压 $V_2$ 的变化')
plt.xlabel('阳极电压 $V_2$ (V)')
plt.ylabel('聚焦电压 $V_1$ (V)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
output_path = 'c:\\Personal Profie\\Profile\\UCAS\\t-Sophomore\\S1 new\\Nomal Physics Experiments\\dsh\\todo1 Electron Beam\\focusing_plot.png'
plt.savefig(output_path)
print(f"Plot saved to {output_path}")
