n,m = map(int,input().split())
apple = int(input())
m-=1 # 이후 계산을 편하게 하기 위해서 바구니 크기를 -1 해준다
left = 1 # 바구니 왼쪽 위치
right = left + m # 바구니 오른쪽 위치
answer=0
for _ in range(apple):
    tmp = int(input())
    if left <= tmp <= right: # 사과가 바구니 범위 안에 속하면 
        continue
    elif left > tmp: # 사과가 바구니보다 왼쪽에 떨어지면
        answer+= left - tmp # 왼쪽으로 이동한 거리만큼 답을 더해준다
        left = tmp # 왼쪽으로 이동
        right = left + m # 왼쪽으로 이동
    elif right < tmp: # 사과과 바구니보다 오른쪽에 떨어지면
        answer += tmp - right # 오른쪽으로 이동한 거리만큼 답을 더해준다
        right = tmp # 오른쪽으로 이동
        left = right - m # 오른쪽으로 이동
print(answer)