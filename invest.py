from datetime import date, timedelta
import pandas as pd, os
import yfinance as yf
from matplotlib import pyplot as plt
import pendulum

#StockName,StartDate,BuyPrice,CloseDate,SellPrice,ProfitLoss
#CDProjketRed,01-01-2021,100,01-12-2022,150,50
def clear(): os.system('cls')

def checkStockPrice():
    tickerName = 'CDR.WA'
    stockInfo = yf.Ticker(tickerName).info
    # stockInfo.keys() for other properties you can explore
    marketPrice = stockInfo['regularMarketPrice']
    previousClosePrice = stockInfo['regularMarketPreviousClose']
    print(tickerName, 'market price: ', marketPrice)
    print(tickerName, 'previous close price: ', previousClosePrice, '\n')

def showStockGraph():
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    price_history = yf.Ticker('CDR.WA').history(period='1mo', interval='1d', actions=False)
    time_series = list(price_history['Open'])
    dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]
    plt.style.use('dark_background')
    plt.plot(dt_list, time_series, linewidth=2)
    plt.show()

def stockMenu():
    while True:
        print('1. Add stock tickers')
        print('2. Check stock prices')
        print('3. Show graph')
        print('4. Return')
        print('----------------')
        choice = input('Choice: ')


        match choice:
            case '1':
                clear()
            case '2':
                clear()
                checkStockPrice()
            case '3':
                clear()
                showStockGraph()
            case '4':
                clear()
                return
            case _:
                print('Inccorrect choice')



    # filePath = './bin/stock/tickers.txt'
    # if not os.path.exists(filePath): 
    #         with open(filePath, 'w') as f:
    #             pass
    

def saveToFile(line):
    thisMonth = date.today().strftime('%B')
    filePath = './bin/log/logInvestements' + str(thisMonth) + '.csv'
    with open(filePath, 'a') as f: f.write(','.join(line) + '\n')

def addInv():
    stockName = input('Stock name: ')
    startDate = input('Start date: ')
    buyPrice = input('Buy price: ')
    return (['CDProjketRed', '01-01-2021', '100'])

def closeInv():
    pass

def printInv():
    thisMonth = date.today().strftime('%B')
    filePath = './bin/log/logInvestements' + str(thisMonth) + '.csv'
    df = pd.read_csv(filePath, sep=',')
    print(df, end='\n\n')

def investMenu():
    while True:
        print('1. Start investement')
        print('2. Close investement')
        print('3. Show investements')
        print('4. Check stocks')
        print('5. Return')
        print('----------------')
        choice = input('Choice: ')
        match choice:
            case '1':
                clear()
                addInv()
            case '2':
                clear()
                closeInv()
            case '3':
                clear()
                printInv()
            case '4':
                clear()
                stockMenu()
            case '5':
                clear()
                return
            case _:
                print('Incorrect choice')


def main():
    checkStockPrice()

if __name__ == '__main__':
    main()