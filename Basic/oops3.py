class Students():
     def getdata(self,Name,Age,City,phone):
          self.x=Name
          self.y=Age
          self.z=City
          self.v=phone
     def display(self):
          print("Name :",self.x)
          print("Age :",self.y)
          print("City :",self.z)
          print("Phone Number :",self.v)

O1=Students()
O1.getdata("SathisKumar Sir",44,"Salem",71279199)
O1.display()
          
  
