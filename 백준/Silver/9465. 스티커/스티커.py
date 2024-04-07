t = int(input()) # 테스트 케이스 입력받음.

for i in range(t):
    n = int(input()) # 스티커 수 입력받음(한줄)

    a = [[] for i in range(2)]

    for i in range(2):
        a[i]+=list(map(int,input().split()))

    d=[[0]*n for i in range(2)]
    # 행 열
    if n==1:
        print(max(a[0][0],a[1][0]))
    else:
        d[0][0]=a[0][0]
        d[1][0]=a[1][0]
        d[0][1]=a[1][0]+a[0][1]
        d[1][1]=a[0][0]+a[1][1]

        for i in range(2,n):
            d[0][i]=a[0][i]+max(d[1][i-1],d[1][i-2])
            d[1][i]=a[1][i]+max(d[0][i-1],d[0][i-2])
            
        print(max(d[0][n-1],d[1][n-1]))