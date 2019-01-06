s = set(input().lower())
az = set("abcdefghijklmnopqrstuvwxyz")
if(s.intersection(az) == az):
    print("pangram")
else:
    print("not pangram")