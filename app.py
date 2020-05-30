from flask import Flask, render_template
import os


app = Flask(__name__)

# get image data after ecSeg is run
imagedict=[]
for file in os.listdir("static/img/ecSegOutput/dapi2"):
    if file.endswith(".png"):
        imagedict.append(file)
# print(imagedict[0])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/visualize')
def visualize():
    return render_template('visualize.html', images=imagedict, imgname=imagedict[0])

@app.route('/mpDetector')
def mpDetector():
    return render_template('mpDetector.html')

if __name__ == "__main__":
    app.run(debug=True)
