import matplotlib.pyplot as plt
import numpy as np

# Data extraction from the table
# Note: Corrected the likely typo in 700V data (39 -> -39 for -5mm deflection)
data = {
    "600V": {
        "I": np.array([39, 79, 124, 167, 206, 245, 0, -41, -86, -128, -173, -216, -257]),
        "D": np.array([5, 10, 15, 20, 25, 30, 0, -5, -10, -15, -20, -25, -30])
    },
    "700V": {
        "I": np.array([37, 77, 114, 155, 192, 228, 0, -39, -78, -119, -159, -200, -238]),
        "D": np.array([5, 10, 15, 20, 25, 30, 0, -5, -10, -15, -20, -25, -30])
    }
}

results = {}

# Set up the plot style
plt.figure(figsize=(12, 5))
# Attempt to use a font that supports Chinese
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'Microsoft YaHei', 'DejaVu Sans'] 
plt.rcParams['axes.unicode_minus'] = False

for i, (key, val) in enumerate(data.items()):
    I = val["I"]
    D = val["D"]
    
    # Linear regression (degree 1)
    slope, intercept = np.polyfit(I, D, 1)
    results[key] = slope
    
    # Plot
    plt.subplot(1, 2, i+1)
    plt.scatter(I, D, label='Data', color='blue', marker='o')
    
    # Create points for line
    x_line = np.linspace(min(I), max(I), 100)
    y_line = slope * x_line + intercept
    
    plt.plot(x_line, y_line, color='red', linestyle='--', label=f'Fit: k={slope:.4f}')
    
    plt.title(f'Anode Voltage {key}')
    plt.xlabel('Deflection Current I (mA)')
    plt.ylabel('Deflection D (mm)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
output_path = 'c:\\Personal Profie\\Profile\\UCAS\\t-Sophomore\\S1 new\\Nomal Physics Experiments\\dsh\\todo1 Electron Beam\\magnetic_deflection_plots.png'
plt.savefig(output_path)
print(f"Plots saved to {output_path}")

print("Calculated Sensitivities (Slope k = D/I):")
for key, val in results.items():
    print(f"{key}: {val:.4f} mm/mA")
