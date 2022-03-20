n = int(input())
s = input()
r = s.split('R')
b = s.split('B')

print(min(len(''.join(r[:-1])),len(''.join(r[1:])),len(''.join(b[:-1])),len(''.join(b[1:]))))




