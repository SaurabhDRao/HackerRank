# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

line = input()
s = line.split()[0]
k = int(line.split()[1])
p = list(permutations(s, k))
p.sort()
for x in p:
    print("".join(x))