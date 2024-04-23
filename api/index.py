from flask import Flask, request
from threading import Thread
import time, requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}
# Example code

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is TheCommCraft'

@app.route('/about/')
def about():
    return f'About'

@app.route("/keep_alive/")
def keep_alive():
    response = requests.get(request.args.get("url") or 'https://abrupt-imaginary-text.glitch.me/hello', headers=headers)
    return "probably alive"
