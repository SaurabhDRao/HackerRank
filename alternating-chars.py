t = int(input())

for _ in range(t):
    s = list(input())
    c = s[0]
    count = 0
    i = 1
    while(i < len(s)):
        try:
            while(c == s[i]):
                s[i] = '0'
                count += 1
                i += 1
            c = s[i]
            i += 1
        except:
            break
    print(count)