N = int(input())

p = list(map(int,input().split()))

p.sort(reverse=True)

ans = 0

for i,t in enumerate(p):
    ans += (i+1)*t

print(ans)
