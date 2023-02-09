import tkinter
import customtkinter
import os
import pandas as pd
from pandastable import Table
from datetime import datetime, date, timedelta

filePath = './bin/log/'

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
        thisMonth = date.today().strftime('%B')
        thisYear = date.today().strftime('%Y')

        filePath = './bin/log/' + str(thisYear)
        if not os.path.exists(filePath): os.makedirs(filePath)
        
        filePath = filePath + '/' + str(thisMonth) + '.txt'

        if line[0]=='' or line[2]=='':
            if not line[3].isNumber() or line[3]=='':
                print('Unable to save')
                return

        if line[1] == '': line[1] = '-'

        # print(line)
        # print(filePath)
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


def createFiles():
    thisYear = date.today().year
    filePath = './bin/log/' + str(thisYear)
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    today = date.today()
    lastDayMonth = (date(today.year, today.month, 1) + timedelta(days=32) - timedelta(days=1)).day
    for day in range(1, lastDayMonth + 1):
        current_date = date(today.year, today.month, day)
        file_name = current_date.strftime('%B') + '.txt'
        fp = os.path.join(filePath, file_name)
        
        # Check if file for the current month already exists
        if not os.path.exists(fp):
            with open(fp, 'w') as file:
                file.write('Type,Shop,Title,Amount\n')



def addLog(app):
    createFiles()

    # creating frames
    frame = customtkinter.CTkFrame(app, width=250, height=490, corner_radius=10)
    frame.place(relx=0.135, rely=0.5, anchor=tkinter.CENTER)

    summaryFrame = customtkinter.CTkFrame(app, width=710, height=490, corner_radius=10)
    summaryFrame.place(relx=0.63, rely=0.5, anchor=tkinter.CENTER)


    def getYear():
        return [os.listdir(filePath)[i] for i in range(len(os.listdir(filePath)))]
    def getMonth():
        return [os.listdir(filePath)[i] for i in range(len(os.listdir(filePath)))]
    
    def yearChoice(event):
        global filePath
        filePath = './bin/log/'
        filePath += yearVal.get() + '/'
        # print(filePath)

    def monthChoice():
        global filePath
        embFP = filePath
        embFP += monthVal.get()
        printTotals(summaryFrame, embFP)
        


    yearVal = customtkinter.StringVar(value=getYear()[0])
    monthVal = customtkinter.StringVar(value='Month')


    yearCombo = customtkinter.CTkComboBox(frame, values=getYear(), width=230, height=50, corner_radius=10, variable=yearVal, state='readonly',
                                        command=lambda event: [yearChoice(event), unlockMonth(event)])
    monthCombo = customtkinter.CTkComboBox(frame, values=getMonth(), width=230, height=50, corner_radius=10, variable=monthVal, state='disabled',
                                        command=lambda event: [monthChoice()])

    yearCombo.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)
    monthCombo.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)

    def unlockMonth(event):
        # print(filePath)
        monthCombo.configure(state='readonly', values=getMonth())
        monthCombo.set(getMonth()[0])

    shop = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Shop")
    shop.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    title = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Title")
    title.place(relx=0.5, rely=0.64, anchor=tkinter.CENTER)

    amount = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Amount (float with '.')")
    amount.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

    typeVar = tkinter.StringVar()
    def segChoice(value):
        if value == '        Income       ': 
            shop.delete(0, 'end')
            shop.configure(state='disabled', fg_color='#191922', placeholder_text='')
            typeVar.set('inc')
        elif value == '       Expense        ': 
            shop.configure(state='normal', fg_color='#343638', placeholder_text='Shop')
            typeVar.set('exp')

    segmentedButton = customtkinter.CTkSegmentedButton(frame, values=['        Income       ', '       Expense        '], width=230, height=50, corner_radius=10, command=segChoice)
    segmentedButton.set('Expense')
    segmentedButton.place(relx=0.5, rely=0.36, anchor=tkinter.CENTER)


    printBudget(summaryFrame)

    saveButton = customtkinter.CTkButton(frame, text='Save', width=230, height=50, command=lambda:
                                [saveToFile([typeVar.get(), shop.get(), title.get(), amount.get()]), 
                                shop.delete(0, 'end'), title.delete(0, 'end'), amount.delete(0, 'end'),
                                printTotals(summaryFrame, filePath + monthVal.get()), shop.icursor()])

    saveButton.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)


def printTotals(frame, embFP):
    expFrame = customtkinter.CTkFrame(frame, width=220, height=50, corner_radius=10)
    expFrame.place(relx=0.172, rely=0.08, anchor=tkinter.CENTER)

    incFrame = customtkinter.CTkFrame(frame, width=220, height=50, corner_radius=10)
    incFrame.place(relx=0.499, rely=0.08, anchor=tkinter.CENTER)

    balFrame = customtkinter.CTkFrame(frame, width=220, height=50, corner_radius=10)
    balFrame.place(relx=0.826, rely=0.08, anchor=tkinter.CENTER)

    print(embFP)
    with open(embFP, 'r') as file:
        data = file.readlines()

    frames = []
    for line in data: frames.append(line.strip('\n'))
    elements = [i.split(',') for i in frames]
    totalInc = 0
    totalExp = 0
    for i in elements:
        if i[0] == 'inc': totalInc += float(i[3])
        elif i[0] == 'exp': totalExp += float(i[3])
    
    # Expense
    titleFont = customtkinter.CTkFont(family='Arial', size=12, weight='bold')
    totalExpTitle = customtkinter.CTkLabel(expFrame, width=50, height=32, text='Total expense: ', font=titleFont)
    totalExpTitle.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

    tev = customtkinter.StringVar(expFrame, value=str(round(totalExp, 2)))
    totalExpValue = customtkinter.CTkLabel(expFrame, width=50, height=30, text=tev.get()+' PLN', font=('Arial', 12))
    totalExpValue.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    # Income
    totalIncTitle = customtkinter.CTkLabel(incFrame, width=50, height=32, text='Total income: ', font=titleFont)
    totalIncTitle.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

    tiv = customtkinter.StringVar(incFrame, value=str(round(totalInc, 2)))
    totalIncValue = customtkinter.CTkLabel(incFrame, width=50, height=30, text=tiv.get()+' PLN', font=('Arial', 12))
    totalIncValue.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    # Balance
    totalBalTtile = customtkinter.CTkLabel(balFrame, width=50, height=32, text='Balance: ', font=titleFont)
    totalBalTtile.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

    tbv = customtkinter.StringVar(balFrame, value=str(round(float(totalInc-totalExp), 2)))
    totalBalValue = customtkinter.CTkLabel(balFrame, width=50, height=30, text=tbv.get()+' PLN', font=('Arial', 12))
    totalBalValue.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    



def printBudget(frame):
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
    # pt = Table(frame, dataframe=df,showtoolbar=False, showstatusbar=False)
    # pt.show()


def main():
    pass

if __name__ == '__main__':
    main()