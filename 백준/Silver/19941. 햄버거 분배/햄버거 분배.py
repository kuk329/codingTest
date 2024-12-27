import sys
input = sys.stdin.readline

# 1. 입력 값을 받는다.
N,k = map(int,input().split())
arr = list(input())
ans = 0

# 이미 먹은 햄버거인 경우 X 로 값을 변경

def eat(x):
    global k
    global ans
    # 자신보다 왼쪽에 있는 햄버거 찾기
    for i in range(k,0,-1):
        if x-i>=0:
            if arr[x-i]=='H':
                arr[x-i]='X'
                ans+=1
                return

    # 자신보다 오른쪽에 있는 햄버거 찾기
    for i in range(1,k+1):
        if x+i<N:
            if arr[x+i]=='H':
                arr[x+i]='X'
                ans+=1
                return


for i in range(N):
    if arr[i]=='P':
        eat(i)

print(ans)
