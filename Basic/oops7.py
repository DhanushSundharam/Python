class Bank:
    Balance=0
    def Deposite(self,Amount):
        
        Amount=Amount
        self.Balance=self.Balance+Amount
        print(f"Account balance has been updated :{self.Balance} ")

    def Withdraw(self,Amount):
         if (Amount>=self.Balance):
             print(f"Insufficient Funds | Balance Available : {self.Balance}")
         else:
             self.Balance=self.Balance-Amount
             print(f"Amount Balance has been updated : {self.Balance}")
x=Bank()
x.Deposite(1000)
output
Account balance has been updated :1000 
x.Withdraw(200)
Amount Balance has been updated : 800
x.Withdraw(100)
Amount Balance has been updated : 700
x.Withdraw(1000)
Insufficient Funds | Balance Available : 700
