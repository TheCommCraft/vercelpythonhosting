from flask import Flask
from threading import Thread
import time

# Example code

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is TheCommCraft'

@app.route('/about')
def about():
    return f'About {t} seconds running.'

start_time = time.time()
t = 0

def main():
    while True:
        time.sleep(10)
        t = time.time() - start_time

thread = Thread(target=main)
thread.start()
