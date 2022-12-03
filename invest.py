from datetime import date
import pandas as pd, os

#StockName,StartDate,BuyPrice,CloseDate,SellPrice,ProfitLoss
#CDProjketRed,01-01-2021,100,01-12-2022,150,50
def clear(): os.system('cls')

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
        print('4. Return')
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
                return
            case _:
                print('Incorrect choice')


def main():
    pass

if __name__ == '__main__':
    main()