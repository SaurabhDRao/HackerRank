# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
A = set([int(x) for x in input().split()])
B = set([int(x) for x in input().split()])

happy = 0
for e in a:
    if(e in A):
        happy += 1
    if(e in B):
        happy -= 1

print(happy)