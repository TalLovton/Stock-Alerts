
import yfinance as yf
import time
from plyer import notification
from Stock import Stock

#extracting the latest stock prices, compare to user input and notificate
def stockAlarm():
    tickersMap = menu()
    tickersList = list(tickersMap.keys())
    while True:
        # Retrieve the last adjusted close price for each ticker
        lastPrices = [yf.Ticker(ticker).history(period='1d')["Close"].iloc[-1] for ticker in tickersList]
        for i in range(len(tickersList)):
            formatPrice = format(lastPrices[i], ".2f")
            symbol = tickersList[i]
            print(symbol + ": " + formatPrice + "\n----------")

            # Check if any prices exceed the upper or lower limits
            tmpEntryPrice = tickersMap.get(symbol).getEntryPrice()
            rangeValue = tmpEntryPrice * 1.5 / 100
            if tmpEntryPrice - rangeValue <= lastPrices[i] <= tmpEntryPrice + rangeValue:
                alert(symbol,formatPrice,"reached your entry price")
            
            
            elif lastPrices[i] >= tickersMap.get(symbol).getProfitPrice():
                alert(symbol,formatPrice,"reached your take profit price")
               

        time.sleep(10)


def menu():
    # creating the portfolio stocks list to be alerted
    stockList = {}
    while (True):
        tickerStr = input("Enter your stock tiker: ").strip().upper()
        if tickerStr in stockList:
            changeVals(stockList,tickerStr)
            break
        entryPrice = input("Enter your entry price: ").strip()
        profitPrice = input("Enter your take profit price: ").strip()
        # validation checks
        if checkValid(entryPrice, profitPrice):
            newStock = Stock(tickerStr, float(entryPrice), float(profitPrice))
            stockList[tickerStr] = newStock
        res = input("Another stock? y/n: ").strip().lower()
        if res != 'y':
            break
    return stockList

#chackin validations of user inputs
def checkValid(entryPrice, profitPrice):
    while True:
        try:
            float(profitPrice)
            float(entryPrice)
            return True
        except ValueError:
            print("Invalid input!. Please enter a valid number.")
            
#editing the values of existing stock at portfolio
def changeVals(stocksList, ticker):
    let = input("The stock is at your traiding list!\nwould you like to edit prices? y/n: ").strip().lower()
    if (let != 'y'):
        return
    entryPrice = float(input("set your new entry price: ").strip())
    profitPrice = float(input("set your new take profit price: ").strip())
    if checkValid(entryPrice, profitPrice):
        stocksList.get(ticker).setEntryPrice(entryPrice)
        stocksList.get(ticker).setProfitPrice(profitPrice)
        print("Changes are saved!")
        
# Send a notification and play a sound for prices reaching the entry price
def alert(symbol,price,msg):
    notification.notify(
                    app_name="StockAlert",
                    title=f"Price Alert for {symbol}",
                    message=f"{symbol} {msg} !\nprice of {price}!!",
                    timeout=5,
                    toast=False,
                    app_icon = "icons/buy.ico"

                )



if __name__ == "__main__":
    stockAlarm()
