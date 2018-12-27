t = int(input())
for i in range(t):
    n = int(input())
    h = 1
    for j in range(n):
        if(j % 2 == 0):
            h += h
        else:
            h += 1
    print(h)
