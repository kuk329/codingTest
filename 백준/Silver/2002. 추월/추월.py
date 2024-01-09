from collections import deque
import sys
input = sys.stdin.readline

q = deque()
d = {}

n = int(input())

for i in range(n):
    tmp = input()
    d[tmp] = i

for i in range(n):
    tmp = input()
    q.append(tmp)

cnt = 0


while q:
    car = q.popleft()
    
    for i in range(len(q)):
        if d[car] > d[q[i]]:
            cnt+=1
            break
    

print(cnt)