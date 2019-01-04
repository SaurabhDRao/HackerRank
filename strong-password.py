import re

n = int(input())
s = input()
p1 = "[0-9]"
p2 = "[a-z]"
p3 = "[A-Z]"
p4 = "[^0-9a-zA-Z]"
count1 = 0
if(len(s) < 6):
    count1 += 6 - len(s)

count2 = 0
if(re.findall(p1, s) == []):
    count2 += 1
if(re.findall(p2, s) == []):
    count2 += 1
if(re.findall(p3, s) == []):
    count2 += 1
if(re.findall(p4, s) == []):
    count2 += 1

print(max(count1, count2))