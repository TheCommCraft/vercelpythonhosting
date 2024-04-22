from flask import Flask

# Example code

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is TheCommCraft'

@app.route('/about')
def about():
    return 'About'
