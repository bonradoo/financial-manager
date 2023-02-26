import tkinter
import customtkinter
from cryptography.fernet import Fernet
import hashlib, base64, os

# Variable that defines if password is correct
acceptance = False

# Function that checks accetance (for external use)
def checkAccept():
    global acceptance
    return acceptance


# Main function for login page
def loginPage(frame):
    # Frame creation for login page
    loginFrame = customtkinter.CTkFrame(frame, width=980, height=580)
    loginFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    # Convert passcode to Fernet Key
    def genFernetKey(passcode:bytes) -> bytes:
        assert isinstance(passcode, bytes)
        hlib = hashlib.md5()
        hlib.update(passcode)
        return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))


    # Create a new password file
    def setPassword(password):
        global acceptance
        passHashed = hashlib.sha512(password.encode())
        with open('./bin/pass.key', 'w') as file:
                file.write(passHashed.hexdigest())
        checkCorrect(password)


    # Check if provided password is correct
    def checkCorrect(password):
        global acceptance
        passHashed = hashlib.sha512(password.encode()).hexdigest()

        with open('./bin/pass.key', 'r') as file:
            key = file.readline()
            
        if passHashed == key:
            # Correct -- clear login page
            acceptance = True
            loginFrame.place_forget()
        else:
            # Incorrect -- clear entry
            acceptance = False
            passwordEntry.delete(0, 'end')


    # Print to screen a label stating if password is correct
    def isCorrect(acceptance):
        if not acceptance:
            incorrect.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)
        else:
            incorrect.place_forget()


    # Create all CTk assets
    loginTitle = customtkinter.CTkLabel(loginFrame, text='FT Login', font=(None, 24))
    signupTitle = customtkinter.CTkLabel(loginFrame, text='FT Sign up', font=(None, 24))
    password = customtkinter.StringVar()
    passwordEntry = customtkinter.CTkEntry(loginFrame, width=200, height=50, placeholder_text='Password', textvariable=password, show='*')
    signupButton = customtkinter.CTkButton(loginFrame, text='Sign up', width=200, height=50, command=lambda: [setPassword(password.get()), isCorrect(acceptance)])
    loginButton = customtkinter.CTkButton(loginFrame, text='Confirm', width=200, height=50, command=lambda: [checkCorrect(password.get()), isCorrect(acceptance)])
    incorrect = customtkinter.CTkLabel(loginFrame, width=200, height=10, text='Incorrect password', font=(None, 12), text_color='red')

    passwordEntry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    passwordEntry.focus()

    # Depending if password file exists place according CTk assets
    if not os.path.exists('./bin/pass.key'):
        signupTitle.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        signupButton.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        passwordEntry.bind('<Return>', command=lambda event: [setPassword(password.get()), isCorrect(acceptance)])
    else:
        loginTitle.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        loginButton.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        passwordEntry.bind('<Return>', command=lambda event: [checkCorrect(password.get()), isCorrect(acceptance)])



if __name__ == '__main__':
    pass