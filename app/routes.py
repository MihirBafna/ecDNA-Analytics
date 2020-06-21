from app import app
from app import imagemanipulation as im
from app import tools
from flask import render_template, redirect, request, session, send_from_directory, abort
import os
from werkzeug.utils import secure_filename
from datetime import datetime



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/input')
def input():
    return render_template('input.html')


@app.route('/uploadInput', methods=["GET", "POST"])
def uploadInput():
    if request.method == "POST":
        if request.files:
            folder = request.files.getlist("input-folder-2[]")
            timestamped = datetime.now().strftime('%Y-%m-%d_%H%M%S')
            folderpath = os.path.join(
                app.config["IMAGE_UPLOADS"], "ecSegOutput", timestamped)
            os.makedirs(folderpath)
            for file in folder:
                print(file.filename)
                if file.filename == "":
                    print("ERROR: File has no filename")
                    return redirect(request.url)
                if im.allowed_image(file.filename, True):
                    path = os.path.join(
                        app.config["IMAGE_UPLOADS"], "ecSegOutput", timestamped, '/'.join(file.filename.split('/')[1:]))
                    file.save(path)
                    print("Image saved " + path)
                else:
                    print("not allowed")
    # RUN ECSEG HERE
    tools.runecSeg(folderpath,1)
    im.reorganizeOutput(timestamped)
    path = os.path.join(app.config["IMAGE_UPLOADS"],
                        "ecSegOutput", timestamped, "orig")+'/'
    session['folder'] = timestamped
    im.tiffToPNG(timestamped)
    session['imagelist'] = im.imglist(path)
    session['imagename'] = session['imagelist'][0]
    return redirect('/visualize')



@app.route('/uploadecSeg', methods=["GET", "POST"])
def uploadecSeg():
    if request.method == "POST":
        if request.files:
            folder = request.files.getlist("input-folder-3[]")
            timestamped = datetime.now().strftime('%Y-%m-%d_%H%M%S')
            folderpath = os.path.join(
                app.config["IMAGE_UPLOADS"], "ecSegOutput", timestamped, "orig")
            os.makedirs(folderpath)
            os.mkdir(os.path.join(
                app.config["IMAGE_UPLOADS"], "ecSegOutput", timestamped, "dapi"))
            os.mkdir(os.path.join(
                app.config["IMAGE_UPLOADS"], "ecSegOutput", timestamped, "labels"))
            for file in folder:
                if file.filename == "":
                    print("ERROR: File has no filename")
                    return redirect(request.url)
                if im.allowed_image(file.filename, False):
                    path = os.path.join(
                        app.config["IMAGE_UPLOADS"], "ecSegOutput", timestamped, '/'.join(file.filename.split('/')[1:]))
                    file.save(path)
                    print(file.filename+" saved")
                else:
                    print(file.filename+" not allowed")
    # im.reorganizeOutput(timestamped)
    path = os.path.join(app.config["IMAGE_UPLOADS"],
                        "ecSegOutput", timestamped, "orig")+'/'
    session['folder'] = timestamped
    im.tiffToPNG(timestamped)
    session['imagelist'] = im.imglist(path)
    session['imagename'] = session['imagelist'][0]
    return redirect('/visualize')


@app.route('/visualize/<img>')
def newimgselect(img):
    session['imagename'] = img
    return redirect('/visualize')




@app.route('/visualize')
def visualize():
    return render_template('visualize.html', images=session['imagelist'], folder=session['folder'], imgname=session['imagename'])




@app.route('/downloadIMG/<img>/<folder>')
def downloadIMG(img,folder):   
    try:
        path = os.path.join(app.config["IMAGE_UPLOADS"],
                                   "ecSegOutput", folder)+'/'
        im.compressImg(img,path, folder)
        # return send_from_directory(app.config["IMAGE_UPLOADS"])
        return ""
    except FileNotFoundError:
        abort(404)

@app.route('/mpDetector')
def mpDetector():
    return render_template('mpDetector.html')



