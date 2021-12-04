n = int(input())

def h(n,position):
    if n==1:
        print(1,3)
        return
    if position ==2:
        h(n-1,3)
        print(1,2)
    elif position==3:
        h(n-1,2)
        print(1,3)
h(n,3)