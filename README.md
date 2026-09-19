# 🔬 Universal Bacterial Growth Curve Analyzer

A lightweight, interactive web application designed to help life science researchers and students transform raw laboratory spreadsheet printouts (Excel/CSV) into publication-ready visual growth curves instantly—without requiring complex local database installations or SQL coding.

## 🔗 Live Application
[👉 Click Here to Open the Live App](https://universal-lab-visualizer-cqbm5aeewf5ljq4kfjwnc8.streamlit.app/)

## ✨ Features
* **Zero-SQL Data Engine:** Fully powered by programmatic Pandas dataframes, keeping memory usage minimal (perfect for 8GB RAM local setups).
* **Universal File Drop:** Drag-and-drop support for standard `.xlsx` and `.csv` files.
* **Dynamic Column Mapping:** Automatically detects spreadsheet header text to adapt the user interface to any custom data names.
* **Responsive Interactive Plotting:** Toggles multi-strain visualization overlays dynamically using an active sidebar control panel.

## 🛠️ Ethical AI Collaboration & Development Disclosure
This project was developed using a modern, collaborative approach bridging biological domain expertise with artificial intelligence scaffolding. 

### Specific Usage of Google AI:
* **UI Scaffolding & Layout Architecture:** Google AI was utilized to generate the structural design layout blocks (`st.columns`), dynamic sidebar filters (`st.sidebar.multiselect`), and the logical framework for the reactive application cycle.
* **Exception Handling & Defensive Programming:** The AI assisted in setting up structural code shielding structures (`try...except` blocks) to prevent runtime web crashes if invalid or corrupted datasets are uploaded.
* **Technical Optimization:** Optimized the environment requirements profile to ensure high-speed reactive performance utilizing direct memory processing rather than heavy database query engines.

*As the developer, I directed the application requirements, conceptualized the scientific problem framework based on lab workflow requirements, tested local runtime operations, and managed production cloud deployment.*

## ⚙️ Installation & Local Execution
To run this application locally on your computer, clone the repository and execute the following commands in your terminal:

```bash
pip install streamlit pandas openpyxl
python -m streamlit run app.py
```
