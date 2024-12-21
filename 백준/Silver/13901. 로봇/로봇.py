R,C = map(int,input().split())
K = int(input())

obstacle = [[0]*C for i in range(R)] # 격자판 정보 저장
tmp = [(0,0),(-1,0),(1,0),(0,-1),(0,1)] #  상 , 하, 좌 , 우
dx = []
dy = []



for _ in range(K):
    a,b = map(int,input().split())
    obstacle[a][b] = 1 # 장애물 놓기

s,r = map(int,input().split()) # 시작 위치


tmp2 = list(map(int,input().split()))

for n in tmp2:
    x, y = tmp[n]
    dx.append(x)
    dy.append(y)

# 현재 위치
ex = s
ey = r
obstacle[ex][ey] = 1 # 시작 위치 방문 처리
finish = False
dir = 0 # 현재 이동 방향

cnt = 0

while True:
    # 현재 사용자 지정 방향으로 이동할 수 있는지 확인
    nx = ex + dx[dir]
    ny = ey + dy[dir]
    if nx >= 0 and nx < R and ny >= 0 and ny < C and obstacle[nx][ny] != 1:

        ex = nx # 해당 위치로 이동
        ey = ny
        obstacle[ex][ey] = 1 # 해당 위치 방문 처리
        cnt = 0
    else:
        dir = (dir+1) % 4 # 갈 수 없을때는 방향 전환
        cnt +=1
    if cnt == 4:
        break



print(ex,ey)



