from collections import Counter

x = sorted(input())

c = Counter(x).most_common(3)

[print(k,v) for k,v in c]