n = int(input())

s = set(input())
for _ in range(n - 1):
    t = set(input())
    s = s.intersection(t)

print(len(s))