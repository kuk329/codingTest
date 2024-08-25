N , S , M = map(int,input().split())

V = [0] + list(map(int,input().split()))
dp = [[False]*(M+1) for i in range(N+1)]

min_v = S - V[1]
max_v = S + V[1]

if min_v >=0:
    dp[1][min_v] = True
if max_v <= M:
    dp[1][max_v] = True


for i in range(2,N+1):
    for j in range(M+1):
        if dp[i-1][j]: # v == True
            max_v = j + V[i]
            min_v = j - V[i]
            if max_v <= M:
                dp[i][max_v]=True
            if min_v >= 0:
                 dp[i][min_v]= True


result = -1
for k in range(M+1):
    if dp[N][k]:
        result = k

#print(dp[N])
print(result)
