from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/visualize')
def visualize():
    return render_template('visualize.html')

@app.route('/mpDetector')
def mpDetector():
    return render_template('mpDetector.html')

if __name__ == "__main__":
    app.run(debug=True)