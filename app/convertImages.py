from PIL import Image
import os


for file in os.listdir("static/img/ecSegOutput/dapi2"):
    if file.endswith(".tif"):
        im = Image.open("static/img/ecSegOutput/dapi2/"+file)
        newim = file[:-3]+"png"
        im.save("static/img/ecSegOutput/dapi2/"+newim)

for file in os.listdir("static/img/ecSegOutput/orig"):
    if file.endswith(".tif"):
        im = Image.open("static/img/ecSegOutput/orig/"+file)
        newim = file[:-3]+"png"
        im.save("static/img/ecSegOutput/orig/"+newim)

