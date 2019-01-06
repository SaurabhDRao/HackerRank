n = int(input())
a = [int(x) for x in input().split()]

t = []
for i in range(100):
    t.append(0)

for i in range(len(a)):
    t[a[i]] += 1

print(" ".join([str(x) for x in t]))