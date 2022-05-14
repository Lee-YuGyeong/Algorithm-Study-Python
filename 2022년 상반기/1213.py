from collections import Counter
ss = list(input())

dic = Counter(ss)
cnt=0
answer=[]
one = ''
for d in dic:
    for i in range(dic[d]//2):
        answer.append(d)
    if dic[d]%2!=0:
        if cnt==1:
            print("I'm Sorry Hansoo")
            break
        else:
            cnt+=1
            one=d

else:
    answer.sort()
    print('%s%s%s'%(''.join(answer),one,''.join(answer[::-1])))
    

    
    

    