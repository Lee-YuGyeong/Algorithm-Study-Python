n = int(input())

for _ in range(n):
    list1 = []
    list2 = []
    ss = list(input())
    for s in ss:
        if s == '<':
            if len(list1) != 0:
                list2.append(list1.pop())
        elif s=='>':
            if len(list2) != 0:
                list1.append(list2.pop())
        elif s=='-':
            if len(list1) != 0:
                list1.pop()
        else:
            list1.append(s)
    list2.reverse()
    print(''.join(list1)+''.join(list2))


