from PIL import Image
from app import app
import os
import shutil
import zipfile


def reorganizeOutput(timestamped):
    path = os.path.join("app/static/img/ecSegOutput/", timestamped)+'/'
    origpath = os.path.join(path, "orig")+'/'
    os.mkdir(origpath)
    for file in os.listdir(path):
        if file.endswith(".tif"):
            shutil.move(path+file,origpath+file)

def tiffToPNG(timestamped):
    path = os.path.join("app/static/img/ecSegOutput/", timestamped, "dapi")
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
    path = os.path.join("app/static/img/ecSegOutput/", timestamped, "labels")
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
    imagelist = []
    for file in os.listdir(filepath):
        if file.endswith(".png"):
            imagelist.append(file)
    return(imagelist)

def correctOutputFolderStructure(path):
    directory = os.listdir(path)
    orig = False
    dapi = False
    labels = False
    onum = 0
    dnum = 0
    lnum = 0
    def countPNG(folder):
        count=0
        for file in os.listdir(os.path.join(path, folder)):
            if file.endswith(".png"):
                count+=1
        return count
    for folder in directory:
        if folder=='orig':
            onum = countPNG(folder)
            orig = True
        if folder == 'dapi':
            dnum = countPNG(folder)
            dapi = True
        if folder == 'labels':
            lnum = countPNG(folder)
            labels = True
    return orig and dapi and labels and onum == dnum == lnum != 0

def correctInputFolderStructure(path):
    return


def compressImg(name, path, folder):
        # zipper = zipfile.ZipFile(name[:-4]+'.zip' , "w")
    # # zipper.write(os.path.join(path))
    # print(path)
    # print(os.listdir(path))
    # for directory in os.listdir(path):        
    #     print(directory)
    #     print(os.listdir(os.path.join(path, directory)))
    #     # zipper.write(directory)
    #     for file in os.listdir(os.path.join(path,directory)):
    #         print(os.path.join(directory, file))
    #         zipper.write(os.path.join(directory,file))
    #     #     for file in files:
    #     #         zipper.write(os.path.join(directory,direct,file))
    #     #     print(os.path.join(directory, file))
    # zipper.close()
    return

def compressAll():
    return
