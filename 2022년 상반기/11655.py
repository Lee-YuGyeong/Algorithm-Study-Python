ss = list(input())

for i,s in enumerate(ss):
    if 'a' <= s <= 'z':
        if 'a' <= chr(ord(s)+13) <= 'z':
            ss[i] = chr(ord(s)+13)
        else:
            ss[i] = chr(ord(s)-13)
    if 'A' <= s <= 'Z':
        if 'A' <= chr(ord(s)+13) <= 'Z':
            ss[i] = chr(ord(s)+13)
        else:
            ss[i] = chr(ord(s)-13)

print(''.join(ss))