from PIL import Image
from app import app
import os
import shutil
import zipfile
import subprocess

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
        if file.endswith(".tif") or file.endswith(".tiff"):
            im = Image.open(path+"/"+file)
            newim = file[:-3]+"png"
            im.save(path+"/"+newim)
    path = os.path.join("app/static/img/ecSegOutput/", timestamped, "orig")
    for file in os.listdir(path):
        if file.endswith(".tif") or file.endswith(".tiff"):
            im = Image.open(path+"/"+file)
            newim = file[:-3]+"png"
            im.save(path+"/"+newim)
    path = os.path.join("app/static/img/ecSegOutput/", timestamped, "labels")
    for file in os.listdir(path):
        if file.endswith(".tif") or file.endswith(".tiff"):
            im = Image.open(path+"/"+file)
            newim = file[:-3]+"png"
            im.save(path+"/"+newim)


def dmdTiffToPNG(timestamped):
    path = os.path.join("app/static/img/deepMetaDetectOutput/", timestamped, "orig")
    for file in os.listdir(path):
        if file.endswith(".tif") or file.endswith(".tiff"):
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
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
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
    directory = os.listdir(path)
    print(directory)
    for file in directory:
        if file.endswith(".tif"):
            return True
    return False

def compressAll(path, folder):
    filename = folder+'.zip'
    with zipfile.ZipFile(filename, "w") as zipper:
        for folderName, subfolders, filenames in os.walk(path):
            for file in filenames:
                filePath = os.path.join(folderName, file)
                basepath = '/'.join(filePath.split('/')[-2:])
                zipper.write(filePath, basepath)
    final = os.path.join("app/static/client/img/",filename)
    move(filename, final)
    return final

def compressIMG(path, name):
    filename = name[:-4]+'.zip'
    with zipfile.ZipFile(filename, "w") as zipper:
        for folderName, subfolders, filenames in os.walk(path):
            for file in filenames:
                filePath = os.path.join(folderName, file)
                basepath = '/'.join(filePath.split('/')[-2:])
                if file[:-4] == name[:-4]:
                    zipper.write(filePath, basepath)
    final = os.path.join("app/static/client/img/", filename)
    move(filename,final)
    return final

def move(initial,final):
    command = f"mv {initial} {final}"
    subprocess.run(command.split())

def remove(path):
    command = f"rm {path}"
    subprocess.run(command.split())

def removeClientCache(path):
    count = 0
    for file in os.listdir(path):
        if file.endswith(".zip"):
            remove(os.path.join(path,file))
            count+=1
    return count
