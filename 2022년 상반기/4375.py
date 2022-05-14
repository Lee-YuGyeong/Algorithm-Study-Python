while True:
    try:
        n = int(input())
    except:
        break
    a = '1'
    while True:
        if int(a)%n==0:
            print(len(a))
            break
        else:
            a+='1'
