a = int(input())

for i in range(a):
    b = int(input())
    cnt=0
    while (b!=0):
        if b%2 == 1: 
            print(cnt,end=" ")
        b = b//2
        cnt+=1
    print()
    20212.11