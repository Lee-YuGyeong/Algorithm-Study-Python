n = int(input())
dic = {chr(ord('a')+i):0 for i in range(26)}

for i in range(n):
    s = input()
    dic[s[:1]]+=1

sol = ''.join(sorted(list(s for s in dic if dic[s] >= 5)))
print(sol if sol else 'PREDAJA')

