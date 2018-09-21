from os import listdir
from dataConverter import *
import os
import zipfile
import shutil


rawDataDirectory = "C:\Program Files (x86)\LiveTickData Client\Downloads\\"
zipfiles = os.listdir(rawDataDirectory)

for file in zipfiles:
    destfolder = "C:\\Users\wyatt\Documents\ForexData\\" + file[6:12]
    with zipfile.ZipFile(rawDataDirectory + file,"r") as zip_ref:
        zip_ref.extractall(destfolder)

    forexfiles = os.listdir(destfolder)
    for forexfile in forexfiles:
        if(forexfile.startswith("History_")):
            filename = destfolder + "\\" + forexfile
    newfilename = destfolder + "\\" + file[6:12] + "_M1.txt"
    print(newfilename)
    shutil.move(filename, newfilename)
    convertData(newfilename, newfilename[:-7] + "_H1.txt", 60)
    convertData(newfilename, newfilename[:-7] + "_H4.txt", 240)
    convertData(newfilename, newfilename[:-7] + "_D.txt", 1440)
