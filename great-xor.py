q = int(input())
for _ in range(q):
    x = int(input())
    print((1 << x.bit_length()) - x - 1)