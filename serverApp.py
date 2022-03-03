from socket import *
from clientObj import clientObj

clients = []


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

def clientExists(name):
    for i in range(len(clients)):
        if clients[i].getName() == name:
            return True
    return False

def getClient(name):
    for i in range(len(clients)):
        if(clients[i].getName() == name):
            return clients[i]

def getClientFromSendAddress(sendAddress):
    for i in range(len(clients)):
        if(clients[i].getSendAddress() == sendAddress):
            return clients[i]

print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode()

    print("Message received")
    if message[0] == "/":         # "/" is used to signal a command
        if message[:len("/knock knock")] == "/knock knock":    #signal received from client receiver port
            name = message[len("/knock knock"):]
            #print("/knock received " + name)
            if clientExists(name):
                serverSocket.sendto("name already taken, try again".encode(), clientAddress)
            else:
                c = clientObj(name)
                c.setReceiveAddress(clientAddress)
                clients.append(c)
                serverSocket.sendto(("Welcome " + name).encode(), clientAddress)

        if message[:len("/come in")] == "/come in":      #signal received from client sender port
            name = message[len("/come in"):]
            #print("/come in received " + name)
            if clientExists(name):
                serverSocket.sendto(("Welcome " + name).encode(), clientAddress)
                getClient(name).setSendAddress(clientAddress)
    else:
        c = getClientFromSendAddress(clientAddress)
        if clientExists(c.getName()):
            for i in range(len(clients)):
                if clients[i] is not c:
                    serverSocket.sendto(message.encode(), clients[i].getReceiveAddress())