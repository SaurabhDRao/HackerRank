q = int(input())

for _ in range(q):
    s = input()
    o = [ord(x) for x in s]
    r = o[::-1]
    lo = [abs(j-i) for i,j in zip(o[:-1], o[1:])]
    lr = [abs(j-i) for i,j in zip(r[:-1], r[1:])]
    if(lo == lr):
        print("Funny")
    else:
        print("Not Funny")