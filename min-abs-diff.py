n = int(input())
a = [int(x) for x in input().split()]

a.sort()

m = abs(a[0] - a[1])
for i in range(1, len(a) - 1):
    if(m > abs(a[i] - a[i + 1])):
        m = abs(a[i] - a[i + 1])

print(m)