t = int(input())
for i in range(t):
    n, c, m = [int(x) for x in input().split()]
    count = n // c
    left = count
    while(True):
        if((left / m) >= 1):
            r = left // m
            count += r
            left = left - (r * m) + r
        else:
            break

    print(count)
