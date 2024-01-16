import sys
from collections import deque 
input = sys.stdin.readline

n = int(input())
arr =[]

for _ in range(n):
    arr.append(list(input())) # 문자 배열로 저장.

dx = [1,-1,0,0]
dy = [0,0,1,-1]



def dfs(i,j):
    global visited
    q = deque()
    visited[i][j] = True
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and arr[x][y]==arr[nx][ny]:
                if not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True

ans1 = 0 
visited= [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            ans1 +=1

ans2 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]=="R":
            arr[i][j]="G"


visited= [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            ans2+=1

print(ans1,ans2)


