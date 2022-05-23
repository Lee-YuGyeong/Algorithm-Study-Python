import heapq
import sys

n = int(input())
arr = []
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    arr.append(tmp)

arr = sorted(arr,key=lambda x:x[0]) # 데드라인 기준으로 오름차순

queue = []

for day,count in arr: 
    heapq.heappush(queue,count) # 컵라면 개수를 넣어준다
    if day < len(queue): # 만약 큐의 길이가 날짜보다 크면
        heapq.heappop(queue) # 가장 작은 컵라면 개수를 빼준다

print(sum(queue))

