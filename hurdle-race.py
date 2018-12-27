n,k = [int(x) for x in input().split()]

h = [int(x) for x in input().split()]

m = max(h)
if(m <= k):
    print("0")
else:
    print(m - k)