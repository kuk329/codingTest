n = int(input())

a = list(map(int,input().split())) # 1 ~ n-1
d=[0]*n
d[0]=a[0]
for i in range(1,n):
    d[i]=a[i]
    if d[i]<d[i-1]+a[i]:
        d[i]=d[i-1]+a[i]

print(max(d))