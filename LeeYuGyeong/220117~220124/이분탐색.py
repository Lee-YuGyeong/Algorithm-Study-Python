def binary_search(a,x):
    start = 0
    end = len(a) -1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x :
            end = mid - 1
        else:
            start = mid + 1


d = [1,2,4,6,8,13,35,60]
print(binary_search(d,13))