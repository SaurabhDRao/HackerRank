t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        l = list(input())
        l = sorted(l)
        grid.append("".join([x for x in l]))
    flag = 0
    for i in range(len(grid[0])):
        temp = []
        for j in range(n):
            temp.append(grid[j][i])
        if(temp != sorted(temp)):
            print("NO")
            flag = 1
            break
    if(flag == 0):
        print("YES")

