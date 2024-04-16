from collections import deque

N, M, T = map(int, input().split())
castle = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    castle.append(tmp)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
hour = [[-1] * M for _ in range(N)]


def normal():
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    hour[0][0] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False and castle[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    hour[nx][ny] = hour[x][y] + 1

    if hour[N-1][M-1]==-1: # 출구에 갈수가 없을때
        return T + 1
    else:
        return hour[N-1][M-1]


def sword():
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    hour[0][0] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]==False:
                if castle[nx][ny] == 2:
                    dis = hour[x][y] + 1 + (N - 1) + (M - 1) - (nx + ny)
                    return dis
                elif castle[nx][ny] == 1:
                    continue
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    hour[nx][ny] = hour[x][y] + 1

    if hour[N-1][M-1]==-1: # 출구에 갈수가 없을때
        return T + 1
    else:
        return hour[N-1][M-1]


first = normal()
hour = [[-1] * M for _ in range(N)]
second = sword()
result = min(first, second)

if result > T:
    print('Fail')
else:
    print(result)
