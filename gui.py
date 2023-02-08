import tkinter
import customtkinter
from datetime import date
import os
import gui_budget, gui_invest



    

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
    app.resizable(False, False)
    app.title('Financial Tracker')
    app.geometry('1000x600')

    

    label = customtkinter.CTkLabel(app, text="Financial Tracker", font=('Athelas', 32))
    label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

    budgetFrame = customtkinter.CTkFrame(app, width=980, height=500, corner_radius=10)
    gui_budget.addLog(budgetFrame)

    investFrame = customtkinter.CTkFrame(app, width=980, height=500, corner_radius=10, fg_color='blue')

    def choice(app):
        def switchFrames(value):
            if value=='Budget': budgetFrame.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER), investFrame.place_forget()
            elif value=='Investements': investFrame.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER), budgetFrame.place_forget()

        segmentedButton = customtkinter.CTkSegmentedButton(app, values=['Budget', 'Investements'], command=switchFrames)
        segmentedButton.place(relx=0.5, rely=0.11, anchor=tkinter.CENTER)

    choice(app)

    app.mainloop()

def main():
    pass

if __name__ == '__main__':
    pass