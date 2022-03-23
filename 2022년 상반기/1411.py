from itertools import combinations

n = int(input())
ss = []
for _ in range(n):
    tmp = input()
    ss.append(tmp)

cnt=0

for s in list(combinations(ss,2)):
    dic = {chr(ord('a')+i):0 for i in range(26)}
    for i in range(len(s[0])):
        if dic[s[0][i]] == 0: # 바꾸지 않았으면
            if s[1][i] not in dic.values(): # 변경된 문자열이 존재하지 않으면
                dic[s[0][i]] = s[1][i] # 변경
            else: # 이미 바꾼 문자열이면
                break # 멈춤
        else: # 변경했으면
            if dic[s[0][i]] != s[1][i]: # 문자열이 다르면
                break # 멈춤
    else:
        cnt+=1
print(cnt)