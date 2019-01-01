# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

line = input()
s = line.split()[0]
k = int(line.split()[1])

for i in range(1, k+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))