t = int(input())
for i in range(t):
    n, m, s = [int(x) for x in input().split()]
    if((m + s - 1) % n == 0):
        print(n)
    else:
        print((m + s - 1) % n)