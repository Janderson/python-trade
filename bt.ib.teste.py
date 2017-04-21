from datetime import datetime
import backtrader as bt

class SmaCross(bt.SignalStrategy):
    params = (('pfast', 10), ('pslow', 30),)
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))

cerebro = bt.Cerebro()

cerebro = bt.Cerebro()
cerebro.broker = bt.brokers.IBBroker(host='127.0.0.1', port=7496, clientId=1001)
#ibstore = bt.stores.IBStore(host='127.0.0.1', port=7496, clientId=1001)
#data = ibstore.getdata(dataname='AAPL', timeframe=bt.TimeFrame.Seconds, compression=5) ; print(data)


# data from yahoo finance
data = bt.feeds.YahooFinanceData(dataname='YHOO', fromdate=datetime(2011, 1, 1), todate=datetime(2012, 12, 31))
cerebro.adddata(data)


cerebro.addstrategy(SmaCross)
print(cerebro.run())
cerebro.plot()
