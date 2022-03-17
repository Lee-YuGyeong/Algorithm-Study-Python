n = int(input())
arr = input().split()

p1_m,p1_j = n,0 # BNP 전략
p2_m,p2_j = n,0 # TIMING 전략
p2_arr = []

arr = list(map(int,arr))

for cost in arr:
    # BNP 전략
    p1_j += p1_m//cost # 살 수 있는만큼 매수
    p1_m = p1_m%cost # 매수하고 남은 돈

    # TIMING 전략
    p2_arr.append(cost)
    if len(p2_arr) >= 4: 
        if p2_arr[0] > p2_arr[1] > p2_arr[2]: # 3일 연속 하락하면 다음날 가격으로 매수
            p2_j += p2_m//cost # 살 수 있는만큼 매수
            p2_m = p2_m%cost # 매수하고 남은 돈
        elif p2_arr[0] < p2_arr[1] < p2_arr[2]: # 3일 연속 상승하면 다음날 가격으로 매도
            p2_m += p2_j*cost # 전량 매도
            p2_j = 0 
        p2_arr.pop(0)

if p1_m + arr[-1]*p1_j > p2_m + arr[-1]*p2_j:
    print('BNP')
elif p1_m + arr[-1]*p1_j < p2_m + arr[-1]*p2_j:
    print('TIMING')
else:
    print('SAMESAME')
    
