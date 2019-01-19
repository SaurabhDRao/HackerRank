# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
headings = input().split()
mi = headings.index("MARKS")
tot = 0
for i in range(n):
    line = input().split()
    tot += int(line[mi])

print("{0:.2f}".format(tot / n))