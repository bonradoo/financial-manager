import tkinter
import customtkinter
from datetime import date
import os
import gui_budget, gui_invest
import tkinter as tk


    

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
    # app.resizable(False, False)
    app.title('Financial Tracker')
    app.geometry('800x600')

    budgetFrame = customtkinter.CTkFrame(app, width=770, height=500, corner_radius=10, fg_color='red')
    gui_budget.addLog(budgetFrame)

    investFrame = customtkinter.CTkFrame(app, width=770, height=500, corner_radius=10, fg_color='blue')

    def choice(app):
        radiobutton_1 = customtkinter.CTkRadioButton(app, text="f2", radiobutton_height=15, radiobutton_width=15, border_width_checked=5, width=30, 
                                                    command=lambda: [investFrame.place(relx=0.016, rely=0.15), budgetFrame.place_forget()])
        radiobutton_1.place(relx=0.13, rely=0.3)

        radiobutton_2 = customtkinter.CTkRadioButton(app, text="bud", radiobutton_height=15, radiobutton_width=15, border_width_checked=5, width=30,
                                                    command=lambda: [budgetFrame.place(relx=0.016, rely=0.15), investFrame.place_forget()])
        radiobutton_2.place(relx=0.02, rely=0.3)

    choice(app)

    app.mainloop()

def main():
    pass

if __name__ == '__main__':
    pass