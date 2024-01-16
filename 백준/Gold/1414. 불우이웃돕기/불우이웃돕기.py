# 최단거리를 구하기 -> MST
# 크루스칼 or 프림

# print(ord('A')) # A : 65
# print(ord('a')) # a : 97

# 소문자는 ord('')-96
# 대문자는 ord('')-38

import heapq
import string
import sys

input = sys.stdin.readline

n = int(input())
arr = []
entire = 0
for _ in range(n):
    arr.append(list(input()))

edges = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] in string.ascii_lowercase:
            tmp = ord(arr[i][j]) - 96
            entire += tmp
            edges[i].append((tmp, j))  # 비용과 연결된 정점 정보 저장
            edges[j].append((tmp, i))
        if arr[i][j] in string.ascii_uppercase:
            tmp = ord(arr[i][j]) - 38
            entire += tmp
            edges[i].append((tmp, j))  # 비용과 연결된 정점 정보 저장
            edges[j].append((tmp, i))

heap = []
visited = [False] * n
visited[0] = True

for cost, edge in edges[0]:
    heapq.heappush(heap, (cost, edge))

min_cost = 0  # 최소 비용 저장
used_edges = 0  # 선택한 간선 개수

while heap:
    cost, edge = heapq.heappop(heap)
    if visited[edge]:
        continue

    visited[edge] = True
    min_cost += cost
    used_edges += 1
    if used_edges==n-1:
        break


    for adj_cost, adj_edge in edges[edge]:
        if not visited[adj_edge]:
            heapq.heappush(heap, (adj_cost, adj_edge))

for i in range(n):  # 방문을 안한 컴퓨터가 있으면
    if not visited[i]:
        print(-1)
        break
else:
    print(entire - min_cost)
