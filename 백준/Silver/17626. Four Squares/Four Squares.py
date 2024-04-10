import math
n = int(input())

d=[0]*(n+1)

if n==1 or n==2:
    print(n)
    exit()

d[1] = 1
d[2] = 2
for i in range(3,n+1):
    d[i] = i
    end = int(math.sqrt(i))+1
    for j in range(1,end):
        if i>=j*j:
            d[i] = min(d[i-j*j]+1,d[i])

print(d[n])