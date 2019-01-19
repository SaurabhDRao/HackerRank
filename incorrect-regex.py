from re import search

t = int(input())
for _ in range(t):
    s = input()
    try:
        search(s, "hello wrld")
        print("True")
    except:
        print("False")