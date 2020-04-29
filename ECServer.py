import socket
import hashlib
from os import system

s = socket.socket()
print("Witaj w szyfrowanym komunikatorze!")
print("Aby móc korzystać z programu należy go skonfigurować\n")
print("Lista adresów przypisana do tego urządzenia: \n",socket.gethostbyname_ex(socket.gethostname()),"\n")
ip = input("Lokalne ip (jedno z wymienionych wyżej): ")
port = int(input("Dowolny niezajęty port: "))
s.bind((ip, port))
print("\nSkonfigurowano serwer na adresie [",ip,"] i porcie [",port,"]")
wordlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","y","z","q"," ","1","2","3","4","5","6","7","8","9","0"]
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
    print("\n\nUzyskano połączenie z ", addr)
    while True:
        try:
            rcvdData = c.recv(1024).decode()
            if(rcvdData == ""):
                print("\n\nZamknięto połączenie z ", addr)
                break
            decryptor(rcvdData, wordlist)
        except:
            print("\n\nZamknięto połączenie z ", addr)
            break
