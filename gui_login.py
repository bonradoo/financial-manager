import tkinter
import customtkinter
from cryptography.fernet import Fernet
import hashlib, base64, os
import gui

acceptance = False



def checkAccept():
    global acceptance
    return acceptance

def loginPage(frame):
    loginFrame = customtkinter.CTkFrame(frame, width=980, height=580)
    loginFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def genFernetKey(passcode:bytes) -> bytes:
        assert isinstance(passcode, bytes)
        hlib = hashlib.md5()
        hlib.update(passcode)
        return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

    def setPassword(password):
        global acceptance
        passHashed = hashlib.sha512(password.encode())
        with open('./bin/pass.key', 'w') as file:
                file.write(passHashed.hexdigest())
        checkCorrect(password)

    def checkCorrect(password):
        global acceptance
        passHashed = hashlib.sha512(password.encode()).hexdigest()

        with open('./bin/pass.key', 'r') as file:
            key = file.readline()
            
        if passHashed == key:
            acceptance = True
            loginFrame.place_forget()
        else:
            acceptance = False
            passwordEntry.delete(0, 'end')

        
    def isCorrect(acceptance):
        if not acceptance:
            incorrect.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)
        else:
            incorrect.place_forget()


    loginTitle = customtkinter.CTkLabel(loginFrame, text='FT Login', font=(None, 24))
    signupTitle = customtkinter.CTkLabel(loginFrame, text='FT Sign up', font=(None, 24))
    password = customtkinter.StringVar()
    passwordEntry = customtkinter.CTkEntry(loginFrame, width=200, height=50, placeholder_text='Password', textvariable=password, show='*')
    signupButton = customtkinter.CTkButton(loginFrame, text='Sign up', width=200, height=50, command=lambda: [setPassword(password.get()), isCorrect(acceptance)])
    loginButton = customtkinter.CTkButton(loginFrame, text='Confirm', width=200, height=50, command=lambda: [checkCorrect(password.get()), isCorrect(acceptance)])
    

    
    passwordEntry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    if not os.path.exists('./bin/pass.key'):
        signupTitle.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        signupButton.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    else:
        loginTitle.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        loginButton.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    
    incorrect = customtkinter.CTkLabel(loginFrame, width=200, height=10, text='Incorrect password', font=(None, 12), text_color='red')



if __name__ == '__main__':
    pass