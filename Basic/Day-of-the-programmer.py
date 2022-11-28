import sys
y=int(input().strip())
if y<1918:
    if y%4!=0:
        print("13.09."+str(y))
    else:
        print("12.09."+str(y))
elif y>1918:
    if y%400==0 or (y%4==0 and y%100!=0):
        print("12.09."+str(y))
    else:
        print("13.09."+str(y))
else:
    print("26.09.1918")
