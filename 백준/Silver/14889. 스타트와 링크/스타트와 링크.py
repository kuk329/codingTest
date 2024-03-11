N = int(input())

a = []

for _ in range(N):
    tmp = list(map(int,input().split()))
    a.append(tmp)

start=[]
link = []
def select(idx,start,link):
    if idx == N: # 모든 사람을 팀에 분배했을 경우
        if len(start)!=N//2:
            return -1
        if len(link)!=N//2:
            return -1
        rank1 = 0
        rank2 = 0
        for i in range(N//2): # 각 팀의 능력치 합 구함
            for j in range(N//2):
                if i == j:
                    continue
                rank1 += a[start[i]][start[j]]
                rank2 += a[link[i]][link[j]]

        diff = abs(rank1-rank2)
        return diff

    if len(start) > N//2:
        return -1
    if len(link) > N//2:
        return -1

    ans = -1
    rank1 = select(idx+1,start+[idx],link)
    if ans == -1 or (rank1!=-1 and ans>rank1):
        ans = rank1
    rank2 = select(idx+1,start,link+[idx])
    if ans == -1 or (rank2!=-1 and ans>rank2):
        ans = rank2
    return ans

result = select(0,[],[])
print(result)



select(0,[],[])

