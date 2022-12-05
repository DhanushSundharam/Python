In [140]: class arithmetic:
     ...:     def initial(self,x,y):
     ...:         self.x=x
     ...:         self.y=y
     ...:     def add(self):
     ...:         return self.x+self.y
     ...:     def sub(self):
     ...:         return self.x-self.y
     ...:     def mul(self):
     ...:         return self.x*self.y
     ...:
     ...:
     ...:

In [141]: o1=arithmetic()

In [142]: o1.initial(23,3)

In [143]: o1.add()
Out[143]: 26

In [144]: o1.sub()
Out[144]: 20

In [145]: o1.mul()
Out[145]: 69

In [146]: arithmetic.initial(o1,10,12)

In [147]: arithmetic.mul(o1)
Out[147]: 120

In [148]:
