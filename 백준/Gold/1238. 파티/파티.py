# 단방향 도로 
# i번째 길을 지나는데 Ti시간 소요
# 최단거리 구하기 -> 모든 정점에서 모든 x 최단거리 -> 다익스트라
# 최소중 최대 
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N,M,X = map(int,input().split())
edge =[[] for _ in range(N)]
for _ in range(M):
    u,v,c = map(int,input().split()) # u->v
    edge[u-1].append((v-1,c)) # 단방향



def dijkstra_pq(graph, start):
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

max_distance = 0
for i in range(N): # 각 노드별로 시작 0 ~ N-1
    go=dijkstra_pq(edge,i) # 갈때
    back = dijkstra_pq(edge,X-1) # 올때
    max_distance = max(go[X-1]+back[i],max_distance)

print(max_distance)