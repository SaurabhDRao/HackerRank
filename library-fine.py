d1, m1, y1 = [int(x) for x in input().split()]
d2, m2, y2 = [int(x) for x in input().split()]

daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
fine = 0

if(y1 == y2 and m1 == m2 and d1 > d2):
    fine = 15 * (d1 - d2)
elif(y1 == y2 and m1 > m2):
    fine = 500 * (m1 - m2)
elif(y1 > y2):
    fine = 10000
    
print(fine)