l = [int(x) for x in input().split()]
w = input()

az = "abcdefghijklmnopqrstuvwxyz"
wList = []

for i in range(len(w)):
    wList.append(l[az.find(w[i])])

print(max(wList) * len(w))