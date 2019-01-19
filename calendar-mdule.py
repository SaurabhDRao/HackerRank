# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m, d, y = [int(x) for x in input().split()]
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())