
import yfinance as yf
import time
from plyer import notification
from Stock import Stock


def stockAlarm():
    tickers = menu()
    while True:
        # Retrieve the last adjusted close price for each ticker
        lastPrices = [yf.Ticker(ticker.tickerStr.upper()).history(period='1d')["Close"].iloc[-1] for ticker in tickers]
        for i in range(len(tickers)):
            formatPrice = format(lastPrices[i], ".2f")
            symbol = tickers[i].tickerStr
            print(symbol + ": " + formatPrice + "\n----------")
            # Check if any prices exceed the upper or lower limits
            if lastPrices[i] <= tickers[i].lowerLimit:
                # Send a notification and play a sound for prices exceeding the upper limit
                notification.notify(
                    app_name="Stock",
                    title=f"Price Alert for {tickers[i].tickerStr}",
                    message=f"{tickers[i].tickerStr} has reached your entry price!\n price of {formatPrice}! Buy?",
                    timeout=5,
                    toast=False,
                    app_icon = "icons/buy.ico"

                )
            elif lastPrices[i] > tickers[i].upperLimit:
                # Send a notification and play a sound for prices below the lower limit
                notification.notify(
                    app_name="Stock",
                    title=f"Price Alert for {tickers[i].tickerStr}",
                    message=f"{tickers[i].tickerStr} has reached your TP price!\n price of {formatPrice}! Sell?",
                    timeout=5,
                    toast=False,
                    app_icon = "icons/buy.ico"

                )

        time.sleep(10)


def menu():
    stockList = []
    while (True):
        tickerStr = input("Enter your stock tiker: ")
        if isContain(stockList, tickerStr):
            break
        profitPrice = input("Enter your take profit price: ")
        entryPrice = input("Enter your entry price: ")
        # validation checks
        if checkValid(entryPrice, profitPrice):
            newStock = Stock(tickerStr, entryPrice, profitPrice)
            stockList.append(newStock)
        else:
            print("problem with your input, try again.")
            continue
        res = input("Another stock? y/n: ")
        if res != 'y' and res != 'Y':
            break
    return stockList


def checkValid(entryPrice, profitPrice):
    try:
        float(profitPrice)
        float(entryPrice)
        return True
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False


def isContain(stocksList, ticker):
    tickerSet = {stock.tickerStr for stock in stocksList}
    if ticker in tickerSet or ticker.upper() in tickerSet:
        flag = changeVals(stocksList, ticker)
        return flag
    return False


def changeVals(stocksList, ticker):
    let = input("The stock is at your traiding list!\nwould you like to edit prices? y/n: ")
    if (let != 'y' and let != 'Y'):
        return False
    newProfit = input("set your new profit price: ")
    newStop = input("set your new stop price: ")
    for stock in stocksList:
        if stock.tickerStr == ticker:
            stock.setLimitPrice(newProfit)
            stock.setStopPrice(newStop)
    return True


if __name__ == "__main__":
    stockAlarm()
