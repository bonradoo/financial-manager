#!/usr/bin/python3
import budget, invest, os

#fix pandas highliting
def clear(): os.system('cls')

def highlight_rows(row):
    value = row.loc['Type']
    if value == 'Python': color = '#FFB3BA' # Red
    elif value == 'inc': color = '#BAFFC9' # Green
    else: color = '#BAE1FF' # Blue
    return ['background-color: {}'.format(color) for r in row]

def mainMenu():
    while True:
        print('1. Add income')
        print('2. Add expense')
        print('3. Show balance')
        print('4. Start investement')
        print('5. Close investement')
        print('6. Show investements')
        print('7. Quit')
        print('----------------')
        choice = input('Choice: ')
        match choice:
            case '1':
                clear()
                budget.saveToFile(budget.addIncome())
            case '2':
                clear()
                budget.saveToFile(budget.addExpense())
            case '3':
                clear()
                budget.printBalance()
            case '4':
                clear()
                invest.saveToFile(invest.addInv())
            case '5':
                clear()
            case '6':
                invest.printInv()
            case '7':
                quit()
            case _:
                print('Incorrect choice')
        
def main():
    mainMenu()
    
if __name__ == '__main__':
    main()
    