def buildMap(s):
    d = {}
    for c in s:
        if(c not in d):
            d[c] = 1
        else:
            d[c] += 1
    return d

s1 = input()
s2 = input()
s3 = [x for x in s1 if(x in s2)]
s4 = [x for x in s2 if(x in s1)]

d1 = buildMap(s3)
d2 = buildMap(s4)

count = (len(s1) - len(s3)) + (len(s2) - len(s4))
for c in d1:
    count += (abs(d1[c] - d2[c]))
    

print(count)