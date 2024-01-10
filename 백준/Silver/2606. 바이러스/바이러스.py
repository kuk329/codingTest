n=int(input())
m=int(input())
network=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)
    
count = 0 #1번 컴을 통해 감염된 컴퓨터 수

def bfs(s):
    global count
    visited[s]=True
    for computer in network[s]:
        if visited[computer]==False:
            count+=1
            bfs(computer)
            
bfs(1)
print(count)

