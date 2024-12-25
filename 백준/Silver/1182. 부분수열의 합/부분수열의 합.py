import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,S = map(int,input().split())
nums = list(map(int,input().split()))

ans = 0

def dfs(idx,total):
    global ans
    if idx==N:
        if total == S:
            ans+=1
        return

    dfs(idx+1,total) # 해당 숫자 선택 X
    dfs(idx+1, total+nums[idx]) # 해당 숫자 선택 O

dfs(0,0)
if S==0:
    ans-=1

print(ans)




