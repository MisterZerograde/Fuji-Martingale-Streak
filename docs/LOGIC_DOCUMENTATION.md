# 📘 Fuji Martingale Streak: Complete Logic & Calculation Guide

This document provides a comprehensive breakdown of how the Fuji Martingale Analyzer processes your data, the mathematics behind the metrics, and how the internal "engine" works.

---

## 1. Data Extraction Engine (Parsing)

The application is designed to be "Smart." It doesn't just read text; it interprets the structure of MetaTrader reports.

### A. Dual-Format Support
The app automatically detects whether you are uploading an **MT4** or **MT5** report:
- **MT5 (Modern)**: It searches for the `Deals` table. This is superior because it shows every single balance change, including commissions and swaps for every leg of the Martingale.
- **MT4 (Classic)**: It searches for the `Closed Transactions` table. Since MT4 doesn't have a "Deals" structure, the app reconstructed sequences based on trade timings and lot size patterns.

### B. The "Net Profit" Calculation
Most traders make the mistake of looking only at the "Profit" column. Fuji Martingale Streak uses the **Realized Net Profit**:
> **Formula:** `Net Profit = Gross Profit + Commission + Swap`

This is critical for Martingale strategies because high-frequency trading generates significant commissions, and deep streaks can last several days, accumulating "Swap" (interest).

---

## 2. The Martingale Sequence Algorithm

Standard MetaTrader reports treat every trade as a separate event. Our algorithm "groups" them into **Sequences**.

### How a Sequence is Identified:
1. **Entry Detection (`IN`)**: A sequence begins the moment a trade is opened (or "scaled in").
2. **The "Layering" Phase**: As long as the bot keeps adding trades (Level 1, Level 2, Level 3...), the app keeps them inside the *same* sequence.
3. **The "Exit" Trigger (`OUT`)**: The sequence only "Closes" when a trade is detected that reduces or completely closes the position. 
4. **Sequence Isolation**: Once a sequence is closed, the very next trade starts "Sequence #2."

---

## 3. Deep-Dive into Metrics

### 📊 Martingale Depth (The "Risk" Metric)
*   **What it is**: The total number of trades opened in a single cycle before it was closed.
*   **Why it matters**: This is your risk indicator. If your bot is designed for 10 levels and the report shows a Depth of 9, you were 1 level away from a potential account wipeout.

### 📈 Lot Progression
*   **Logic**: The app tracks the volume (Lot) of every trade in the sequence.
*   **Example**: `0.01, 0.02, 0.04, 0.08, 0.16`
*   **Purpose**: This allows you to visually verify if your lot multiplier (e.g., 2.0x) is functioning correctly throughout the history.

### ⏱️ Frequency & Probability (The "Time" Metric)
This is the most advanced part of the tool. It calculates how often you "hit" certain depths.
*   **Calculation**: `(Total Days in Report) / (Number of occurrences of Depth X)`
*   **Interpretation**: If the report spans 100 days and you hit "Depth 7" 10 times, the tool will show: **"Avg: 1 per 10.0d"**.
*   **Actionable Insight**: This tells you exactly how many days of "safety" you have on average before the next big streak occurs.

---

## 4. UI & Interactive Features

### 🔍 Minimum Depth Filter
By default, the app might show hundreds of small "Depth 1" or "Depth 2" trades. 
- You can set the **"MIN DEPTH"** filter (e.g., to 5).
- The app will instantly hide all "noise" and show only the dangerous streaks (5 levels or deeper).
- The charts and tables will update in real-time to reflect only this high-risk data.

### 📥 Export Capabilities
- **CSV Export**: Generates a professional spreadsheet of every Martingale sequence, sorted by start time.
- **Image Export**: (Coming soon) Allows you to save the Frequency Distribution chart to share with other traders.

---

## 5. Troubleshooting & Tips

### "No deals found" Error?
This usually happens if you exported the "Orders" report instead of the "Deals" report in MT5. 
- **Solution**: In MT5, go to the `History` tab, right-click, select `Report`, and then `HTML`. Ensure you are on the `Deals` view when you right-click.

### Accuracy Check
If the "Total Profit" in the app looks slightly different from your MT5 balance, remember that the app *only* calculates profit from trades. It ignores deposits, withdrawals, and balance adjustments to give you a "Pure" trading performance view.

---
*Document Version: 2.0*
*Focus: Precision, Risk Analysis, and Transparency.*
