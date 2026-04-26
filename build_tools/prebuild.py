import base64
import os

# Paths relative to this script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UI_PATH = os.path.join(BASE_DIR, 'app', 'ui', 'index.html')
OUTPUT_PATH = os.path.join(BASE_DIR, 'app', 'src', 'main.py')

# 1. Read the HTML
with open(UI_PATH, 'rb') as f:
    html_bytes = f.read()

# 2. Encode to Base64
b64_data = base64.b64encode(html_bytes).decode('ascii')

# 3. Create the clean Python script using Flask (Small size version)
script_content = f'''import sys
import base64
import os
import threading
import webbrowser
import logging
from flask import Flask

app = Flask(__name__)

# The entire application UI is contained within this encoded block for portability and small size
HTML_B64 = "{b64_data}"

@app.route('/')
def index():
    try:
        html = base64.b64decode(HTML_B64).decode("utf-8", errors="ignore")
        return html
    except Exception as e:
        return f"<h1>Error loading application</h1><p>{{str(e)}}</p>"

def open_browser():
    # Wait for the server to start then launch browser
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    # Start browser in a separate thread
    threading.Timer(1.5, open_browser).start()
    
    # Run the server quietly (no terminal spam)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    
    # Run the local server
    app.run(port=5000, debug=False, use_reloader=False)
'''

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(script_content)

print(f"Application logic updated successfully at {OUTPUT_PATH}")
