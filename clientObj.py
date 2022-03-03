class clientObj:

    def __init__(self, name):
        self.name = name

        self.receiveAddress = None
        self.sendAddress= None


    def isInitialized(self):
        return self.hasReceiveAddress() and self.hasSendAddress()


    def setReceiveAddress(self, address):
        self.receiveAddress = address
    def getReceiveAddress(self):
        return self.receiveAddress
    def hasReceiveAddress(self):
        return self.receiveAddress is not None

    def setSendAddress(self, address):
        self.sendAddress = address
    def getSendAddress(self):
        return self.sendAddress
    def hasSendAddress(self):
        return self.sendAddress is not None

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name