# UCAS Normal Physics Experiments (中国科学院大学 普通物理实验)

本项目包含了中国科学院大学（UCAS）普通物理实验课程的实验报告、数据处理脚本及相关材料。
作者：Dengsihao (邓思豪)

## 实验目录

本项目涵盖了以下实验的内容：

- **[Air Rail (气垫导轨实验)](<dsh/Air Rail>)**
- **[Circuit Resonance (RLC电路的谐振现象)](<dsh/Circuit Resonance>)**
- **[Electron Beam (电子荷质比和弗兰克-赫兹实验)](<dsh/Electron Beam>)**
- **[Flourier Optics (傅里叶光学实验)](<dsh/Flourier Optics>)**
- **[Hysteresis Loop (磁滞回线)](<dsh/Hysteresis Loop>)**
- **[Laser Optical Path (激光光路)](<dsh/Laser Optical Path>)**
- **[Measurement of Magnetic Field (磁场测量)](<dsh/Measurement of Magnetic Field>)**
- **[Millikan Experiment and Coefficeient of Viscosity (密里根油滴实验和粘滞系数实验)](<dsh/Millikan Experiment and Coefficeient of Viscosity>)**
- **[Photoelectric Detection (光电探测)](<dsh/Photoelectric Detection>)**
- **[Spectroscopic Instrument (分光仪的调节与使用)](<dsh/Spectroscopic Instrument>)**
- **[Temperature Measurement (温度测量)](<dsh/Temperature Measurement>)**
- **[Virtual Instrument (虚拟仪器)](<dsh/Virtual Instrument>)**
- **[Young Modulus (杨氏模量)](<dsh/Young Modulus>)**
- **[Standing Waves on the String (弦上驻波实验 - 待完成)](<dsh/todo6 Standing Waves on the String>)**

## 目录结构

每个实验目录下通常包含以下内容：
- **`.tex` 文件**：实验报告的 LaTeX 源代码。
- **`.pdf` 文件**：编译后生成的实验报告最终文档。
- **`.py` / 数据处理文件**：用于处理实验数据并绘制图表的 Python 脚本。
- **图片与数据记录**：实验过程中的原始数据记录、设备照片及报告中所用插图。

## 使用说明

1. **实验报告编译**  
   报告主体采用 LaTeX 编写，建议使用 `XeLaTeX` 进行编译，或者使用集成环境（如 TeX Live, MacTeX, TeXstudio 等）配合 `latexmk` 进行自动编译。
   
2. **数据处理**  
   数据处理部分大多采用 Python 编写。如需运行相关脚本，需确保已安装常用的科学计算库（如 `numpy`, `pandas`, `matplotlib`, `scipy` 等）。
   
## 免责声明

本仓库中的实验报告、数据和代码仅供学习、参考和交流，**请遵守学术诚信，请勿直接抄袭**。希望能为大家更好地理解物理实验与掌握数据处理方法提供帮助。

---
*University of Chinese Academy of Sciences (UCAS) - Normal Physics Experiments*
