class Stock:
    def __init__(self,tickerStr, lowerLimit, upperLimit):
        self.tickerStr = tickerStr
        self.lowerLimit = float(lowerLimit)
        self.upperLimit = float(upperLimit)

    def setLowerLimitPrice(self,newPrice):
        self.lowerLimit = float(newPrice)

    def setUpperLimitPrice(self, newPrice):
        self.upperLimit = float(newPrice)

