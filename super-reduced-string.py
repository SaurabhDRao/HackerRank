s = input()
i = 1

while(i < len(s)):
    if(s[i] == s[i - 1]):
        s = s[0 : i - 1] + s[i + 1 : ]
        i = 0
    i += 1

if(s != ""):
    print(s)
else:
    print("Empty String")