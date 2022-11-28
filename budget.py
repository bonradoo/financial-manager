
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

def main():
    pass

if __name__ == '__main__':
    main()