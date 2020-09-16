import subprocess
import os
import smtplib
from concurrent.futures import ProcessPoolExecutor
from app import app
from app import imagemanipulation as im
import functools

executor = ProcessPoolExecutor(max_workers=1)

def initializeTaskQueue(workers):
    executor = ProcessPoolExecutor(max_workers=workers)

def addToQueue(folderpath,email,timestamped):
    fut = executor.submit(runecSeg,folderpath)
    fut.add_done_callback(functools.partial(runIsComplete, email,timestamped))

def runecSeg(folderpath):
    path=os.path.abspath(folderpath)
    command = "python3 ../ecSeg/ecSeg.py -i /" +path +"/ -m ../ecSeg/ecDNA_ResUnet.h5"
    subprocess.run(command.split())

def runIsComplete(timestamped,email):
    sendaddress = app.config["EMAIL_USERNAME"]
    sendpassword = app.config["EMAIL_PASSWORD"]
    im.reorganizeOutput(timestamped)
    path = os.path.join(app.config["IMAGE_UPLOADS"],
                        "ecSegOutput", timestamped, "orig")+'/'
    im.tiffToPNG(timestamped)
    if email:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sendaddress, sendpassword)
            subject = 'Your Visualization is Ready'
            body = f'Dear User: \n\necSeg was run successfully on your given input images and parameters. View the visualization by inputting the folder name {timestamped} in panel 3. \n\nDo not reply to this email. If you have a problem with the ecDNA Analytics webtool, create an issue on github (linked below). \nhttps://github.com/MihirBafna/ecDNA-Analytics/issues/new \n\n- ecDNA Analytics Support'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(sendaddress, email, msg)

def runDeepMetaDetect(folderpath):
    path = os.path.abspath(folderpath)
    command = "python3 ../deepMetaDetect/FILENAME"
    subprocess.run(command.split())
