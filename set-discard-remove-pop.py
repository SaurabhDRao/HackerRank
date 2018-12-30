n = int(input())
s = set(map(int, input().split()))
nc = int(input())
for i in range(nc):
    line = input().split()
    com = line[0]
    if(com == "pop"):
        s.pop()
    elif(com == "remove"):
        s.remove(int(line[1]))
    elif(com == "discard"):
        s.discard(int(line[1]))

print(sum(s))