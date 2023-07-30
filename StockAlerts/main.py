
import yfinance as yf
import time
from plyer import notification
from Stock import Stock
import pandas as pd


path = 'clientPortfolio.csv'
#extracting the latest stock prices, compare to user input and notificate
def stockAlarm():
    tickersMap = loadPortfolio()
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
            rangeValue = tmpEntryPrice * 1.5 / 100  # 1.5% below or above to entryPrice
            if tmpEntryPrice - rangeValue <= lastPrices[i] <= tmpEntryPrice + rangeValue:
                alert(symbol,formatPrice,"reached your entry price")
            
            
            elif lastPrices[i] >= tickersMap.get(symbol).getProfitPrice():
                alert(symbol,formatPrice,"reached your take profit price")
               

        time.sleep(10)

# loading/creating the data csv
def loadPortfolio():
    stockList = {}
    try:
        df = pd.read_csv(path)
        createMapPortfolio(df, stockList)
        print("you already have a portfolio!)")
        checkPortfolio(df, stockList)
        return stockList
    except:
        print("Welcome! lets set your portfolio first...")
        df = pd.DataFrame(columns=['Ticker', 'EntryPrice', 'ProfitPrice'])
        setPortfolio(df,stockList)
    return stockList

# converting the data from csv to dictionary
def createMapPortfolio(df,stocks):
    for inedx, row in df.iterrows():
        ticker = row['Ticker']
        entryPrice = row['EntryPrice']
        profitPrice = row['ProfitPrice']
        newStock = Stock(ticker, float(entryPrice), float(profitPrice))
        stocks[ticker] = newStock


# creating the portfolio stockslist to be alerted, input validations
def setPortfolio(df, stockList):
    while (True):
        tickerStr = input("Enter your stock ticker: ").strip().upper()
        if tickerStr in stockList:
            changeVals(stockList,tickerStr)
            break
        entryPrice = input("Enter your entry price: ").strip()
        profitPrice = input("Enter your take profit price: ").strip()
        # validation checks
        if checkValid(entryPrice, profitPrice) and checkValidTicker(tickerStr):
            df.loc[len(df)] = [tickerStr,entryPrice,profitPrice]
        else:
            continue
        res = input("Another stock? y/n: ").strip().lower()
        if res != 'y':
            break
    df.to_csv(path, index=False)
    createMapPortfolio(df,stockList)


# if portfolio is already exist, check for actions
def checkPortfolio(df,stocksList):
    while(True):
        ans = input("would like to add/remove ticker? (a/r) or n)").strip()
        if ans != 'a' and ans != 'r' and ans != 'n':
            print("your answer is invalid, please try again")
            continue
        if(ans == 'a'):
            setPortfolio(df,stocksList)
            break
        elif(ans == 'r'):
            removeStock(df,stocksList)
            break
        break

# removing stock from portfolio
def removeStock(df,stockList):
    flag = True
    while(flag):
        ticker = input("which ticker would you like to remove? ").strip()
        print(df['Ticker'].values)
        if checkValidTicker(ticker) and ticker in df['Ticker'].values:
            for index, row in df.iterrows():
                if row['Ticker'] == ticker:
                    df = df.drop(df[df['Ticker'] == ticker].index)
                    stockList.pop(ticker)
                    df.to_csv(path, index=False)
                    flag = False
                    break
        else:
            # if df is empty -> setPortfolio
            if df.empty:
                print("your portfolio is empty")
                setPortfolio(df,stockList)
                break
            continue


# chacking validations of user sticker input, except only if .info is None
def checkValidTicker(ticker):
    tickerCheck = yf.Ticker(ticker)
    try:
        info = tickerCheck.info
        return True
    except:
        print("Ticker is not exist...please enter valid ticker")
        return False


#chackin validations of user inputs
def checkValid(entryPrice, profitPrice):
        try:
            float(profitPrice)
            float(entryPrice)
            return True
        except ValueError:
            print("Invalid input!. Please enter a valid number.")
            return False

            
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
