#!/usr/bin/python3
import budget, invest, os, userControl

#fix pandas highliting
def clear(): os.system('cls')

def mainMenu():

    if os.path.exists('./bin/log/pass.txt'):
        if not os.stat('./bin/log/pass.txt').st_size == 0:
            while True:
                if userControl.checkCorrect():
                    # store hashed key in some variable (decode files only when needed)
                    break
                else:
                    print('Incorrect password')
        else:
            userControl.setPassword()            
    else:
        userControl.setPassword()

    clear()
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
    