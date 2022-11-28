date,month,year = map(int,input().split('/'))
valid = False
if year>1:
    if month in [1,3,5,7,8,10,12] and date in range(1,32):
        valid = True
    elif month in [4,6,9,11] and date in range (1,32):
        valid = True
    elif date == 29 and ( year%4 ==0 and year%100!=0 and year%400==0):
        valid = True
    elif date in range(1,29) and month==2:
        valid = True
if valid:
    if month in [1,2]:
        month+= 10
        year-=1
    else:
        month-=2
    D=year%100
    C=year//100
    f = (date+(13*month-1)//5 + D + D//4 + C//4 - 2 * C) % 7
    days=['Sunday' , 'Monday' , 'Tuesday' , 'Wednesday' , 'Thursdaay' , 'Friday' , 'Saturday']
    print(days[f])
else:
    print("Invalid")
