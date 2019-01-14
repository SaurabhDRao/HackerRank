n = int(input())
onos = []
prep = []
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    onos.append(a)
    prep.append(b)

st = {}
for i in range(n):
    st[i + 1] = onos[i] + prep[i]

print(" ".join([str(x) for x in sorted(st, key = st.__getitem__)]))
