N = int(input())

d = [[0]*3 for i in range(N+1)]

d[1][0] = 1 # [X,X]
d[1][1] = 1 # [0,X]
d[1][2] = 1 # [X,0]

MOD = 9901


for i in range(2,N+1):
    d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2])%MOD
    d[i][1] = (d[i-1][0] + d[i-1][2])%MOD
    d[i][2] = (d[i-1][0] + d[i-1][1])%MOD 

ans = d[N][0] + d[N][1] + d[N][2]

print(ans%9901)