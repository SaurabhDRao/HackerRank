n = int(input())
c = [int(x) for x in input().split()]
c = sorted(c, reverse = True)

totc = 0
for i in range(len(c)):
    totc += ((2 ** i) * c[i])

print(totc)