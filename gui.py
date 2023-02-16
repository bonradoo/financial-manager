import tkinter
import customtkinter
import gui_budget, gui_invest, gui_login
import os


def run(app):
    # Create budget module frame
    budgetFrame = customtkinter.CTkFrame(app, width=980, height=500, corner_radius=10)

    # Create investement module frame
    investFrame = customtkinter.CTkFrame(app, width=980, height=500, corner_radius=10)

    # Create a quit button
    # quitButton = customtkinter.CTkButton(app, text='Exit ⭕', command=lambda event: [app.destroy, exit], width=32, height=32, fg_color='transparent', hover_color='red')
    # quitButton.place(relx=0.95, rely=0.05, anchor=customtkinter.CENTER)

    # Function responsible for changing modules
    def choice(app):
        def switchFrames(value):
            if value=='Budget': 
                budgetFrame.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)
                investFrame.place_forget()
                for widget in investFrame.winfo_children(): widget.destroy()
                gui_budget.addLog(budgetFrame)
            elif value=='Investements': 
                investFrame.place(relx=0.5, rely=0.57, anchor=tkinter.CENTER)
                budgetFrame.place_forget()
                for widget in budgetFrame.winfo_children(): widget.destroy()

        segmentedButton = customtkinter.CTkSegmentedButton(app, values=['Budget', 'Investements'], command=switchFrames)
        segmentedButton.place(relx=0.5, rely=0.11, anchor=tkinter.CENTER)

    # App title
    appTitle = customtkinter.CTkLabel(app, text="Financial Tracker", font=('Athelas', 32))
    appTitle.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
    choice(app)

    # Login page covers main app before accepting credentials
    gui_login.loginPage(app)


def start():
    # Setting up main window
    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('blue')
    app = customtkinter.CTk()
    app.resizable(False, False)
    app.title('Financial Tracker')
    app.geometry('1000x600')

    # Run main function
    run(app)

    # App quit function for protocol
    def appQuit():
        for after_id in app.eval('after info').split():
            app.after_cancel(after_id)
        app.destroy()
        exit()
    app.protocol('WM_DELETE_WINDOW', appQuit)

    # Mainloop for the app
    app.mainloop()

if __name__ == '__main__':
    pass