class Calcualtor:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        print(f"Addition value is : {self.x+self.y}")
    def sub(self):
        print(f"Subtraction value is :{self.x-self.y}")
    def multi(self):
        print(f"Multiolication Value is :{self.y*self.y}")
    def divi(self):
        print(f"Division Value is : {self.x/self.y}")

o1=Calcutor(12,89)
o1.add()
