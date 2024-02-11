N,S = map(int,input().split())

a = list(map(int,input().split()))
cnt = 0

def bf(index , total):
    global cnt
    if index == N:
        if total == S:
            cnt+=1
        return
    
    bf(index+1,total+a[index])
    bf(index+1,total)

bf(0,0)
if S==0:
    cnt-=1

print(cnt)