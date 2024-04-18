N, K = map(int,input().split())
height=list(map(int,input().split()))
diff = []

for i in range(0,N-1):
    tmp = height[i+1] - height[i]
    diff.append(tmp)

diff.sort(reverse=True)

print(sum(diff[K-1:]))
    