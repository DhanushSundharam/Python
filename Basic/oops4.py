class Calci:
    def add(self,x,y):
        self.x=x
        self.y=y
        z=self.x+self.y
        print("Final Value is :",z)   
    def sub(self,x,y):
        self.x=x
        self.y=y
        z=self.x-self.y
        print("Final Value is :",z)   
    def multi(self,x,y):
        self.x=x
        self.y=y
        z=self.x*self.y
        print("Final Value is :",z)   
     
O1=Calci()
O1.add(12,45)
