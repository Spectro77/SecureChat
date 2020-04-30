import socket
import time
import hashlib

def splitword(word):
    return [char for char in word]
print("   _____                                        _             _   ")
print("  / ____|                                      | |           | |  ")
print(" | (___    ___   ___  _   _  _ __  ___     ___ | |__    __ _ | |_ ")
print("  \___ \  / _ \ / __|| | | || '__|/ _ \   / __|| '_ \  / _` || __|")
print("  ____) ||  __/| (__ | |_| || |  |  __/  | (__ | | | || (_| || |_ ")
print(" |_____/  \___| \___| \__,_||_|   \___|   \___||_| |_| \__,_| \__|")
print("                                   C L I E N T                  \n")
print("Welcome in Secure Chat!")
print("To use program you need to connect with configured server\n")
s = socket.socket()
nickname = input("Nickname: ")
ip = input("Server's ip: ")
port = int(input("Server's port: "))
seed = int(input("Seed: "))
s.connect((ip, port))
print("\nConnected with [", ip," : ",port,"]")
print("To close connection type /close")
while True:
    i = input("Type message:")
    if(i == "/close"):
        s.close()
        break
    i = (nickname + ": " + i +"|").lower()
    i = splitword(i)
    i = splitword(i)
    for word in i:
        time.sleep(0.1)
        wordascii = str(int(ord(word))*seed)
        wordres = hashlib.md5(wordascii.encode()).hexdigest()
        print(wordres," - ",word)
        wordres = bytes(wordres, "utf8")
        s.send(wordres)
