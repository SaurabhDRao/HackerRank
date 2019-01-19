q = int(input())
for _ in range(q):
    n = int(input())
    bn = bin(n)[2:]
    flip = ""
    for x in bin(n)[2:]:
        flip += "" + str(int(x) ^ 1)
    print(int(("1" * (32 - len(flip))) + flip, 2))