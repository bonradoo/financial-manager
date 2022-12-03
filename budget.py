from datetime import date
import pandas as pd, os

#Type,Shop,Title,Amount
#inc,-,Income,Amount
#exp,Amazon,Jedzenie,Amount
def clear(): os.system('cls')

def saveToFile(line):
    try:
        thisMonth = date.today().strftime('%B')
        filePath = './bin/log/logFinance' + str(thisMonth) + '.csv'
        with open(filePath, 'a') as f: f.write(','.join(line) + '\n')
    except:
        print('Error occured while saving the file')

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
    print('Choose file: ')
    for i in range(len(os.listdir('./bin/log'))): print(str(i+1) + '.', os.listdir('./bin/log')[i])


    try:
        thisMonth = date.today().strftime('%B')
        filePath = './bin/log/logFinance' + str(thisMonth) + '.csv'
        df = pd.read_csv(filePath, sep=',')
        #df.style.apply(highlight_rows, axis=1)
        print(df, end='\n\n')
    except:
        print('Error occured while trying to open the file')

def budgetMenu():
    while True:
        print('1. Add income')
        print('2. Add expense')
        print('3. Show balance')
        print('4. Return')
        print('----------------')
        choice = input('Choice: ')
        match choice:
            case '1':
                clear()
                addIncome()
            case '2':
                clear()
                addExpense()
            case '3':
                clear()
                printBalance()
            case '4':
                clear()
                return
            case _:
                print('Incorrect choice')

def main():
    pass

if __name__ == '__main__':
    main()