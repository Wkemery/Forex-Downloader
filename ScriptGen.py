import os



FOREX_DATA_PATH = "C:\\Users\\wyatt\\Documents\\ForexData"
OUTFILE = "download.txt"



def get_current_month_num(current_month):
    if current_month < 10:
        return "0" + str(current_month)
    else:
        return str(current_month)

def get_current_month_name(current_month):
    if current_month is 1:
        return "January"
    elif current_month is 2:
        return "February"
    elif current_month is 3:
        return "March"
    elif current_month is 4:
        return "April"
    elif current_month is 5:
        return "May"
    elif current_month is 6:
        return "June"
    elif current_month is 7:
        return "July"
    elif current_month is 8:
        return "August"
    elif current_month is 9:
        return "September"
    elif current_month is 10:
        return "October"
    elif current_month is 11:
        return "November"
    elif current_month is 12:
        return "December"


outfile = open(OUTFILE, 'w')

FX_pairs = os.listdir(FOREX_DATA_PATH)

start_month = int(input("Enter Start month (as a number 1-12): "))
start_week = int(input("Enter Start Week (as a number 1-5): "))
start_year = int(input("Enter Start year (as a number 10-18): "))
end_month = int(input("Enter End Month (as a number 1-12): "))
end_week = int(input("Enter End Week (as a number 1-5): "))
end_year = int(input("Enter End Year (as a number 10-18: )"))

for pair in FX_pairs:

    current_month = start_month
    current_year = start_year
    current_week = start_week
    downloading = True

    while downloading:
        lineout = "http://ratedata.gaincapital.com/" + "20" + str(current_year) + "/" + get_current_month_num(current_month) + "%20" + get_current_month_name(current_month) + "/" + pair[0:3] + "_" + pair[3:6] + "_Week" + str(current_week) + ".zip"
        outfile.write(lineout + "\n")

        if current_year is end_year and current_month is end_month and current_week is end_week:
            downloading = False

        if current_month is 12 and current_week is 5:
            current_year = current_year + 1
        if current_week is 5:
            current_month = (current_month % 12) + 1
        current_week = (current_week % 5) + 1



outfile.close()
