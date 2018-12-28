s1 = input()
s2 = input()
k = int(input())

if(len(s1) > len(s2)):
    d = [i for i in range(min(len(s1), len(s2))) if s1[i] != s2[i]]
    count = len(s1[len(s2):])
    minC = count + (len(d) * 2)
elif(len(s1) < len(s2)):
    d = [i for i in range(min(len(s1), len(s2))) if s1[i] != s2[i]]
    count = len(s2[len(s1):])
    minC = count + (len(d) * 2)
else:
    d = [i for i in range(min(len(s1), len(s2))) if s1[i] != s2[i]]
    minC = len(d) * 2

if(minC <= k):
    print("Yes")
else:
    print("No")

