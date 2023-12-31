# d[i][j] : 길이가 i 이고 마지막 자리가 j로 끝 나는 계단수 개수
# 0<=j<=9
MOD = 1_000_000_000

n = int(input()) # 1 ~ 100

d=[[0]*10 for _ in range(n+1)]

for i in range(1,10):
    d[1][i]=1

for i in range(2,n+1):
    for j in range(10):
        if j==0:
            d[i][j] = d[i-1][j+1]
        elif j==9:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = d[i-1][j-1]+d[i-1][j+1]


result = 0
for i in range(10):
    result+=d[n][i]
    
print(result%MOD)