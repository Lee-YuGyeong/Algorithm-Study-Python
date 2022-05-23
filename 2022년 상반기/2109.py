import sys
import heapq
n = int(input())
money = 0
arr = []
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    arr.append([tmp[0],tmp[1]])

arr = sorted(arr,key=lambda x: (x[1])) # 데드라인 오름차순

queue = []

for pay,day in arr:
    heapq.heappush(queue,pay)

    if day < len(queue): # 날짜보다 queue의 길이가 더 크면 
        heapq.heappop(queue) # 최소금액 pop

print(sum(queue))