from datetime import date
import pandas as pd

#Type,Shop,Title,Amount
#inc,-,Income,Amount
#exp,Amazon,Jedzenie,Amount

def saveToFile(line):
    thisMonth = date.today().strftime('%B')
    filePath = './bin/log/logFinance' + str(thisMonth) + '.csv'
    with open(filePath, 'a') as f: f.write(','.join(line) + '\n')

def addIncome():
    while True:
        incTitle = input('Income title: ')
        incAmount = input('Income amount: ')
        if ((incAmount.replace('.', '', 1)).replace(',', '', 1)).isdigit(): return['inc', '-', incTitle, "\"" + incAmount.replace('.', ',', 1) + "\""]
        else: print('Incorrect input. Try again')

def addExpense():
    while True:
        expTitle = input('Expense title: ')
        expPlace = input('Expense place: ')
        expAmount = input('Expense amount: ')
        if ((expAmount.replace('.', '', 1)).replace(',', '', 1)).isdigit(): return['exp', expPlace, expTitle, "\"" + expAmount.replace('.', ',', 1) + "\""]
        else: print('Incorrect input. Try again')

def printBalance():
    thisMonth = date.today().strftime('%B')
    filePath = './bin/log/logFinance' + str(thisMonth) + '.csv'
    df = pd.read_csv(filePath, sep=',')
    #df.style.apply(highlight_rows, axis=1)
    print(df, end='\n\n')

def main():
    pass

if __name__ == '__main__':
    main()