t = int(input())
rem = 3
while(t > rem):
    t -= rem
    rem *= 2
print(rem - t + 1)