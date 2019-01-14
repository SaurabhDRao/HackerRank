n = int(input())
if(n == 0):
    print("1")
else:
    l = list(bin(n))[2:]
    print(2 ** (l.count("0")))