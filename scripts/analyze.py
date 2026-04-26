
from bs4 import BeautifulSoup
import collections
import matplotlib.pyplot as plt
import os

file_path = r"c:\Users\COMPUTER\Desktop\martinglae\ReportTester-12139132.html"
output_dir = r"c:\Users\COMPUTER\Desktop\martinglae\artifacts"
os.makedirs(output_dir, exist_ok=True)

def run_lite_analysis():
    with open(file_path, 'r', encoding='utf-16') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    rows = soup.find_all('tr')
    deals = []
    found_deals = False
    headers = None
    
    for row in rows:
        texts = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])]
        if not found_deals:
            if "Deals" in texts: found_deals = True
            continue
        if not headers:
            if "Time" in texts and "Deal" in texts: headers = texts
            continue
        if found_deals and len(texts) == len(headers) and texts[1].isdigit():
            deals.append(dict(zip(headers, texts)))

    results = []
    streak = []
    for d in deals:
        if d.get('Comment') == '#Martingale rsi':
            streak.append({'id': d['Deal'], 'lot': d['Volume']})
        elif streak:
            results.append(streak)
            streak = []
    if streak: results.append(streak)

    # Filter for Depth >= 5
    final_seqs = [s for s in results if len(s) >= 5]
    
    # 1. Log
    log_path = os.path.join(output_dir, "analysis_report.txt")
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("=== FINAL MARTINGALE REPORT ===\n\n")
        for i, s in enumerate(final_seqs):
            f.write(f"Seq #{i+1} | Depth: {len(s)} | Lots: {', '.join([x['lot'] for x in s])}\n")

    # 2. Chart
    counts = collections.Counter([len(s) for s in final_seqs])
    if counts:
        plt.figure(figsize=(8, 5))
        plt.bar([f"{d} Trades" for d in sorted(counts.keys())], [counts[d] for d in sorted(counts.keys())], color='skyblue')
        plt.title("Martingale Frequency")
        plt.savefig(os.path.join(output_dir, "analysis_chart.png"))

if __name__ == "__main__":
    run_lite_analysis()
