import sys
input = sys.stdin.readline

N = int(input())

tri = []

for _ in range(N):
    tri.append(list(map(int, input().split())))

dp = [[0] * (i + 1) for i in range(N)]
dp[0][0] = tri[0][0]


for x in range(1,N):
    for y in range(len(tri[x])):
        if y-1 >=0:
            dp[x][y] = dp[x-1][y-1]
        if y < len(tri[x-1]):
            dp[x][y] = max(dp[x][y],dp[x-1][y])

        dp[x][y] += tri[x][y]


print(max(dp[N-1]))