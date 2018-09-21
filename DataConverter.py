import pandas as pd
from DataFormatter import *
import os

def convertFromTick(infile):

    data_frame = pd.read_csv(infile, names=['Symbol', 'Date_Time', 'Bid', 'Ask'], index_col=1, parse_dates=True)
    data_bid =  data_frame['Bid'].resample('15Min').ohlc()
    data_bid.to_csv(infile[:-4] + "M15.csv", header=False)

def convertFromM15(infile):

    data_frame = pd.read_csv(infile, names=['Date_Time', 'open', 'high', 'low', 'close'], index_col=0, parse_dates=True)
    data_bid =  data_frame.resample('1H').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'})
    data_bid.to_csv(infile[:-7] + "H1T.csv", header=False)
    append(infile[:-7] + "H1.csv", infile[:-7] + "H1T.csv")

    data_bid =  data_frame.resample('4H').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'})
    data_bid.to_csv(infile[:-7] + "H4T.csv", header=False)
    append(infile[:-7] + "H4.csv", infile[:-7] + "H4T.csv")

    data_bid =  data_frame.resample('1D').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'})
    data_bid.to_csv(infile[:-7] + "DT.csv", header=False)
    append(infile[:-7] + "D.csv", infile[:-7] + "DT.csv")

    os.remove(infile[:-7] + "DT.csv")
    os.remove(infile[:-7] + "H4T.csv")
    os.remove(infile[:-7] + "H1T.csv")
