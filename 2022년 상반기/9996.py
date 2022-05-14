n = int(input())
ss = list(input().split('*'))
for i in range(n):
    aa = input()
    if len(ss[0])+len(ss[1])<=len(aa):
        for a,b in zip(ss[0],aa):
            if a!=b: 
                print('NE')
                break
        else:
            for a,b in zip(ss[1][::-1],aa[::-1]):
                if a!=b: 
                    print('NE')
                    break
            else:
                print('DA')
    else:
        print('NE')
    