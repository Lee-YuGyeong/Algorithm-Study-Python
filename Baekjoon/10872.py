n = int(input())

def cal(n):
    if n<=1:
        return n
    return cal(n-1)+cal(n-2)

print(cal(n))