# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    try:
        a, b = [int(x) for x in input().split()]
        print(a // b)
    except ZeroDivisionError as zde:
        print("Error Code: integer division or modulo by zero")
    except ValueError as ve:
        print("Error Code:", ve)
