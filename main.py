#!/usr/bin/python3
from datetime import date
import pandas as pd

#fix pandas highliting

#Type,Shop,Title,Amount
#inc,NaN,Income,Amount
#exp,Amazon,Jedzenie,Amount

def highlight_rows(row):
    value = row.loc['type']
    if value == 'Python': color = '#FFB3BA' # Red
    elif value == 'inc': color = '#BAFFC9' # Green
    else: color = '#BAE1FF' # Blue
    return ['background-color: {}'.format(color) for r in row]

def addIncome():
    pass

def addExpense():
    pass

def saveToFile(line):
    thisMonth = date.today().strftime('%B')
    filePath = 'logFinance' + str(thisMonth) + '.csv'
    with open(filePath, 'a') as f:
        f.write(','.join(line) + '\n')

def printBalance():
    thisMonth = date.today().strftime('%B')
    filePath = 'logFinance' + str(thisMonth) + '.csv'
    df = pd.read_csv(r'example.csv', sep=',')
    df.style.apply(highlight_rows, axis=1)
    print(df)

def main():
    #saveToFile(['Amazon', 'Food', str(130.12)])
    printBalance()
    

if __name__ == '__main__':
    main()
    