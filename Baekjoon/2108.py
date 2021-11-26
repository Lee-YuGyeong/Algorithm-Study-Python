import sys
input = sys.stdin.readline
n = int(input())
dic={}
arr=[]
for _ in range(n):
    m = int(input())
    if m in dic: dic[m]+=1
    else : dic[m]=1
    arr.append(m)

dic = sorted(dic.items(),key=lambda x:(-x[1],x[0]))
print(int(round(sum(arr)/n,0)))
print(sorted(arr)[n//2])
if len(dic)<2:
    print(dic[0][0])
else:
    if dic[0][1] == dic[1][1]:
        print(dic[1][0])
    else:
        print(dic[0][0])
print(max(arr)-min(arr))

