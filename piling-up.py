for _ in range(int(input())):
    n = int(input())
    lst = [int(x) for x in input().split()]
    l = len(lst)
    i = 0
    while(i < l - 1 and lst[i] >= lst[i+1]):
        i += 1
    while(i < l - 1 and lst[i] <= lst[i+1]):
        i += 1
    print("Yes" if(i == l - 1) else "No")