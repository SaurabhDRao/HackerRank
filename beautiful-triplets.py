n, d = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

count = 0
for i in a:
    if(((i + d) in a) and ((i + (2 * d)) in a)):
        count += 1

print(count)