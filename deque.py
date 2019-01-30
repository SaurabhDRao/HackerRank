from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    line = input().split()
    op = line[0]
    val = "".join(line[1:])
    eval("d." + op + "(" + val + ")")

print(" ".join([str(x) for x in d]))