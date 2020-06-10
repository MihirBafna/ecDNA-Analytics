from PIL import Image
from app import app
import os

def tiffToPNG(timestamped):
    print(os.getcwd())
    path = os.path.join("app/static/img/ecSegOutput/", timestamped, "dapi2")
    for file in os.listdir(path):
        if file.endswith(".tif"):
            im = Image.open(path+"/"+file)
            newim = file[:-3]+"png"
            im.save(path+"/"+newim)
    path = os.path.join("app/static/img/ecSegOutput/", timestamped, "orig")
    for file in os.listdir(path):
        if file.endswith(".tif"):
            im = Image.open(path+"/"+file)
            newim = file[:-3]+"png"
            im.save(path+"/"+newim)


def allowed_image(filename, inout):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if inout and ext.upper() in app.config["ALLOWED_INPUT_IMAGE_EXTENSIONS"]:
        return True
    elif not inout and ext.upper() in app.config["ALLOWED_OUTPUT_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def imglist(filepath):  # get image data after ecSeg is run
    print(os.listdir(filepath))
    imagelist = []
    for file in os.listdir(filepath):
        if file.endswith(".png"):
            imagelist.append(file)
    return(imagelist)
