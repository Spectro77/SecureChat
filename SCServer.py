import socket
import hashlib
from os import system

s = socket.socket()
print("   _____                                    _         _             _   ")
print("  / ____|                                  | |       | |           | |  ")
print(" | (___    ___   ___  _   _  _ __  ___   __| |   ___ | |__    __ _ | |_ ")
print("  \___ \  / _ \ / __|| | | || '__|/ _ \ / _` |  / __|| '_ \  / _` || __|")
print("  ____) ||  __/| (__ | |_| || |  |  __/| (_| | | (__ | | | || (_| || |_ ")
print(" |_____/  \___| \___| \__,_||_|   \___| \__,_|  \___||_| |_| \__,_| \__|")
print("                                          S E R V E R                 \n")
print("Witaj w szyfrowanym komunikatorze!")
print("Aby móc korzystać z programu należy go skonfigurować")
print("Lista adresów przypisana do tego urządzenia: \n",socket.gethostbyname_ex(socket.gethostname()),"\n")
ip = input("Lokalne ip (jedno z wymienionych wyżej): ")
port = int(input("Dowolny niezajęty port: "))
seed = float(input("Wpisz dowolną liczbę: "))
s.bind((ip, port))
print("Skonfigurowano serwer na adresie [",ip,"] i porcie [",port,"]")
wordlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","y","z","q"," ","1","2","3","4","5","6","7","8","9","0",":"]
print("Lista dostępnych znaków: ", wordlist)
print("Żeby wysyłać wiadomości trzeba połączyć klienta")
def decryptor(rcvdData, wordlist):
    for i in wordlist:
        ires = hashlib.md5(i.encode()).hexdigest()
        if (ires == rcvdData):
            print(i, end = "")
while True:
    s.listen(5)
    c, addr = s.accept()
    print("\nUzyskano połączenie z ", addr)
    while True:
        try:
            rcvdData = c.recv(1024).decode()
            rcvdData = int(rcvdData)
            rcvdData = bytes(rcvdData / seed)
            rcvdData = rcvdData.decode()
            if(rcvdData == "b99834bc19bbad24580b3adfa04fb947"):
                print("")
            if(rcvdData == ""):
                print("\nZamknięto połączenie z ", addr)
                break
            decryptor(rcvdData, wordlist)
        except:
            print("\nZamknięto połączenie z ", addr)
            break
