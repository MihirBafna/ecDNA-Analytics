import subprocess
import os
from app import app

def runecSeg(folderpath, arguments):
    path=os.path.abspath(folderpath)
    command = "python3 ../ecSeg/ecSeg.py -i /" +path +"/ -m ../ecSeg/ecDNA_ResUnet.h5"
    subprocess.run(command.split())

def runMetaDetect():
    return
