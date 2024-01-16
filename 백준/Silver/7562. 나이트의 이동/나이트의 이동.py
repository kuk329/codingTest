from collections import deque
import sys
input = sys.stdin.readline
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

n= int(input())
for _ in range(n):
    l=int(input())
    now_x,now_y=map(int,input().split())
    goal_x,goal_y=map(int,input().split())
    dist=[[-1]*l for _ in range(l)]
    q= deque()
    q.append((now_x,now_y))
    dist[now_x][now_y] = 0
    while q:
        x,y = q.popleft()
        for k in range(8):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<l and 0<=ny<l:
                if dist[nx][ny]==-1:
                    q.append((nx,ny))
                    dist[nx][ny]=dist[x][y]+1

    print(dist[goal_x][goal_y])