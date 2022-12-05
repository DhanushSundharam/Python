In [118]: class student:
     ...:     def getstudent(self,name,age,city):
     ...:         self.name=name
     ...:         self.age=age
     ...:         self.city=city
     ...:     def displaystudent(self):
     ...:         print("Name=",self.name)
     ...:         print("Age=",self.age)
     ...:         print("City=",self.city)
     ...:
     ...:

In [119]: # creation of object for the class student

In [120]: s1=student()

In [121]: s1.getstudent("sathish",32,"salem")

In [122]: s1.displaystudent()
Name= sathish
Age= 32
City= salem

In [123]: s2=student()

In [124]: s2.getstudentdata("Dhanush",21,"Mettur")
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Input In [124], in <cell line: 1>()
----> 1 s2.getstudentdata("Dhanush",21,"Mettur")

AttributeError: 'student' object has no attribute 'getstudentdata'

In [125]: s2.getstudent("Dhanush",21,"Mettur")

In [126]: s2.name
Out[126]: 'Dhanush'

In [127]: s1.name
Out[127]: 'sathish'

In [128]: s2.city
Out[128]: 'Mettur'

In [129]: s1.age
Out[129]: 32

In [130]: s2.age
Out[130]: 21

In [131]: s3=student()

In [132]: s3.getstudent("Aswin",26,"Chennai")

In [133]: s4=student()

In [134]: s4.getstudent("Raj",32,"Madurai")

In [135]: s2.name
Out[135]: 'Dhanush'

In [136]: s3.name
Out[136]: 'Aswin'

In [137]: s4.name
Out[137]: 'Raj'

In [138]: s3.city
Out[138]: 'Chennai'

In [139]:
