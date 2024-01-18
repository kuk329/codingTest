import sys
input = sys.stdin.readline

N,K = map(int,input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))


coins.sort(reverse=True) # 내림차순 정렬 

cnt = 0
i=0

while K>0:
    cnt += K//coins[i] # 해당 동전 몇개를 사용해서 만들수 있는지 저장
    K = K%coins[i] # 해당 동전으로 K원을 만들고 난 나머지 저장
    i+=1



print(cnt)
    
