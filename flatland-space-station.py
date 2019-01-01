n, m = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
global_max = 0
L = len(c)
for i in range(0,L + 1):
    if(i == 0):
        local_max = c[i]
    elif(i == L):
        local_max = (n-1) - c[L-1]
    elif(c[i] - c[i-1] >1):
        local_max = (c[i]-c[i-1]) // 2
    if(local_max > global_max):
        global_max = local_max

print(global_max)