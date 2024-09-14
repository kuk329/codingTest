n = 4
a = [list(input()) for _ in range(n)]
k = int(input())

for _ in range(k):
    no, dir = map(int,input().split())
    no-=1 # 배열 인덱스는 0부터 시작이므로
    d = [0]*n # 각 톱니바퀴의 회전 방향을 저장하기 위한 배열
    d[no] = dir
    # 현재 톱니에서 왼쪽 톱니를 연쇄적으로 구함
    for i in range(no-1,-1,-1):
        if a[i][2] != a[i+1][6]:
            d[i] = -d[i+1] # 현재 톱니와 반대 방향으로 회전하는 정보를 저장
        else: # 하나라도 회전을 하지 않는 톱니가 나타나면 연쇄 회전은 중단
            break

    for i in range(no+1,n):
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i-1]
        else:
            break

    for i in range(n): # 각 톱니바퀴마다 회전 방향을 토대로 회전 시키기
        if d[i] == 0: # 0은 회전하지 않는 것을 의미
            continue
        if d[i] == 1: # 시계방향 회전
            temp = a[i][7]
            for j in range(7,0,-1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp
        elif d[i] ==-1: # 반시계방향 회전
            temp = a[i][0]
            for j in range(0,7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp


ans = 0
if a[0][0]=='1':
    ans+=1
if a[1][0]=='1':
    ans+=2
if a[2][0]=='1':
    ans+=4
if a[3][0]=='1':
    ans+=8

print(ans)

