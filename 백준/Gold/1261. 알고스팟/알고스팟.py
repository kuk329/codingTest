from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m,n = map(int,input().split()) # m : 가로, n : 세로
a=[list(map(int,list(input()))) for _ in range(n)]
dist = [[-1]*m for _ in range(n)] # 해당 지점에 벽을 몇개 부수어야 갈수있는지를 저장. 


# ---- 초기값 ---- 
q = deque()
nxt_q = deque()
q.append((0,0))
dist[0][0] = 0

while q:
    x,y = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1: # 방문을 안했을경우만
                if a[nx][ny] == 0: # 벽이 없는 곳으로 이동
                    dist[nx][ny] = dist[x][y]
                    q.append((nx,ny))
                else:    # 벽을 부숨.
                    dist[nx][ny] = dist[x][y] + 1
                    nxt_q.append((nx,ny))


    if not q: # 가장 적에 벽을 부수고 갈수있는 지점을 모두 방문
        q = nxt_q
        nxt_q = deque()


            
print(dist[n-1][m-1])

