from socket import *
import threading

serverName = "127.0.0.1"
serverPort = 12000

global nameG 

def receive():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    global nameG
    while True:  #loop will iterate until client chooses a unique name
        name = input("Enter name: ")
        msg = "/knock knock" + name
        clientSocket.sendto(msg.encode(), (serverName, serverPort))
        message, address = clientSocket.recvfrom(2048)
        print(message.decode())
        if message.decode()[:len("Welcome " + name)] == "Welcome " + name: #server confirms name is unique
            nameG = name
            sendThread.start()
            break

    while True:
        message, address = clientSocket.recvfrom(2048)
        message = message.decode()
        print(message)


def send():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    msg = "/come in" + nameG
    clientSocket.sendto(msg.encode(), (serverName, serverPort))
    while True:
        message = input("Message: ")
        clientSocket.sendto(message.encode(), (serverName, serverPort))


receiveThread = threading.Thread(target=receive)
sendThread = threading.Thread(target=send)

receiveThread.start()
