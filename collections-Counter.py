# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
sd = Counter(a)
tot = 0
for i in range(m):
    s, p = [int(x) for x in input().split()]
    if(sd[s] != 0):
        tot += p
        sd[s] -= 1
print(tot)