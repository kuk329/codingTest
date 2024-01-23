
n , m = map(int,input().split())

a1=[]
a2=[]
max_distance = 0

tmp = map(int,input().split())
for n in tmp:
    max_distance = max(max_distance,abs(n))
    if n<0:
        a2.append(-n)
    else:
        a1.append(n)

a1.sort(reverse=True)
a2.sort(reverse=True)

ans = 0

for i in range(0,len(a1),m):
    ans += a1[i]*2 # 왕복이므로 *2

for i in range(0,len(a2),m):
    ans += a2[i]*2 # 왕복이므로 *2

#max_distance = max(a1[0],a2[0])

ans -= max_distance # 가장 긴 거리는 가장 마지막에 한번만 감.

print(ans)
