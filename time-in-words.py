h = int(input())
m = int(input())

numToWords = [
    "o' clock",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "quarter",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
    "twenty one",
    "twenty two",
    "twenty three",
    "twenty four",
    "twenty five",
    "twenty six",
    "twenty seven",
    "twenty eight",
    "twenty nine",
    "half"
]
if(m == 0):
    print(numToWords[h], numToWords[0])
elif(m >= 1 and m <= 30):
    s = ""
    if(m == 1):
        s = numToWords[1] + " minute"
    elif(m == 15):
        s = numToWords[15]
    elif(m == 30):
        s = numToWords[30]
    else:
        s = numToWords[m] + " minutes"
    print(s, "past", numToWords[h])
else:
    d = 60 - m
    s = ""
    if(d == 1):
        s = numToWords[1] + " minute"
    elif(d == 15):
        s = numToWords[15]
    elif(d == 30):
        s = numToWords[30]
    else:
        s = numToWords[d] + " minutes"
    print(s, "to", numToWords[(h + 1) % 12])