class MyString:
    def __init__(self):
        self.string = "3232"
    def getString(self):
        self.string=input("Enter a string pink: ")
    def printString(self):
        print(self.string.upper())
s = MyString()
s.getString()
s.printString()