import sys
input = sys.stdin.readline

# 1. 필요한 값을 입력 및 초기화
E, S, M = map(int,input().split())
temp = [1,1,1]
cnt = 1

# 2. 주어진 조건에 따라 만족하는 값 찾기
while True:
    if E==temp[0] and S==temp[1] and M==temp[2]:
        break

    # E S M 하나씩 증가
    temp[0]+=1
    temp[1]+=1
    temp[2]+=1
    if temp[2]==20:
        temp[2]=1
    if temp[1]==29:
        temp[1]=1
    if temp[0]==16:
        temp[0]= 1
    cnt+=1

# 3. 결과값 출력
print(cnt)