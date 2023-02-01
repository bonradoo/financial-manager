import tkinter
import customtkinter
import os
import pandas as pd
from pandastable import Table



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

        if line[0]=='' or line[2]=='':
            if not line[3].isNumber() or line[3]=='':
                print('Unable to save')
                return

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
    frame.place(relx=0.5, rely=0.07, anchor=tkinter.CENTER)

    shop = customtkinter.CTkEntry(frame, width=150, placeholder_text="Shop")
    shop.place(relx=0.32, rely=0.5, anchor=tkinter.CENTER)

    title = customtkinter.CTkEntry(frame, width=150, placeholder_text="Title")
    title.place(relx=0.53, rely=0.5, anchor=tkinter.CENTER)

    amount = customtkinter.CTkEntry(frame, width=150, placeholder_text="Amount (float with '.')")
    amount.place(relx=0.74, rely=0.5, anchor=tkinter.CENTER)

    typeVar = tkinter.StringVar()
    radiobutton_1 = customtkinter.CTkRadioButton(frame, text="Income", radiobutton_height=15, radiobutton_width=15, border_width_checked=5, width=30,
                                                variable=typeVar, value='inc', command=lambda: [shop.delete(0, 'end'), shop.configure(state='disabled', fg_color='#191922')])
    radiobutton_1.place(relx=0.16, rely=0.5, anchor=tkinter.CENTER)

    radiobutton_2 = customtkinter.CTkRadioButton(frame, text="Expense", radiobutton_height=15, radiobutton_width=15, border_width_checked=5, width=30,
                                                variable=typeVar, value='exp', command=lambda: shop.configure(state='normal', fg_color='#343638'))
    radiobutton_2.place(relx=0.06, rely=0.5, anchor=tkinter.CENTER)
        
    printTotals(app)
    printBudget(app)

    saveButton = customtkinter.CTkButton(frame, text='Save', width=100, command=lambda:
                                [saveToFile([typeVar.get(), shop.get(), title.get(), amount.get()]), 
                                shop.delete(0, 'end'), title.delete(0, 'end'), amount.delete(0, 'end'),
                                printTotals(app)])
    
    # def checkEntry():
    #     if typeVar.get()=='' or shop.get()=='' or title.get()=='' or amount.get()=='': 
    #         saveButton.configure(state='disabled')
    #     else: 
    #         saveButton.configure(state='normal')
    saveButton.place(relx=0.92, rely=0.5, anchor=tkinter.CENTER)


def printTotals(frame):
    totalsFrame = customtkinter.CTkFrame(frame, width=740, height=50, corner_radius=10)
    totalsFrame.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    
    expFrame = customtkinter.CTkFrame(totalsFrame, width=200, height=40, corner_radius=10)
    expFrame.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

    incFrame = customtkinter.CTkFrame(totalsFrame, width=200, height=40, corner_radius=10)
    incFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    balFrame = customtkinter.CTkFrame(totalsFrame, width=200, height=40, corner_radius=10)
    balFrame.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

    def getExp():
        filePath = 'logs.txt'
        frames = []
        with open(filePath, 'r', encoding='utf-8') as file:
            for line in file: frames.append(line.strip('\n'))
        elements = [i.split(',') for i in frames]
        totalExp = 0
        for i in elements:
            if i[0] == 'exp': totalExp += float(i[3])
        return round(totalExp, 2)
    
    def getInc():
        filePath = 'logs.txt'
        frames = []
        with open(filePath, 'r', encoding='utf-8') as file:
            for line in file: frames.append(line.strip('\n'))
        elements = [i.split(',') for i in frames]
        totalInc = 0
        for i in elements:
            if i[0] == 'inc': totalInc += float(i[3])
        return round(totalInc, 2)
    
    titleFont = customtkinter.CTkFont(family='Arial', size=12, weight='bold')
    totalExpTitle = customtkinter.CTkLabel(expFrame, width=50, height=32, text='Total expense: ', font=titleFont)
    totalExpTitle.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

    tev = customtkinter.StringVar(expFrame, value=str(getExp()))
    totalExpValue = customtkinter.CTkLabel(expFrame, width=50, height=30, text=tev.get()+' PLN', font=('Arial', 12))
    totalExpValue.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    totalIncTitle = customtkinter.CTkLabel(incFrame, width=50, height=32, text='Total income: ', font=titleFont)
    totalIncTitle.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

    tiv = customtkinter.StringVar(incFrame, value=str(getInc()))
    totalIncValue = customtkinter.CTkLabel(incFrame, width=50, height=30, text=tiv.get()+' PLN', font=('Arial', 12))
    totalIncValue.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

def printBudget(frame):
    insideFrame = customtkinter.CTkFrame(frame, width=740, height=250, corner_radius=10)
    insideFrame.place(relx=0.02, rely=0.4)

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
    
    # df = pd.DataFrame(resDict)
    # pt = Table(insideFrame, dataframe=df,showtoolbar=False, showstatusbar=False)
    # pt.show()


def main():
    pass

if __name__ == '__main__':
    main()