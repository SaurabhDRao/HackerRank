n = int(input())
a = [int(x) for x in input().split()]

sum = 0
count = 0
for i in range(n):
    sum += a[i]
    if(sum % 2 == 1):
        count += 2

print(count if(sum % 2 == 0) else "NO")