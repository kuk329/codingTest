N , M , K = map(int,input().split())
# N : 행 ,
d = [[0]*M for i in range(N)]

x = (K-1)//M
y = (K-1)%M

d[0][0] = 1

if K==0:
    for i in range(N):
        for j in range(M):
            if j-1>=0:
                d[i][j]+=d[i][j-1]
            if i-1>=0:
                d[i][j]+=d[i-1][j]

    print(d[N-1][M-1])
else:
    result = 1
    for i in range(x+1):
        for j in range(y+1):
            if j-1>=0:
                d[i][j]+=d[i][j-1]
            if i-1>=0:
                d[i][j]+=d[i-1][j]

 #   print(d)
    result *= d[x][y]
    d = [[0] * M for i in range(N)]
    d[x][y] = 1

    for i in range(x,N):
        for j in range(y,M):
            if j-1>=0:
                d[i][j] +=d[i][j-1]
            if i-1>=0:
                d[i][j]+=d[i-1][j]

    result *= d[N-1][M-1]
    print(result)

