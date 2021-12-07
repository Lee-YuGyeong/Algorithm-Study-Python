from collections import Counter
s = input().upper()
s = Counter(s).most_common()
if len(s)>1 and s[0][1] == s[1][1]:
    print("?")
else:
    print(s[0][0])