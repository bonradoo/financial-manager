#!/usr/bin/python3
from datetime import date
import os
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

def addIncome():
    while True:
        incTitle = input('Income title: ')
        incAmount = input('Income amount: ')
        if incAmount.isnumeric(): return['inc', '-', incTitle, incAmount]
        else: print('Incorrect input. Try again')

def addExpense():
    while True:
        expTitle = input('Expense title: ')
        expPlace = input('Expense place: ')
        expAmount = input('Expense amount: ')
        if expAmount.isnumeric(): return['exp', expPlace, expTitle, expAmount]
        else: print('Incorrect input. Try again')

def saveToFile(line):
    thisMonth = date.today().strftime('%B')
    filePath = 'logFinance' + str(thisMonth) + '.csv'
    with open(filePath, 'a') as f:
        f.write(','.join(line) + '\n')

def printBalance():
    thisMonth = date.today().strftime('%B')
    filePath = 'logFinance' + str(thisMonth) + '.csv'
    df = pd.read_csv(filePath, sep=',')
    df.style.apply(highlight_rows, axis=1)
    print(df)

def budgetMenu():
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
                saveToFile(addIncome())
            case '2':
                clear()
                saveToFile(addExpense())
            case '3':
                clear()
                printBalance()
            case '4':
                quit()
            case _:
                print('Incorrect choice')
        

def main():
    budgetMenu()
    

if __name__ == '__main__':
    main()
    