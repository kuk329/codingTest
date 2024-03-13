import sys
input = sys.stdin.readline
N = int(input())

tip = []
for _ in range(N):
    tip.append(int(input()))

tip.sort(reverse=True) # 내림차순 정렬


result = 0

for i in range(N):
    tmp = (tip[i] - i)
    if tmp>0:
        result+=tmp

print(result)
