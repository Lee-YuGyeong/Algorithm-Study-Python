import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
arr=[]
for _ in range(n):
    m = int(input())
    arr.append(m)
arr.sort()
arr2 = Counter(arr).most_common()
print(round(sum(arr)/n))
print(sorted(arr)[n//2])
if len(arr2)<2:
    print(arr2[0][0])
else:
    if arr2[0][1] == arr2[1][1]:
        print(arr2[1][0])
    else:
        print(arr2[0][0])
print(max(arr)-min(arr))

