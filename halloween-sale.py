p, d, m, s = [int(x) for x in input().split()]

count = 0
s -= p
while(s >= 0):
    count += 1
    p -= d
    if(p <= m):
        s -= m   
    else:
        s -= p

print(count)