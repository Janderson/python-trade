from time import sleep, strftime
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message
import pandas as pd
import numpy as np

def nextValidId_handler(msg):
    print(msg)
    inner()

hist = []

def my_hist_data_handler(msg):
    print(msg)
    if "finished" in msg.date:
        print('disconnecting', con.disconnect())
        df = df = pd.DataFrame(index=np.arange(0, len(hist)), columns=('date', 'close', 'volume'))
        for index, msg in enumerate(hist):
                df.loc[index,'date':'volume'] = msg.date, msg.close, msg.volume
        print(df )
    else:
        hist.append(msg)
        #print ("a")

def error_handler(msg):
    print(msg)


def inner():
        qqqq = Contract()
        qqqq.m_secType = "STK"
        qqqq.m_symbol = "AAPL"
        qqqq.m_currency = "USD"
        qqqq.m_exchange = "SMART"
        endtime = strftime('%Y%m%d %H:%M:%S')
        print(endtime)
        con.reqHistoricalData(1,qqqq,endtime,"1 W","1 day","MIDPOINT",1,2)

if __name__ == '__main__':

    con = ibConnection(port=7496,clientId=1001)
    con.register(error_handler, message.Error)
    con.register(nextValidId_handler, message.nextValidId)
    con.register(my_hist_data_handler, message.historicalData)
    con.connect()

    print(con.isConnected())

    inner()
    print(con.isConnected())
