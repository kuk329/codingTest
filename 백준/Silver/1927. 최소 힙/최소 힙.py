
import heapq
import sys
input = sys.stdin.readline

n = int(input()) # 연산의 개수

h =[]

for _ in range(n):
    x = int(input()) # 연산 정보
    if x==0: # 삭제
        if h: #값이 존재하면
            print(heapq.heappop(h))
        else:
            print(0)

    else: # 추가
        heapq.heappush(h,x)
