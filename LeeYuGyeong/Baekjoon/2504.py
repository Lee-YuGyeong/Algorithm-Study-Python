str = input()

l = []
sol=1
for i,s in enumerate(str):
    if s == ')' and l[-1] =='(':
        if str[i-2] == '(' or str[i-2] == '[':
            print(str[i-2])
            sol*=2
            print("*2")
        else:
            sol+=2
            print("+2")
        l.pop(-1)
    elif s == ']' and l[-1] == '[':
        print(str[i-2])
        if str[i-2] == '(' or str[i-2] == '[':
            sol*=3
            print("*3")
        else:
            sol+=3
            print("+3")
        l.pop(-1)
    elif s=='(' or s=='[':
        l.append(s)
    else:
        print("error")
        break
    print(sol)