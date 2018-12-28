def kaprekar(n):
    if(n >= 1 and n <= 9):
        if(n == 1 or n == 9):
            return True
        else:
            return False

    s = str(n * n)
    if(int(s[:len(s) // 2]) + int(s[len(s) // 2:]) == n):
        return True
    else:
        return False

p = int(input())
q = int(input())
flag = 0
for i in range(p, q + 1):
    if(kaprekar(i)):
        print(i, end=" ")
        flag = 1

if(flag == 0):
    print("INVALID RANGE")