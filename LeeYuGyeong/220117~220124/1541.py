a = input().split('-') #-로 나누어줌
num = []
for i in a: # 나눈 문자 순회
    cnt = 0 
    s = i.split('+') # +로 나눔
    for j in s: # +로 나눈 문자열을 순회하면서
        cnt += int(j) # cnt에 더하기
    num.append(cnt) # 계산한 숫자를 리스트에 넣기
n = num[0] # 첫 숫자에서 빼기 위해서 첫 숫자로 초기화
for i in range(1, len(num)):
    n -= num[i] # 빼주기
print(n)