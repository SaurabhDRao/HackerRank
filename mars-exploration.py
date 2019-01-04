import re

s = "SOS"
l = re.findall("...", input())
count = 0
for x in l:
    count += len([i for i in range(3) if(s[i] != x[i])])

print(count)