class Stock:
    tickerStr = None
    entryPrice = 0.00
    takeProfitPrice = 0.00
    
    def __init__(self,tickerStr, entry, profit):
        self.tickerStr = tickerStr
        self.entryPrice = entry
        self.takeProfitPrice = profit 

    def setEntryPrice(self,newPrice):
        self.entryPrice = newPrice
        

    def setProfitPrice(self, newPrice):
        self.takeProfitPrice = newPrice

    def getEntryPrice(self):
        return self.entryPrice
        

    def getProfitPrice(self):
        return self.takeProfitPrice

