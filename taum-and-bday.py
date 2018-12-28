t = int(input())
for i in range(t):
    b, w = [int(x) for x in input().split()]
    bc, wc, z = [int(x) for x in input().split()]
    cost = 0
    if(bc > wc + z):
        cost = ((b + w) * wc) + (b * z)
    elif(wc > bc + z):
        cost = ((b + w) * bc) + (w * z)
    else:
        cost = (b * bc) + (w * wc)
    print(cost)