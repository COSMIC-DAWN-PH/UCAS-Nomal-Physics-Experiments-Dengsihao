import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy import stats

# 1. 输入实验数据 (砝码质量M单位: g, 平均长度l单位: mm)
M = np.array([250, 500, 750, 1000, 1250, 1500, 1750, 2000])
l = np.array([0.34, 0.625, 0.89, 1.15, 1.43, 1.695, 1.98, 2.25])

# 2. 单位转换: g -> kg, mm -> m
M_kg = M / 1000  # 转换为千克
l_m = l / 1000    # 转换为米

# 3. 绘制l随M的变化曲线
plt.figure(figsize=(10, 6))
plt.scatter(M_kg, l_m, color='red', label='实验数据')

# 4. 线性拟合: l = k*M + b
slope, intercept, r_value, p_value, std_err = stats.linregress(M_kg, l_m)
line = slope * M_kg + intercept

# 绘制拟合直线
plt.plot(M_kg, line, 'b--', label=f'线性拟合: l = {slope:.6f}M + {intercept:.6f}')

# 设置图表属性
plt.xlabel('砝码质量 M (kg)')
plt.ylabel('长度 l (m)')
plt.title('长度l随砝码质量M的变化关系及线性拟合')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('l_vs_M.png', dpi=300)  # 保存图像

# 额外：将当前图保存为 PDF（单页）
pdf_filename = 'l_vs_M.pdf'
with PdfPages(pdf_filename) as pdf:
	pdf.savefig(bbox_inches='tight')

print(f"已保存图像: l_vs_M.png 和 PDF: {pdf_filename}")

plt.show()

# 5. 输出拟合结果
print(f"线性拟合方程: l = {slope:.6f}*M + {intercept:.6f}")
print(f"斜率 k = {slope:.6f} m/kg")
print(f"相关系数 R² = {r_value**2:.6f}")

# 6. 计算杨氏模量Y
g = 9.807        # 重力加速度 (m/s²)
L = 0.791        # 钢丝长度 (m)，根据实际测量值修改
d = 0.000191     # 钢丝直径 (m)，根据实际测量值修改

Y = (4 * g * L) / (np.pi * d**2 * abs(slope))
print(f"杨氏模量计算值: Y = {Y:.6e} N/m²")

# 7. 计算相对误差
Y_standard = 2.3e11  # 标准值，根据实际材料修改
relative_error = abs(Y - Y_standard) / Y_standard * 100
print(f"相对误差: {relative_error:.2f}%")
    