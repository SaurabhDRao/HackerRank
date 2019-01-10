t = int(input())

for _ in range(t):
    s1 = set(input())
    s2 = set(input())
    if(len(s1.intersection(s2)) > 0):
        print("YES")
    else:
        print("NO")