class printDoc:
    def __init__(self, s, senderID):
        self.str = s
        self.senderID = senderID

    def setStr(self, s, senderID):
        self.str = s
        self.senderID = senderID

    def getStr(self):
        return self.str

    def getSender(self):
        return self.senderID