n = int(input())
s = list(input())
k = int(input())

az = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(s)):
    if(s[i].isalpha()):
        r = ""
        x = s[i]
        for j in range(len(x)):
            ind = az.index(x[j].lower())
            t = az[(ind + k) % 26]
            if(x[j].isupper()):
                t = t.upper()
            r += t
        s[i] = r
print("".join(s))

