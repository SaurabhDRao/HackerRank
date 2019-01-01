s, n, m = map(int, input().split())

keyboard = sorted(map(int, input().split()), reverse=True)
usb = sorted(map(int, input().split()))

i = j = 0
ans = -1

for i in keyboard:
    for j in usb:
        if i + j > s:
            break
        ans = max(ans, i + j)

print(ans)