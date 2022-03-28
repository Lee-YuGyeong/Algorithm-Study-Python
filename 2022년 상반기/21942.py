import sys
input = sys.stdin.readline

n,l,f = input().split()
n = int(n)
f = int(f)
x = l.split('/')
y = x[1].split(':')
l = int(x[0]) * 24* 60 + int(y[0]) * 60 + int(y[1])

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
time = [0]*n
dic = {}
result = {}
for i in range(n):
    arr = input().split()
    y,m,d = arr[0].split('-')
    time[i] = (sum(day[:int(m)]) + int(d)) * 24 * 60
    h,m = arr[1].split(':')
    time[i] += (int(h) * 60 + int(m)) # 시간 구해줌
    ss = arr[2] + '/' + arr[3] # 부품이름/동아리 회원 닉네임
    if ss in dic: # 딕셔너리에 있으면 반납하는 것
        tmp = time[i] - dic[ss] - l # 빌린 시간 - 벌금 부여 시간
        del dic[ss] # 반납했으므로 삭제
        if tmp > 0: # 벌금을 내야하면 result 딕셔너리에 벌금 추가하기
            if arr[3] not in result: 
                result[arr[3]] = tmp * f
            else:
                result[arr[3]]+= tmp * f
    else: # 딕셔너리에 없으면 빌리는 것
        dic[ss] = time[i]


if len(result): 
    for i in sorted(result.items(),key=lambda x:x[0]):
        print(*i)
else: print(-1)

