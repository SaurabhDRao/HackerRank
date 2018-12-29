n = int(input())
a = [int(x) for x in input().split()]

s = set(a)
s.discard(max(s))
print(max(s))