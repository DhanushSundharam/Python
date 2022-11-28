units=float(input())
if units<=100:
    print("%.2f"%0)
elif units<=200:
    print("%.2f"%((units-100)*1.5+20))
elif units<=500:
    print("%.2f"%((100*2)+(units-200)*3+30))
else:
    print("%.2f"%((100*3.5)+(300*4.6)+(units-500)*6.6+50))
