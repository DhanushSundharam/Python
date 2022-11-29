# downward triangle star pattern
n = 5

for i in range(n):
    # internal loop run for n - i times
    for j in range(n - i):
        print('*', end='')
    print()
