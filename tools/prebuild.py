import base64
import os

# 1. Read the HTML
with open('index.html', 'rb') as f:
    html_bytes = f.read()

# 2. Encode to Base64
b64_data = base64.b64encode(html_bytes).decode('ascii')

# 3. Create the clean Python script
script_content = f'''import sys
import base64
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

HTML_B64 = "{b64_data}"

class FujiStreakApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fuji Martingale Streak")
        self.resize(1280, 800)
        
        self.browser = QWebEngineView()
        self.browser.setContextMenuPolicy(Qt.NoContextMenu)
        
        # Decode the hidden code
        try:
            html = base64.b64decode(HTML_B64).decode("utf-8", errors="ignore")
            self.browser.setHtml(html)
        except Exception as e:
            self.browser.setHtml(f"<h1>Error loading application</h1><p>{{str(e)}}</p>")
            
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.browser)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FujiStreakApp()
    window.show()
    sys.exit(app.exec())
'''

with open('fuji_app.py', 'w', encoding='utf-8') as f:
    f.write(script_content)

print("fuji_app.py generated successfully.")
