def buildMap(s):
    m = {}
    for c in s:
        if(c not in m):
            m[c] = 1
        else:
            m[c] += 1
    return m

def anagram(s):
    if(len(s) % 2 == 1):
        return -1
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    m1 = buildMap(s1)
    m2 = buildMap(s2)

    count = 0
    for key in m2.keys():
        if(key not in m1):
            count += m2[key]
        else:
            count += max(0, m2[key] -m1[key])

    return count

t = int(input())

for _ in range(t):
    s = input()
    print(anagram(s))
