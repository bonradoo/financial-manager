from datetime import date
import pandas as pd

#StockName,StartDate,BuyPrice,CloseDate,SellPrice,ProfitLoss
#CDProjketRed,01-01-2021,100,01-12-2022,150,50

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

def main():
    pass

if __name__ == '__main__':
    main()