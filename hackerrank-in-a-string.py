t = int(input())
for i in range(t):
    s = input()
    h = "hackerrank"
    flag = 0
    p = 0
    for j in range(len(s)):
        if(s[j] == h[p]):
            p += 1
            if(p == len(h)):
                break
    print("YES" if(p == len(h)) else "NO")

