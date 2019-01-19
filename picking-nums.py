def isLeap(y):
    if(y >= 1919):
        if((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)):
            return True
    elif(y >= 1700):
        if(y % 4 == 0):
            return True
    else:    
        return False 

y = int(input())
if(isLeap(y)):
    print("12.09." + str(y))
elif(y == 1918):
    print("26.09.1918")
else:
    print("13.09." + str(y))