import sys
from collections import deque
input = sys.stdin.readline
q = deque()
dic = dict()

N, d, k, c = map(int,input().split())
belt =[]
for _ in range(N):
    belt.append(int(input()))

start = 0
end = k - 1
q.extend(belt[:k])

max_num = len(set(list(q) + [c]))

while start<N:
    q.popleft()
    start += 1
    end += 1
    if end == N:
        end = 0
    q.append(belt[end])

    tmp_num = len(set(list(q)+[c]))
    if tmp_num>max_num:
        max_num = tmp_num


print(max_num)
