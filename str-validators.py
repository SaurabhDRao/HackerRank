s = input()

aln, al, d, lc, uc = 0, 0, 0, 0, 0 
for c in s:
    if(c.isalnum()):
        aln = 1
    if(c.isalpha()):
        al = 1
    if(c.isdigit()):
        d = 1
    if(c.islower()):
        lc = 1
    if(c.isupper()):
        uc = 1
    if(aln == 1 and al == 1 and d == 1 and lc == 1 and uc == 1):
        break

if(aln == 1):
    print("True")
else:
    print("False")

if(al == 1):
    print("True")
else:
    print("False")

if(d == 1):
    print("True")
else:
    print("False")

if(lc == 1):
    print("True")
else:
    print("False")

if(uc == 1):
    print("True")
else:
    print("False")