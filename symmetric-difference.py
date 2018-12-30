# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set([int(x) for x in input().split()])
m = int(input())
b = set([int(x) for x in input().split()])

d1 = a.difference(b)
d2 = b.difference(a)
d = set()
d.update(d1)
d.update(d2)
for x in sorted(d):
    print(x)