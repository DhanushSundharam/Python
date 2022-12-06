>>> x=["abith","abithversion","abishek","arunkarthik","Dhaniswar","Dhanraj","Dhanush","gokul","gopi"]
>>> for i in x:
...     if i=="abith" or i=="gokul" or i=="gopi":
...        print("No internal Marks for this guys",i)
...        continue
...     print("Internals marks ",i,91)
...
No internal Marks for this guys abith
Internals marks  abithversion 91
Internals marks  abishek 91
Internals marks  arunkarthik 91
Internals marks  Dhaniswar 91
Internals marks  Dhanraj 91
Internals marks  Dhanush 91
No internal Marks for this guys gokul
No internal Marks for this guys gopi
