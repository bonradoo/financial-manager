#!/usr/bin/python3
import budget, invest, os

#fix pandas highliting
def clear(): os.system('cls')

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
    