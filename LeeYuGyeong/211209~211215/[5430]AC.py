import sys
input=sys.stdin.readline

T = int(input())
for _ in range(T):
    s = list(input())
    n = int(input())
    if n==0:
        arr = input()
        if 'D' in s: # 길이가 0인데 D가 있을 경우 에러 발생
            print("error")
            continue
        else: # 길이가 0인데 D가 없을 경우에는 []출력
            print("[]") 
            continue
    arr = list(input()[1:-2].split(',')) # 앞 뒤 []을 잘라주고 ,로 나눠준다.
    isRe = False # reverse 여부
    start,end=0,0 # index 선언
    for index in s[:-1]:
        if index=="R":
            isRe = not isRe
        else:
            if n==0:
                print("error")
                break
            n-=1
            if isRe: end+=1
            else: start+=1
    else:
        if isRe:
            arr.reverse()
            if start==0: arr = arr[end:]
            else: arr = arr[end:-start]
        else:
            if end==0: arr = arr[start:]
            else: arr = arr[start:-end]
        print("["+",".join(arr)+"]")

            

