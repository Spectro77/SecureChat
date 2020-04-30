import socket
import time
import hashlib

def splitword(word):
    return [char for char in word]
print("   _____                                    _         _             _   ")
print("  / ____|                                  | |       | |           | |  ")
print(" | (___    ___   ___  _   _  _ __  ___   __| |   ___ | |__    __ _ | |_ ")
print("  \___ \  / _ \ / __|| | | || '__|/ _ \ / _` |  / __|| '_ \  / _` || __|")
print("  ____) ||  __/| (__ | |_| || |  |  __/| (_| | | (__ | | | || (_| || |_ ")
print(" |_____/  \___| \___| \__,_||_|   \___| \__,_|  \___||_| |_| \__,_| \__|")
print("                                          C L I E N T                 \n")
print("Witaj w szyfrowanym komunikatorze!")
print("Aby móc korzystać z programu należy połączyć się ze skonfigurowanym serwerem\n")
s = socket.socket()
nickname = input("Wpisz nazwę użytkownika: ")
ip = input("Wpisz ip serwera: ")
port = int(input("Wpisz port serwera: "))
seed = int(input("Wpisz dowolną liczbę: "))
s.connect((ip, port))
print("\nPołączono się z [", ip,"], [",port,"]")
while True:
    i = input("Wpisz wiadomość:")
    if(i == "/close"):
        s.close()
        break
    i = (nickname + ": " + i +"|").lower()
    i = splitword(i)
    i = splitword(i)
    for word in i:
        time.sleep(0.1)
        counter = 1
        wordres = hashlib.md5(word.encode()).hexdigest()
        word
        wordres = bytes(wordres, "utf8")
        print(wordres," - ",word)
        s.send(wordres)
