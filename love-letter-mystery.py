t = int(input())

for _ in range(t):
    s = input()
    count = 0
    for i in range(len(s) // 2):
        count += abs(ord(s[i]) - ord(s[len(s) - i - 1]))
    print(count)
