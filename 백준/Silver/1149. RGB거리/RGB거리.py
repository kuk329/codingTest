import sys
input = sys.stdin.readline

n = int(input())

d = []

# d[i][j] : j로 i를 칠했을때 최소
for _ in range(n):
    d.append(list(map(int,input().split())))


for i in range(1,n):
    d[i][0] = min(d[i-1][1],d[i-1][2]) + d[i][0]
    d[i][1] = min(d[i-1][0],d[i-1][2]) + d[i][1]
    d[i][2] = min(d[i-1][0],d[i-1][1]) + d[i][2]

ans = min(d[n-1][0],d[n-1][1],d[n-1][2])
print(ans)


    
