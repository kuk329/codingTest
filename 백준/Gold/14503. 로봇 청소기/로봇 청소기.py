n,m = map(int,input().split())
x,y,dir = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

#    북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 0 # 청소를 한 칸의 개수

while True:
    if a[x][y]==0: # 현재 로봇 청소기가 있는 칸의 위치가 청소를 안한 빈칸일 경우
        a[x][y]=2 # 청소 처리
        cnt+=1

    # 주변 4칸중 청소되지 않은 빈 칸이 없는 경우
    if a[x-1][y]!=0 and a[x+1][y]!=0 and a[x][y-1]!=0 and a[x][y+1]!=0:
        nx = x - dx[dir]
        ny = y - dy[dir] 
        if a[nx][ny] == 1: # 벽이면 청소 중지
            break
        else: # 벽이 아니면 청소기 위치 이동
            x = nx
            y = ny 
    else: # 주변 4칸중 청소되지 않은 빈 칸이 하나라도 있는 경우
        dir = ( dir + 3 ) % 4 # 반 시계방향으로 90도 회전
        nx = x + dx[dir]
        ny = y + dy[dir]
        if a[nx][ny] == 0: # 90도 회전후 앞쪽 칸이 청소되지 않은 빈칸인 경우 전진
            x = nx
            y = ny
        
print(cnt)