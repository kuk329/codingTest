from collections import deque 

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]

t = int(input())

def bfs(i,j,chess,z,w,d):
    d[i][j]=0 # 거리 초기화
    chess[i][j] = 1 # 방문 처리
    q= deque()
    q.append((i,j))

    while q:
        x,y = q.popleft()
        if x==z and y==w:
            break
        for k in range(8):
            nx,ny = x+dx[k],y+dy[k]
            if nx>=0 and nx<l and ny>=0 and ny<l:
                if chess[nx][ny]==0:
                    d[nx][ny]=d[x][y]+1
                    chess[nx][ny]=1
                    q.append((nx,ny))


for _ in range(t):
    l = int(input())
    chess = [[0]*l for _ in range(l)] # 체스판 초기화
    d=[[0]*l for _ in range(l)]
    x,y = map(int,input().split())
    z,w = map(int,input().split())
    bfs(x,y,chess,z,w,d)
    print(d[z][w])


