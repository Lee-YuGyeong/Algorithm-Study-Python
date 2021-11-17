def solution(sizes):
    for s in sizes:
        if s[0] > s[1] : s[0],s[1] = s[1],s[0]
    
    return max([s[0] for s in sizes]) * max([s[1] for s in sizes])