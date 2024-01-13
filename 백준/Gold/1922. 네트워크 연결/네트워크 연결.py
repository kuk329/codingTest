# 모든 컴퓨터를 연결하는데 최소 비용 구하기 -> 간선의 가중치가 다 다를 때 -> MST -> 프림 or 크루스칼 
import heapq
import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터 수 (노드 수)
M = int(input()) # 간선 수 

edges = [[] for _ in range(N+1)] # 간선 정보 저장
for _ in range(M):
    u,v,c = map(int,input().split())
    edges[u].append((c,v))
    edges[v].append((c,u))


def prim():
    # 우선 순위 큐에 비용정보를 저장
    heap = []
    used_edges = 0
    result = 0
    visited = [False]*(N+1) # 방문한 정점 체크
    visited[1] = True # 정점 1부터 방문

    for cost,edge in edges[1]: # 정점 1번과 연결된 간선(정점,가중치) 정보 꺼내서 min heap에 저장
        heapq.heappush(heap,(cost,edge))

    while used_edges<N-1: # 간선은 N-1 개 선택해야됨.
        cost , edge  = heapq.heappop(heap) # 우선순위가 가장 높은 정보 하나 출력
        if visited[edge]:
            continue
        visited[edge] = True

        result += cost
        used_edges += 1

        for adj_cost,adj_edge in edges[edge]:
            if not visited[adj_edge]:
                heapq.heappush(heap,(adj_cost,adj_edge))

    return result


    
# 정답 출력

print(prim())