n, k = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
e = 100
i = 0
while(i < n):
    try:
        if(c[i] == 1):
            e -= 2
        i = i + k
    except:
        e -= 1
        break
    e -= 1

print(e)