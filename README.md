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
- **[Standing Waves on the String (弦上驻波实验)](<dsh/Standing Waves on the String>)**

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

3. **报告自动化与模板**  
   仓库提供了 Codex skill：`.agents/skills/physics_report_builder/`。通用报告模板位于 `.agents/skills/physics_report_builder/assets/template.tex`，新建实验报告时可复制该模板作为起点。

## Physics Report Builder Skill

`physics_report_builder` 是面向本仓库实验目录结构的物理实验报告自动化工具。它能够完成以下工作：

- 定位 `dsh/` 下的实验目录及实验指导手册。
- 提取 PDF 手册文本，识别实验目的、仪器、原理、步骤和思考题。
- 整理实验图片并生成图片资源清单。
- 在保留原有报告结构和个人信息的前提下填充 LaTeX 模板。
- 结合实验数据与图片完成数据处理、误差分析和思考题解答。
- 使用 `latexmk` 或 `XeLaTeX` 编译报告，并根据日志处理编译错误。

使用该 skill 时需要提供实验目录、PDF 手册和 LaTeX 模板。例如：

```text
使用 physics_report_builder，根据讲义完成 Air Rail 实验报告。
实验目录：dsh/Air Rail
PDF 手册：气垫导轨实验讲义.pdf
LaTeX 模板：dsh/Air Rail/Air Rail.tex
```

预处理脚本也可以单独执行：

```powershell
python .agents/skills/physics_report_builder/workflow_preprocess.py "Air Rail" "气垫导轨实验讲义.pdf"
```

脚本会在实验目录生成 `extracted_manual.txt` 和 `preprocess_manifest.md`。完整规则请参阅 [`SKILL.md`](.agents/skills/physics_report_builder/SKILL.md)。
   
## 免责声明

本仓库中的实验报告、数据和代码仅供学习、参考和交流，**请遵守学术诚信，请勿直接抄袭**。希望能为大家更好地理解物理实验与掌握数据处理方法提供帮助。

---
*University of Chinese Academy of Sciences (UCAS) - Normal Physics Experiments*
