n, k = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])

toys = 0
for i in range(n):
    if(k - a[i] > 0):
        toys += 1
        k -= a[i]
    else:
        break

print(toys)