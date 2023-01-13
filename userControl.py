from cryptography import fernet
import hashlib, getpass

def checkCorrect():
    password = getpass.getpass('Please input your password: ')
    passHashed = hashlib.sha512(password.encode()).hexdigest()

    with open('./bin/log/pass.txt', 'r') as file:
        key = file.readline()
        
    if passHashed == key:
        return True
    return False

def setPassword():
    password = input('Please input your new password: ')
    passHashed = hashlib.sha512(password.encode())
    
    with open('./bin/log/pass.txt', 'w') as file:
        file.write(passHashed.hexdigest())

def main():
    setPassword()
    res = checkCorrect()
    
    if res:
        print('Nice')

if __name__ == '__main__':
    main()