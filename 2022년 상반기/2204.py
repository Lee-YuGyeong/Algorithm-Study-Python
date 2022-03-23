while True:
    n = int(input())
    if n==0: break
    arr = []
    for _ in range(n):
        ss = input()
        arr.append([ss.upper(),ss])
    print(sorted(arr,key = lambda x : (x[0]))[0][1])