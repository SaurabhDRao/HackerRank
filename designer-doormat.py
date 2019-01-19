# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = [int(x) for x in input().split()]
o = 1
for i in range(n // 2):
    a = "-" * ((m - (3 * o)) // 2)
    b = ".|." * o
    print(a + b + a)
    o += 2
print(("-" * ((m - 7) // 2)) + "WELCOME" + ("-" * ((m - 7) // 2)))
for i in range(n // 2):
    o -= 2
    a = "-" * ((m - (3 * o)) // 2)
    b = ".|." * o
    print(a + b + a)