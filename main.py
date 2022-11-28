#!/usr/bin/python3
import budget, invest, os
from datetime import date
import pandas as pd

#fix pandas highliting

#Type,Shop,Title,Amount
#inc,-,Income,Amount
#exp,Amazon,Jedzenie,Amount
def clear(): os.system('cls')

def highlight_rows(row):
    value = row.loc['type']
    if value == 'Python': color = '#FFB3BA' # Red
    elif value == 'inc': color = '#BAFFC9' # Green
    else: color = '#BAE1FF' # Blue
    return ['background-color: {}'.format(color) for r in row]

def saveToFile(line):
    thisMonth = date.today().strftime('%B')
    filePath = 'logFinance' + str(thisMonth) + '.csv'
    with open(filePath, 'a') as f:
        f.write(','.join(line) + '\n')

def printBalance():
    thisMonth = date.today().strftime('%B')
    filePath = 'logFinance' + str(thisMonth) + '.csv'
    df = pd.read_csv(filePath, sep=',')
    #df.style.apply(highlight_rows, axis=1)
    print(df, end='\n\n')

def mainMenu():
    while True:
        print('1. Add income')
        print('2. Add expense')
        print('3. Show balance')
        print('4. Quit')
        print('----------------')
        choice = input('Choice: ')
        match choice:
            case '1':
                clear()
                saveToFile(budget.addIncome())
            case '2':
                clear()
                saveToFile(budget.addExpense())
            case '3':
                clear()
                printBalance()
            case '4':
                quit()
            case _:
                print('Incorrect choice')
        

def main():
    mainMenu()
    

if __name__ == '__main__':
    main()
    