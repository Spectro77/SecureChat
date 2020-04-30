import socket
import hashlib
from os import system

s = socket.socket()
print("   _____                                        _             _   ")
print("  / ____|                                      | |           | |  ")
print(" | (___    ___   ___  _   _  _ __  ___     ___ | |__    __ _ | |_ ")
print("  \___ \  / _ \ / __|| | | || '__|/ _ \   / __|| '_ \  / _` || __|")
print("  ____) ||  __/| (__ | |_| || |  |  __/  | (__ | | | || (_| || |_ ")
print(" |_____/  \___| \___| \__,_||_|   \___|   \___||_| |_| \__,_| \__|")
print("                                   S E R V E R                  \n")
print("Welcome in Secure Chat!")
print("To use program you need to configure it")
print("Adresses assigned to this device: \n",socket.gethostbyname_ex(socket.gethostname()),"\n")
ip = input("Local ip (one of above): ")
port = int(input("Port: "))
seed = float(input("Seed: "))
s.bind((ip, port))
print("Server configured [",ip," : ",port,"]")
wordlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","y","z","q"," ","1","2","3","4","5","6","7","8","9","0",":"]
print("Available characters: ", wordlist)
print("To send messages client need's to connect")
def decryptor(rcvdData, wordlist):
    for i in wordlist:
        ires = str(int(int(ord(i))*seed))
        print(ires)
        ires = hashlib.md5(ires.encode()).hexdigest()
        if (ires == rcvdData):
            print(i, end = "")
            break
while True:
    s.listen(5)
    c, addr = s.accept()
    print("\nConnected with ", addr)
    while True:
        try:
            rcvdData = c.recv(1024).decode()
            if(rcvdData == hashlib.md5(str(int(int(ord("|"))*seed)).encode()).hexdigest()):
                print("")
            if(rcvdData == ""):
                print("\nClosed connection with ", addr)
                break
            decryptor(rcvdData, wordlist)
        except:
            print("\nClosed connection with z ", addr)
            break
