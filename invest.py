from datetime import date
import pandas as pd
import os
import yfinance as yf
from matplotlib import pyplot as plt
import pendulum
import csv
import misc

#StockName,StartDate,BuyPrice,CloseDate,SellPrice,ProfitLoss,CurrentPrice
#CDProjketRed,01-01-2021,100,01-12-2022,150,50,132
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

def marketMenu():
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

def saveToFile(line):
    try:
        filePath = './bin/stock/logInvestement.txt'
        #StockName,StartDate,BuyPrice,CloseDate,SellPrice,ProfitLoss,CurrentPrice
        if not os.path.exists(filePath): 
            with open(filePath, 'w') as f: 
                f.write('Stock Name,Start Date,Buy Amount,Buy Price,Close Date,Sell Amount,Sell Price,Profit/Loss\n')

        with open(filePath, 'r') as f:
            try:
                hasHeading = csv.Sniffer().has_header(f.read(1024))
            except csv.Error:
                print('Error')
                hasHeading = False

        with open(filePath, 'a') as f:
            if hasHeading:
                f.write(','.join(line) + '\n')
            else:
                f.write('Stock Name,Start Date,Buy Amount,Buy Price,Close Date,Sell Amount,Sell Price,Profit/Loss\n')
                f.write(','.join(line) + '\n')
    except:
        print('Error occured while saving the file')

#Stock Name, Start Date, Buy Amount, Buy Price, Close Date, Sell Amount, Sell Price, Profit / Loss
def addInv():
    stockName = input('Stock ticker: ')
    buyDate = input('Start date: ')
    buyAmount = input('Stock amount: ')
    buyPrice = input('Individual stock price: ')
    saveToFile([stockName, buyDate, buyAmount, buyPrice, '-', '-', '-', '-'])
    clear()

def closeInv():
    stockName = input('Stock ticker: ')
    sellDate = input('End date: ')
    sellAmount = input('Stock amount: ')
    sellPrice = input('Individual stock price: ')

def calcPortfolio():
    filePath = './bin/stock/logInvestement.txt'
    if not os.path.exists(filePath): 
        print('No file to show portfolio from')
        return
    with open(filePath, 'r') as file:
        lines = file.read()
        print(lines)

def printInv():
    filePath = './bin/stock/logInvestement.txt'

    with open(filePath, 'r') as file:
        frames = [line.strip('\n') for line in file]
    elements = [i.split(',') for i in frames]

    res = [[elements[0][i], elements[1][i]] for i in range(len(elements[0]))]

    resDict = {}
    for i in res:
        misc.addToDict(resDict, i[0], i[1:]) 
    
    df = pd.DataFrame(resDict)
    print(df)
    

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
                marketMenu()
            case '5':
                clear()
                return
            case _:
                print('Incorrect choice')


def main():
    pass

if __name__ == '__main__':
    main()