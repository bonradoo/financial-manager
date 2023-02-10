import tkinter
import customtkinter
from datetime import date
import os
import gui_budget, gui_invest, gui_login


def run(app):
    budgetFrame = customtkinter.CTkFrame(app, width=980, height=500, corner_radius=10)
    gui_budget.addLog(budgetFrame)

    investFrame = customtkinter.CTkFrame(app, width=980, height=500, corner_radius=10, fg_color='blue')

    def choice(app):
        def switchFrames(value):
            if value=='Budget': budgetFrame.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER), investFrame.place_forget()
            elif value=='Investements': investFrame.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER), budgetFrame.place_forget()

        segmentedButton = customtkinter.CTkSegmentedButton(app, values=['Budget', 'Investements'], command=switchFrames)
        segmentedButton.place(relx=0.5, rely=0.11, anchor=tkinter.CENTER)

    

    
    

    # Title
    appTitle = customtkinter.CTkLabel(app, text="Financial Tracker", font=('Athelas', 32))
    appTitle.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
    choice(app)

    gui_login.loginPage(app)

def start():
    
    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('blue')
    app = customtkinter.CTk()
    app.resizable(False, False)
    app.title('Financial Tracker')
    app.geometry('1000x600')

    run(app)
    app.mainloop()

def main():
    pass

if __name__ == '__main__':
    pass