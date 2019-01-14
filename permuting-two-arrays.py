q = int(input())
for _ in range(q):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    if((min(a) + max(b) >= k) and (min(b) + max(a) >= k) and (sum(a)+sum(b)>=len(b)*k)):
        print("YES")
    else:
        print("NO")