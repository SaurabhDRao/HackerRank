n = int(input())
sticks = [int(x) for x in input().split()]
rem = []

while(True):
    count = len(sticks)
    m = min(sticks)
    sticks = [x-m for x in sticks if (x-m != 0)]
    rem.append(count)
    if(len(sticks) == 0):
        break

for i in rem:
    print(i)