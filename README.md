# Fuji Martingale Streak Analyzer

A high-performance trading report analyzer designed to identify and visualize Martingale sequence patterns in MetaTrader 4/5 reports.

## 🚀 Project Structure

```text
/
├── app/                 # Main Desktop Application
│   ├── src/             # Python source code (PySide6)
│   └── ui/              # User Interface (HTML/CSS/JS)
├── build_tools/         # Executable build scripts and configuration
├── data/                # Data storage
│   └── reports/         # MT4/MT5 HTML reports for analysis
├── docs/                # Project documentation
├── scripts/             # Useful standalone utility scripts
├── artifacts/           # Generated analysis reports and exports
└── README.md            # Project overview (this file)
```

## 🛠️ Getting Started

### Prerequisites
- Python 3.10+
- PySide6
- Chart.js (Loaded via CDN in the UI)

### Running the App
1. Navigate to `app/src/`
2. Run `python main.py`

### Analyzing Reports
- Open the application.
- Drag and drop your MetaTrader HTML report into the "Drop Zone".
- The system will automatically parse the "Deals" table and group trades into Martingale sequences.
- Use the **Min Depth** filter to isolate deeper streaks (e.g., 5+, 7+, 9+).

## 📊 Features
- **Intelligent Sequence Grouping**: Automatically identifies Martingale streaks based on "In" and "Out" deal directions.
- **Dynamic Frequency Chart**: Visualizes the distribution of sequence depths.
- **Deep Analytics**: Calculates average frequency of deep streaks (e.g., "1 per 3 days").
- **High-End Export**: Generate professional PNG reports and CSV data exports.

## 🔧 Maintenance
- UI changes should be made in `app/ui/index.html`.
- If you modify the UI, run the `build_tools/prebuild.py` (if available) to update the embedded Base64 in `main.py`, or ensure `main.py` is updated accordingly.
