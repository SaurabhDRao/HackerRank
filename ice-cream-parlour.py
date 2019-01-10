t = int(input())
for _ in range(t):
    m = int(input())
    n = int(input())
    a = [int(x) for x in input().split()]
    l = len(a) - 1
    for i in range(len(a)):
        j = 0
        while(a[j] + a[i] != m and j < i):
            j += 1
        if(a[i] + a[j] == m and j < i):
            print(j + 1, i + 1)
            break