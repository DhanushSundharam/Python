n [87]: employee=["sathish","dhanush","sai","aswin","abisheak"]

In [88]: salary=12000

In [89]: for i in employee:
    ...:     if(i=='sai'):
    ...:         print("No Bonous",salary)
    ...:         continue
    ...:     print("Bonus",(salary*10/100))
    ...:
    ...:
Bonus 1200.0
Bonus 1200.0
No Bonous 12000
Bonus 1200.0
Bonus 1200.0

In [90]: for i in employee:
    ...:     if(i=='sai'):
    ...:         print("No Bonous",salary)
    ...:         continue
    ...:     print(i,(salary*10/100))
    ...:
sathish 1200.0
dhanush 1200.0
No Bonous 12000
aswin 1200.0
abisheak 1200.0

In [91]: for i in employee:
    ...:     if(i=='sai'):
    ...:         print("No Bonous",salary)
    ...:         continue
    ...:     print(i,salary+(salary*10/100))
    ...:
sathish 13200.0
dhanush 13200.0
No Bonous 12000
aswin 13200.0
abisheak 13200.0

In [92]: for i in employee:
    ...:     if(i=='sai'):
    ...:         print(i,"No Bonous",salary)
    ...:         continue
    ...:     print(i,salary+(salary*10/100))
    ...:
sathish 13200.0
dhanush 13200.0
sai No Bonous 12000
aswin 13200.0
abisheak 13200.0

In [93]:
