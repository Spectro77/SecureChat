import socket
import time
import hashlib

def splitword(word):
    return [char for char in word]
print("Witaj w szyfrowanym komunikatorze")
print("Aby móc korzystać z programu należy połączyć się ze skonfigurowanym serwerem")
s = socket.socket()
ip = input("Wpisz ip serwera: ")
port = int(input("Wpisz port serwera: "))
s.connect((ip, port))
print("Połączono się z [", ip,"], [",port,"]")
while True:
    i = input("Wpisz wiadomość:")
    if(i == "/close"):
        s.close()
        break
    i = splitword(i)
    for word in i:
        time.sleep(0.1)
        wordres = hashlib.md5(word.encode()).hexdigest()
        print(wordres," - ",word)
        wordres = bytes(wordres, "utf8")
        s.send(wordres)