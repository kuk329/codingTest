A,B = map(int,input().split())

count = 1 # 출력값에 1 더함.

while A<=B:
    if A == B:
        print(count)
        exit() # 종료
    if B%2 == 0:  # 짝수일때
        B = B//2
    elif B%10 == 1: # 맨 끝에 자리가 1일때
        B = (B-1)//10
    else: # 이도 저도 아닐때. (만들기 불가능 한 값일때)
        break # while 문 빠져나와서 -1 출력

    count +=1
print(-1)
