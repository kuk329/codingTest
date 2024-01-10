import sys
input = sys.stdin.readline

N = int(input())
apart = []
visited = [[False]*N for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(N):
    apart.append(input())

# == 재귀 풀이 ==
def DFS(i,j,cnt):
    visited[i][j]=True
    for k in range(4):
        nx , ny = i + dx[k] , j + dy[k]
        if nx>=0 and nx<N and ny>=0 and ny<N:
            if visited[nx][ny]==False and apart[nx][ny]=="1":
                cnt+=1
                cnt=DFS(nx,ny,cnt)

    return cnt

ans = []
count = 0

for i in range(N):
    for j in range(N):
        if visited[i][j]==False and apart[i][j]=="1":
            cnt=DFS(i,j,1)
            count+=1
            ans.append(cnt)
ans.sort()

print(count)

for n in ans:
    print(n)