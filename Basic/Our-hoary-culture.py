n = int(input())
c = 'R'
dis = 10
x,y=0,0
for i in range(n):
    if c=='R':
        x=x+dis
        c='U'
        dis=dis+10
    elif c=='U':
        y=y+dis
        c='L'
        dis=dis+10
    elif c=='L':
        x=x-dis
        c='D'
        dis=dis+10
    elif c=='D':
        y=y-dis
        c='A'
        dis=dis+10
    elif c=='A':
        x=x+dis
        c='R'
        dis=dis+10
print(x,y)
