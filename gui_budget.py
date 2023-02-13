import tkinter
import customtkinter
import os
from datetime import date, timedelta

# Main file path
filePath = './bin/log/'

# Function clearing entries
def clearEntry(shop, title, amount):
    shop.delete()
    title.delete()
    amount.delete()

# Function checking if provided number is float
def isNumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
# Function Saving to file
def saveToFile(line):
    try:
        # File path config
        thisMonth = date.today().strftime('%B')
        thisYear = date.today().strftime('%Y')
        filePath = './bin/log/' + str(thisYear)
        if not os.path.exists(filePath): os.makedirs(filePath)
        filePath = filePath + '/' + str(thisMonth) + '.txt'

        # Checking formatting
        if line[0]=='' or line[2]=='':
            if not line[3].isNumber() or line[3]=='':
                print('Unable to save')
                return
        if line[1] == '': line[1] = '-'

        # Checking if file exists
        if not os.path.exists(filePath): 
            with open(filePath, 'w') as f: 
                f.write('Type,Shop,Title,Amount\n')

        # Checking if file has heading
        with open(filePath, 'r') as f:
            if f.readline() == 'Type,Shop,Title,Amount\n': hasHeading = True
            else: hasHeading = False

        with open(filePath, 'a', encoding='utf-8') as f:
            if hasHeading:
                f.write(','.join(line) + '\n')
            else:
                f.write('Type,Shop,Title,Amount\n')
                f.write(','.join(line) + '\n')   
    except:
        print('Error occured while saving the file')


# Create files depending on current year and month
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


# Main budget frame
def addLog(app):
    createFiles()

    # creating frames
    frame = customtkinter.CTkFrame(app, width=250, height=490, corner_radius=10)
    summaryFrame = customtkinter.CTkFrame(app, width=710, height=490, corner_radius=10)

    # Placing frames
    frame.place(relx=0.135, rely=0.5, anchor=tkinter.CENTER)
    summaryFrame.place(relx=0.63, rely=0.5, anchor=tkinter.CENTER)

    def getYear():
        return [os.listdir(filePath)[i] for i in range(len(os.listdir(filePath)))]
    def getMonth():
        return [os.listdir(filePath)[i] for i in range(len(os.listdir(filePath)))]
    
    def yearChoice(event):
        global filePath
        filePath = './bin/log/'
        filePath += yearVal.get() + '/'

    def monthChoice():
        global filePath
        embFP = filePath
        embFP += monthVal.get()
        printTotals(summaryFrame, embFP)
        

    # Creating CTk assets
    yearVal = customtkinter.StringVar(value=getYear()[0])
    monthVal = customtkinter.StringVar(value='Month')
    yearCombo = customtkinter.CTkComboBox(frame, values=getYear(), width=230, height=50, corner_radius=10, variable=yearVal, state='readonly',
                                        command=lambda event: [yearChoice(event), unlockMonth(event)])
    monthCombo = customtkinter.CTkComboBox(frame, values=getMonth(), width=230, height=50, corner_radius=10, variable=monthVal, state='disabled',
                                        command=lambda event: [monthChoice()])

    # Placing CTk assets
    yearCombo.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)
    monthCombo.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)

    # Function for unlocking month choice
    def unlockMonth(event):
        monthCombo.configure(state='readonly', values=getMonth())
        monthCombo.set(getMonth()[0])

    # Creating CTk entries
    shop = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Shop")
    title = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Title")
    amount = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Amount (float with '.')")

    # Placing CTk entries
    amount.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)
    shop.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    title.place(relx=0.5, rely=0.64, anchor=tkinter.CENTER)

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

    # Save button action
    def saveAction():
        saveToFile([typeVar.get(), shop.get(), title.get(), amount.get()])
        shop.delete(0, 'end')
        title.delete(0, 'end')
        amount.delete(0, 'end')
        printTotals(summaryFrame,filePath + monthVal.get())
        shop.focus()
        print('2')
    
    saveButton = customtkinter.CTkButton(frame, text='Save', width=230, height=50, command=saveAction)
    saveButton.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)


# Function for totals
def printTotals(frame, embFP):
    # Creating totals CTk frames
    expFrame = customtkinter.CTkFrame(frame, width=220, height=50, corner_radius=10)
    incFrame = customtkinter.CTkFrame(frame, width=220, height=50, corner_radius=10)
    balFrame = customtkinter.CTkFrame(frame, width=220, height=50, corner_radius=10)

    # Placing totals CTk frames
    expFrame.place(relx=0.172, rely=0.07, anchor=tkinter.CENTER)
    incFrame.place(relx=0.499, rely=0.07, anchor=tkinter.CENTER)
    balFrame.place(relx=0.826, rely=0.07, anchor=tkinter.CENTER)

    # Calculate totals
    with open(embFP, 'r', encoding='utf-8') as file:
        data = file.readlines()
    frames = []
    for line in data: frames.append(line.strip('\n'))
    elements = [i.split(',') for i in frames]
    totalInc = 0.00
    totalExp = 0.00
    for i in elements:
        if i[0] == 'inc': 
            totalInc += float(i[3])
            totalInc = round(totalInc, 2)
        elif i[0] == 'exp': 
            totalExp += float(i[3])
            totalExp = round(totalExp, 2)
    
    # Expense
    titleFont = customtkinter.CTkFont(family='Arial', size=12, weight='bold')
    totalExpTitle = customtkinter.CTkLabel(expFrame, width=50, height=32, text='Total expense: ', font=titleFont)
    totalExpTitle.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

    tev = customtkinter.StringVar(expFrame, value=str(round(totalExp, 3)))
    totalExpValue = customtkinter.CTkLabel(expFrame, width=50, height=30, text=tev.get()+' PLN', font=('Arial', 12))
    totalExpValue.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    # Income
    totalIncTitle = customtkinter.CTkLabel(incFrame, width=50, height=32, text='Total income: ', font=titleFont)
    totalIncTitle.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

    tiv = customtkinter.StringVar(incFrame, value=str(round(totalInc, 3)))
    totalIncValue = customtkinter.CTkLabel(incFrame, width=50, height=30, text=tiv.get()+' PLN', font=('Arial', 12))
    totalIncValue.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    # Balance
    totalBalTtile = customtkinter.CTkLabel(balFrame, width=50, height=32, text='Balance: ', font=titleFont)
    totalBalTtile.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

    tbv = customtkinter.StringVar(balFrame, value=str(round(float(totalInc-totalExp), 3)))
    totalBalValue = customtkinter.CTkLabel(balFrame, width=50, height=30, text=tbv.get()+' PLN', font=('Arial', 12))
    totalBalValue.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)


# Fuction that prints table of expenses and income
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

if __name__ == '__main__':
    pass