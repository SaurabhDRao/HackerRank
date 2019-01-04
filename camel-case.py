s = input()
if(len(s) == 0):
    print("0")
else:
    count = 1
    for x in s:
        if(x.isupper()):
            count += 1
    print(count)