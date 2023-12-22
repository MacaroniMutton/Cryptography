import os
import random

def encrypt(str):
    encr = ""
    key = random.randint(1,100)
    for char in str:
        if(ord(char)<32 or ord(char)>126):
            encr += char
            continue
        if(ord(char)+key<127):
            char = chr(ord(char)+key)
        else:
            char = chr(32 + (ord(char)+key)%127)
        encr += char
    return encr, key

def decrypt(str, key):
    decr = ""
    for char in str:
        if(ord(char)<32 or ord(char)>126):
            decr += char
            continue
        if(ord(char)-key>31):
            char = chr(ord(char)-key)
        else:
            temp = ord(char)-32-key
            while not 32<=temp<=126:
                temp += 127
            char = chr(temp)
        decr += char
    return decr


def encryptFile(path):
    try:

        with open(path, 'r') as file:
            fileContent = file.read()

        with open(path, 'w') as file:
            encrypted, key = encrypt(fileContent)
            file.write(encrypted)

        with open(keyPath, 'a') as keyfile:
            keyfile.write(str(key)+" "+path)
            keyfile.write("\n")

    except Exception as e:
        print("Error occurred")
    else:
        print("File Encrypted")


def decryptFile(path, keyPath):
    try:

        with open(keyPath, 'r') as keyfile:
            keyfileContent = keyfile.readlines()
            key = None
            reqLineNumber = None
            for line in keyfileContent:
                if path in line:
                    reqLineNumber = keyfileContent.index(line)
                    key = int(line[:line.index(' ')])

        keyfileContent[reqLineNumber] = ""       
        with open(keyPath, 'w') as keyfile:
            keyfile.writelines(keyfileContent)

        with open(path, 'r') as file:
            fileContent = file.read()

        with open(path, 'w') as file:
            decrypted = decrypt(fileContent, key)
            file.write(decrypted)

    except Exception as e:
        print("Cannot be decrypted")
    else:
        print("File Decrypted")


while True:
    again = None
    pathtemp = input("Enter the path name : ")
    path = ""
    for ch in pathtemp:
        path += ch
        if ch=='\\':
            path += ch

    keyPath = "keys.txt"
    choice = None

    while choice not in ('E', 'D'):
        choice = input("Press E to Encrypt, D to Decrypt : ").upper()

    if choice=='E':
        encryptFile(path)

    if choice=='D':
        decryptFile(path, keyPath)
    
    while again not in ('Y', 'N'):
        again = input("For encrypting/decrypting another file, press Y, otherwise press N to exit : ").upper()

    if again=='N':
        break



