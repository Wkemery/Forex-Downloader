import urllib.request
import csv
import os
import zipfile
import shutil
from DataFormatter import *
from DataConverter import *

ERROR_FILE = "failed_urls.txt"

err_file = open(ERROR_FILE, 'w')
downloadfile = open("download.txt", 'r', newline='')
dlreader = csv.reader(downloadfile, delimiter=',')

for row in dlreader:
    #download and extract the 1 week data
    urlparts = row[0].split("/")

    try:
        urllib.request.urlretrieve(row[0], urlparts[-1])
    except:
        err_file.write(row[0])
        continue

    fxnames = urlparts[-1].split("_")
    fxname = fxnames[0] + fxnames[1]
    destfolder = "C:\\Users\wyatt\Documents\ForexData\\" + fxname

    with zipfile.ZipFile(urlparts[-1],"r") as zip_ref:
            zip_ref.extractall(destfolder)


    tick_data_file = destfolder + "\\" + urlparts[-1][:-3]  + "csv"
    tick_formatted_file = destfolder + "\\" + urlparts[-1][:-4] + "_tick.csv"

    #format tick data so that panda can read it
    pandaFormatData(tick_data_file, tick_formatted_file)

    #convert tick data to 15 minute data
    convertFromTick(tick_formatted_file)

    #append 15 minute data to big file
    append(destfolder + "\\" + fxname + "_M15.csv", tick_formatted_file[:-4] + "M15.csv")

    #recalculate M15 data as H1, H4, and D
    convertFromM15(destfolder + "\\" + fxname + "_M15.csv")

    os.remove(tick_data_file)
    os.remove(tick_formatted_file)
    os.remove(tick_formatted_file[:-4] + "M15.csv")
    os.remove(urlparts[-1])
    print('.', end='', flush=True)

err_file.close()
