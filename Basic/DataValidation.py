day,month,year=map(int,input().split("/"))
if year > 0:
    if month in [1,3,5,7,8,10]:
        x=31
    elif month in [4,6,9,11]:
        x=30
    elif year%4==0 and year%100!=0 or year%400==0: 
        x=29
    else:
        x=28
    if month<1 or month>12:
        print("Invalid")
    elif day<1 or day>x:
        print("Invalid")
    else:
        print("Valid")
else:
    print("Invalid")
