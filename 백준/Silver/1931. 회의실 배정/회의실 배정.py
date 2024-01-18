
import sys
input = sys.stdin.readline

N = int(input())
meetings = []

for _ in range(N):
    s,e = map(int,input().split())
    meetings.append((s,e))

meetings.sort(key=lambda x : (x[1],x[0]))

ans = 0
now = 0


for s , e in meetings:
    if now<=s:
        ans+=1
        now = e


print(ans)
