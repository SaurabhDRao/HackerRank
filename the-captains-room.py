# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
p = [int(x) for x in input().split()]
r = set(p)
print(((sum(r)*k)-(sum(p)))//(k-1))