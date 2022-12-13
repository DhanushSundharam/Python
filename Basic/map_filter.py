def findodd(x):
    if x%3==1:
        return f"{x} is odd Number"

z=[1,2,3,4,5,6,7,8]
x=list(map(findodd,z))
print(x)

x=list(filter(findodd,z))
print(x)
