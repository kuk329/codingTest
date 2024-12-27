import sys
input = sys.stdin.readline

n = int(input())
H = list(map(int,input().split()))
A = list(map(int,input().split()))

ans = 0

# 초기 나무 크기 전체
ans += sum(H)

A.sort() # 오름차순 정렬

for i in range(n):
    ans+= A[i]*i

print(ans)