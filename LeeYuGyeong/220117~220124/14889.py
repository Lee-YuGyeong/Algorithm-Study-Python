from itertools import permutations,combinations
import sys
input = sys.stdin.readline

n = int(input())
score=[]
for _ in range(n):
    score.append(list(map(int,input().split())))
team_range = [i for i in range(n)]
team = list(combinations(team_range,n//2)) # 조합 가능한 팀을 구함
start,link = 0,0

def cal(arr): # 팀의 점수를 계산하는 함수
    tot = []
    for a,b in combinations(arr,2):
        tot.append(score[a][b])
        tot.append(score[b][a])
    return sum(tot)

mininum = 10**9
cnt=0
for a,b in zip(team,team[::-1]): # 팀 점수가 최소인 것을 구함
    if cnt==len(team)//2-1: break
    mininum = min(mininum,abs(cal(a) - cal(b)))
print(mininum)