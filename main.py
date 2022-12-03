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
        print('1. Budget menu')
        print('2. Investement menu')
        print('3. Quit')
        print('----------------')
        choice = input('Choice: ')
        match choice:
            case '1':
                clear()
                budget.budgetMenu()
            case '2':
                clear()
                invest.investMenu()
            case '3':
                clear()
                quit()
            case _:
                print('Incorrect choice')
        
def main():
    mainMenu()
    
if __name__ == '__main__':
    main()
    