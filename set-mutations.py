# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set([int(x) for x in input().split()])
t = int(input())
for i in range(t):
    e = input()
    l = e.split()
    op = l[0]
    m = int(l[1])
    b = set([int(x) for x in input().split()])
    d = {
        "intersection_update": "a.intersection_update(b)",
        "update": "a.update(b)",
        "symmetric_difference_update": "a.symmetric_difference_update(b)",
        "difference_update": "a.difference_update(b)"
    }
    eval(d[op])

print(sum(a))