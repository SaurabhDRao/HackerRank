t = int(input())
for i in range(t):
    n = input()
    count = 0
    for x in n:
        if(x == '0'):
            continue
        if(int(n) % int(x) == 0):
            count += 1
    print(count)