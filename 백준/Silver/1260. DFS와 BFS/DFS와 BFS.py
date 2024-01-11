from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
adj = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(n+1):
    adj[i].sort() # 간선을 오름차순으로 정렬

#print(adj)

def dfs(v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in adj[v]:
        if not visited[i]:
            dfs(i,visited)

def bfs(v):
    visited=[False]*(n+1)
    q = deque()
    q.append(v)
    visited[v]=True # 방문 처리
    while q:
        x = q.popleft()
        print(x,end=' ')
        for i in adj[x]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
        


visited=[False]*(n+1)
dfs(v,visited)
print()
bfs(v)