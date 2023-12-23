import os
import random
import string
import ast

def encrypt(str):
    encr = ""
    chars = " " + "\n" + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    values = chars.copy()
    random.shuffle(values)
    key = dict(zip(chars, values))
    for char in str:
        encr += key[char]
    return encr, key

def decrypt(str, key):
    decr = ""
    for char in str:
        decr += list(key.keys())[list(key.values()).index(char)]
    return decr


def encryptFile(path):
    try:

        with open(path, 'r') as file:
            fileContent = file.read()

        with open(path, 'w') as file:
            encrypted, key = encrypt(fileContent)
            file.write(encrypted)

        with open(keyPath, 'a') as keyfile:
            keyfile.write(f"{key} {path}")
            keyfile.write("\n")

    except Exception as e:
        print(e)
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
                    key = ast.literal_eval(line[:line.index("} ")+1])

        keyfileContent[reqLineNumber] = ""       
        with open(keyPath, 'w') as keyfile:
            keyfile.writelines(keyfileContent)

        with open(path, 'r') as file:
            fileContent = file.read()

        with open(path, 'w') as file:
            decrypted = decrypt(fileContent, key)
            file.write(decrypted)

    except Exception as e:
        print(e)
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



