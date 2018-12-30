# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set([int(x) for x in input().split()])
m = int(input())
b = set([int(x) for x in input().split()])

print(len(a.symmetric_difference(b)))