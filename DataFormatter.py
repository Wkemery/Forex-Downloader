import csv

#take in tick data from gain capital and format for Panda

def pandaFormatData(filein, fileout):

    infile = open(filein, 'r', newline='')
    forexreader = csv.reader(infile, delimiter=',')

    outfile = open(fileout, 'w', newline='')
    forexwriter = csv.writer(outfile, delimiter=',')

    rowcount = 1
    for row in forexreader:
        if rowcount is not 1:
            forexwriter.writerow([row[2], row[3], row[4], row[5]])
        rowcount = rowcount + 1

def append(appendto, appendfrom):
    infile = open(appendfrom, 'r', newline='')
    forexreader = csv.reader(infile, delimiter=',')

    outfile = open(appendto, 'a', newline='')
    forexwriter = csv.writer(outfile, delimiter=',')

    rowcount = 1
    for row in forexreader:
        if rowcount is not 1:
            forexwriter.writerow([row[0], row[1], row[2], row[3], row[4]])
        rowcount = rowcount + 1

def completedFormat(filein, fileout, intra):

    infile = open(filein, 'r', newline='')
    forexreader = csv.reader(infile, delimiter=',')

    outfile = open(fileout, 'w', newline='')
    forexwriter = csv.writer(outfile, delimiter=',')

    rowcount = 1
    for row in forexreader:
        if rowcount is not 1 and row[1] is not "":
            if intra is True:
                date, time = row[0].split(" ")
                year,month,day = date.split("-")
                forexwriter.writerow([year + "/" + month + "/" + day, time, row[1], row[2], row[3], row[4]])
            else:
                year,month,day = row[0].split("-")
                forexwriter.writerow([year + "/" + month + "/" + day, row[1], row[2], row[3], row[4]])
        rowcount = rowcount + 1
