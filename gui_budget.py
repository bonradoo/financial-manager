import tkinter
import customtkinter
import os
from datetime import date, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict

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
        if line[0]=='' or line[1]=='' or line[2]=='' or line[3]=='':
            if not line[3].isNumber():
                print('Unable to save')
                return
            return
        line[3] = str(line[3]).replace(',', '.')

        # Checking if file exists
        if not os.path.exists(filePath): 
            with open(filePath, 'w') as f:
                print(1)
                f.write('Type,Place,Title,Amount\n')

        # Checking if file has heading
        with open(filePath, 'r') as f:
            if f.readline() == 'Type,Place,Title,Amount\n':
                hasHeading = True
            else:
                hasHeading = False

        with open(filePath, 'a', encoding='utf-8') as f:
            if hasHeading:
                f.write(','.join(line) + '\n')
            else:
                f.write('Type,Place,Title,Amount\n')
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
                file.write('Type,Place,Title,Amount\n')

# Main budget frame
def addLog(app):
    createFiles()

    # Create main frames
    frame = customtkinter.CTkFrame(app, width=250, height=490, corner_radius=10)
    summaryFrame = customtkinter.CTkFrame(app, width=710, height=490, corner_radius=10)

    # Create frames for records summary
    recordsFrame = customtkinter.CTkScrollableFrame(summaryFrame, width=322, height=397)
    graphFrame = customtkinter.CTkFrame(summaryFrame, width=340, height=410)

    # Creating totals CTk frames
    expFrame = customtkinter.CTkFrame(summaryFrame, width=220, height=50, corner_radius=10)
    incFrame = customtkinter.CTkFrame(summaryFrame, width=220, height=50, corner_radius=10)
    balFrame = customtkinter.CTkFrame(summaryFrame, width=220, height=50, corner_radius=10)

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
        printTotals(expFrame, incFrame, balFrame, embFP)
        printBudget(recordsFrame, graphFrame, embFP)
        

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
    place = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Place")
    title = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Title")
    amount = customtkinter.CTkEntry(frame, width=230, height=50, placeholder_text="Amount")

    # Placing CTk entries
    amount.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)
    place.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    title.place(relx=0.5, rely=0.64, anchor=tkinter.CENTER)

    # Segmented button function
    def segChoice(value):
        if value == '        Income       ': typeVar.set('inc')
        elif value == '       Expense        ': typeVar.set('exp')

    typeVar = tkinter.StringVar()
    segmentedButton = customtkinter.CTkSegmentedButton(frame, values=['        Income       ', '       Expense        '], 
                                                       width=230, height=50, corner_radius=10, command=segChoice)
    segmentedButton.place(relx=0.5, rely=0.36, anchor=tkinter.CENTER)

    

    # Save button action
    def saveAction():
        saveToFile([typeVar.get(), place.get(), title.get(), amount.get()])
        place.delete(0, 'end')
        title.delete(0, 'end')
        amount.delete(0, 'end')
        printTotals(expFrame, incFrame, balFrame, filePath + monthVal.get())
        printBudget(recordsFrame, graphFrame, filePath + monthVal.get())
        place.focus()
    
    saveButton = customtkinter.CTkButton(frame, text='Save', width=230, height=50, command=saveAction)
    saveButton.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)

# Function for totals
def printTotals(expFrame, incFrame, balFrame, embFP):
    # Forget prexisting frames
    expFrame.place_forget()
    incFrame.place_forget()
    balFrame.place_forget()

    # Placing totals CTk frames
    expFrame.place(relx=0.172, rely=0.07, anchor=tkinter.CENTER)
    incFrame.place(relx=0.499, rely=0.07, anchor=tkinter.CENTER)
    balFrame.place(relx=0.826, rely=0.07, anchor=tkinter.CENTER)

    # Clearing previous widgets
    for widgets in expFrame.winfo_children(): widgets.destroy()
    for widgets in incFrame.winfo_children(): widgets.destroy()
    for widgets in balFrame.winfo_children(): widgets.destroy()

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
def printBudget(recordsFrame, graphFrame, embFP):
    # Forget prexisting frames
    recordsFrame.place_forget()
    graphFrame.place_forget()

    # Placing frames
    recordsFrame.place(relx=0.743, rely=0.56, anchor=tkinter.CENTER)
    graphFrame.place(relx=0.25, rely=0.56, anchor=tkinter.CENTER)

    # Clearing prexisting widgets
    for widgets in recordsFrame.winfo_children(): widgets.destroy()
    for widgets in graphFrame.winfo_children(): widgets.destroy()

    frames = []
    with open(embFP, 'r', encoding='utf-8') as file:
        for line in file: frames.append(line.strip('\n'))
    elements = [i.split(',') for i in frames]
    elements = elements[1:]
    elements.reverse()
    
    # Creating CTk assets
    titleFrame = customtkinter.CTkFrame(recordsFrame, width=310, height=40, corner_radius=10)
    headFont = customtkinter.CTkFont(family='Arial', size=16, weight='bold')
    placeLabel = customtkinter.CTkLabel(titleFrame, text='Place', font=headFont)
    titleLabel = customtkinter.CTkLabel(titleFrame, text='Title', font=headFont)
    amountLabel = customtkinter.CTkLabel(titleFrame, text='Amount', font=headFont)
    
    
    # Placing CTk assets inside title frame
    placeLabel.place(relx=0.15, rely=0.5, anchor=tkinter.CENTER)
    titleLabel.place(relx=0.45, rely=0.5, anchor=tkinter.CENTER)
    amountLabel.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    # Packing title frame
    titleFrame.pack()

    # Prints record
    def printRecord(index):
        if elements[index][0] == 'inc': record = customtkinter.CTkFrame(recordsFrame, width=310, height=32, fg_color='#90c695')
        elif elements[index][0] == 'exp': record = customtkinter.CTkFrame(recordsFrame, width=310, height=32, fg_color='#ff9478')

        # Deletes record in file
        def deleteRecord():
            toDelete = ','.join(elements[index]) + '\n'
            try:
                # Get all lines in file
                lines = []
                with open(embFP, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # Check if record exists in file, if so - delete
                if toDelete in lines:
                    lines.remove(toDelete)

                # Save modified file
                with open(embFP, 'w', encoding='utf-8') as file:
                    file.writelines(lines)

                printBudget(recordsFrame, graphFrame, embFP)
                
            except:
                print('Error')

        # Creating CTk title assets
        plaL = customtkinter.CTkLabel(record, text=str(elements[index][1]), text_color='black')
        titL = customtkinter.CTkLabel(record, text=str(elements[index][2]), text_color='black')
        amtL = customtkinter.CTkLabel(record, text=str(elements[index][3]), text_color='black')
        delButton = customtkinter.CTkButton(record, text='❌', width=24, height=24, fg_color='transparent', hover_color='red', command=deleteRecord)

        # Placing record elements
        plaL.place(relx=0.15, rely=0.5, anchor=tkinter.CENTER)
        titL.place(relx=0.45, rely=0.5, anchor=tkinter.CENTER)
        amtL.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)
        delButton.place(relx=0.92, rely=0.5, anchor=tkinter.CENTER)

        # Packing everything
        record.pack(pady=3)

    # Making a list of records
    for i in range(len(elements)):
        printRecord(i)

    # Income graph
    # incomeG = [str(i[2]).upper() for i in elements if i[0]=='inc']
    # valuesG = [str(i[3]).upper() for i in elements if i[0]=='inc']

    statsT = [(str(i[2]).upper(), i[3]) for i in elements if i[0]=='inc']
    
    result = {}

    for i in statsT:
        result.setdefault(i[0], []).append(float(i[1]))

    for i in result:
        zmienna = sum(result[i])
        result[i] = zmienna

    titles = [name for name, value in result.items()]
    values = [value for name, value in result.items()]

    figure = plt.Figure(figsize=(4, 4), dpi=100)
    figure, ax = plt.subplots()
    ax.pie(values, labels=titles, autopct='%1.1f%%')
    bar1 = FigureCanvasTkAgg(figure, graphFrame)
    bar1.get_tk_widget().place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    

if __name__ == '__main__':
    pass