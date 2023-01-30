import tkinter
import customtkinter
import os
import pandas as pd
import pandastable


def clearEntry(shop, title, amount):
    shop.delete()
    title.delete()
    amount.delete()


def isNumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    

def saveToFile(line):
    try:
        # thisMonth = date.today().strftime('%B')
        # thisYear = date.today().strftime('%Y')

        # filePath = './bin/log/' + str(thisYear)
        # if not os.path.exists(filePath): os.makedirs(filePath)
        
        # filePath = filePath + '/logFinance' + str(thisMonth) + '.txt'

        if line[1] == '': line[1] = '-'

        filePath = 'logs.txt'   #for testing purpose
        if not os.path.exists(filePath): 
            with open(filePath, 'w') as f: 
                f.write('Type,Shop,Title,Amount\n')

        with open(filePath, 'r') as f:
            if f.readline() == 'Type,Shop,Title,Amount\n':
                hasHeading = True
            else:
                print('No header')
                hasHeading = False

        with open(filePath, 'a', encoding='utf-8') as f:
            if hasHeading:
                f.write(','.join(line) + '\n')
            else:
                f.write('Type,Shop,Title,Amount\n')
                f.write(','.join(line) + '\n')
            
    except:
        print('Error occured while saving the file')


def addLog(app):
    frame = customtkinter.CTkFrame(app, width=740, height=50, corner_radius=10)
    frame.place(relx=0.02, rely=0.01)

    shop = customtkinter.CTkEntry(frame, width=150, placeholder_text="Shop")
    shop.place(relx=0.33, rely=0.47, anchor=tkinter.CENTER)

    title = customtkinter.CTkEntry(frame, width=150, placeholder_text="Title")
    title.place(relx=0.53, rely=0.47, anchor=tkinter.CENTER)

    amount = customtkinter.CTkEntry(frame, width=150, placeholder_text="Amount (float with '.')")
    amount.place(relx=0.73, rely=0.47, anchor=tkinter.CENTER)

    typeVar = tkinter.StringVar()
    radiobutton_1 = customtkinter.CTkRadioButton(frame, text="Income", radiobutton_height=15, radiobutton_width=15, border_width_checked=5, width=30,
                                                variable=typeVar, value='inc', command=lambda: shop.configure(state='disabled', fg_color='#191922'))
    radiobutton_1.place(relx=0.13, rely=0.28)

    radiobutton_2 = customtkinter.CTkRadioButton(frame, text="Expense", radiobutton_height=15, radiobutton_width=15, border_width_checked=5, width=30,
                                                variable=typeVar, value='exp', command=lambda: shop.configure(state='normal', fg_color='#343638'))
    radiobutton_2.place(relx=0.02, rely=0.28)
        
    button = customtkinter.CTkButton(frame, text='Save', width=100, command=lambda:
                                    [saveToFile([typeVar.get(), shop.get(), title.get(), amount.get()]), 
                                    shop.delete(0, 'end'), title.delete(0, 'end'), amount.delete(0, 'end')])
    button.place(relx=0.92, rely=0.47, anchor=tkinter.CENTER)

    printBudget(app)

def printBudget(frame):
    insideFrame = customtkinter.CTkFrame(frame, width=740, height=250, corner_radius=10)
    insideFrame.place(relx=0.02, rely=0.4)

    textbox = customtkinter.CTkTextbox(insideFrame, width=600, height=200)
    textbox.place(relx=0.02, rely=0.1)

    # dic = {'name': 'jan pawel ii', 'date': '2137', 'real': 'karol wojtyla'}
    # df = pd.DataFrame(dic)
    # textbox.insert('0.3', 'Amount\t\t')
    # textbox.insert('0.2', 'Title\t\t')
    # textbox.insert('0.1', 'Shop\t\t')
    # textbox.insert('0.0', 'Type\t\t')

    # textbox.insert('1.3', '1000\t\t')
    # textbox.insert('1.2', 'Wypłata\t\t')
    # textbox.insert('1.1', '-\t\t')
    # textbox.insert('1.0', 'inc\t\t')



    def addToDict(sample_dict, key, list_of_values):
        if key not in sample_dict.keys():
            sample_dict[key] = list()
        sample_dict[key].extend(list_of_values)
        return sample_dict

    filePath = 'logs.txt'

    frames = []
    with open(filePath, 'r', encoding='utf-8') as file:
        for line in file: frames.append(line.strip('\n'))
    elements = [i.split(',') for i in frames]

    res = []
    for j in range(3):
        temp = []
        for i in range(len(elements)):
            temp.append(elements[i][j])
        res.append(temp)

    resDict = {}
    for i in res:
        addToDict(resDict, i[0], i[1:]) 

    # print(resDict)
    
    # df = pd.DataFrame(resDict)
    # print(df)

    



    for i in range(5):
        textbox.insert(str(i) + '.0','\n')
        for j in range(4):
            textbox.insert(str(i) + '.' + str(j), 'Amount\t\t')
    
    # textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
    # text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

    textbox.configure(state="disabled") 


def main():
    pass

if __name__ == '__main__':
    main()