t = int(input())
for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    s = 0
    f = (n - 1) * min(a, b)
    print(f, end=" ")
    while((s + f) < (n - 1) * max(a, b)):
        s += abs(b - a)
        print(f + s, end = " ")
    print()