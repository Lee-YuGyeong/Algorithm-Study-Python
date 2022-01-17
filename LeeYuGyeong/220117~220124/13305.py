n = int(input())
dis = list(map(int,input().split()))
cost = list(map(int,input().split()))

sol=0
now = cost[0]
for c,d in zip(cost,dis): # 가격과 거리를 하나씩 가져온다.
    if now > c: # 현재 가격이 이제 도착한 주유소의 가격보다 비싸면
        now = c # 가격 갱신
    sol+=now*d # 계산
print(sol)