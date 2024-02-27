

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N,M = map(int,input().split())
a = [input() for _ in range(N)]

dist = [[0]*M for _ in range(N)] # 사이클의 출발 지점과의 거리 저장
check = [[False]*M for _ in range(N)] # 해당 정점 방문 여부

def cycle(x, y, cnt, color):
    if check[x][y]:
        if cnt-dist[x][y] >= 4:
            return True
        else:
            return False
    check[x][y] = True
    dist[x][y] = cnt
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if a[nx][ny] == color:
                if cycle(nx,ny,cnt+1,color):
                    return True
    return False


for i in range(N):
    for j in range(M):
        if check[i][j]: # 이미 방문한 정점이면 pass
            continue
        dist = [[0]*M for _ in range(N)] # 거리 배열 초기화
        ok = cycle(i,j,1,a[i][j])
        if ok:
            print('Yes')
            exit()
print('No')