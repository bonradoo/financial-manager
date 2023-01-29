import tkinter
import customtkinter
from datetime import date
import os

def isNumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def saveToFile(line):
    print(line)
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

def clearEntry(shop, title, amount):
    shop.delete()
    title.delete()
    amount.delete()

def testo(app):
    typeVar = tkinter.IntVar()
    radiobutton_1 = customtkinter.CTkRadioButton(app, text="0", radiobutton_height=15, radiobutton_width=15, border_width_checked=5, width=30,
                                                variable=typeVar, value=0)
    radiobutton_1.place(relx=0.13, rely=0.3)

    radiobutton_2 = customtkinter.CTkRadioButton(app, text="1", radiobutton_height=15, radiobutton_width=15, border_width_checked=5, width=30,
                                                variable=typeVar, value=1)
    radiobutton_2.place(relx=0.02, rely=0.3)
    return typeVar.get()

def frame2(app):
    frame = customtkinter.CTkFrame(app, width=770, height=50, corner_radius=10, bg_color='red')
    frame.place(relx=0.02, rely=0.5)

    return frame

def addLog(app):
    frame = customtkinter.CTkFrame(app, width=770, height=50, corner_radius=10)
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

    return frame

    # def printVar():
    #     if (len(shop.get()) and len(title.get()) and len(amount.get()) and len(typeVar.get())) == 0: 
    #         print('Cannot submit empty entry')
    #         return
    #     if isNumber(amount.get()):
    #         print(typeVar.get(), shop.get(), title.get(), amount.get())
    #     else:
    #         print('Amount needs to be numeric')

    # button = customtkinter.CTkButton(app, text='Print', command=printVar, width=100)
    # button.place(relx=0.9, rely=0.5, anchor=tkinter.CENTER)

def start():
    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('blue')
    app = customtkinter.CTk()
    app.title('Financial Tracker')
    app.geometry('800x600')

    print(testo(app))
    if testo(app):
        run = addLog(app)
    else:
        run = frame2(app)
    
    

    app.mainloop()

def main():
    pass

if __name__ == '__main__':
    pass