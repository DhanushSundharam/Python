size = 5
for i in range(size):
    # print spaces
    for j in range(i):
        print(" ", end="")
    # print numbers
    for k in range(2 * (size - i) - 1):
        print(k+1, end="")
    print()
