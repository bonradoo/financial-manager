from datetime import date
import pandas as pd, os, csv

#Type,Shop,Title,Amount
#inc,-,Income,Amount
#exp,Amazon,Jedzenie,Amount
def clear(): os.system('cls')

def saveToFile(line):
    try:
        thisMonth = date.today().strftime('%B')
        thisYear = date.today().strftime('%Y')

        filePath = './bin/log/' + str(thisYear)
        if not os.path.exists(filePath): os.makedirs(filePath)
        
        filePath = filePath + '/logFinance' + str(thisMonth) + '.csv'
        if not os.path.exists(filePath): 
            with open(filePath, 'w') as f: f.write('Type,Shop,Title,Amount\n')

        with open(filePath, 'r') as f:
            try:
                hasHeading = csv.Sniffer().has_header(f.read(1024))
                
            except csv.Error:
                hasHeading = False
                print('asdf')

        with open(filePath, 'a') as f:
            if hasHeading:
                f.write(','.join(line) + '\n')
            else:
                f.write('Type,Shop,Title,Amount\n')
                f.write(','.join(line) + '\n')
            
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
    yearArr = [str(i+1) + '. ' + os.listdir('./bin/log')[i] for i in range(len(os.listdir('./bin/log')))]
    for i in yearArr: print(i)
    yearChoice = input('Choice: ')
    for i in yearArr:
        if yearChoice == i[0]: 
            filePath = './bin/log/' + i.replace(yearChoice + '. ', '', 1) + '/'
            if os.listdir(filePath): 
                monthArr = [str(n+1) + '. ' + os.listdir(filePath)[n] for n in range(len(os.listdir(filePath)))]
            else:
                print('Empty directory')
                break

            for j in monthArr: print(j)
            monthChoice = input('Choice: ')
            for j in monthArr:
                if monthChoice == j[0]:
                    filePath = filePath + j.replace(monthChoice + '. ', '', 1)
    try:
        df = pd.read_csv(filePath, sep=',')
        clear()
        for i in yearArr:
            if yearChoice == i[0]: print(i.replace(yearChoice + '. ', '', 1), end=', ')
        for h in monthArr:
            if monthChoice == h[0]: print(h.replace(monthChoice + '. ', '', 1))
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
                saveToFile(addIncome())
            case '2':
                clear()
                saveToFile(addExpense())
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