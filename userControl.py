from cryptography.fernet import Fernet
import hashlib, getpass, base64

def genFernetKey(passcode:bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

def checkCorrect():
    password = getpass.getpass('Please input your password: ')
    passHashed = hashlib.sha512(password.encode()).hexdigest()

    with open('./bin/pass.key', 'r') as file:
        key = file.readline()
        
    if passHashed == key:
        return True
    return False

def setPassword():
    password = input('Please input your new password: ')
    passHashed = hashlib.sha512(password.encode())
    
    with open('./bin/pass.key', 'w') as file:
        file.write(passHashed.hexdigest())

def encryptLine(line):
    with open('./bin/pass.key') as file:
        hashCode = file.readline()
    key = genFernetKey(hashCode.encode('utf-8'))
    fernet = Fernet(key)

    encrypted = fernet.encrypt(line)
    return encrypted

def decryptLine():
    pass


def main():
    pass

if __name__ == '__main__':
    main()