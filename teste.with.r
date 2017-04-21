library(IBrokers)

tws <- twsConnect() 
tws 
reqCurrentTime(tws) 

twsFuture("YM","ECBOT","200809")
reqContractDetails(tws, twsEquity("QQQQ"))
reqMktData(tws, twsEquity("QQQQ"))

aapl.csv  <-  file("AAPL.csv", open="w") 
reqMktData (tws, twsSTK("AAPL"), eventWrapper = eWrapper.MktData.CSV(1), file = aapl.csv)  
close(aapl.csv)



serverVersion(tws) 
twsDisconnect(tws)

