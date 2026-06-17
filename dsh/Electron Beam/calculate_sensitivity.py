import matplotlib.pyplot as plt
import numpy as np

# Data extraction from the table
data = {
    "600V_X": {
        "U": np.array([4.9, 8.0, 12.3, 16.4, 20.5, 27.1, 0, 33.6, 40.6, -7.0, -13.5, -20.9, -27.1]),
        "D": np.array([4, 5.5, 9, 12, 15, 20, 0, 25, 30, -5, -10, -15, -20])
    },
    "600V_Y": {
        "U": np.array([-4.6, -9.6, -14.2, -19.1, -23.7, -28.3, 0, 4.8, 9.4, 14.0, 18.2, 22.5, 26.6]),
        "D": np.array([-5, -10, -15, -20, -25, -30, 0, 5, 10, 15, 20, 25, 30])
    },
    "700V_X": {
        "U": np.array([7.6, 15.8, 23.0, 31.2, 38.8, 46.6, 0, -8.0, -15.8, -23.9, -30.9, -38.5, -46.7]),
        "D": np.array([5, 10, 15, 20, 25, 30, 0, -5, -10, -15, -20, -25, -30])
    },
    "700V_Y": {
        "U": np.array([-5.8, -11.2, -16.9, -22.2, -27.6, -32.9, 0, 5.2, 10.5, 15.8, 21.0, 25.8, 30.2]),
        "D": np.array([-5, -10, -15, -20, -25, -30, 0, 5, 10, 15, 20, 25, 30])
    }
}

results = {}

# Set up the plot style
plt.figure(figsize=(12, 10))
# Attempt to use a font that supports Chinese, but fallback to default if necessary
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'Microsoft YaHei', 'DejaVu Sans'] 
plt.rcParams['axes.unicode_minus'] = False

for i, (key, val) in enumerate(data.items()):
    U = val["U"]
    D = val["D"]
    
    # Linear regression (degree 1)
    slope, intercept = np.polyfit(U, D, 1)
    results[key] = slope
    
    # Plot
    plt.subplot(2, 2, i+1)
    plt.scatter(U, D, label='Data', color='blue', marker='o')
    
    # Create points for line
    x_line = np.linspace(min(U), max(U), 100)
    y_line = slope * x_line + intercept
    
    plt.plot(x_line, y_line, color='red', linestyle='--', label=f'Fit: k={slope:.4f}')
    
    title_parts = key.split('_')
    voltage = title_parts[0]
    direction = title_parts[1]
    
    plt.title(f'Anode Voltage {voltage} - {direction} Direction')
    plt.xlabel('Deflection Voltage U (V)')
    plt.ylabel('Deflection D (mm)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
output_path = 'c:\\Personal Profie\\Profile\\UCAS\\t-Sophomore\\S1 new\\Nomal Physics Experiments\\dsh\\todo1 Electron Beam\\deflection_plots.png'
plt.savefig(output_path)
print(f"Plots saved to {output_path}")

print("Calculated Sensitivities (Slope k = D/U):")
for key, val in results.items():
    print(f"{key}: {val:.4f} mm/V")
